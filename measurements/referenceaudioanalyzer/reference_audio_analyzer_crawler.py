# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
from PIL import Image, ImageDraw
import colorsys
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex
from measurements.crawler import Crawler
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class ReferenceAudioAnalyzerCrawler(Crawler):
    @staticmethod
    def read_name_index():
        return NameIndex.read_tsv(os.path.join(DIR_PATH, 'name_index.tsv'))

    def write_name_index(self):
        self.name_index.write_tsv(os.path.join(DIR_PATH, 'name_index.tsv'))

    @staticmethod
    def get_existing():
        return NameIndex.read_files(os.path.join(DIR_PATH, 'data', '*', '*'))

    def get_urls(self):
        if self.driver is None:
            raise TypeError('self.driver cannot be None')

        document = self.get_beautiful_soup('https://reference-audio-analyzer.pro/en/catalog-reports.php?sp_1=1&tp=1')
        anchors = document.find(name='article', attrs={'class': 'ar3'}).find_all('a')
        urls = {}
        for anchor in anchors:
            if not anchor.has_attr('href'):
                continue
            urls[anchor.text] = f'https://reference-audio-analyzer.pro{anchor["href"]}'
        return urls

    @staticmethod
    def parse_image(im, model):
        """Parses graph image downloaded from innerfidelity.com"""
        # Crop by left and right edges
        box = (69, 31, 550, 290)
        im = im.crop(box)

        px_a_max = 0
        px_a_min = im.size[1]
        # im.show()

        # X axis
        f_min = 20
        f_max = 20000
        f_step = (f_max / f_min) ** (1 / im.size[0])
        f = [f_min]
        for _ in range(1, im.size[0]):
            f.append(f[-1] * f_step)

        # Y axis
        a_max = 150
        a_min = 66
        a_res = (a_max - a_min) / (px_a_min - px_a_max)

        _im = im.copy()
        inspection = _im.load()
        amplitude = []
        # Iterate each column
        for x in range(im.size[0]):
            pxs = []  # Graph pixels
            # Iterate each row (pixel in column)
            for y in range(im.size[1]):
                # Convert read RGB pixel values and convert to HSV
                h, s, v = colorsys.rgb_to_hsv(*[v / 255.0 for v in im.getpixel((x, y))][:3])
                # Graph pixels are colored
                if 0.8 < s < 1.0 and 203 / 360 < h < 206 / 360:
                    pxs.append(float(y))
                else:
                    p = im.getpixel((x, y))
                    inspection[x, y] = (int(0.3 * p[0]), int(255 * 0.7 + 0.3 * p[1]), int(0 + 0.3 * p[2]))
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
        x0 = np.log(30 / f_min) / np.log(f_step)
        x1 = np.log(10000 / f_min) / np.log(f_step)
        y_0 = px_a_max + 12 / a_res
        y_1 = px_a_min - 12 / a_res
        draw.rectangle(((x0, y_0), (x1, y_1)), outline='magenta')
        draw.rectangle(((x0 + 1, y_0 + 1), (x1 - 1, y_1 - 1)), outline='magenta')

        # Create frequency response
        fr = FrequencyResponse(model, f, amplitude)
        fr.interpolate()
        fr.smoothen_fractional_octave(window_size=1/3, treble_window_size=1/3)
        fr.raw = fr.smoothed.copy()
        fr.smoothed = np.array([])
        fr.center()

        return fr, _im

    def download_image(self, url, item, image_dir):
        document = self.get_beautiful_soup(url)  # Reports page
        try:
            anchor = document.find(attrs={'class': 'imgblock_pro'}).find_all('a')[1]  # Link to pro report
        except:
            print(f'Failed {url}')
        self.driver.get(f'https://reference-audio-analyzer.pro{anchor["href"]}')  # Pro report
        graph = self.driver.find_element_by_id('response9').find_element_by_tag_name('div')  # FR Graph
        url = graph.value_of_css_property('background-image').replace('url("', '').replace('")', '')  # Background image
        self.download(url, item.true_name, image_dir)

    def process(self, item, url):
        image_dir = os.path.join(DIR_PATH, 'images')
        inspection_dir = os.path.join(DIR_PATH, 'inspection')
        data_dir = os.path.join(DIR_PATH, 'data')
        out_dir = os.path.join(data_dir, item.form, item.true_name)

        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(os.path.join(inspection_dir, 'parse'), exist_ok=True)
        os.makedirs(os.path.join(inspection_dir, 'fr'), exist_ok=True)
        os.makedirs(out_dir, exist_ok=True)

        # Download and parse image
        self.download_image(url, item, image_dir)
        im = Image.open(os.path.join(image_dir, f'{item.true_name}.png'))
        fr, inspection = ReferenceAudioAnalyzerCrawler.parse_image(im, item.true_name)
        if im is None:
            try:
                os.rmdir(out_dir)
            except OSError:
                pass
            return

        # Save inspection images
        inspection.save(os.path.join(inspection_dir, 'parse', f'{item.true_name}.png'))
        fr.plot_graph(show=False, file_path=os.path.join(inspection_dir, 'fr', f'{item.true_name}.png'))

        # Write to CSV
        fr.write_to_csv(os.path.join(out_dir, f'{item.true_name}.csv'))
