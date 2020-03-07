# -*- coding: utf-8 -*-

import os
import sys
import requests
import shutil
import json
from abc import ABC, abstractmethod
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.name_index import NameItem
from measurements.utils import prompt_name, prompt_form


class Crawler(ABC):
    def __init__(self, driver=None):
        self.driver = driver
        self.name_index = self.read_name_index()
        self.existing = self.get_existing()
        self.links = self.get_links()

    @staticmethod
    @abstractmethod
    def read_name_index():
        """Reads name index as Index

        Returns:
            Index
        """
        pass

    @abstractmethod
    def write_name_index(self):
        """Writes name index to a file

        Returns:
            Index
        """
        pass

    @staticmethod
    @abstractmethod
    def get_existing():
        """Reads existing files as Index

        Returns:
            Index
        """
        pass

    @abstractmethod
    def get_links(self):
        """Crawls measurement links

        Returns:
            Dict where headphone names are keys and URLs are values
        """
        pass

    @staticmethod
    @abstractmethod
    def process(item, link):
        """Downloads a single link and processes it

        Args:
            item: Item
            link: URL to measurement

        Returns:
            None
        """
        pass

    def process_new(self, prompt=True):
        """Processes all new measurements

        Updates name index with the new entries now found in the name index previously.

        Returns:
            None
        """
        for false_name, link in self.links.items():
            try:
                item = self.name_index.find_by_false_name(false_name)
                if item:
                    # Name index contains the entry
                    if self.existing.find_by_true_name(item.true_name):
                        # Exists already, skip
                        continue
                    self.process(item, link)
                else:
                    if prompt:
                        print(f'"{false_name}" is not known.')
                        true_name = prompt_name([false_name])
                        form = prompt_form()
                        item = NameItem(false_name, true_name, form)
                        self.name_index.add(item)
                        self.process(item, link)
                    else:
                        print(f'"{false_name}" is not known. Add true name and form to name index and run this again.')
                        self.name_index.add(NameItem(false_name, None, None))

            except Exception as err:
                raise err
                print(f'Failed to process {false_name}: {str(err)}')

    @staticmethod
    def download(url, true_name, output_dir, file_type=None):
        output_dir = os.path.abspath(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        res = requests.get(url, stream=True)
        if res.status_code != 200:
            print(f'Failed to download "{true_name}" at "{url}"')
            return False
        if file_type is None:
            file_type = url.split('.')[-1]
            file_type = file_type.split('?')[0]
        file_path = os.path.join(output_dir, '{}.{}'.format(true_name, file_type))
        with open(file_path, 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print('Downloaded to "{}"'.format(file_path))
        return True
