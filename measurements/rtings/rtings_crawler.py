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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from autoeq.frequency_response import FrequencyResponse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex, NameItem
from measurements.crawler import Crawler

RTINGS_PATH = Path(__file__).parent
OVEREAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(RTINGS_PATH, 'resources', 'rtings_compensation_w_bass.csv'))
INEAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(RTINGS_PATH, 'resources', 'rtings_inear_compensation_w_bass.csv'))


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
        if item.form is None or item.name is None:
            return None
        return RTINGS_PATH.joinpath('data', item.form, f'{item.name}.csv')

    @staticmethod
    def json_path(item):
        uid = item.url.split('/')[-2]
        return RTINGS_PATH.joinpath('json', f'{uid}.json')

    @staticmethod
    def parse_json(json_data):
        """Parses Rtings.com JSON data

        Args:
            json_data: JSON data object as returned by Rtings API

        Returns:
            Parsed FrequencyResponse
        """
        header = json_data['header']
        data = np.array(json_data['data'])
        frequency = data[:, header.index('Frequency')]
        target = data[:, header.index('Target Response')]
        # Raw Left FR data has "Left Avg", raw right FR data has "Right Avg" and bass, mid and treble data has both
        # "Left" and "Right" columns
        col_ix = None
        for col_name in ['Left Avg', 'Left', 'Right Avg', 'Right']:
            if col_name in header:
                col_ix = header.index(col_name)
                break
        if col_ix is None:
            raise RtingsProcessingError('Could not find any of the data columns in JSON')
        fr = FrequencyResponse(name='fr', frequency=frequency, raw=data[:, col_ix], target=target)
        return fr

    def process_group(self, items, new_only=True):
        if items[0].form == 'ignore':
            return
        file_path = self.target_path(items[0])
        if new_only and file_path.exists():
            return
        frs = []
        for item in items:
            raw = self.download(item.url, self.json_path(item))
            frs.append(self.parse_json(json.loads(raw.decode('utf-8'))))
        if len(frs) < 3:  # Raw frequency responses for left and right in separate files, unless single ear unit
            fr = FrequencyResponse(
                name=items[0].name,
                frequency=frs[0].frequency,
                raw=np.mean([fr.raw for fr in frs], axis=0))
        elif len(frs) == 3:  # Bass, mid and treble responses in separate files
            fr = FrequencyResponse(
                name=items[0].name,
                frequency=np.concatenate([fr.frequency for fr in frs]),  # All three have different frequency ranges
                raw=np.concatenate([fr.raw for fr in frs]))
        else:
            raise RtingsProcessingError(f'{len(frs)} JSON files grouped together, don\'t know what to do.')
        fr.interpolate()
        fr.center()
        # Write to file
        file_path.parent.mkdir(exist_ok=True, parents=True)
        fr.write_to_csv(file_path)
        print(f'Saved "{fr.name}" to "{file_path}"')

    def list_existing_files(self):
        return list(RTINGS_PATH.joinpath('data').glob('**/*.csv'))


class RtingsCrawlError(Exception):
    pass


class RtingsProcessingError(Exception):
    pass
