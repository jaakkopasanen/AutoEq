# -*- coding: utf-8 -*-

import os
import sys
import requests
import json
import numpy as np
from bs4 import BeautifulSoup
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex
from measurements.crawler import Crawler
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))

# Compensation
ONEAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(DIR_PATH, 'resources', 'rtings_compensation_w_bass.csv')
)
INEAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(DIR_PATH, 'resources', 'rtings_inear_compensation_w_bass.csv')
)


class RtingsCrawler(Crawler):
    @staticmethod
    def read_name_index():
        return NameIndex.read_tsv(os.path.join(DIR_PATH, 'name_index.tsv'))

    def write_name_index(self):
        self.name_index.write_tsv(os.path.join(DIR_PATH, 'name_index.tsv'))

    @staticmethod
    def get_existing():
        return NameIndex.read_files(os.path.join(DIR_PATH, 'data', '*', '*'))

    def get_urls(self):
        res = requests.get('https://www.rtings.com/headphones/1-4/graph')
        document = BeautifulSoup(res.content, 'html.parser')
        urls = {}
        for child in document.find(id='product_select').find_all('option'):
            name = child.text.strip()
            urls[name] = f'https://www.rtings.com/images/graphs/{child["data-urlpart"]}/graph-frequency-response-14.json'
        return urls

    @staticmethod
    def parse_json(json_data):
        header = json_data['header']
        data = np.array(json_data['data'])
        frequency = data[:, header.index('Frequency')]
        target = data[:, header.index('Target Response')]
        left_col = header.index('Left')
        right_col = header.index('Left')

        for row in data:
            if row[left_col] == np.array(None):
                row[left_col] = row[len(header) - header[::-1].index('Left') - 1]
            if row[right_col] == np.array(None):
                row[right_col] = row[len(header) - header[::-1].index('Right') - 1]

        left = data[:, left_col]
        right = data[:, right_col]

        raw = np.mean([left, right], axis=0)
        if np.std(target) > 0:
            raw += target
        fr = FrequencyResponse(name='', frequency=frequency, raw=raw)
        target = FrequencyResponse(name='', frequency=frequency, raw=target)
        return fr, target

    def process(self, item, url):
        if not Crawler.download(url, item.true_name, os.path.join(DIR_PATH, 'json')):
            return
        with open(os.path.join(DIR_PATH, 'json', f'{item.true_name}.json'), 'r') as fh:
            json_data = json.load(fh)

        fr, target = RtingsCrawler.parse_json(json_data)
        fr.name = item.true_name
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
        fr.plot_graph(file_path=file_path, show=False)

        # Write to file
        dir_path = os.path.join(DIR_PATH, 'data', item.form, fr.name)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, fr.name + '.csv')
        fr.write_to_csv(file_path)
        print(f'Saved "{fr.name}" to "{file_path}"')
