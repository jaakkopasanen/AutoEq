# -*- coding: utf-8 -*-

import os
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

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


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
        rows = []

        # Ears-711 measurements name index
        res = requests.get('https://crinacle.com/graphing/data_hp/phone_book.json')
        hp_book = self.parse_book(res.json())
        for false_name, true_name in hp_book.items():
            rows.append([false_name, true_name, 'over-ear'])

        # 711 IEM measurements name index
        res = requests.get('https://crinacle.com/graphing/data/phone_book.json')
        iem_book = self.parse_book(res.json())
        for false_name, true_name in iem_book.items():
            rows.append([false_name, true_name, 'in-ear'])

        # Gras measurements name index
        res = requests.get('https://crinacle.com/graphing/data_hp_gras/phone_book.json')
        gras_book = self.parse_book(res.json())
        for false_name, true_name in gras_book.items():
            rows.append([false_name, true_name, 'over-ear'])

        # 4620 measurements name index
        res = requests.get('https://crinacle.com/graphing/data_4620/phone_book.json')
        bk4620_book = self.parse_book(res.json())
        for false_name, true_name in bk4620_book.items():
            rows.append([false_name, true_name, 'in-ear'])

        self.book_name_index = NameIndex(rows)

    @staticmethod
    def parse_book(data):
        """Parses a phone book as dict with false names as keys and true names as values.

        Args:
            data: Phone book object

        Returns:
            Dict with false names and true names
        """
        book = dict()
        for manufacturer in data:
            manufacturer_name = manufacturer['name']
            if 'suffix' in manufacturer:
                manufacturer_name += f' {manufacturer["suffix"]}'
            for model in manufacturer['phones']:
                if type(model) == str:
                    # Plain string
                    book[model.strip()] = f'{manufacturer_name} {model}'.strip()

                else:
                    # Object
                    if type(model['file']) == str:
                        # Single file as string, wrap in list
                        model['file'] = [model['file']]

                    if 'suffix' in model:
                        for f, suffix in zip(model['file'], model['suffix']):
                            book[f.strip()] = f'{manufacturer_name} {model["name"]} {suffix}'.strip()
                    else:
                        for f in model['file']:
                            book[f.strip()] = f'{manufacturer_name} {model["name"]}'.strip()

        return book

    @staticmethod
    def read_name_index():
        return NameIndex.read_tsv(os.path.join(DIR_PATH, 'name_index.tsv'))

    def write_name_index(self):
        self.name_index.write_tsv(os.path.join(DIR_PATH, 'name_index.tsv'))

    @staticmethod
    def get_existing():
        return NameIndex.read_files(os.path.join(DIR_PATH, 'data', '**', '*.csv'))

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

        patreon_dir = os.path.join(DIR_PATH, 'raw_data')

        # IEMs
        iem_711_source_paths = list(glob(os.path.join(patreon_dir, 'IEC60318-4 IEM Measurements (TSV txt)', '*.txt')))
        for fp in iem_711_source_paths:
            add_to(fp, '711')

        # Ears + 711
        legacy_source_paths = list(glob(os.path.join(patreon_dir, 'EARS + 711 (TSV txt) (Legacy)', '*.txt')))
        for fp in legacy_source_paths:
            add_to(fp, 'legacy')

        # Gras
        gras_source_paths = list(glob(os.path.join(patreon_dir, 'GRAS 43AG-7', '*.txt')))
        for fp in gras_source_paths:
            add_to(fp, 'gras')

        iem_4620_source_paths = list(glob(os.path.join(patreon_dir, '4620 IEM Measurements', '*.txt')))
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

        avg_fr = FrequencyResponse(name=item.true_name)
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
                        print(f'C-weighted measurement: {item.false_name}')
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
            fr = FrequencyResponse(name=item.true_name, frequency=freq, raw=raw)
            fr.interpolate()
            fr.center()
            avg_fr.raw += fr.raw

        avg_fr.raw /= len(file_paths)

        # Save
        os.makedirs(target_dir, exist_ok=True)
        file_path = os.path.join(target_dir, f'{avg_fr.name}.csv')
        avg_fr.write_to_csv(file_path)
        print(f'Saved "{avg_fr.name}" to "{file_path}"')

    def prompt_callback(self, false_name, file_paths, target_dir):
        def callback(true_name, form):
            if form == 'ignore':
                self.active_list_item.resolution = 'ignore'
                self.next_prompt(True)
                self.update_name_index(NameItem(false_name, None, form))
                return
            manufacturer, match = self.manufacturers.find(true_name, ignore_case=True)
            if manufacturer is None:
                raise UnknownManufacturerError(f'Manufacturer is not known for "{true_name}"')
            self.active_list_item.resolution = 'success'
            self.next_prompt(False)
            item = NameItem(false_name, true_name, form)
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
        for false_name, rigs_and_file_paths in self.urls.items():
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

                    item = self.name_index.find_one(false_name=false_name)
                    if item and item.form == 'ignore':
                        continue
                    if not item or not item.true_name or not item.form:
                        if not prompt:
                            print(f'{false_name} is unknown and prompting is prohibited, skipping the item.')
                            continue
                        # Name doesn't exist in the name index
                        intermediate_name = self.intermediate_name(false_name)
                        manufacturer, manufacturer_match = self.manufacturers.find(intermediate_name)
                        if manufacturer:
                            model = re.sub(re.escape(manufacturer_match), '', intermediate_name, flags=re.IGNORECASE)
                            model = model.strip()
                            name_proposals = self.get_name_proposals(intermediate_name)
                            similar_names = self.get_name_proposals(
                                intermediate_name, n=4, normalize_digits=True, normalize_extras=True, threshold=0)
                            similar_names = [item.true_name for item in similar_names.items]
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
                                    self.prompt_callback(false_name, file_paths, target_dir),
                                    manufacturer=manufacturer,
                                    name_proposals=name_proposals,
                                    search_callback=self.search,
                                    false_name=false_name,
                                    form=form,
                                    similar_names=similar_names
                                ),
                                self.switch_prompt
                            ))
                    else:
                        existing = self.existing.find_one(true_name=item.true_name)
                        if not existing:
                            self.process_one(item, file_paths, target_dir=target_dir)
                except Exception as err:
                    print(f'Processing failed for "{false_name}"')
                    raise err
        if len(unknown_manufacturers) > 0:
            warning = 'Headphones with unknown manufacturers:\n  * '
            warning += '\n  * '.join(unknown_manufacturers)
            warning += '\nAdd them to manufacturers.tsv and run this cell again'
            print(warning)
        self.reload_ui()

    def intermediate_name(self, false_name):
        """Gets intermediate name with false name."""
        ni = self.book_name_index.find_one(false_name=false_name)
        if ni:
            name = ni.true_name
            name = name.replace('(w/ ', '(')
            name = name.replace(' pads)', ' earpads)')
            if re.search(r'S\d$', name):
                match = re.search(r'S\d$', name)[0]
                name = name.replace(match, match.replace('S', 'sample '))
            return name
        return false_name


def main():
    crawler = CrinacleCrawler()
    crawler.process(prompt=False)


if __name__ == '__main__':
    main()
