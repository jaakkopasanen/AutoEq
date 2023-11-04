# -*- coding: utf-8 -*-

import sys
from pathlib import Path
import numpy as np
import json
from autoeq.frequency_response import FrequencyResponse
from dbtools.crinacle_crawler_base import CrinacleCrawlerBase
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.name_index import NameIndex, NameItem
from dbtools.constants import MEASUREMENTS_PATH


class SquigCrawler(CrinacleCrawlerBase):
    def __init__(
            self, driver=None, delete_existing_on_prompt=True, redownload=False,
            username=None, name=None, dbs=None):
        if username is None:
            raise ValueError('username must be given')
        if name is None:
            raise ValueError('name must be given')
        if dbs is None:
            raise ValueError('dbs must be given')
        self.username = username
        self.name = name
        self.dbs = dbs
        super().__init__(driver=driver, delete_existing_on_prompt=delete_existing_on_prompt, redownload=redownload)
        self.book_maps = self.parse_books()

    @property
    def measurements_path(self):
        return MEASUREMENTS_PATH.joinpath(self.name)

    @property
    def base_url(self):
        return f'https://{self.username}.squig.link'

    def db_url(self, db):
        return f'{self.base_url}{db["folder"]}data'

    def parse_books(self):
        """Downloads parses phone books to get names

        Returns:
            NameIndex
        """
        self.measurements_path.joinpath('phone_books').mkdir(parents=True, exist_ok=True)
        book_maps = {}
        for db in self.dbs:
            # 4620 measurements name index
            raw = self.download(
                f'{self.db_url(db)}/phone_book.json',
                self.measurements_path.joinpath('phone_books', f'{db["type"]}.json'), headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
                })
            book_maps[db['type']] = self.parse_book(json.loads(raw.decode('utf-8')))
        return book_maps

    def read_name_index(self):
        path = self.measurements_path.joinpath('name_index.tsv')
        if not path.exists():
            return NameIndex()
        return NameIndex.read_tsv(path)

    def write_name_index(self):
        self.name_index.write_tsv(self.measurements_path.joinpath('name_index.tsv'))

    def source_group_key(self, item):
        return '/'.join(item.url.split('/')[:-1] + [self.normalize_file_name(item.url.split('/')[-1])])

    def crawl(self):
        self.name_index = self.read_name_index()
        self.crawl_index = NameIndex()
        for db in self.dbs:
            document = self.get_beautiful_soup(self.db_url(db), use_selenium=False, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
            })
            # Iterate table rows from 4th to second to last. The first three are headers and the last is footer.
            for row in document.find_all('tr')[3:-1]:
                anchor = row.find('a')
                self.crawl_index.add(
                    NameItem(
                        source_name=anchor.text,
                        form='in-ear' if db['type'] == 'IEMs' else 'over-ear',
                        url=f'{self.db_url(db)}/{anchor["href"]}',
                        rig=db['rig'] if 'rig' in db and db['rig'] else None  # TODO
                    ))
        return self.crawl_index

    def raw_path(self, item):
        return self.measurements_path.joinpath('raw_data', item.form, item.url.split('/')[-1])

    def get_item_from_url(self, url):
        index_item = self.name_index.find_one(url=url)
        if index_item is not None:  # Existing item in the name index, ground truth
            item = index_item.copy()
        else:
            item = NameItem(url=url)
        return item

    def guess_name(self, item):
        """Gets intermediate name with false name."""
        print(item.url)
        self.download(item.url, self.raw_path(item), headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
        })
        name = item.source_name
        if name is None:  # This checks if a known item already exists in name index
            name = self.get_item_from_url(item.url).source_name
        if name is None:  # This looks for a name in the phone book
            normalized_file_name = self.normalize_file_name(item.url.split('/')[-1])
            if item.form is not None:  # Form is known, use the phone book
                if normalized_file_name in self.book_maps[item.form]:
                    name = self.book_maps[item.form][normalized_file_name]
            else:  # Form is not know, iterate through all phone books
                for book_map in self.book_maps.values():
                    if normalized_file_name in book_map:
                        name = book_map[normalized_file_name]
                        break
        if name is None:  # Name still not known, resort to (normalized) file name
            name = self.normalize_file_name(item.url.split('/')[-1])
        return name

    def process_group(self, items, new_only=True):
        if items[0].is_ignored:
            return
        file_path = self.target_path(items[0])
        if new_only and file_path.exists():
            return
        avg_fr = FrequencyResponse(name=items[0].name)
        avg_fr.raw = np.zeros(avg_fr.frequency.shape)
        for item in items:
            self.download(item.url, self.raw_path(item))
            fr = FrequencyResponse.read_csv(self.raw_path(item))
            fr.interpolate()
            fr.center()
            avg_fr.raw += fr.raw
        avg_fr.raw /= len(items)
        Path(file_path.parent).mkdir(exist_ok=True, parents=True)
        avg_fr.write_csv(file_path)
