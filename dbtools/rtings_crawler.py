# -*- coding: utf-8 -*-

import sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from tqdm.auto import tqdm
import json
import re
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from autoeq.frequency_response import FrequencyResponse
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.name_index import NameIndex, NameItem
from dbtools.crawler import Crawler, ProcessingError
from dbtools.constants import MEASUREMENTS_PATH


class RtingsCrawler(Crawler):
    def __init__(self, driver=None, delete_existing_on_prompt=True, redownload=False):
        if driver is None:
            opts = Options()
            opts.add_argument('--headless')
            driver = webdriver.Chrome(options=opts)
        super().__init__(driver=driver, delete_existing_on_prompt=delete_existing_on_prompt, redownload=redownload)

    @property
    def measurements_path(self):
        return MEASUREMENTS_PATH.joinpath('Rtings')

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
        for version in ['1-6', '1-5', '1-4', '1-2']:
            html = requests.get(f'https://www.rtings.com/headphones/{version}/graph').text
            document = BeautifulSoup(html, 'html.parser')
            test_bench = json.loads(document.find(class_='app-body').find('div').get('data-props'))['test_bench']
            for product in test_bench['comparable_products']:
                if product["fullname"] in [payload['source_name'] for payload in product_graph_data_url_payloads]:
                    # The versions are iterated from newest to oldest, if product with the same name already exists,
                    # that means it was included in the results of the newer test methodology and so this one can
                    # be skipped
                    continue
                # IDs of all the tests done for the current headphone
                tids = set([test_result['test']['original_id'] for test_result in product['review']['test_results']])
                valid_test_ids = []
                # Look for test IDs that correspond to left channel raw frequency response
                matching_raw_fr_l_ids = [
                    tid for tid in tids if tid in ['4011', '7917', '21564', '1344', '2060', '3182']]
                if matching_raw_fr_l_ids:
                    valid_test_ids.append(matching_raw_fr_l_ids[0])
                # Look for test IDs that correspond to right channel raw frequency response
                matching_raw_fr_r_ids = [
                    tid for tid in tids if tid in ['4012', '7918', '21565', '1343', '2061', '3183']]
                if matching_raw_fr_r_ids:
                    valid_test_ids.append(matching_raw_fr_r_ids[0])
                if not valid_test_ids:
                    # This must be one of the tests that don't have raw FR, but instead has bass, mid and treble, skip
                    continue
                product_graph_data_url_payloads.append({
                    'source_name': product['fullname'],
                    'payloads': [{
                        'named_version': 'public',
                        'product_id': product['id'],
                        'test_original_id': test_id
                    } for test_id in valid_test_ids]
                })
        return product_graph_data_url_payloads

    @staticmethod
    def graph_data_url(payload):
        """Fetches URL for JSON file from API"""
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
        if self.measurements_path.joinpath('crawl_graph_data_urls.json').exists():
            with open(self.measurements_path.joinpath('crawl_graph_data_urls.json')) as fh:
                graph_data_url_cache = json.load(fh)
        else:
            graph_data_url_cache = {}
        self.name_index = self.read_name_index()
        self.crawl_index = NameIndex()
        for product_payloads in tqdm(self.graph_data_url_payloads()):
            for payload in product_payloads['payloads']:
                item = NameItem(source_name=product_payloads['source_name'], rig='HMS II.3')
                cache_key = f'{payload["product_id"]}/{payload["test_original_id"]}'
                if cache_key in graph_data_url_cache:  # Item found in cache
                    item.url = graph_data_url_cache[cache_key]
                else:  # Item not found in cache, get URL with API call
                    item.url = self.graph_data_url(payload)
                if item.url is not None:
                    graph_data_url_cache[cache_key] = item.url
                self.resolve(item)
                self.crawl_index.add(item)
        with open(self.measurements_path.joinpath('crawl_graph_data_urls.json'), 'w', encoding='utf-8') as fh:
            json.dump(graph_data_url_cache, fh, ensure_ascii=False, indent=4)
        return self.crawl_index

    def json_path(self, item):
        uid = item.url.split('/')[-2]
        return self.measurements_path.joinpath('json', f'{uid}.json')

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
        col_ix = None
        for col_name in ['Left Avg', 'Right Avg']:
            if col_name in header:
                col_ix = header.index(col_name)
                break
        if col_ix is None:
            raise ProcessingError('Could not find any of the data columns in JSON')
        fr = FrequencyResponse(name='fr', frequency=frequency, raw=data[:, col_ix], target=target)
        return fr

    def process_group(self, items, new_only=True):
        if items[0].is_ignored:
            return
        if len(items) == 0 or len(items) > 2:
            raise ProcessingError(f'{len(items)} measurements grouped together, don\'t know what to do.')
        file_path = self.target_path(items[0])
        if new_only and file_path.exists():
            return
        frs = []
        for item in items:
            raw = self.download(item.url, self.json_path(item))
            frs.append(self.parse_json(json.loads(raw.decode('utf-8'))))
        fr = FrequencyResponse(
            name=items[0].name,
            frequency=frs[0].frequency,
            raw=np.mean([fr.raw for fr in frs], axis=0))
        fr.interpolate()
        fr.center()
        # Write to file
        file_path.parent.mkdir(exist_ok=True, parents=True)
        fr.write_csv(file_path)

