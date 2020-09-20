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
        return NameIndex.read_files(os.path.join(DIR_PATH, 'data', '*', '*'))

    def get_urls(self):
        # Link source is not a web page but raw_data folder
        file_paths = dict()
        for fp in glob(os.path.join(DIR_PATH, 'raw_data', '*')):
            name = os.path.split(fp)[1]
            name = re.sub(r' [LR]\d*\.txt', '', name).replace('.txt', '')
            name = re.sub(r' #\d$', '', name)
            name = name.replace('.mdat', '')
            if name not in file_paths:
                file_paths[name] = []
            file_paths[name].append(fp)
        return file_paths

    def process(self, item, file_paths):
        fr = FrequencyResponse(name=item.true_name)
        fr.raw = np.zeros(fr.frequency.shape)
        for fp in file_paths:
            if re.search(r'\.mdat$', fp):
                # Read mdat file for Gras headphone measurements
                raise TypeError('Crinacle\'s Gras measurements are not supported yet!')
            else:
                # Read text file for IEM and Ears-711 headphone measurements
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

                frp = line.split(' ')
                if len(frp) == 1:
                    frp = line.split('\t')
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
            _fr = FrequencyResponse(name=item.true_name, frequency=freq, raw=raw)
            _fr.interpolate()
            _fr.center()
            fr.raw += _fr.raw

        fr.raw /= len(file_paths)

        # Save
        dir_path = os.path.join(DIR_PATH, 'data', item.form, fr.name)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f'{fr.name}.csv')
        fr.write_to_csv(file_path)
        print(f'Saved "{fr.name}" to "{file_path}"')
