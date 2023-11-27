# -*- coding: utf-8 -*-

import sys
import urllib
from abc import abstractmethod, ABC
from pathlib import Path
import re
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.crawler import Crawler


class CrinacleCrawlerBase(Crawler, ABC):
    def __init__(self, driver=None, delete_existing_on_prompt=True, redownload=False):
        super().__init__(driver=driver, delete_existing_on_prompt=delete_existing_on_prompt, redownload=redownload)

    @property
    @abstractmethod
    def measurements_path(self):
        pass

    @staticmethod
    def parse_book(data):
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
    def normalize_file_name(file_name):
        file_name = urllib.parse.unquote(file_name)
        file_name = re.sub(r' [LR]\d?\.txt$', '', file_name)
        file_name = re.sub(r'\.txt$', '', file_name)
        return file_name

    @abstractmethod
    def source_group_key(self, item):
        pass

    def resolve(self, item):
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
