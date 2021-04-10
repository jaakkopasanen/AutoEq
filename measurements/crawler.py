# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(1, str(Path(__file__).resolve().parent))
import pandas as pd
from rapidfuzz import fuzz
import requests
import shutil
import re
from bs4 import BeautifulSoup
import ipywidgets as widgets
import webbrowser
from abc import ABC, abstractmethod
from time import sleep
from measurements.name_index import NameIndex, NameItem
from measurements.manufacturer_index import ManufacturerIndex
from measurements.name_prompt import NamePrompt

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class Crawler(ABC):
    def __init__(self, driver=None):
        self.driver = driver
        self.name_index = self.read_name_index()
        self.manufacturers = ManufacturerIndex()
        self.name_proposals = None
        self.init_name_proposals()
        self.existing = self.get_existing()
        self.urls = self.get_urls()

        # UI
        self.prompts = widgets.VBox([])
        self.iframe = widgets.VBox([])
        self.widget = widgets.HBox([self.prompts, self.iframe])

    @staticmethod
    @abstractmethod
    def read_name_index():
        """Reads name index as Index

        Returns:
            NameIndex
        """
        pass

    def init_name_proposals(self):
        """Gets name proposals for new measurements

        Returns:
            NameIndex
        """
        name_proposals = NameIndex()
        for db in ['crinacle', 'oratory1990', 'rtings', 'referenceaudioanalyzer']:
            name_index = NameIndex.read_tsv(os.path.join(DIR_PATH, db, 'name_index.tsv'))
            name_proposals.concat(name_index)
        for db in ['innerfidelity', 'headphonecom']:
            name_index = NameIndex.read_files(os.path.join(DIR_PATH, db, 'data', '**', '*.csv'))
            name_proposals.concat(name_index)
        name_proposals.remove_duplicates()

        manufacturer_pattern = rf'^({"|".join([m[0] for m in self.manufacturers.manufacturers])})'
        proposal_data = {
            'form': [],
            'manufacturer': [],
            'model': []
        }
        for item in name_proposals.items:
            if not item.true_name or item.form == 'ignore':
                continue
            manufacturer = re.search(manufacturer_pattern, item.true_name, flags=re.IGNORECASE)
            if not manufacturer:
                continue
            manufacturer = manufacturer[0]
            proposal_data['form'].append(item.form)
            proposal_data['manufacturer'].append(manufacturer)
            proposal_data['model'].append(item.true_name.replace(manufacturer, '').strip())
        self.name_proposals = pd.DataFrame(proposal_data)

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
    def get_urls(self):
        """Crawls measurement URLs

        Returns:
            Dict where headphone names are keys and URLs are values
        """
        pass

    @abstractmethod
    def process(self, item, url):
        """Downloads a single URL and processes it

        Args:
            item: Item
            url: URL to measurement

        Returns:
            None
        """
        pass

    def update_name_index(self, item):
        """Updates name index"""
        exact_match = self.name_index.find_one(false_name=item.false_name, true_name=item.true_name, form=item.form)
        if not exact_match:
            self.name_index.update(item, false_name=item.false_name)
            self.write_name_index()

    def prompt_callback(self, false_name, url):
        def callback(true_name, form):
            self.process(NameItem(false_name, true_name, form), url)
        return callback

    def process_new(self):
        """Processes all new measurements

        Updates name index with the new entries now found in the name index previously.

        Returns:
            None
        """
        prompts = []
        for false_name, url in self.urls.items():
            ni = self.name_index.find(false_name=false_name)
            item = ni.items[0] if ni else None
            if not item:
                # Name doesn't exist in the name index
                manufacturer, manufacturer_match = self.manufacturers.find(false_name)
                name_proposals = self.get_name_proposals(false_name)
                prompts.append(NamePrompt(false_name, name_proposals, lambda *args, **kwargs: None).widget)
        self.widget.children = prompts

    def search(self, name):
        url = f'https://google.com/search?q={name.replace(" ", "+")}&tbm=isch'
        webbrowser.open(url)

    def get_name_proposals(self, false_name):
        """Prompts manufacturer, model and form from the user

        Args:
            false_name: Name as it exists in the measurement source

        Returns:
            NameItem
        """
        false_name = self.intermediate_name(false_name)
        manufacturer, manufacturer_match = self.manufacturers.find(false_name)
        if not manufacturer:
            return NameIndex([])
        false_model = re.sub(re.escape(manufacturer_match), '', false_name, flags=re.IGNORECASE).strip()
        # Select only the items with the same manufacturer
        models = self.name_proposals[self.name_proposals.manufacturer == manufacturer]
        scores = [fuzz.ratio(model.lower(), false_model.lower()) for model in models.model.tolist()]
        models = models.assign(score=scores)
        models = models[models.score > 60]
        models.sort_values('score', ascending=False, inplace=True)
        proposals = []
        for i, row in models.iterrows():
            proposals.append(NameItem(None, f'{manufacturer} {row.model}', row.form))
        return NameIndex(items=proposals)

    def intermediate_name(self, false_name):
        """Gets intermediate name with false name."""
        return false_name

    @staticmethod
    def download(url, true_name, output_dir, file_type=None):
        """Downloads a file from a URL

        Args:
            url: URL to download
            true_name: True name of the item to download
            output_dir: Where to write the downloaded file
            file_type: File extension. Detected automatically if None.

        Returns:
            Bool depicting if download succeeded or not
        """
        output_dir = os.path.abspath(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        res = requests.get(url, stream=True)
        if res.status_code != 200:
            print(f'Failed to download "{true_name}" at "{url}"')
            return None
        if file_type is None:
            file_type = url.split('.')[-1]
            file_type = file_type.split('?')[0]
        file_path = os.path.join(output_dir, '{}.{}'.format(true_name, file_type))
        with open(file_path, 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print('Downloaded to "{}"'.format(file_path))
        return file_path

    def get_beautiful_soup(self, url):
        self.driver.get(url)
        sleep(1)  # Giving some time for Selenium to render the page
        html = self.driver.find_element_by_tag_name('html').get_attribute('outerHTML')
        return BeautifulSoup(html, 'html.parser')
