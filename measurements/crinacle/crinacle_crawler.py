# -*- coding: utf-8 -*-

import os
from pathlib import Path, WindowsPath
import sys
import re
import numpy as np
import requests
from autoeq.frequency_response import FrequencyResponse
from measurements.prompt_list_item import PromptListItem

sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_prompt import NamePrompt
from measurements.name_index import NameIndex, NameItem
from measurements.crawler import Crawler, UnknownManufacturerError

DIR_PATH = Path(__file__).parent
ROOT_PATH = DIR_PATH.parent.parent


class UnknownRigError(Exception):
    pass


class CrinacleCrawler(Crawler):
    def __init__(self, driver=None):
        super().__init__(driver=driver)
        self.register_start_time('parse_books()')
        self.book_name_index = None
        self.parse_books()
        self.register_end_time('parse_books()')
        self.register_start_time('get_urls()')
        self.urls = self.get_urls()
        self.register_end_time('get_urls()')

    def parse_books(self):
        """Downloads parses phone books to get names

        Returns:
            NameIndex
        """
        items = []

        # Ears-711 measurements name index
        res = requests.get('https://crinacle.com/graphing/data_hp/phone_book.json')
        hp_book = self.parse_book(res.json())
        for source_name, name in hp_book.items():
            items.append(NameItem(source_name, name, 'over-ear'))

        # 711 IEM measurements name index
        res = requests.get('https://crinacle.com/graphing/data/phone_book.json')
        iem_book = self.parse_book(res.json())
        for source_name, name in iem_book.items():
            items.append(NameItem(source_name, name, 'in-ear'))

        # Gras measurements name index
        res = requests.get('https://crinacle.com/graphing/data_hp_gras/phone_book.json')
        gras_book = self.parse_book(res.json())
        for source_name, name in gras_book.items():
            items.append(NameItem(source_name, name, 'over-ear'))

        # 4620 measurements name index
        res = requests.get('https://crinacle.com/graphing/data_4620/phone_book.json')
        bk4620_book = self.parse_book(res.json())
        for source_name, name in bk4620_book.items():
            items.append(NameItem(source_name, name, 'in-ear'))

        self.book_name_index = NameIndex(items=items)

    def parse_book(self, data):
        """Parses a phone book as dict with false names as keys and true names as values.

        Args:
            data: Phone book object

        Returns:
            Dict with file names as keys and and phone book names as values
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
    def read_name_index():
        return NameIndex.read_tsv(DIR_PATH.joinpath('name_index.tsv'))

    def write_name_index(self):
        self.name_index.write_tsv(DIR_PATH.joinpath('name_index.tsv'))

    @staticmethod
    def get_existing():
        # FIXME: Tanchjim Zero exists in 711 measurements, seeing that in 4620 raw_data will be ignored when crawling
        return NameIndex.read_files(os.path.join(DIR_PATH, 'data', '**', '*.csv'))

    @staticmethod
    def normalize_file_name(file_name):
        file_name = re.sub(r' #\d+ [LR]\.txt', '', file_name)
        file_name = re.sub(r' [LR](?:\d+)?\.txt$', '', file_name)
        file_name = re.sub(r'\.txt$', '', file_name)
        return file_name

    def get_item_from_file_path(self, file_path):
        file_name = self.normalize_file_name(file_path.name)
        url = file_path.relative_to(ROOT_PATH)
        url = 'file://' + str(url).replace('\\', '/') if type(url) == WindowsPath else str(url)
        index_item = self.name_index.find_one(url=url)
        if index_item is not None:  # Existing item in the name index, ground truth
            item = NameItem(index_item.source_name, index_item.name, index_item.form, url=url, rig=None)
        else:
            book_item = self.book_name_index.find_one(source_name=file_name)
            if book_item is not None:  # File name to Crinacle's name mapping exists
                item = NameItem(book_item.name, None, book_item.form, url=url, rig=None)
            else:  # Nothing is known about this item
                item = NameItem(None, None, None, url=url, rig=None)
        return item

    def get_urls(self):
        raw_data_dir = DIR_PATH.joinpath('raw_data')
        items = []
        dirs_rigs_forms = [
            ('IEC60318-4 IEM Measurements (TSV txt)', 'in-ear', '711'),
            ('4620 IEM Measurements', 'in-ear', 'Bruel & Kjaer 4620'),
            ('EARS + 711 (TSV txt) (Legacy)', 'over-ear', 'EARS + 711'),
            ('GRAS 43AG-7', 'over-ear', 'GRAS 43AG-7'),
        ]
        for dir_name, form, rig in dirs_rigs_forms:
            for fp in raw_data_dir.joinpath(dir_name).glob('*.txt'):
                item = self.get_item_from_file_path(fp)
                if item.form is None:
                    item.form = form
                item.rig = rig
                items.append(item)
        return NameIndex(items=items)

    def process_one(self, items):
        """Reads measurement files for a single unit and saves an average frequency response

        Args:
            items: List of items for all of the measurements of the same unit

        Returns:
            None
        """
        if items[0].form == 'ignore':
            return
        avg_fr = FrequencyResponse(name=items[0].name)
        avg_fr.raw = np.zeros(avg_fr.frequency.shape)
        for item in items:
            fr = FrequencyResponse.read_from_csv(ROOT_PATH.joinpath(item.url.replace('file://', '')))
            fr.interpolate()
            fr.center()
            avg_fr.raw += fr.raw
        avg_fr.raw /= len(items)

        file_path = self.item_target_path(items[0])
        Path(file_path.parent).mkdir(exist_ok=True, parents=True)
        avg_fr.write_to_csv(file_path)
        print(f'Saved "{avg_fr.name}" to "{file_path}"')

    def create_prompt_callback(self, original_items):
        def callback(prompted_item):
            self.active_list_item.resolution = 'ignore' if prompted_item.form == 'ignore' else 'success'
            self.next_prompt()

            if not prompted_item.form == 'ignore':
                manufacturer, manufacturer_match = self.manufacturers.find(prompted_item.name, ignore_case=True)
                if manufacturer is None:
                    raise UnknownManufacturerError(f'Manufacturer is not known for "{prompted_item.name}"')
                prompted_item.name = self.manufacturers.replace(prompted_item.name)

            new_items = []
            for original_item in original_items:
                new_item = original_item.copy()
                new_item.name = prompted_item.name if prompted_item.form != 'ignore' else None
                new_item.form = prompted_item.form
                new_items.append(new_item)
                self.update_name_index(new_item, write=False)
            self.write_name_index()

            if prompted_item.form == 'ignore':
                return

            self.process_one(new_items)

        return callback

    @staticmethod
    def item_target_path(item):
        if item.form is None or item.rig is None or item.name is None:
            return None
        return DIR_PATH.joinpath('data', item.form, item.rig, f'{item.name}.csv')

    def group_key(self, url):
        file_path = Path(url.replace('file://', '')).parent.joinpath(
            self.normalize_file_name(url.split('/')[-1]))
        return str(file_path.relative_to(file_path.parent.parent))

    def process(self, new_only=True):
        """Processes all new measurements

        Updates name index with the new entries now found in the name index previously.

        Returns:
            None
        """
        self.register_start_time('process()')
        groups = {}
        for item in self.urls.items:
            key = self.group_key(item.url)
            if key not in groups:
                groups[key] = []
            groups[key].append(item)

        unknown_manufacturers = []
        for group_key, group_items in groups.items():
            try:
                name_prompt_item = group_items[0].copy()
                if name_prompt_item.form == 'ignore':
                    continue
                target_path = self.item_target_path(name_prompt_item)
                if target_path and target_path.exists() and new_only:  # Target file exists, nothing to do
                    continue
                elif name_prompt_item.name is not None:  # True name is known already but file doesn't exist
                    self.process_one(group_items)
                    continue

                # Use known source name or last part of URL as source name
                if name_prompt_item.source_name is not None:
                    guessed_name = name_prompt_item.source_name
                else:
                    guessed_name = self.normalize_file_name(name_prompt_item.url.split('/')[-1])
                guessed_name = self.intermediate_name(guessed_name)
                manufacturer, manufacturer_match = self.manufacturers.find(guessed_name)
                if manufacturer:
                    guessed_name = guessed_name.replace(manufacturer_match, manufacturer)
                else:
                    unknown_manufacturers.append(guessed_name)

                name_proposals = self.get_name_proposals(guessed_name, n=4) if manufacturer else None
                similar_names = [
                    item.name for item in self.get_name_proposals(
                        guessed_name, n=4, normalize_digits=True, normalize_extras=True, threshold=0
                    ).items]

                name_prompt = NamePrompt(
                    name_prompt_item,
                    self.create_prompt_callback(group_items),
                    manufacturer=manufacturer,
                    search_callback=self.search,
                    guessed_name=guessed_name,
                    name_proposals=name_proposals,
                    similar_names=similar_names)
                self.prompts.append(PromptListItem(name_prompt, self.switch_prompt))

            except Exception as err:
                print(f'Processing failed for "{group_items[0].url}"')
                raise err
        if len(unknown_manufacturers) > 0:
            warning = 'Headphones with unknown manufacturers:\n  * '
            warning += '\n  * '.join(unknown_manufacturers)
            warning += '\nAdd them to manufacturers.tsv and run this cell again'
            print(warning)
        self.prompts = sorted(self.prompts, key=lambda pli: pli.name_prompt.name)
        self.register_end_time('process()')
        self.reload_ui()

    def intermediate_name(self, source_name):
        """Gets intermediate name with false name."""
        name = source_name.replace('(w/ ', '(')
        name = re.sub(r' pads\)', ' earpads)', name, flags=re.IGNORECASE)
        match = re.search(r' S\d+[$ ]', name)
        if match:
            name = re.sub(r' S(\d+)[$ ]', r' (sample \1) ', name)
            name = re.sub(r'\s{2,}', ' ', name)
        return name


def main():
    crawler = CrinacleCrawler()
    crawler.process(prompt=False)


if __name__ == '__main__':
    main()
