# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import colorsys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from autoeq.frequency_response import FrequencyResponse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_prompt import NamePrompt
from measurements.name_index import NameIndex, NameItem
from measurements.crawler import Crawler

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class ReferenceAudioAnalyzerCrawler(Crawler):
    pro_report_regex = re.compile(r'^pro report$', re.I)
    performed_on_stand_regex = re.compile(r'^Measurements were performed on the stands?:$')

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
        suffix_regex = re.compile(r' \(.*\)$')
        name_index = NameIndex.read_files(os.path.join(DIR_PATH, 'data', '**', '*.csv'))
        # Add models without mod suffixes which don't exist
        for i, row in name_index.df.iterrows():
            model = re.sub(suffix_regex, '', row.true_name)
            if model != row.true_name:
                name_index.df = pd.concat([name_index.df, pd.DataFrame(
                    [[row.false_name, model, row.form]],
                    columns=name_index.df.columns
                )])
        name_index.df.drop_duplicates()
        return name_index

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
    def find_curve(im, inspection, min_hue, max_hue, min_saturation, max_saturation, a_max, a_res):
        amplitude = []
        # Iterate each column
        for x in range(im.size[0]):
            pxs = []  # Graph pixels
            # Iterate each row (pixel in column)
            for y in range(im.size[1]):
                # Convert read RGB pixel values and convert to HSV
                h, s, v = colorsys.rgb_to_hsv(*[v / 255.0 for v in im.getpixel((x, y))][:3])
                # Graph pixels are colored
                if min_saturation < s < max_saturation and min_hue / 360 < h < max_hue / 360:
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
        return amplitude, im, inspection

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

        # Try blue curve
        _im = im.copy()
        inspection = _im.load()
        amplitude, _im, _inspection = ReferenceAudioAnalyzerCrawler.find_curve(
            _im, inspection, 203, 206, 0.8, 1.0, a_max, a_res
        )
        if len([x for x in amplitude if x is None]) >= 0.5 * len(amplitude):
            # More than half of the pixels were discarded, try green curve
            _im = im.copy()
            inspection = _im.load()
            amplitude, _im, _inspection = ReferenceAudioAnalyzerCrawler.find_curve(
                _im, inspection, 119, 121, 0.8, 1.0, a_max, a_res
            )

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
        if len(fr.frequency) < 2:
            im.show()
            raise ValueError(f'Failed to parse image for {fr.name}')
        fr.smoothen_fractional_octave(window_size=1/3, treble_window_size=1/3)
        fr.raw = fr.smoothed.copy()
        fr.smoothed = np.array([])
        fr.center()

        return fr, _im

    def process(self, item, url):
        if item.form == 'ignore':
            return

        image_dir = os.path.join(DIR_PATH, 'images')
        inspection_dir = os.path.join(DIR_PATH, 'inspection')
        data_dir = os.path.join(DIR_PATH, 'data')

        os.makedirs(image_dir, exist_ok=True)
        os.makedirs(os.path.join(inspection_dir, 'parse'), exist_ok=True)
        os.makedirs(os.path.join(inspection_dir, 'fr'), exist_ok=True)

        # Download and parse image
        self.download_images(url, item, data_dir, image_dir, inspection_dir, callback=self.process_image)

    def download_images(self, url, item, data_dir, image_dir, inspection_dir, callback):
        document = self.get_beautiful_soup(url)  # Reports page
        for label in document.find_all(name='span', text=self.pro_report_regex):
            parent = label.parent.parent.parent
            anchor = parent.find_all('a')[1]
            report_url = f'https://reference-audio-analyzer.pro{anchor["href"]}'
            suffix = anchor.text.lower().strip()
            name = item.true_name
            if suffix != item.false_name.lower() and suffix != 'default':
                name += f' ({suffix})'
                # The suffixes above are read automatically from the reports compilation page.
                # However these might not be the names that should exist in AutoEq.
                mods = self.name_index.find(false_name=name)
                if mods:
                    # Find an item in name index which has the given name with automatic
                    # suffixes as false name and replace the name with it's true name.
                    true_name = mods.items[0].true_name
                    image_path, rig = self.download_image(report_url, image_dir, item.false_name, true_name, item.form)
                    if image_path:
                        callback(image_path, rig, true_name, item.form, data_dir, inspection_dir)
                else:
                    # Not in the name index, prompt user
                    manufacturer, manufacturer_match = self.manufacturers.find(name)
                    if manufacturer:
                        model = re.sub(re.escape(manufacturer_match), '', name, flags=re.IGNORECASE).strip()
                        name_proposals = self.get_name_proposals(name)
                        similar_names = self.get_name_proposals(name, n=6, normalize_digits=True, threshold=0)
                        similar_names = [item.true_name for item in similar_names.items]
                    else:
                        model = name
                        name_proposals = None
                        similar_names = None
                    prompt = NamePrompt(
                        model,
                        self.prompt_mod_callback(name, report_url, data_dir, image_dir, inspection_dir, callback),
                        manufacturer=manufacturer,
                        name_proposals=name_proposals,
                        search_callback=self.search,
                        false_name=item.false_name,
                        similar_names=similar_names
                    ).widget
                    if len(self.prompts.children) > 0:
                        if type(self.prompts.children) == tuple:
                            self.prompts.children = [x for x in self.prompts.children] + [prompt]
                        else:
                            self.prompts.children.append(prompt)
                    else:
                        self.prompts.children = [prompt]
            else:
                true_name = name
                image_path, rig = self.download_image(report_url, image_dir, item.false_name, true_name, item.form)
                if image_path:
                    callback(image_path, rig, true_name, item.form, data_dir, inspection_dir)

    def prompt_mod_callback(self, false_name, report_url, data_dir, image_dir, inspection_dir, callback):
        def fn(true_name, form):
            self.name_index.add(NameItem(false_name, true_name, form))
            self.write_name_index()
            image_path, rig = self.download_image(report_url, image_dir, false_name, true_name, form)
            if image_path:
                callback(image_path, rig, true_name, form, data_dir, inspection_dir)
        return fn

    def download_image(self, report_url, image_dir, false_name, true_name, form):
        document = self.get_beautiful_soup(report_url)  # Sets the driver also
        el = document.find(name='li', text=self.performed_on_stand_regex)
        try:
            rig = el.parent.find(name='ul').find(name='a').text
        except AttributeError as err:
            rig = 'HDM-X' if form == 'onear' else 'SIEC'
            print(f'Measurement rig could not be read for "{false_name}", guessing {rig}')
        try:
            graph = self.driver.find_element_by_id('response9').find_element_by_tag_name('div')  # FR Graph
        except Exception:
            print(f'No graph for {false_name}')
            return None, None
        # Background image
        report_url = graph.value_of_css_property('background-image').replace('url("', '').replace('")', '')
        file_path = self.download(report_url, true_name, image_dir)
        return file_path, rig

    def process_image(self, image_path, rig, name, form, data_dir, inspection_dir):
        im = Image.open(image_path)
        if im is None:
            print(f'Could not open image in "{image_path}"')
            return

        mod = self.name_index.find(true_name=name)
        # Get the form from name index if an entry already exists
        form = mod.items[0].form if mod else form

        fr, inspection = ReferenceAudioAnalyzerCrawler.parse_image(im, name)

        out_dir = os.path.join(data_dir, form, rig, name)
        os.makedirs(out_dir, exist_ok=True)

        # Save inspection images
        inspection.save(os.path.join(inspection_dir, 'parse', f'{name}.png'))
        fig, ax = fr.plot_graph(show=False, file_path=os.path.join(inspection_dir, 'fr', f'{name}.png'))
        plt.close(fig)

        # Write to CSV
        fr.write_to_csv(os.path.join(out_dir, f'{name}.csv'))
        print(f'Wrote CSV to "{os.path.join(out_dir, f"{name}.csv")}"')


def main():
    crawler = ReferenceAudioAnalyzerCrawler()
    crawler.process_new(prompt=False)


if __name__ == '__main__':
    main()
