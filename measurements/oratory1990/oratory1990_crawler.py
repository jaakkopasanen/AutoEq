# -*- coding: utf-8 -*-

import os
import sys
from ghostscript import Ghostscript
import PyPDF2
from PIL import Image, ImageDraw
import colorsys
import numpy as np
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from autoeq.frequency_response import FrequencyResponse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex
from measurements.crawler import Crawler
from measurements.image_graph_parser import ImageGraphParser

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class Oratory1990Crawler(Crawler):
    def __init__(self, driver=None):
        if driver is None:
            opts = Options()
            opts.add_argument('--headless')
            driver = webdriver.Chrome(os.path.abspath(os.path.join(DIR_PATH, '..', 'chromedriver')), options=opts)
        super().__init__(driver=driver)

    @staticmethod
    def read_name_index():
        return NameIndex.read_tsv(os.path.join(DIR_PATH, 'name_index.tsv'))

    def write_name_index(self):
        self.name_index.write_tsv(os.path.join(DIR_PATH, 'name_index.tsv'))

    @staticmethod
    def get_existing():
        return NameIndex.read_files(os.path.join(DIR_PATH, 'data', '*', '*', '*'))

    def get_urls(self):
        if self.driver is None:
            raise TypeError('self.driver cannot be None')

        document = self.get_beautiful_soup('https://www.reddit.com/r/oratory1990/wiki/index/list_of_presets')
        urls = {}
        table_header = document.find(id='wiki_full_list_of_eq_settings.3A')
        if table_header is None:
            raise RedditCrawlFailed('Failed to parse Reddit page.')
        tbody = table_header.parent.find('table').find('tbody')
        manufacturer = None
        model = None
        for row in tbody.find_all('tr'):
            cells = row.find_all('td')

            # Parse cells
            manufacturer = cells[0].text.strip() if cells[0].text.strip() != '-' else manufacturer
            model = cells[1].text.strip() if cells[1].text.strip() != '-' else model
            url = cells[2].find('a')['href'].replace('?dl=0', '?dl=1')
            notes = cells[3].text.strip()

            words = [x.strip().lower() for x in notes.split()]
            if bool([x for x in ['band', 'eq', 'setting', 'crinacle', 'adi-2'] if x in words]):
                # Skip various EQ settings
                continue

            false_name = f'{manufacturer} {model}'
            if notes:
                false_name += f' ({notes})'
            if false_name not in urls:
                urls[false_name] = url

        # Manual additions which have not been added to the list yet
        #urls['Avantone Planar'] = 'https://www.dropbox.com/s/o867ox65g124mp1/Avantone%20Planar.pdf?dl=1'

        return urls

    @staticmethod
    def parse_image(im, model, px_top=800, px_bottom=4400, px_left=0, px_right=2500):
        """Parses graph image downloaded from innerfidelity.com"""
        # Crop out everything but graph area (roughly)
        box = (px_left, px_top, im.size[0] - px_right, im.size[1] - px_bottom)
        im = im.crop(box)
        # im.show()

        # Find graph edges
        v_lines = ImageGraphParser.find_lines(im, 'vertical')
        h_lines = ImageGraphParser.find_lines(im, 'horizontal')

        # Crop by graph edges
        try:
            box = (v_lines[0], h_lines[0], v_lines[1], h_lines[1])
        except IndexError as err:
            raise GraphParseFailed('Failed to parse PDF')
        im = im.crop(box)
        # im.show()

        # X axis
        f_min = 10
        f_max = 20000
        f_step = (f_max / f_min) ** (1 / im.size[0])
        f = [f_min]
        for _ in range(1, im.size[0]):
            f.append(f[-1] * f_step)

        # Y axis
        a_max = 30
        a_min = -20
        a_res = (a_max - a_min) / im.size[1]

        _im = im.copy()
        pix = _im.load()
        amplitude = []
        y_legend = 40 / 50 * im.size[1]
        x0_legend = np.log(70 / f_min) / np.log(f_step)
        x1_legend = np.log(1000 / f_min) / np.log(f_step)
        # Iterate each column
        for x in range(im.size[0]):
            pxs = []  # Graph pixels
            # Iterate each row (pixel in column)
            for y in range(im.size[1]):
                if y > y_legend and x0_legend < x < x1_legend:
                    # Skip pixels in the legend box
                    continue

                # Convert read RGB pixel values and convert to HSV
                h, s, v = colorsys.rgb_to_hsv(*[v / 255.0 for v in im.getpixel((x, y))])
                # Graph pixels are colored
                if 0.7 < s < 0.9 and 20 / 360 < h < 30 / 360:
                    pxs.append(float(y))
                else:
                    p = im.getpixel((x, y))
                    pix[x, y] = (int(0.3 * p[0]), int(255 * 0.7 + 0.3 * p[1]), int(0.3 * p[2]))
            if not pxs:
                # No graph pixels found on this column
                amplitude.append(None)
            else:
                # Mean of recorded pixels
                v = np.mean(pxs)
                # Convert to dB value
                v = a_max - v * a_res
                amplitude.append(v)

        # Inspection image
        draw = ImageDraw.Draw(_im)
        x0 = np.log(20 / f_min) / np.log(f_step)
        x1 = np.log(10000 / f_min) / np.log(f_step)
        draw.rectangle(((x0, 10 / a_res), (x1, 40 / a_res)), outline='magenta')
        draw.rectangle(((x0 + 1, 10 / a_res + 1), (x1 - 1, 40 / a_res - 1)), outline='magenta')

        fr = FrequencyResponse(model, f, amplitude)
        fr.interpolate()
        fr.center()
        return fr, _im

    @staticmethod
    def pdf_to_image(input_file, output_file):
        input_file = os.path.abspath(input_file)
        output_file = os.path.abspath(output_file)

        # Read headphone model from the PDF
        f = open(input_file, 'rb')
        text = PyPDF2.PdfFileReader(f).getPage(0).extractText()
        if 'crinacle' in text.lower():
            raise ValueError('Measured by Crinacle')

        # Convert to image with ghostscript
        # Using temporary paths with Ghostscript because it seems to be unable to work with non-ascii characters
        tmp_in = os.path.join(os.path.split(input_file)[0], '__tmp.pdf')
        tmp_out = os.path.join(os.path.split(output_file)[0], '__tmp.png')
        if tmp_in == input_file or tmp_out == output_file:
            # Skip tmp files in case it was passed as input
            raise ValueError('tmp file')
        shutil.copy(input_file, tmp_in)
        gs = Ghostscript(
            b'pdf2png',
            b'-dNOPAUSE',
            b'-sDEVICE=png16m',
            b'-dBATCH',
            b'-r600',
            b'-dUseCropBox',
            f'-sOutputFile={tmp_out}'.encode('utf-8'),
            tmp_in.encode('utf-8')
        )
        gs.exit()
        shutil.copy(tmp_out, output_file)
        print('  Saved image to "{}"\n'.format(output_file))
        f.close()

        return Image.open(output_file)

    def process(self, item, url):
        if item.form == 'ignore':
            return

        pdf_dir = os.path.join(DIR_PATH, 'pdf')
        image_dir = os.path.join(DIR_PATH, 'images')
        inspection_dir = os.path.join(DIR_PATH, 'inspection')
        data_dir = os.path.join(DIR_PATH, 'data')
        out_dir = os.path.join(data_dir, item.form, item.true_name)

        os.makedirs(pdf_dir, exist_ok=True)
        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(inspection_dir, exist_ok=True)
        os.makedirs(out_dir, exist_ok=True)

        pdf_path = Crawler.download(url, item.true_name, pdf_dir)
        if not pdf_path:
            return
        try:
            im = Oratory1990Crawler.pdf_to_image(
                os.path.join(pdf_dir, f'{item.true_name}.pdf'),
                os.path.join(image_dir, f'{item.true_name}.png')
            )
        except ValueError as err:
            if str(err) == 'Measured by Crinacle':
                ignored = item.copy()
                ignored.form = 'ignore'
                self.name_index.update(ignored, false_name=item.false_name, true_name=item.true_name, form=item.form)
                self.write_name_index()
                print(f'  Ignored {item.false_name} because it is measured by Crinacle.\n')
            return
        fr, inspection = Oratory1990Crawler.parse_image(im, item.true_name)
        inspection.save(os.path.join(inspection_dir, f'{item.true_name}.png'))
        fr_path = os.path.join(out_dir, f'{item.true_name}.csv')
        fr.write_to_csv(fr_path)
        print(f'  Saved CSV to "{fr_path}"')


class RedditCrawlFailed(Exception):
    pass


class GraphParseFailed(Exception):
    pass


def main():
    crawler = Oratory1990Crawler()
    crawler.process_new(prompt=False)


if __name__ == '__main__':
    main()
