# -*- coding: utf-8 -*-

import os
import sys
import json
import re
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from autoeq.frequency_response import FrequencyResponse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex
from measurements.crawler import Crawler

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))

# Compensation
ONEAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(DIR_PATH, 'resources', 'rtings_compensation_w_bass.csv')
)
INEAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(DIR_PATH, 'resources', 'rtings_inear_compensation_w_bass.csv')
)


class RtingsCrawler(Crawler):
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
        # Line 2422
        # var sel_product = document.getElementById("product_select");
        # var product1 = sel_product.options[sel_product.selectedIndex].value
        # "https://www.rtings.com/graph/data/" + product1 + "/" + comparison_id
        if self.driver is None:
            raise TypeError('self.driver cannot be None')
        document = self.get_beautiful_soup('https://www.rtings.com/headphones/1-5/graph')
        urls = {}
        style = 'display: block; visibility: visible;'
        for child in document.find(id='product_select').find_all('option', attrs={'style': style}):
            try:
                data_id = child['value']
            except KeyError:
                # Dropdown option doesn't have value, perhaps it's default value placeholder
                continue

            name = child.text.strip()
            #urls[name] = f'https://www.rtings.com/images/graphs/{urlpart}/graph-frequency-response-14.json'
            urls[name] = f'https://www.rtings.com/graph/data/{data_id}/3992'
        return urls

    @staticmethod
    def parse_json(json_data):
        """Parses Rtings.com JSON data

        The columns should be "Frequency", "Left", "Right", "Target Response", "Left", "Right". Some rows might have
        data in the first Left and Right, some might have it in the second left and right

        Args:
            json_data: JSON data object as returned by Rtings API

        Returns:
            - Parsed raw frequency response as FrequencyResponse
            - Parsed target response as FrequencyResponse
        """
        header = json_data['header']
        data = np.array(json_data['data'])
        frequency = data[:, header.index('Frequency')]
        target = data[:, header.index('Target Response')]
        left_col = header.index('Left')
        right_col = header.index('Right')

        for row in data:
            if row[left_col] == np.array(None):
                # Data missing at the first "Left" column, use the last "Left" column
                row[left_col] = row[len(header) - header[::-1].index('Left') - 1]
            if row[right_col] == np.array(None):
                # Data missing at the first "Right" column, use the last "Right" column
                row[right_col] = row[len(header) - header[::-1].index('Right') - 1]

        left = data[:, left_col]
        right = data[:, right_col]

        raw = np.mean([left, right], axis=0)
        if np.std(target) > 0:
            raw += target
        fr = FrequencyResponse(name='fr', frequency=frequency, raw=raw)
        target = FrequencyResponse(name='target', frequency=frequency, raw=target)
        return fr, target

    def process(self, item, url):
        if item.form == 'ignore':
            return

        json_file = Crawler.download(url, item.true_name, os.path.join(DIR_PATH, 'json'), file_type='json')
        if json_file is not None:
            with open(os.path.join(DIR_PATH, 'json', f'{item.true_name}.json'), 'r', encoding='utf-8') as fh:
                json_data = json.load(fh)
            fr, target = RtingsCrawler.parse_json(json_data)
            fr.name = item.true_name
        else:
            raise FileNotFoundError(f'Could not download JSON file for{item.true_name} at {url}')
            # # No frequency response available, download bass, mid and treble
            # # Bass
            # Crawler.download(
            #     url.replace('frequency-response-14.json', 'bass.json'),
            #     f'{item.true_name}-bass', os.path.join(DIR_PATH, 'json')
            # )
            # with open(os.path.join(DIR_PATH, 'json', f'{item.true_name}-bass.json'), 'r', encoding='utf-8') as fh:
            #     bass_fr, bass_target = self.parse_json(json.load(fh))
            # # Mid
            # Crawler.download(
            #     url.replace('frequency-response-14.json', 'mid.json'),
            #     f'{item.true_name}-mid', os.path.join(DIR_PATH, 'json')
            # )
            # with open(os.path.join(DIR_PATH, 'json', f'{item.true_name}-mid.json'), 'r', encoding='utf-8') as fh:
            #     mid_fr, mid_target = self.parse_json(json.load(fh))
            # # Treble
            # Crawler.download(
            #     url.replace('frequency-response-14.json', 'treble.json'),
            #     f'{item.true_name}-treble', os.path.join(DIR_PATH, 'json')
            # )
            # with open(os.path.join(DIR_PATH, 'json', f'{item.true_name}-treble.json'), 'r', encoding='utf-8') as fh:
            #     treble_fr, treble_target = self.parse_json(json.load(fh))
            # fr = FrequencyResponse(
            #     name=item.true_name,
            #     frequency=np.concatenate([bass_fr.frequency, mid_fr.frequency, treble_fr.frequency]),
            #     raw=np.concatenate([bass_fr.raw, mid_fr.raw, treble_fr.raw])
            # )
            # target = FrequencyResponse(
            #     name=item.true_name,
            #     frequency=np.concatenate([bass_target.frequency, mid_target.frequency, treble_target.frequency]),
            #     raw=np.concatenate([bass_target.raw, mid_target.raw, treble_target.raw])
            # )

        fr.interpolate()
        if np.std(fr.raw) == 0:
            # Frequency response data has non-zero target response, use that
            target.interpolate()
            target = target
            print(f'Using target for {fr.name}')
        elif item.form == 'inear':
            # Using in-ear target response
            target = INEAR_TARGET
        else:
            # Using on-ear or earbud target response
            target = ONEAR_TARGET
        target.center()
        fr.raw += target.raw
        fr.center()

        # Inspection
        dir_path = os.path.join(DIR_PATH, 'inspection')
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f'{fr.name}.png')
        fig, ax = fr.plot_graph(file_path=file_path, show=False)
        plt.close(fig)

        # Write to file
        dir_path = os.path.join(DIR_PATH, 'data', item.form, fr.name)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, fr.name + '.csv')
        fr.write_to_csv(file_path)
        print(f'Saved "{fr.name}" to "{file_path}"')

    def intermediate_name(self, false_name):
        return re.sub(r'(Truly Wireless|True Wireless|Wireless)$', '', false_name).strip()


def main():
    crawler = RtingsCrawler()
    crawler.process_new(prompt=False)


if __name__ == '__main__':
    main()
