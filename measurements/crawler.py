# -*- coding: utf-8 -*-

import os
import sys
import requests
import shutil
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from time import sleep
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.name_index import NameIndex, NameItem
from measurements.manufacturer_index import ManufacturerIndex

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class Crawler(ABC):
    def __init__(self, driver=None):
        self.driver = driver
        self.name_index = self.read_name_index()
        self.name_proposals = self.get_name_proposals()
        self.existing = self.get_existing()
        self.urls = self.get_urls()
        self.manufacturers = ManufacturerIndex()

    @staticmethod
    @abstractmethod
    def read_name_index():
        """Reads name index as Index

        Returns:
            NameIndex
        """
        pass

    def get_name_proposals(self):
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
        return name_proposals

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

    @staticmethod
    def prompt_true_name(name_options):
        """Prompts true name from the user."""
        name_options = name_options if name_options is not None else []
        if 'skip' not in name_options:
            name_options.insert(0, 'skip')
        s = 'What is it\'s true name?'
        if len(name_options):
            s += ' Select a number or write the name if none of the options.'
        print(s)
        if len(name_options):
            print(f'\n'.join(f'[{i}] {o}' for i, o in enumerate(name_options)))
        while True:
            name = input('> ')
            try:
                name = name_options[int(name)]
                if name == 'skip':
                    return None
                break
            except (KeyError, ValueError):
                break
            except IndexError:
                print('That didn\'t work, try again.')
        return name

    @staticmethod
    def prompt_manufacturer(name_options):
        """Prompts true manufacturer from the user."""
        name_options = name_options if name_options is not None else []
        s = 'What is it\'s true manufacturer name?'
        if len(name_options):
            s += ' Select a number or write the name if none of the options.'
        print(s)
        if len(name_options):
            print(f'\n'.join(f'[{i + 1}] {o}' for i, o in enumerate(name_options)))
        while True:
            name = input('> ')
            try:
                name = name_options[int(name) - 1]
                break
            except (KeyError, ValueError):
                break
            except IndexError:
                print('That didn\'t work, try again.')
        print('Which part of the name to replace')
        replace = input('> ')
        return name, replace

    @staticmethod
    def prompt_form():
        """Prompts form from the user."""
        options = ['onear', 'inear', 'earbud']
        print('What is it\'s type?')
        print(f'\n'.join(f'[{i + 1}] {o}' for i, o in enumerate(options)))
        while True:
            form = input('> ')
            try:
                return options[int(form) - 1]
            except (IndexError, ValueError):
                print('That didn\'t work, try again.')

    def prompt(self, false_name):
        """Prompts user for true name and form based on false name."""
        form = None
        if self.name_proposals is not None:
            # Name proposals initialized, add matching entries to options in prompt
            matches = []
            matches += self.name_proposals.search_by_false_name(false_name)
            matches += self.name_proposals.search_by_true_name(false_name)
            names_and_ratios = []
            for match in matches:
                if not match[0].true_name:
                    # Skip items without true name
                    continue
                if match[1] == 100:
                    # Exact match
                    match[0].true_name += ' ✓'
                if match[0].true_name not in [x[0] for x in names_and_ratios]:
                    # New match
                    names_and_ratios.append((match[0].true_name, match[1], match[0].form))
                else:
                    # Existing match, update ratio
                    for i in range(len(names_and_ratios)):
                        if match[0].true_name == names_and_ratios[i][0] and match[1] > names_and_ratios[i][1]:
                            names_and_ratios[i] = (names_and_ratios[i][0], match[1], names_and_ratios[i][2])

            name_options = [x[0] for x in sorted(names_and_ratios, key=lambda x: x[1], reverse=True)[:4]]
            if false_name not in name_options:
                name_options.append(false_name)  # Add the false name

            # Prompt
            true_name = self.prompt_true_name(name_options)

            if true_name is None:
                return None

            # Find and replace true manufacturer name or prompt it
            if self.manufacturers.find(true_name)[0] is None:
                # Unknown manufacturer, find options with the two first words and prompt it
                manufacturer_options = []
                for i in range(1, min(3, len(true_name.split()))):
                    candidate = ' '.join(true_name.split()[:i])
                    print(candidate)
                    manufacturer_options += self.manufacturers.search(candidate)
                    if candidate not in [x[0] for x in manufacturer_options]:
                        manufacturer_options.append((candidate, 0))
                manufacturer_options = sorted(manufacturer_options, key=lambda x: x[1], reverse=True)
                manufacturer_options = [x[0] for x in manufacturer_options]
                manufacturer, replace = self.prompt_manufacturer(manufacturer_options)
                _, match = self.manufacturers.find(manufacturer)
                if match:
                    # Add as a new variant in existing manufacturer
                    for m in self.manufacturers.manufacturers:
                        if m[0] == match:
                            m.append(replace)
                else:
                    # Add new manufacturer
                    self.manufacturers.manufacturers.append([manufacturer])
                self.manufacturers.write()
            # Replace
            true_name = self.manufacturers.replace(true_name)

            # Find the answer and select form
            for name, ratio, f in names_and_ratios:
                if true_name == name:
                    form = f
                    break
            true_name = true_name.replace(' ✓', '')

        else:
            true_name = self.prompt_true_name([false_name])
            form = None

        if true_name is None:
            # User skipped
            return None

        if form is None:
            # Form not found in name proposals, prompt it
            form = self.prompt_form()

        return NameItem(false_name, true_name, form)

    def process_new(self, prompt=True):
        """Processes all new measurements

        Updates name index with the new entries now found in the name index previously.

        Returns:
            None
        """
        for false_name, url in self.urls.items():
            try:
                ni = self.name_index.find(false_name=false_name)
                item = ni.items[0] if ni else None

                if item and item.form == 'ignore':
                    continue

                if item and item.true_name:
                    # Name index contains the entry
                    if not self.existing.find(true_name=item.true_name):
                        # Doesn't exist already
                        self.process(item, url)

                else:
                    # Unknown item
                    if prompt:
                        # Prompt true name and form
                        print(f'\n"{false_name}" is not known.')
                        item = self.prompt(false_name)
                        if item is None:
                            self.name_index.update(NameItem(false_name, None, 'ignore'), false_name=false_name)
                            continue
                        self.name_index.update(item, false_name=false_name)
                        self.process(item, url)
                    else:
                        print(f'"{false_name}" is not known. Add true name and form to name index and run again.')
                        self.name_index.update(NameItem(false_name, None, None), false_name=false_name)
                    self.write_name_index()
            except Exception as err:
                print(f'Processing failed for "{false_name}"')
                raise err

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
