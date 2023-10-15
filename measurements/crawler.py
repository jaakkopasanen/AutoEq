# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
from measurements.PromptListItem import PromptListItem
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
from selenium.webdriver.common.by import By
import urllib.parse
from abc import ABC, abstractmethod
from time import sleep
from measurements.name_index import NameIndex, NameItem
from measurements.manufacturer_index import ManufacturerIndex
from measurements.name_prompt import NamePrompt

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class UnknownManufacturerError(Exception):
    pass


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
        self.prompts = []
        self.prompt_list = None
        self.active_list_item = None
        self.widget = widgets.HBox([])

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
        for db in ['crinacle', 'oratory1990', 'rtings']:
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
            if not item.name or item.form == 'ignore':
                continue
            manufacturer = re.search(manufacturer_pattern, item.name, flags=re.IGNORECASE)
            if not manufacturer:
                continue
            manufacturer = manufacturer[0]
            proposal_data['form'].append(item.form)
            proposal_data['manufacturer'].append(manufacturer)
            proposal_data['model'].append(item.name.replace(manufacturer, '').strip())
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

    def reload_ui(self):
        if self.prompt_list is None:
            self.prompt_list = widgets.VBox([prompt.widget for prompt in self.prompts])
        children = [self.prompt_list]
        if self.active_list_item:
            children.append(self.active_list_item.name_prompt.widget)
        self.widget.children = children

    def switch_prompt(self, prompt_list_item):
        for i, item in enumerate(self.prompts):
            item.inactive_style()
        self.active_list_item = prompt_list_item
        if self.active_list_item:
            self.active_list_item.active_style()
        self.reload_ui()

    def next_prompt(self, is_ignored):
        ix = self.prompts.index(self.active_list_item)
        self.switch_prompt(self.prompts[ix + 1] if ix + 1 < len(self.prompts) else None)

    @abstractmethod
    def process_one(self, item, url):
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
        exact_match = self.name_index.find_one(source_name=item.source_name, name=item.name, form=item.form)
        if not exact_match:
            self.name_index.update(item, source_name=item.source_name)
            self.write_name_index()

    def prompt_callback(self, source_name, url):
        def callback(name, form):
            if form == 'ignore':
                self.active_list_item.resolution = 'ignore'
                self.next_prompt(True)
                self.update_name_index(NameItem(source_name, None, form))
                return
            manufacturer, match = self.manufacturers.find(name, ignore_case=True)
            if manufacturer is None:
                raise UnknownManufacturerError(f'Manufacturer is not known for "{name}"')
            self.active_list_item.resolution = 'success'
            self.next_prompt(False)
            item = NameItem(source_name, name, form)
            self.process_one(NameItem(source_name, name, form), url)
            self.update_name_index(item)
        return callback

    def process(self, prompt=True, new_only=True):
        """Processes all new measurements

        Updates name index with the new entries now found in the name index previously.

        Args:
            prompt: Should the user be prompted for a name?
            new_only: Process only new items?

        Returns:
            None
        """
        unknown_manufacturers = []
        for source_name, url in self.urls.items():
            item = self.name_index.find_one(source_name=source_name)
            if item and item.form == 'ignore':
                continue
            if not item:
                if not prompt:
                    print(f'{source_name} is unknown and prompting is prohibited, skipping the item.')
                    continue
                # Name doesn't exist in the name index
                intermediate_name = self.intermediate_name(source_name)
                manufacturer, manufacturer_match = self.manufacturers.find(intermediate_name)
                if manufacturer:
                    model = re.sub(re.escape(manufacturer_match), '', intermediate_name, flags=re.IGNORECASE).strip()
                    name_proposals = self.get_name_proposals(source_name)
                    similar_names = self.get_name_proposals(source_name, n=4, normalize_digits=True, threshold=0)
                    similar_names = [item.name for item in similar_names.items]
                else:
                    unknown_manufacturers.append(intermediate_name)
                    model = intermediate_name
                    name_proposals = None
                    similar_names = None
                # Not sure about the name, ask user
                self.prompts.append(
                    PromptListItem(
                        NamePrompt(
                            model,
                            self.prompt_callback(source_name, url),
                            manufacturer=manufacturer,
                            name_proposals=name_proposals,
                            search_callback=self.search,
                            source_name=source_name,
                            similar_names=similar_names
                        ),
                        self.switch_prompt)
                )
            else:
                existing = self.existing.find_one(name=item.name)
                if not new_only or not existing:
                    # Name found in name index but the measurement doesn't exist
                    self.process_one(item, url)
        if len(unknown_manufacturers) > 0:
            warning = 'Headphones with unknown manufacturers:\n  * '
            warning += '\n  * '.join(unknown_manufacturers)
            warning += '\nAdd them to manufacturers.tsv and run this cell again'
            print(warning)
        self.reload_ui()

    def search(self, name):
        quoted = urllib.parse.quote_plus(name)
        url = f'https://google.com/search?q={quoted}&tbm=isch'
        webbrowser.open(url)

    def get_name_proposals(self, source_name, n=4, normalize_digits=False, normalize_extras=False, threshold=60):
        """Prompts manufacturer, model and form from the user

        Args:
            source_name: Name as it exists in the measurement source
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

        manufacturer, manufacturer_match = self.manufacturers.find(source_name)
        if not manufacturer:
            return NameIndex([])
        false_model = re.sub(re.escape(manufacturer_match), '', source_name, flags=re.IGNORECASE).strip()
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

    def intermediate_name(self, source_name):
        """Gets intermediate name with false name."""
        return source_name

    @staticmethod
    def download(url, name, output_dir, file_type=None):
        """Downloads a file from a URL

        Args:
            url: URL to download
            name: True name of the item to download
            output_dir: Where to write the downloaded file
            file_type: File extension. Detected automatically if None.

        Returns:
            Bool depicting if download succeeded or not
        """
        output_dir = os.path.abspath(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        res = requests.get(url, stream=True)
        if res.status_code != 200:
            print(f'Failed to download "{name}" at "{url}"')
            return None
        if file_type is None:
            file_type = url.split('.')[-1]
            file_type = file_type.split('?')[0]
        file_path = os.path.join(output_dir, f'{name}.{file_type}')
        with open(file_path, 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print('Downloaded to "{}"'.format(file_path))
        return file_path

    def get_beautiful_soup(self, url):
        self.driver.get(url)
        sleep(2)  # Giving some time for Selenium to render the page
        html = self.driver.find_element(By.TAG_NAME, 'html').get_attribute('outerHTML')
        return BeautifulSoup(html, 'html.parser')
