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
import urllib.parse
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
            if form == 'ignore':
                self.update_name_index(NameItem(false_name, None, form))
                return
            if self.manufacturers.find(true_name, ignore_case=False)[0] is None:
                raise ValueError(f'Manufacturer of "{true_name}" not recognized!')
            item = NameItem(false_name, true_name, form)
            self.process(NameItem(false_name, true_name, form), url)
            self.update_name_index(item)
        return callback

    def process_new(self, prompt=True):
        """Processes all new measurements

        Updates name index with the new entries now found in the name index previously.

        Returns:
            None
        """
        prompts = []
        unknown_manufacturers = []
        for false_name, url in self.urls.items():
            item = self.name_index.find_one(false_name=false_name)
            if item and item.form == 'ignore':
                continue
            if not item:
                if not prompt:
                    print(f'{false_name} is unknown and prompting is prohibited, skipping the item.')
                    continue
                # Name doesn't exist in the name index
                intermediate_name = self.intermediate_name(false_name)
                manufacturer, manufacturer_match = self.manufacturers.find(intermediate_name)
                if manufacturer:
                    model = re.sub(re.escape(manufacturer_match), '', intermediate_name, flags=re.IGNORECASE).strip()
                    name_proposals = self.get_name_proposals(false_name)
                    similar_names = self.get_name_proposals(false_name, n=6, normalize_digits=True, threshold=0)
                    similar_names = [item.true_name for item in similar_names.items]
                else:
                    unknown_manufacturers.append(intermediate_name)
                    model = intermediate_name
                    name_proposals = None
                    similar_names = None
                # Not sure about the name, ask user
                prompts.append(NamePrompt(
                    model,
                    self.prompt_callback(false_name, url),
                    manufacturer=manufacturer,
                    name_proposals=name_proposals,
                    search_callback=self.search,
                    false_name=false_name,
                    similar_names=similar_names
                ).widget)
            else:
                existing = self.existing.find_one(true_name=item.true_name)
                if not existing:
                    # Name found in name index but the measurement doesn't exist
                    self.process(item, url)
        if len(unknown_manufacturers) > 0:
            print('Headphones with unknown manufacturers\n  ' + '\n  '.join(unknown_manufacturers))
            print('Add them to manufacturers.tsv and run this cell again')
        self.prompts.children = prompts

    def search(self, name):
        quoted = urllib.parse.quote_plus(name)
        url = f'https://google.com/search?q={quoted}&tbm=isch'
        webbrowser.open(url)

    def get_name_proposals(self, false_name, n=4, normalize_digits=False, normalize_extras=False, threshold=60):
        """Prompts manufacturer, model and form from the user

        Args:
            false_name: Name as it exists in the measurement source
            n: Number of proposals to return
            normalize_digits: Normalize all digits to zeros before calculating fuzzy string matching score
            normalize_extras: Remove extra details in the parentheses
            threshold: Score threshold

        Returns:
            NameItem
        """
        def fuzzy(fn, a, b):
            a = a.lower()
            b = b.lower()
            if normalize_digits:
                a = re.sub(r'\d', '0', a).strip()
                b = re.sub(r'\d', '0', b).strip()
            if normalize_extras:
                a = re.sub(r'\(.+\)$', '', a).strip()
                b = re.sub(r'\(.+\)$', '', b).strip()
            return fn(a, b)

        manufacturer, manufacturer_match = self.manufacturers.find(false_name)
        if not manufacturer:
            return NameIndex([])
        false_model = re.sub(re.escape(manufacturer_match), '', false_name, flags=re.IGNORECASE).strip()
        # Select only the items with the same manufacturer
        models = self.name_proposals[self.name_proposals.manufacturer == manufacturer]

        # Calculate ratios
        partial_ratios = [fuzzy(fuzz.partial_ratio, model, false_model) for model in models.model.tolist()]
        ratios = [fuzzy(fuzz.ratio, model, false_model) for model in models.model.tolist()]

        models = models.assign(partial_ratio=partial_ratios)
        models = models.assign(ratio=ratios)
        models = models[models.partial_ratio >= threshold]
        models.sort_values('ratio', ascending=False, inplace=True)
        proposals = []
        for i, row in models.iterrows():
            proposals.append(NameItem(None, f'{manufacturer} {row.model}', row.form))
        ni = NameIndex(items=proposals)
        ni.df = ni.df.head(n)
        return ni

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
        file_path = os.path.join(output_dir, f'{true_name}.{file_type}')
        with open(file_path, 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print('Downloaded to "{}"'.format(file_path))
        return file_path

    def get_beautiful_soup(self, url):
        self.driver.get(url)
        sleep(2)  # Giving some time for Selenium to render the page
        html = self.driver.find_element_by_tag_name('html').get_attribute('outerHTML')
        return BeautifulSoup(html, 'html.parser')
