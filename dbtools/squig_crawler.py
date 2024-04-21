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
from autoeq.utils import make_file_name_allowed
from dbtools.crinacle_crawler_base import CrinacleCrawlerBase
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.name_index import NameIndex, NameItem
from dbtools.constants import MEASUREMENTS_PATH


_squig_rigs = {
    'Auriculares Argentina': {'in-ear': '711', 'over-ear': 'KB501x + 711'},
    'Bakkwatan': {'in-ear': '711'},
    'DHRME': {'in-ear': '711'},
    'Fahryst': {'in-ear': '711'},
    'Filk': {'in-ear': '711', 'over-ear': 'KB006x + 711'},
    'freeryder05': {'in-ear': '711'},
    'Harpo': {'in-ear': '711'},
    'Hi End Portable': {'in-ear': '711'},
    'Jaytiss': {'in-ear': '711'},
    'Kazi': {'in-ear': '711'},
    'kr0mka': {'in-ear': '711', 'over-ear': 'KB501x + 711'},
    'Kuulokenurkka': {'in-ear': '711', 'over-ear': 'KB501x + 711'},
    'Regan Cipher': {'in-ear': '711', 'over-ear': 'KB500x + 711'},
    'RikudouGoku': {'in-ear': '711'},
    'Super Review': {'in-ear': '711', 'over-ear': 'KB006x + 711'},
    'Ted\'s Squig Hoard': {'in-ear': '711', 'over-ear': 'KB500x + 711'},
    'ToneDeafMonk': {'in-ear': '711'},
}


class SquigCrawlerManager:
    def __init__(self):
        sites = requests.get('https://squig.link/squigsites.json', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
        }).json()
        self._crawlers = [
            SquigCrawler(
                username=site['username'],
                name=make_file_name_allowed(site['name']),
                dbs=site['dbs']
            ) for site in sites
        ]

    @property
    def crawlers(self):
        return iter(self._crawlers)

    def crawler(self, name):
        for crawler in self.crawlers:
            if name == crawler.name:
                return crawler

    def run(self, name):
        for crawler in self.crawlers:
            if crawler.name == name:
                crawler.run()
                return crawler
        raise ValueError(f'Unknown squig.link site "{name}"')

    def process(self, name=None, new_only=True):
        for crawler in self.crawlers:
            if name is None or crawler.name == name:
                crawler.process(new_only=new_only)
                if name is not None:
                    return


class SquigCrawler(CrinacleCrawlerBase):
    def __init__(
            self, driver=None, delete_existing_on_prompt=True, redownload=False,
            username=None, name=None, dbs=None):
        if username is None:
            raise ValueError('name must be given')
        if name is None:
            raise ValueError('name must be given')
        if dbs is None:
            raise ValueError('dbs must be given')
        self.username = username
        self.name = name
        self.dbs = dbs
        super().__init__(driver=driver, delete_existing_on_prompt=delete_existing_on_prompt, redownload=redownload)
        self.book_maps = None

    @property
    def measurements_path(self):
        return MEASUREMENTS_PATH.joinpath(make_file_name_allowed(self.name))

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
        book_maps = {}
        for db in self.dbs:
            # 4620 measurements name index
            raw = self.download(
                f'{self.db_url(db)}/phone_book.json',
                self.measurements_path.joinpath(f'phone_book_{db["type"]}.json'), headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
                })
            form = 'in-ear' if db['type'] == 'IEMs' else 'over-ear'
            book_maps[form] = self.parse_book(json.loads(raw.decode('utf-8')))
        return book_maps

    def source_group_key(self, item):
        return '/'.join(item.url.split('/')[:-1] + [self.normalize_file_name(item.url.split('/')[-1])])

    def crawl(self):
        self.book_maps = self.parse_books()
        self.name_index = self.read_name_index()
        self.crawl_index = NameIndex()
        for db in self.dbs:
            document = self.get_beautiful_soup(self.db_url(db), use_selenium=False, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
            })
            # Iterate table rows from 4th to second to last. The first three are headers and the last is footer.
            for row in document.find_all('tr')[3:-1]:
                anchor = row.find('a')
                form = 'in-ear' if db['type'] == 'IEMs' else 'over-ear'
                book = self.book_maps[form]
                file_name = anchor['href']
                if re.search(r'Target.txt$', file_name) or file_name == 'phone_book.json':  # Skip targets and book
                    continue
                normalized_file_name = self.normalize_file_name(urllib.parse.unquote(file_name))
                try:
                    rig = _squig_rigs[self.name][form]
                except KeyError as err:
                    print(f'{self.name} has no rig for {form}. Skipping {normalized_file_name}')
                    continue
                item = NameItem(
                        url=f'{self.db_url(db)}/{anchor["href"]}',
                        source_name=book[normalized_file_name] if normalized_file_name in book else None,
                        form=form,
                        rig=rig
                    )
                self.resolve(item)
                self.crawl_index.add(item)
        return self.crawl_index

    def raw_data_path(self, item):
        return self.measurements_path.joinpath('raw_data', item.form, make_file_name_allowed(urllib.parse.unquote(item.url.split('/')[-1])))

    def get_item_from_url(self, url):
        index_item = self.name_index.find_one(url=url)
        if index_item is not None:  # Existing item in the name index, ground truth
            item = index_item.copy()
        else:
            item = NameItem(url=url)
        return item

    def guess_name(self, item):
        """Gets intermediate name with false name."""
        name = item.source_name
        if name is None:  # This checks if a known item already exists in name index
            name = self.get_item_from_url(item.url).source_name
        if name is None:  # This looks for a name in the phone book
            normalized_file_name = self.normalize_file_name(item.url.split('/')[-1])
            if item.form is not None:  # Form is known, use the phone book
                if item.form in self.book_maps and normalized_file_name in self.book_maps[item.form]:
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
            self.download(item.url, self.raw_data_path(item), headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
            })
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
