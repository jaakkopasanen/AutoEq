# -*- coding: utf-8 -*-

import sys
import re
import tempfile
from pathlib import Path
from ghostscript import Ghostscript
import PyPDF2
from PIL import Image, ImageDraw
import colorsys
import numpy as np
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from autoeq.frequency_response import FrequencyResponse
from autoeq.utils import make_file_name_allowed, is_file_name_allowed
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.name_index import NameIndex, NameItem
from dbtools.crawler import Crawler
from dbtools.image_graph_parser import ImageGraphParser
from dbtools.constants import MEASUREMENTS_PATH

ORATORY1990_PATH = MEASUREMENTS_PATH.joinpath('oratory1990')


class Oratory1990Crawler(Crawler):
    def __init__(self, driver=None, delete_existing_on_prompt=True, redownload=False):
        if driver is None:
            opts = Options()
            opts.add_argument('--headless')
            driver = webdriver.Chrome(options=opts)
        super().__init__(driver=driver, delete_existing_on_prompt=delete_existing_on_prompt, redownload=redownload)

    def read_name_index(self):
        self.name_index = NameIndex.read_tsv(ORATORY1990_PATH.joinpath('name_index.tsv'))
        return self.name_index

    def write_name_index(self):
        self.name_index.write_tsv(ORATORY1990_PATH.joinpath('name_index.tsv'))

    def guess_name(self, item):
        """Tries to guess what the name might be."""
        return item.source_name

    @staticmethod
    def image_path(item):
        return ORATORY1990_PATH.joinpath('images', f'{make_file_name_allowed(item.source_name)}.png')

    @staticmethod
    def pdf_path(item):
        return ORATORY1990_PATH.joinpath('pdf', f'{make_file_name_allowed(item.source_name)}.pdf')

    def parse_pdf(self, item):
        pdf_path = self.pdf_path(item)
        if not pdf_path.exists():
            self.download(item.url, self.pdf_path(item))
        image_path = self.image_path(item)
        # Convert to image with ghostscript
        # Using temporary paths with Ghostscript because it seems to be unable to work with non-ascii characters
        tmp_in = Path(tempfile.gettempdir()).joinpath('__tmp.pdf')
        tmp_out = Path(tempfile.gettempdir()).joinpath('__tmp.png')
        shutil.copy(pdf_path, tmp_in)
        Ghostscript(
            b'pdf2png', b'-dNOPAUSE', b'-sDEVICE=png16m', b'-dBATCH', b'-r600', b'-dUseCropBox',
            f'-sOutputFile={tmp_out}'.encode('utf-8'), str(tmp_in).encode('utf-8')).exit()
        shutil.copy(tmp_out, image_path)
        return image_path

    def read_pdf_text(self, item):
        self.download(item.url, self.pdf_path(item))
        with open(self.pdf_path(item), 'rb') as fh:
            return PyPDF2.PdfReader(fh).pages[0].extract_text()

    @staticmethod
    def extract_rig(text, item):
        text = text.lower()
        rig = re.search(r'gras ?(?:/?4[35][ -]?[ABCG]+)+[ -]?\d*', text, flags=re.IGNORECASE)
        if rig is None:
            return None
        rig = re.sub(r'^gras4', r'GRAS 4', rig[0], flags=re.IGNORECASE)
        if re.search(r'43 ?ac ?/ ?43 ?ag', rig, flags=re.IGNORECASE):
            rig = 'GRAS 43AC' if item.form == 'in-ear' else 'GRAS 43AG'
        return rig.upper()

    @staticmethod
    def is_by_3rd_party(text):
        return re.search(r'(?:measured|measurements?) (?:by|from)', text, flags=re.IGNORECASE) or \
               re.search(r'(?:head-fi|crinacle)', text, flags=re.IGNORECASE)

    def resolve(self, item):
        true_item = self.name_index.find_one(source_name=item.source_name)
        if true_item is not None:
            if true_item.name is not None:
                item.name = true_item.name
            if true_item.form is not None:
                item.form = true_item.form
            if true_item.rig is not None:
                item.rig = true_item.rig
        super().resolve(item)
        if item.form is not None and item.rig is not None:
            return
        text = self.read_pdf_text(item)
        if self.is_by_3rd_party(text):  # Ignore stuff done based on 3rd party measurements
            item.form = 'ignore'
        else:
            item.rig = self.extract_rig(text, item)

    def is_prompt_needed(self, item):
        if item.is_ignored:
            return False
        return item.name is None or item.form is None or item.rig is None

    def crawl(self):
        if self.driver is None:
            raise TypeError('self.driver cannot be None')
        self.name_index = self.read_name_index()
        document = self.get_beautiful_soup('https://www.reddit.com/r/oratory1990/wiki/index/list_of_presets')
        table_header = document.find(id='wiki_full_list_of_eq_settings.3A')
        if table_header is None:
            raise RedditCrawlFailed('Failed to parse Reddit page. Maybe try again?')
        self.crawl_index = NameIndex()
        manufacturer, model = None, None
        for row in table_header.parent.find('table').find('tbody').find_all('tr'):
            cells = row.find_all('td')
            # Parse cells
            # Try to read manufacturer from the first cell and if it fails (cell is empty), use the previous name
            manufacturer = cells[0].text.strip() if cells[0].text.strip() != '-' else manufacturer
            # Try to read model from the second cell and if it fails (cell is empty), use the previous name
            model = cells[1].text.strip() if cells[1].text.strip() != '-' else model
            source_name = f'{manufacturer} {model}'
            # Third cell contains hyperlink, where the anchor is the PDF and text is target name
            url = cells[2].find('a')['href'].replace('?dl=0', '?dl=1')
            form = 'over-ear' if 'over-ear' in cells[2].text.strip().lower() else 'in-ear'
            # Fourth cell is notes
            notes = cells[3].text.strip()
            if 'preliminary' in notes.lower() or ' EQ' in notes:
                continue  # Skip various EQ settings and preliminary measurements
            if notes and notes.lower() != 'standard':
                source_name += f' ({notes})'
            item = NameItem(url=url, source_name=source_name, form=form)
            known_item = self.name_index.find_one(url=url)
            if known_item is not None:
                if known_item.name is not None:
                    item.name = known_item.name
                if known_item.form is not None:
                    item.form = known_item.form
                if known_item.rig is not None:
                    item.rig = known_item.rig
            if not self.crawl_index.find(source_name=source_name):
                self.crawl_index.add(item)
        return self.crawl_index

    @staticmethod
    def parse_image(path, px_top=800, px_bottom=4400, px_left=0, px_right=2500):
        """Parses graph images converted from oratory1990 PDFs"""
        im = Image.open(path)
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
        # Create FR object
        fr = FrequencyResponse('parsed', f, amplitude)
        fr.interpolate()
        fr.center()
        return fr, _im

    def target_group_key(self, item):
        """Key for grouping measurements (NameItems) that should be averaged"""
        return f'{item.form}/{item.name}'

    def target_path(self, item):
        """Target file path for the item in measurements directory"""
        if item.is_ignored or item.form is None or item.name is None:
            return None
        path = ORATORY1990_PATH.joinpath('data', item.form, f'{item.name}.csv')
        if not is_file_name_allowed(item.name):
            raise ValueError(f'Target path cannot be "{path}"')
        return path

    def process_group(self, items, new_only=True):
        if items[0].is_ignored:
            return
        file_path = self.target_path(items[0])
        if new_only and file_path.exists():
            return
        inspection_path = ORATORY1990_PATH.joinpath('inspection')
        inspection_path.mkdir(exist_ok=True, parents=True)
        avg_fr = FrequencyResponse(items[0].name)
        avg_fr.raw = np.zeros(avg_fr.frequency.shape)
        for item in items:
            image_path = self.parse_pdf(item)
            fr, inspection = Oratory1990Crawler.parse_image(image_path)
            avg_fr.raw += fr.raw
            inspection.save(inspection_path.joinpath(f'{make_file_name_allowed(item.source_name)}.png'))
        avg_fr.raw /= len(items)
        fr_path = self.target_path(items[0])
        avg_fr.write_csv(fr_path)

    def list_existing_files(self):
        return list(ORATORY1990_PATH.joinpath('data').glob('**/*.csv'))


class RedditCrawlFailed(Exception):
    pass


class GraphParseFailed(Exception):
    pass

