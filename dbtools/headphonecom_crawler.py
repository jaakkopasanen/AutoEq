# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from autoeq.utils import is_file_name_allowed
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.name_index import NameIndex, NameItem
from dbtools.crawler import Crawler
from dbtools.constants import MEASUREMENTS_PATH

HEADPHONECOM_PATH = MEASUREMENTS_PATH.joinpath('Headphone.com Legacy')


class HeadphonecomCrawler(Crawler):
    def read_name_index(self):
        self.name_index = NameIndex()
        for fp in HEADPHONECOM_PATH.joinpath('data').glob('**/*.csv'):
            self.name_index.add(NameItem(name=fp.name.replace('.csv', ''), form=fp.parent.name, rig='HMS II.3'))
        return self.name_index

    def write_name_index(self):
        return

    def update_name_index(self, item, write=True):
        return

    def crawl(self):
        raise NotImplementedError('Headphone.com Legacy graphs cannot be processed anymore')

    def resolve(self, item):
        raise NotImplementedError('Headphone.com Legacy graphs cannot be processed anymore')

    def guess_name(self, item):
        raise NotImplementedError('Headphone.com Legacy graphs cannot be processed anymore')

    def target_group_key(self, item):
        return f'{item.form}/{item.name}'

    def target_path(self, item):
        if item.is_ignored or item.form is None or item.name is None:
            return None
        path = HEADPHONECOM_PATH.joinpath('data', item.form, f'{item.name}.csv')
        if not is_file_name_allowed(item.name):
            raise ValueError(f'Target path cannot be "{path}"')
        return path

    def process_group(self, items, new_only=True):
        raise NotImplementedError('Headphone.com Legacy graphs cannot be processed anymore')

    def list_existing_files(self):
        return list(HEADPHONECOM_PATH.joinpath('data').glob('**/*.csv'))
