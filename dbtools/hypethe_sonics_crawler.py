# -*- coding: utf-8 -*-
import re
import sys
import urllib
from pathlib import Path
import numpy as np
import json
import requests
from autoeq.csv import CsvParseError
from autoeq.frequency_response import FrequencyResponse
from autoeq.utils import make_file_name_allowed, is_file_name_allowed
from dbtools.crawler import Crawler
from dbtools.crinacle_crawler_base import CrinacleCrawlerBase
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.name_index import NameIndex, NameItem
from dbtools.constants import MEASUREMENTS_PATH


class HypetheSonicsCrawler(CrinacleCrawlerBase):
    def __init__(
            self, driver=None, delete_existing_on_prompt=True, redownload=False):
        super().__init__(driver=driver, delete_existing_on_prompt=delete_existing_on_prompt, redownload=redownload)

    @property
    def measurements_path(self):
        return MEASUREMENTS_PATH.joinpath('HypetheSonics')

    def source_group_key(self, item):
        return '/'.join(item.url.split('/')[:-1] + [self.normalize_file_name(item.url.split('/')[-1])])

    def crawl(self):
        self.name_index = self.read_name_index()
        self.crawl_index = NameIndex()
        raw = self.download(
            'https://www.hypethesonics.com/dbc/SPLdata/phone_book.json',
            self.measurements_path.joinpath('phone_book_iemdbc.json'))
        iemdbc_map = self.parse_book(json.loads(raw.decode('utf-8')))
        for file_name, source_name in iemdbc_map.items():
            self.crawl_index.add(NameItem(
                source_name=source_name, form='in-ear', rig='GRAS RA0045',
                url=f'https://www.hypethesonics.com/dbc/SPLdata/{file_name} L.txt'))
            self.crawl_index.add(NameItem(
                source_name=source_name, form='in-ear', rig='GRAS RA0045',
                url=f'https://www.hypethesonics.com/dbc/SPLdata/{file_name} R.txt'))
        raw = self.download(
            'https://www.hypethesonics.com/hatsdbc/SPLdata/phone_book.json',
            self.measurements_path.joinpath('phone_book_iemhatsdbc.json'))
        iemhatsdbc_map = self.parse_book(json.loads(raw.decode('utf-8')))
        for file_name, source_name in iemhatsdbc_map.items():
            self.crawl_index.add(NameItem(
                source_name=source_name, rig='Bruel & Kjaer 5128',
                url=f'https://www.hypethesonics.com/hatsdbc/SPLdata/{file_name} L.txt'))
            self.crawl_index.add(NameItem(
                source_name=source_name, rig='Bruel & Kjaer 5128',
                url=f'https://www.hypethesonics.com/hatsdbc/SPLdata/{file_name} R.txt'))
        for item in self.crawl_index.items:
            self.resolve(item)
        return self.crawl_index

    def raw_data_path(self, item):
        return self.measurements_path.joinpath(
            'raw_data', item.form,
            make_file_name_allowed(urllib.parse.unquote(item.url.split('/')[-1])))

    def guess_name(self, item):
        """Gets intermediate name with false name."""
        item = self.crawl_index.find_one(url=item.url)
        if item.name is not None:
            return item.name
        return self.manufacturers.replace(item.source_name)

    def resolve(self, item):
        ground_truth = self.name_index.find_one(url=item.url)  # Find with exact URL first
        if not ground_truth:
            # No exact URL match, find with normalized URL
            group_key = self.source_group_key(item)
            for true_item in self.name_index.items:
                if self.source_group_key(true_item) == group_key:
                    ground_truth = true_item
                    break
        if ground_truth:
            if ground_truth.name:
                item.name = ground_truth.name
            if ground_truth.form:
                item.form = ground_truth.form

    def target_path(self, item):
        if item.is_ignored or item.form is None or item.rig is None or item.name is None:
            return None
        if item.form == 'in-ear':
            path = self.measurements_path.joinpath('data', item.form, item.rig, f'{item.name}.csv')
        else:
            path = self.measurements_path.joinpath('data', item.form, f'{item.name}.csv')
        if not is_file_name_allowed(item.name):
            raise ValueError(f'Target path cannot be "{path}"')
        return path

    def process_group(self, items, new_only=True):
        if items[0].is_ignored:
            return
        file_path = self.target_path(items[0])
        if new_only and file_path.exists():
            return
        avg_fr = FrequencyResponse(name=items[0].name)
        avg_fr.raw = np.zeros(avg_fr.frequency.shape)
        for item in items:
            self.download(item.url, self.raw_data_path(item))
            try:
                fr = FrequencyResponse.read_csv(self.raw_data_path(item))
            except CsvParseError as err:
                print(f'Failed to parse "{self.raw_data_path(item)}": {str(err)}')
                return
            fr.interpolate()
            fr.center()
            avg_fr.raw += fr.raw
        avg_fr.raw /= len(items)
        Path(file_path.parent).mkdir(exist_ok=True, parents=True)
        avg_fr.write_csv(file_path)
