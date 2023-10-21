# -*- coding: utf-8 -*-

import os
from pathlib import Path, WindowsPath
import sys
import re
from time import time
import numpy as np
import requests
from autoeq.frequency_response import FrequencyResponse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex, NameItem
from measurements.crawler import Crawler

CRINACLE_PATH = Path(__file__).parent
ROOT_PATH = CRINACLE_PATH.parent.parent


class UnknownRigError(Exception):
    pass


class CrinacleCrawler(Crawler):
    raw_data_rig_map = {
        '4620 IEM Measurements': 'Bruel & Kjaer 4620',
        'EARS + 711 (TSV txt) (Legacy)': 'EARS + 711',
        'GRAS 43AG-7': 'GRAS 43AG-7',
        'IEC60318-4 IEM Measurements (TSV txt)': '711',
    }

    raw_data_form_map = {
        '4620 IEM Measurements': 'in-ear',
        'EARS + 711 (TSV txt) (Legacy)': 'over-ear',
        'GRAS 43AG-7': 'over-ear',
        'IEC60318-4 IEM Measurements (TSV txt)': 'in-ear',
    }

    def __init__(self, driver=None):
        super().__init__(driver=driver)
        self.book_index = self.parse_books()

    def parse_books(self):
        """Downloads parses phone books to get names

        Returns:
            NameIndex
        """
        # 4620 measurements name index
        res = requests.get('https://crinacle.com/graphing/data_4620/phone_book.json')
        bk4620_book = self.parse_book(res.json())
        # Ears-711 measurements name index
        res = requests.get('https://crinacle.com/graphing/data_hp/phone_book.json')
        ears_711_map = self.parse_book(res.json())
        # Gras measurements name index
        res = requests.get('https://crinacle.com/graphing/data_hp_gras/phone_book.json')
        gras_map = self.parse_book(res.json())
        # 711 IEM measurements name index
        res = requests.get('https://crinacle.com/graphing/data/phone_book.json')
        iem_711_map = self.parse_book(res.json())
        return {
            '4620 IEM Measurements': bk4620_book,
            'EARS + 711 (TSV txt) (Legacy)': ears_711_map,
            'GRAS 43AG-7': gras_map,
            'IEC60318-4 IEM Measurements (TSV txt)': iem_711_map,
        }

    def parse_book(self, data):
        """Parses a phone book as dict with false names as keys and true names as values.

        Args:
            data: Phone book object

        Returns:
            Dict with phone book file names as keys and and phone book names as values
        """
        book = dict()
        for manufacturer in data:
            # Manufacturer name in the phone books is made up of "name" and potentially "suffix"
            # e.g. name="Final", suffix="Audio Design" --> "Final Audio Design"
            manufacturer_name = manufacturer['name']
            if 'suffix' in manufacturer:
                manufacturer_name += f' {manufacturer["suffix"]}'
            for model in manufacturer['phones']:
                if type(model) == str:
                    # Sometimes the model is nothing but a single string
                    book[model.strip()] = f'{manufacturer_name} {model}'.strip()
                else:
                    # Sometimes the model is an object with "name", "collab", list of "file"s and list of "suffix"es
                    # Collab(oration) field is ignored, naming needs to be checked manually against other dbs anyways
                    if type(model['file']) == str:  # Wrap a single file string in list to iterate with others
                        model['file'] = [model['file']]
                    if 'suffix' in model:
                        # Suffixes indicate modes (passive, active, ANC, ...) and other such things
                        # When suffix field is present, the suffixes and files are lists with matching indexes for
                        # the items
                        for file_name, suffix in zip(model['file'], model['suffix']):
                            book[file_name.strip()] = f'{manufacturer_name} {model["name"]} {suffix}'
                    else:
                        for file_name in model['file']:
                            book[file_name.strip()] = f'{manufacturer_name} {model["name"]}'
        return book

    @staticmethod
    def read_name_index():
        return NameIndex.read_tsv(CRINACLE_PATH.joinpath('name_index.tsv'))

    def write_name_index(self):
        self.name_index.write_tsv(CRINACLE_PATH.joinpath('name_index.tsv'))

    @staticmethod
    def get_existing():
        # FIXME: Tanchjim Zero exists in 711 measurements, seeing that in 4620 raw_data will be ignored when crawling
        return NameIndex.read_files(os.path.join(CRINACLE_PATH, 'data', '**', '*.csv'))

    @staticmethod
    def get_url_from_file_path(raw_data_file_path):
        """Creates URL from file path"""
        url = raw_data_file_path.relative_to(ROOT_PATH)
        return 'file://' + str(url).replace('\\', '/') if type(url) == WindowsPath else str(url)

    def get_item_from_file_path(self, raw_data_file_path):
        """Creates NameItem from path to a TXT file in raw_data"""
        url = self.get_url_from_file_path(raw_data_file_path)
        index_item = self.name_index.find_one(url=url)
        if index_item is not None:  # Existing item in the name index, ground truth
            item = NameItem(index_item.source_name, index_item.name, index_item.form, url=url, rig=None)
        else:
            item = NameItem(
                None, None,
                self.raw_data_form_map[raw_data_file_path.parent.name],
                url=url,
                rig=self.raw_data_rig_map[raw_data_file_path.parent.name])
        return item

    def crawl(self):
        self.name_index = self.read_name_index()
        items = []
        for dir_path in CRINACLE_PATH.joinpath('raw_data').glob('*'):
            for item in [self.get_item_from_file_path(fp) for fp in dir_path.glob('*.txt')]:
                if item.form != 'ignore':
                    items.append(item)
        self.crawl_index = NameIndex(items=items)
        return self.crawl_index

    @staticmethod
    def get_file_path_from_url(url):
        return Path(re.sub(r'^file://', '', url)).resolve()

    @staticmethod
    def normalize_file_name(file_name):
        file_name = re.sub(r' #\d+ [LR]\.txt$', '', file_name)
        file_name = re.sub(r' [LR](?:\d+)?\.txt$', '', file_name)
        file_name = re.sub(r'\.txt$', '', file_name)
        return file_name

    def source_group_key(self, item):
        return self.normalize_file_name(re.sub(r'^file://', '', item.url))

    def resolve_name(self, item):
        """Resolve name for a single item. Updates the item in place.

        Args:
            item: The crawl index NameItem to resolve

        Returns:
            True if resolution was successful, False if user needs to be prompted
        """
        group_key = self.source_group_key(item)
        for true_item in self.name_index.items:
            if group_key == self.source_group_key(true_item):
                if true_item.name is not None:
                    item.name = true_item.name
                if true_item.source_name is not None:
                    item.source_name = true_item.source_name
                if true_item.form is not None:
                    item.form = true_item.form
                if true_item.rig is not None:
                    item.rig = true_item.rig
                return item
        return None

    def guess_name(self, item):
        """Gets intermediate name with false name."""
        name = item.source_name
        if name is None:
            file_path = self.get_file_path_from_url(item.url)
            item_from_url = self.get_item_from_file_path(file_path)
            name = item_from_url.source_name
        if name is None:
            normalized_file_name = self.normalize_file_name(file_path.name)
            if normalized_file_name in self.book_index[file_path.parent.name]:
                name = self.book_index[file_path.parent.name][normalized_file_name]
            else:
                return normalized_file_name
        name = name.replace('(w/ ', '(')
        name = re.sub(r' pads\)', ' earpads)', name, flags=re.IGNORECASE)
        match = re.search(r' S\d+[$ ](?:\.txt)?$', name)
        if match:
            name = re.sub(r' S(\d+)[$ ]', r' (sample \1) ', name)
            name = re.sub(r'\s{2,}', ' ', name)
        return name

    def target_group_key(self, item):
        return f'{item.form}/{item.rig}/{item.name}'

    def target_path(self, item):
        if item.form is None or item.rig is None or item.name is None:
            return None
        return CRINACLE_PATH.joinpath('data', item.form, item.rig, f'{item.name}.csv')

    def process_group(self, items, new_only=True):
        if items[0].form == 'ignore':
            return
        file_path = self.target_path(items[0])
        if new_only and file_path.exists():
            return
        avg_fr = FrequencyResponse(name=items[0].name)
        avg_fr.raw = np.zeros(avg_fr.frequency.shape)
        for item in items:
            fr = FrequencyResponse.read_from_csv(self.get_file_path_from_url(item.url))
            fr.interpolate()
            fr.center()
            avg_fr.raw += fr.raw
        avg_fr.raw /= len(items)
        Path(file_path.parent).mkdir(exist_ok=True, parents=True)
        avg_fr.write_to_csv(file_path)
        print(f'Saved "{avg_fr.name}" to "{file_path}" with {len(items)} measurements')
