# -*- coding: utf-8 -*-

import os
import sys
import requests
from bs4 import BeautifulSoup
from tqdm.auto import tqdm
import json
import re
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from autoeq.frequency_response import FrequencyResponse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex, NameItem
from measurements.crawler import Crawler

RTINGS_PATH = Path(__file__).parent

# Compensation
OVEREAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(RTINGS_PATH, 'resources', 'rtings_compensation_w_bass.csv'))
INEAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(RTINGS_PATH, 'resources', 'rtings_inear_compensation_w_bass.csv'))


class RtingsCrawlError(Exception):
    pass


class RtingsCrawler(Crawler):
    def __init__(self, driver=None, delete_existing_on_prompt=True, redownload=False):
        if driver is None:
            opts = Options()
            opts.add_argument('--headless')
            driver = webdriver.Chrome(options=opts)
        super().__init__(driver=driver)

    @staticmethod
    def read_name_index():
        return NameIndex.read_tsv(os.path.join(RTINGS_PATH, 'name_index.tsv'))

    def write_name_index(self):
        self.name_index.write_tsv(os.path.join(RTINGS_PATH, 'name_index.tsv'))

    def guess_name(self, item):
        name = re.sub(r'(Truly Wireless|True Wireless|Wireless)$', '', item.source_name).strip()
        name = self.manufacturers.replace(name)
        return name

    def resolve(self, item):
        """Resolve name for a single item. Updates the item in place."""
        ground_truths = self.name_index.find(source_name=item.source_name)
        if ground_truths is None:
            return
        for ground_truth in ground_truths:
            if ground_truth.name is not None:
                item.name = ground_truth.name
            if ground_truth.form is not None:
                item.form = ground_truth.form
            if ground_truth.rig is not None:
                item.rig = ground_truth.rig

    @staticmethod
    def graph_data_url_payloads():
        product_graph_data_url_payloads = []
        for version in ['1-5', '1-4', '1-2']:
            html = requests.get(f'https://www.rtings.com/headphones/{version}/graph').text
            document = BeautifulSoup(html, 'html.parser')
            test_bench = json.loads(document.find(class_='graph_tool_page').get('data-props'))['test_bench']
            with open(RTINGS_PATH.joinpath(f'test_bench_{version}.json'), 'w', encoding='utf-8') as fh:
                json.dump(test_bench, fh, ensure_ascii=False, indent=4)
            for product in test_bench['comparable_products']:
                if product["fullname"] in [payload['source_name'] for payload in product_graph_data_url_payloads]:
                    # The versions are iterated from newest to oldest, if product with the same name already exists,
                    # that means it was included in the results of the newer test methodology and so this one can
                    # be skipped
                    continue
                graph_type = None
                tids = set([test_result['test']['original_id'] for test_result in product['review']['test_results']])
                valid_test_ids = []
                matching_raw_fr_l_ids = [
                    tid for tid in tids if tid in ['4011', '7917', '21564', '1344', '2060', '3182']]
                if matching_raw_fr_l_ids:
                    valid_test_ids.append(matching_raw_fr_l_ids[0])
                    graph_type = 'raw-left-right'
                matching_raw_fr_r_ids = [
                    tid for tid in tids if tid in ['4012', '7918', '21565', '1343', '2061', '3183']]
                if matching_raw_fr_r_ids:
                    valid_test_ids.append(matching_raw_fr_r_ids[0])
                    graph_type = 'raw-left-right'
                if not valid_test_ids:
                    if '436' in tids and '437' in tids and '438' in tids:
                        valid_test_ids = ['436', '437', '438']
                        graph_type = 'bass-mid-treble'
                if not valid_test_ids:
                    print(f'No valid test_original_id found for {product["fullname"]}')
                    continue
                product_graph_data_url_payloads.append({
                    'source_name': product['fullname'],
                    'graph_type': graph_type,
                    'payloads': [{
                        'named_version': 'public',
                        'product_id': product['id'],
                        'test_original_id': test_id
                    } for test_id in valid_test_ids]
                })
        return product_graph_data_url_payloads

    @staticmethod
    def graph_data_url(payload):
        res = requests.post('https://www.rtings.com/api/v2/safe/graph_tool__product_graph_data_url', data=payload)
        if res.status_code < 200 or res.status_code >= 300:
            print(f'Failed to get graph URL with payload {payload}: {res.text}')
            return None
        data = res.json()
        try:
            path = data['data']['product']['review']['test_results'][0]['graph_data_url']
            return f'https://i.rtings.com{path}'
        except:
            print(f'Graph data URL for {payload} returned an unexpected data format: {data}')
            return None

    def crawl(self):
        if RTINGS_PATH.joinpath('crawl_graph_data_urls.json').exists():
            with open(RTINGS_PATH.joinpath('crawl_graph_data_urls.json')) as fh:
                graph_data_url_cache = json.load(fh)
        else:
            graph_data_url_cache = {}
        self.name_index = self.read_name_index()
        self.crawl_index = NameIndex()
        for product_payloads in tqdm(self.graph_data_url_payloads()):
            for payload in product_payloads['payloads']:
                item = NameItem(product_payloads['source_name'], None, None, url=None, rig='HMS II.3')
                cache_key = f'{payload["product_id"]}/{payload["test_original_id"]}'
                if cache_key in graph_data_url_cache:  # Item found in cache
                    item.url = graph_data_url_cache[cache_key]
                else:  # Item not found in cache, get URL with API call
                    item.url = self.graph_data_url(payload)
                if item.url is not None:
                    graph_data_url_cache[cache_key] = item.url
                self.resolve(item)
                self.crawl_index.add(item)
        with open(RTINGS_PATH.joinpath('crawl_graph_data_urls.json'), 'w', encoding='utf-8') as fh:
            json.dump(graph_data_url_cache, fh, ensure_ascii=False, indent=4)
        return self.crawl_index

    def target_group_key(self, item):
        return f'{item.form}/{item.name}'

    def target_path(self, item):
        return RTINGS_PATH.joinpath('data', item.form, f'{item.name}.csv')

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

    def process_group(self, items, new_only=True):
        if items[0].form == 'ignore':
            return
        file_path = self.target_path(items[0])
        if new_only and file_path.exists():
            return
        for item in items:
            json_file = Crawler.download(f'https://i.rtings.com{item.url}', self.target_path(item))

        json_file = Crawler.download(url, items.name, os.path.join(RTINGS_PATH, 'json'), file_type='json')
        if json_file is not None:
            with open(os.path.join(RTINGS_PATH, 'json', f'{items.name}.json'), 'r', encoding='utf-8') as fh:
                json_data = json.load(fh)
            fr, target = RtingsCrawler.parse_json(json_data)
            fr.name = items.name
        else:
            raise FileNotFoundError(f'Could not download JSON file for{items.name} at {url}')
        fr.interpolate()
        if np.std(fr.raw) == 0:
            # Frequency response data has non-zero target response, use that
            target.interpolate()
            target = target
            print(f'Using target for {fr.name}')
        elif items.form == 'in-ear':
            # Using in-ear target response
            target = INEAR_TARGET
        else:
            # Using on-ear or earbud target response
            target = OVEREAR_TARGET
        target.center()
        fr.raw += target.raw
        fr.center()
        # Inspection
        dir_path = os.path.join(RTINGS_PATH, 'inspection')
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f'{fr.name}.png')
        fig, ax = fr.plot_graph(file_path=file_path, show=False)
        plt.close(fig)
        # Write to file
        dir_path = os.path.join(RTINGS_PATH, 'data', items.form)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, fr.name + '.csv')
        fr.write_to_csv(file_path)
        print(f'Saved "{fr.name}" to "{file_path}"')


def main():
    crawler = RtingsCrawler()
    crawler.process_all(prompt=False)


if __name__ == '__main__':
    main()
