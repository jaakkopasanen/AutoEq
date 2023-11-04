# -*- coding: utf-8 -*-

import sys
from pathlib import Path, WindowsPath
import re
import numpy as np
import json
from autoeq.frequency_response import FrequencyResponse
from dbtools.crinacle_crawler_base import CrinacleCrawlerBase

ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.name_index import NameIndex, NameItem
from dbtools.constants import MEASUREMENTS_PATH


class CrinacleCrawler(CrinacleCrawlerBase):
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

    def __init__(self, driver=None, delete_existing_on_prompt=True, redownload=False):
        super().__init__(driver=driver, delete_existing_on_prompt=delete_existing_on_prompt, redownload=redownload)
        self.book_maps = None

    @property
    def measurements_path(self):
        return MEASUREMENTS_PATH.joinpath('crinacle')

    def parse_books(self):
        """Downloads parses phone books to get names

        Returns:
            NameIndex
        """
        # 4620 measurements name index
        raw = self.download(
            'https://crinacle.com/graphing/data_4620/phone_book.json',
            self.measurements_path.joinpath('phone_book_4620.json'))
        bk4620_map = self.parse_book(json.loads(raw.decode('utf-8')))
        # Ears-711 measurements name index
        raw = self.download(
            'https://crinacle.com/graphing/data_hp/phone_book.json',
            self.measurements_path.joinpath('phone_book_hp.json'))
        ears_711_map = self.parse_book(json.loads(raw.decode('utf-8')))
        # Gras measurements name index
        raw = self.download(
            'https://crinacle.com/graphing/data_hp_gras/phone_book.json',
            self.measurements_path.joinpath('phone_book_hp_gras.json'))
        gras_map = self.parse_book(json.loads(raw.decode('utf-8')))
        # 711 IEM measurements name index
        raw = self.download(
            'https://crinacle.com/graphing/data/phone_book.json',
            self.measurements_path.joinpath('phone_book.json'))
        iem_711_map = self.parse_book(json.loads(raw.decode('utf-8')))
        return {
            '4620 IEM Measurements': bk4620_map,
            'EARS + 711 (TSV txt) (Legacy)': ears_711_map,
            'GRAS 43AG-7': gras_map,
            'IEC60318-4 IEM Measurements (TSV txt)': iem_711_map,
        }

    def read_name_index(self):
        self.name_index = NameIndex.read_tsv(self.measurements_path.joinpath('name_index.tsv'))
        return self.name_index

    def write_name_index(self):
        self.name_index.write_tsv(self.measurements_path.joinpath('name_index.tsv'))

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
            item = index_item.copy()
        else:
            item = NameItem(
                url=url,
                form=self.raw_data_form_map[raw_data_file_path.parent.name],
                rig=self.raw_data_rig_map[raw_data_file_path.parent.name])
        return item

    def crawl(self):
        self.book_maps = self.parse_books()
        self.name_index = self.read_name_index()
        self.crawl_index = NameIndex()
        for dir_path in self.measurements_path.joinpath('raw_data').glob('*'):
            for item in [self.get_item_from_file_path(fp) for fp in dir_path.glob('*.txt')]:
                self.crawl_index.add(item)
        return self.crawl_index

    @staticmethod
    def get_file_path_from_url(url):
        return ROOT_PATH.joinpath(re.sub(r'^file://', '', url))

    @staticmethod
    def normalize_file_name(file_name):
        # File names often have L.txt or R.txt to indicate which side of the headphone has been measured
        # Some file names indicate reseat number with #N before L/R.txt
        file_name = re.sub(r' #\d+ [LR]\.txt$', '', file_name)
        # Some file names have reseat number betwee L/R and .txt
        file_name = re.sub(r' [LR](?:\d+)?\.txt$', '', file_name)
        # some file names have nothing extra
        file_name = re.sub(r'\.txt$', '', file_name)
        return file_name

    def source_group_key(self, item):
        return self.normalize_file_name(re.sub(r'^file://', '', item.url))

    def guess_name(self, item):
        """Gets intermediate name with false name."""
        name = item.source_name
        if name is None:
            file_path = self.get_file_path_from_url(item.url)
            item_from_url = self.get_item_from_file_path(file_path)
            name = item_from_url.source_name
        if name is None:
            normalized_file_name = self.normalize_file_name(file_path.name)
            if normalized_file_name in self.book_maps[file_path.parent.name]:
                name = self.book_maps[file_path.parent.name][normalized_file_name]
            else:
                return normalized_file_name
        name = name.replace('(w/ ', '(')
        name = re.sub(r' pads\)', ' earpads)', name, flags=re.IGNORECASE)
        match = re.search(r' S\d+[$ ](?:\.txt)?$', name)
        if match:
            name = re.sub(r' S(\d+)[$ ]', r' (sample \1) ', name)
            name = re.sub(r'\s{2,}', ' ', name)
        return name

    def target_group_key(self, item):  # TODO: Check this
        return f'{item.form}/{item.rig}/{item.name}'

    def process_group(self, items, new_only=True):
        if items[0].is_ignored:
            return
        file_path = self.target_path(items[0])
        if new_only and file_path.exists():
            return
        avg_fr = FrequencyResponse(name=items[0].name)
        avg_fr.raw = np.zeros(avg_fr.frequency.shape)
        for item in items:
            fr = FrequencyResponse.read_csv(self.get_file_path_from_url(item.url))
            fr.interpolate()
            fr.center()
            avg_fr.raw += fr.raw
        avg_fr.raw /= len(items)
        Path(file_path.parent).mkdir(exist_ok=True, parents=True)
        avg_fr.write_csv(file_path)
