# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import re
import numpy as np
import requests
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex
from measurements.crawler import Crawler
from frequency_response import FrequencyResponse
from measurements.name_index import NameItem

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class CrinacleCrawler(Crawler):
    def get_name_proposals(self):
        """Downloads parses phone books to get names

        Returns:
            NameIndex
        """
        names = super().get_name_proposals()
        rows = []

        # Ears-711 measurements name index
        res = requests.get('https://crinacle.com/graphing/data_hp/phone_book.json')
        hp_book = self.parse_book(res.json())
        for false_name, true_name in hp_book.items():
            rows.append([false_name, true_name, 'onear'])

        # IEM measurements name index
        res = requests.get('https://crinacle.com/graphing/data/phone_book.json')
        iem_book = self.parse_book(res.json())
        for false_name, true_name in iem_book.items():
            rows.append([false_name, true_name, 'inear'])

        # Gras measurments name index
        res = requests.get('https://crinacle.com/graphing/data_hp_gras/phone_book.json')
        gras_book = self.parse_book(res.json())
        for false_name, true_name in gras_book.items():
            rows.append([false_name, true_name, 'onear'])

        names.concat(NameIndex(rows))
        return names

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
        iem_source_paths = list(glob(os.path.join(patreon_dir, 'IEM Measurements (TSV)', '*.txt')))
        for fp in iem_source_paths:
            add_to(fp, 'iem')

        # Ears + 711
        legacy_source_paths = list(glob(os.path.join(patreon_dir, 'Legacy Data (EARS + 711)', '*.txt')))
        for fp in legacy_source_paths:
            add_to(fp, 'legacy')

        # Gras
        gras_source_paths = list(glob(os.path.join(patreon_dir, 'FR Data (CSV)', '*.txt')))
        for fp in gras_source_paths:
            add_to(fp, 'gras')

        for name, rigs_and_file_paths in file_paths.items():
            if (
                    'iem' in rigs_and_file_paths and
                    ('legacy' in rigs_and_file_paths or 'gras' in rigs_and_file_paths)
            ):
                # Remove IEM rig measurements if Ears-711 or GRAS measurements exist
                # This means the headphone is onear model and the files found in IEM folder are duplicates
                del rigs_and_file_paths['iem']

        return file_paths

    def process(self, item, file_paths, target_dir=None):
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
        dir_path = os.path.join(target_dir, avg_fr.name)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f'{avg_fr.name}.csv')
        avg_fr.write_to_csv(file_path)
        print(f'Saved "{avg_fr.name}" to "{file_path}"')

    def prompt(self, false_name, form=None):
        """Prompts user for true name and form based on false name."""
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
                if form is not None and form != match[0].form:
                    # Skip items which don't match the given form
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
        for false_name, rigs_and_file_paths in self.urls.items():
            for rig, file_paths in rigs_and_file_paths.items():
                try:
                    ni = self.name_index.find(false_name=false_name)
                    item = ni.items[0] if ni else None

                    if item and item.form == 'ignore':
                        continue

                    # TODO: Infer form from the file path
                    file_paths = [os.path.abspath(p) for p in file_paths]
                    if rig == 'gras':
                        form = 'onear'
                        target_dir = os.path.join(DIR_PATH, 'data', 'onear', 'GRAS 43AG-7')
                    elif rig == 'legacy':
                        form = 'onear'
                        target_dir = os.path.join(DIR_PATH, 'data', 'onear', 'Ears-711')
                    else:
                        form = None
                        target_dir = os.path.join(DIR_PATH, 'data', 'inear')

                    if item and item.true_name:
                        # Name index contains the entry
                        if not self.existing.find(true_name=item.true_name):
                            # Doesn't exist yet
                            if form is not None:
                                item.form = form
                            self.process(item, file_paths, target_dir=target_dir)

                    else:
                        # Unknown item
                        if prompt:
                            # Prompt true name and form
                            print(f'\n"{false_name}" is not known.')
                            item = self.prompt(false_name, form=form)
                            if item is None:
                                self.name_index.update(NameItem(false_name, None, 'ignore'), false_name=false_name)
                                continue
                            self.name_index.update(item, false_name=false_name)
                            self.process(item, file_paths, target_dir=target_dir)
                        else:
                            print(f'"{false_name}" is not known. Add true name and form to name index and run again.')
                            self.name_index.update(NameItem(false_name, None, None), false_name=false_name)
                        self.write_name_index()
                except Exception as err:
                    print(f'Processing failed for "{false_name}"')
                    raise err
