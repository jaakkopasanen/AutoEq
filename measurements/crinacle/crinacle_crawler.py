# -*- coding: utf-8 -*-

import os
from pathlib import Path
import sys
from glob import glob
import re
import numpy as np
import requests
from autoeq.frequency_response import FrequencyResponse
from measurements.PromptListItem import PromptListItem

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
        self.book_name_index = None
        self.parse_books()
        super().__init__(driver=driver)

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

    def get_urls_new(self):
        raw_data_dir = DIR_PATH.joinpath('raw_data')
        items = []
        for fp in raw_data_dir.joinpath('IEC60318-4 IEM Measurements (TSV txt)').glob('*.txt'):
            file_name = re.sub(r' [LR](?:\d+)?.txt', '', fp.name)
            url = fp.relative_to(ROOT_PATH)
            book_item = self.book_name_index.find_one(source_name=file_name)
            source_name = book_item.name if book_item is not None else None
            index_item = self.name_index.find_one(url=url)
            if index_item is None and source_name is not None:
                index_item = self.name_index.find_one(source_name=source_name)
            if index_item is None:
                index_item = self.name_index.find_one(source_name=file_name)
            name = index_item.name if index_item is not None else None
            item = NameItem(source_name, name, 'in-ear', url=url, rig='711')
            items.append(item)
        return NameIndex(items=items)

    def get_urls(self):
        # Link source is not a web page but raw_data folder
        # { hp_name: { rig: [ file_path1, ... ] }
        file_paths = dict()

        def add_to(_fp, _rig):
            name = os.path.split(fp)[1]
            name = re.sub(r' [LR]\d*\.txt', '', name).replace('.txt', '')
            name = re.sub(r' #\d$', '', name)
            if name not in file_paths:
                file_paths[name] = dict()
            if _rig not in file_paths[name]:
                file_paths[name][_rig] = []
            file_paths[name][_rig].append(fp)

        raw_data_dir = os.path.join(DIR_PATH, 'raw_data')

        # 711 in-ear measurements
        iem_711_source_paths = list(glob(os.path.join(raw_data_dir, 'IEC60318-4 IEM Measurements (TSV txt)', '*.txt')))
        for fp in iem_711_source_paths:
            add_to(fp, '711')
        # Ears + 711 over-ear measurements
        legacy_source_paths = list(glob(os.path.join(raw_data_dir, 'EARS + 711 (TSV txt) (Legacy)', '*.txt')))
        for fp in legacy_source_paths:
            add_to(fp, 'legacy')
        # Gras over-ear measurements
        gras_source_paths = list(glob(os.path.join(raw_data_dir, 'GRAS 43AG-7', '*.txt')))
        for fp in gras_source_paths:
            add_to(fp, 'gras')
        # B&K 4620 in-ear measurements
        iem_4620_source_paths = list(glob(os.path.join(raw_data_dir, '4620 IEM Measurements', '*.txt')))
        for fp in iem_4620_source_paths:
            add_to(fp, '4620')

        for name, rigs_and_file_paths in file_paths.items():
            if (
                    '711' in rigs_and_file_paths and
                    ('legacy' in rigs_and_file_paths or 'gras' in rigs_and_file_paths)
            ):
                # Remove IEM rig measurements if Ears-711 or GRAS measurements exist
                # This means the headphone is over-ear model and the files found in IEM folder are duplicates
                del rigs_and_file_paths['711']

        return file_paths

    def process_one(self, item, file_paths, target_dir=None):
        if item.form == 'ignore':
            return

        if target_dir is None:
            raise TypeError('"target_dir" must be given')

        avg_fr = FrequencyResponse(name=item.name)
        avg_fr.raw = np.zeros(avg_fr.frequency.shape)
        for fp in file_paths:
            with open(fp, 'r', encoding='utf-8') as fh:
                s = fh.read()

            freq = []
            raw = []
            for line in s.split('\n'):
                if len(line) == 0 or line[0] == '*':
                    # Skip empty lines and comments
                    if 'C-weighting compensation: On' in line:
                        print(f'C-weighted measurement: {item.source_name}')
                    continue

                frp = line.split(', ')
                if len(frp) == 1:
                    frp = line.split('\t')
                if len(frp) == 1:
                    frp = line.split(' ')
                if len(frp) == 2:
                    f, r = frp
                elif len(frp) == 3:
                    f, r, p = frp
                else:
                    # Must be comment line
                    continue

                if f == '?' or r == '?':
                    # Skip lines with missing data
                    continue

                try:
                    freq.append(float(f))
                    raw.append(float(r))
                except ValueError as err:
                    # Failed to convert values to floats, must be header or comment row, skip
                    continue

            # Create standard fr object
            fr = FrequencyResponse(name=item.name, frequency=freq, raw=raw)
            fr.interpolate()
            fr.center()
            avg_fr.raw += fr.raw

        avg_fr.raw /= len(file_paths)

        # Save
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(target_dir, f'{avg_fr.name}.csv')
        avg_fr.write_to_csv(file_path)
        print(f'Saved "{avg_fr.name}" to "{file_path}"')

    def prompt_callback(self, source_name, file_paths, target_dir):
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
            self.process_one(item, file_paths, target_dir=target_dir)
            self.update_name_index(item)
        return callback

    def process(self, prompt=True):
        """Processes all new measurements

        Updates name index with the new entries now found in the name index previously.

        Returns:
            None
        """
        unknown_manufacturers = []
        for source_name, rigs_and_file_paths in self.urls.items():
            for rig, file_paths in rigs_and_file_paths.items():
                try:
                    file_paths = [os.path.abspath(p) for p in file_paths]
                    if rig == 'gras':
                        target_dir = os.path.join(DIR_PATH, 'data', 'over-ear', 'GRAS 43AG-7')
                        form = 'over-ear'
                    elif rig == 'legacy':
                        target_dir = os.path.join(DIR_PATH, 'data', 'over-ear', 'EARS + 711')
                        form = 'over-ear'
                    elif rig == '4620':
                        target_dir = os.path.join(DIR_PATH, 'data', 'in-ear', 'Bruel & Kjaer 4620')
                        form = 'in-ear'
                    elif rig == '711':
                        target_dir = os.path.join(DIR_PATH, 'data', 'in-ear', '711')
                        form = 'in-ear'
                    else:
                        raise UnknownRigError()

                    item = self.name_index.find_one(source_name=source_name)
                    if item and item.form == 'ignore':
                        continue
                    if not item or not item.name or not item.form:
                        if not prompt:
                            print(f'{source_name} is unknown and prompting is prohibited, skipping the item.')
                            continue
                        # Name doesn't exist in the name index
                        intermediate_name = self.intermediate_name(source_name)
                        manufacturer, manufacturer_match = self.manufacturers.find(intermediate_name)
                        if manufacturer:
                            model = re.sub(re.escape(manufacturer_match), '', intermediate_name, flags=re.IGNORECASE)
                            model = model.strip()
                            name_proposals = self.get_name_proposals(intermediate_name)
                            similar_names = self.get_name_proposals(
                                intermediate_name, n=4, normalize_digits=True, normalize_extras=True, threshold=0)
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
                                    self.prompt_callback(source_name, file_paths, target_dir),
                                    manufacturer=manufacturer,
                                    name_proposals=name_proposals,
                                    search_callback=self.search,
                                    source_name=source_name,
                                    form=form,
                                    similar_names=similar_names
                                ),
                                self.switch_prompt
                            ))
                    else:
                        existing = self.existing.find_one(name=item.name)
                        if not existing:
                            self.process_one(item, file_paths, target_dir=target_dir)
                except Exception as err:
                    print(f'Processing failed for "{source_name}"')
                    raise err
        if len(unknown_manufacturers) > 0:
            warning = 'Headphones with unknown manufacturers:\n  * '
            warning += '\n  * '.join(unknown_manufacturers)
            warning += '\nAdd them to manufacturers.tsv and run this cell again'
            print(warning)
        self.reload_ui()

    def intermediate_name(self, source_name):
        """Gets intermediate name with false name."""
        ni = self.book_name_index.find_one(source_name=source_name)
        if ni:
            name = ni.name
            name = name.replace('(w/ ', '(')
            name = name.replace(' pads)', ' earpads)')
            if re.search(r'S\d$', name):
                match = re.search(r'S\d$', name)[0]
                name = name.replace(match, match.replace('S', 'sample '))
            return name
        return source_name


def main():
    crawler = CrinacleCrawler()
    crawler.process(prompt=False)


if __name__ == '__main__':
    main()
