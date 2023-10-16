# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
from measurements.prompt_list_item import PromptListItem
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
from time import sleep, time
from measurements.name_index import NameIndex, NameItem
from measurements.manufacturer_index import ManufacturerIndex
from measurements.name_prompt import NamePrompt

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class UnknownManufacturerError(Exception):
    pass


class Crawler(ABC):
    """Crawler base class for crawling a frequency response measurement database index, resolving names, downloading
    data and processing the data to save in a standard AutoEq format in a correct target location in measurements
    directory.

    1. The database index is crawled and URLs for the data files are created
    2. Source names, AutoEq names, heapdhone forms and measurement rigs are attempted to be resolved
    3. Measurements for individual unit are grouped together to be processed together
    4. A set of user prompts are created for IPyWidgets based UI
    5. User goes through the prompts, crawl index items and name index are updated
    6. All groups are processed (file download, PDF parsing, image digitization, JSON / CSV parsing, ...)

    """
    def __init__(self, driver=None):
        self._start_time = time()
        self._timings = {}
        # Name resolutions
        self.name_index = None
        self.manufacturers = ManufacturerIndex()
        self.name_proposals = None
        self.groups = None
        # Crawler
        self.driver = driver
        self.crawl_index = None
        # UI
        self.prompts = []
        self.prompt_list = None
        self.active_list_item = None
        self.widget = widgets.HBox([])

    # Name resolution methods

    @staticmethod
    @abstractmethod
    def read_name_index():
        """Reads name index as Index

        Returns:
            NameIndex
        """
        pass

    @abstractmethod
    def write_name_index(self):
        """Writes name index to a file

        Returns:
            Index
        """
        pass

    def update_name_index(self, item, write=True):
        """Updates name index"""
        exact_match = self.name_index.find_one(url=item.url)
        if not exact_match:
            self.name_index.update(item)
            if write:
                self.write_name_index()

    def init_name_proposals(self):
        """Gets name proposals for new measurements

        Returns:
            NameIndex
        """
        name_proposals = NameIndex()
        for db in ['crinacle', 'oratory1990', 'rtings']:
            name_index = NameIndex.read_tsv(os.path.join(DIR_PATH, db, 'name_index.tsv'))
            name_proposals.concat(name_index)
        # TODO: Name index for Innerfidelity
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

    def guess_name(self, item):
        """Tries to guess what the name might be."""
        return item.name or item.source_name or re.sub(r'\.(?:txt|csv)$', '', item.url.split('/')[-1], flags=re.IGNORECASE)

    def resolve_name(self, item):
        """Resolve name for a single item

        Args:
            item: The crawl index NameItem to resolve

        Returns:
            True if resolution was successful, False if user needs to be prompted
        """
        ground_truth = self.name_index.find_one(url=item.url)
        if ground_truth and ground_truth.rig is not None:
            item.name = ground_truth.name
            item.rig = ground_truth.rig
            if ground_truth.source_name is not None:  # Source name doesn't exist for all items
                item.source_name = ground_truth.source_name
            return True
        return False

    def resolve_names(self):
        if self.name_index is None:
            self.name_index = self.read_name_index()
        if self.crawl_index is None:
            self.crawl()  # Produced URLs and source names

        self.prompts = []
        for item in self.crawl_index.items:
            if not self.resolve_name(item):
                self.prompts.append(item)

    def create_prompt_callback(self, original_items):
        def callback(prompted_item):
            self.active_list_item.resolution = 'ignore' if prompted_item.form == 'ignore' else 'success'
            self.next_prompt()
            # Replace manufacturer name with the true manufacturer name
            if not prompted_item.form == 'ignore':
                manufacturer, manufacturer_match = self.manufacturers.find(prompted_item.name, ignore_case=True)
                if manufacturer is None:
                    raise UnknownManufacturerError(f'Manufacturer is not known for "{prompted_item.name}"')
                prompted_item.name = self.manufacturers.replace(prompted_item.name)
            # Update crawl index items and name index
            for original_item in original_items:
                original_item.name = prompted_item.name if prompted_item.form != 'ignore' else None
                original_item.form = prompted_item.form
                self.update_name_index(original_item, write=False)
            self.write_name_index()
        return callback

    def resolution_callback(self, item):
        """Creates a function to do extra name, form or rig resolutions during prompting."""
        return NameItem(None, None, None, url=None, rig=None)

    @abstractmethod
    def group_key(self, item):
        """Creates grouping key for an item to group items of the same unit together."""
        pass

    def group_prompts(self):
        """Groups measurements in the crawl index belonging to the same unit together and creates prompts."""
        if self.crawl_index is None:
            self.crawl()
        self.groups = {}
        for item in self.crawl_index.items:
            key = self.group_key(item)
            if key not in self.groups:
                self.groups[key] = []
            self.groups[key].append(item)
        for key, group_items in self.groups.items():
            item = group_items[0]
            if item.form is not None and item.rig is not None and item.name is not None:
                # All important attributes are known, can skip prompt for this group (unit)
                continue
            guessed_name = self.guess_name(item)
            name_prompt = NamePrompt(
                item,
                self.create_prompt_callback(group_items),
                search_callback=self.google_image_search,
                resolution_callback=self.resolution_callback,
                guessed_name=guessed_name,
                name_proposals=self.get_name_proposals(guessed_name, n=4),
                similar_names=[
                    item.name for item in self.get_name_proposals(
                        guessed_name, n=4, normalize_digits=True, normalize_extras=True, threshold=0
                    ).items])
            self.prompts.append(PromptListItem(name_prompt, self.switch_prompt))
        self.prompts = sorted(self.prompts, key=lambda pli: pli.name_prompt.name)

    # Crawler methods

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

    @abstractmethod
    def crawl(self):
        """Crawls measurement URLs

        Returns:
            NameIndex with the crawled items
        """
        pass

    # Processing methods

    @abstractmethod
    def process_group(self, group):
        """Processes measurements for a single unit

        Args:
            group: List of NameItems belonging to the same unit to be processed together

        Returns:
            None
        """
        pass

    def process_groups(self, new_only=True):
        """Processes all new measurements

        Updates name index with the new entries now found in the name index previously.

        Args:
            new_only: Process only new items?

        Returns:
            None
        """

    # UI methods

    def reload_ui(self):
        """Refreshes IPyWidgets UI"""
        if self.prompt_list is None:
            self.prompt_list = widgets.VBox([prompt.widget for prompt in self.prompts])
        children = [self.prompt_list]
        if self.active_list_item:
            children.append(self.active_list_item.name_prompt.widget)
        self.widget.children = children

    def switch_prompt(self, prompt_list_item):
        """Switches to a different item in the prompt list in the IPyWidgets UI"""
        for i, item in enumerate(self.prompts):
            item.inactive_style()
        self.active_list_item = prompt_list_item
        if self.active_list_item:
            self.active_list_item.active_style()
            self.active_list_item.name_prompt.resolve()  # Trigger extra resolution
        self.reload_ui()

    def next_prompt(self):
        """Switches to next prompt in the IPyWidgets UI"""
        ix = self.prompts.index(self.active_list_item)
        self.switch_prompt(self.prompts[ix + 1] if ix + 1 < len(self.prompts) else None)

    def google_image_search(self, name):
        quoted = urllib.parse.quote_plus(name)
        url = f'https://google.com/search?q={quoted}&tbm=isch'
        webbrowser.open(url)

    def prompt(self):
        self.reload_ui()

    # Control flow

    def run(self):
        self.crawl()
        self.resolve_names()
        self.group_prompts()
        # Crawler.process_groups() needs to be invoked after user has resolved prompts
