# -*- coding: utf-8 -*-
import sys
from pathlib import Path

from measurements.name_prompt import NamePrompt

ROOT_PATH = Path(__file__).resolve().parent.parent.parent
DIR_PATH = Path(__file__).resolve().parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
import re
import numpy as np
from measurements.crawler import Crawler
from measurements.name_index import NameIndex, NameItem
from frequency_response import FrequencyResponse


class Oratory1990DropboxCrawler(Crawler):
    def __init__(self, driver=None):
        super().__init__(driver=driver)

    @staticmethod
    def read_name_index():
        return NameIndex.read_tsv(DIR_PATH.joinpath('dropbox_name_index.tsv'))

    def write_name_index(self):
        self.name_index.write_tsv(DIR_PATH.joinpath('dropbox_name_index.tsv'))

    @staticmethod
    def get_existing():
        return NameIndex.read_files(str(DIR_PATH.joinpath('data/*/*/*')))

    def get_urls(self):
        file_paths = dict()
        for fp in DIR_PATH.rglob('raw_data/**/*.csv'):
            name = fp.name.replace('.csv', '')
            file_paths[name] = str(fp)
        return file_paths

    def process(self, item, url):
        if item.form == 'ignore':
            return
        out_dir = DIR_PATH.joinpath('data', item.form, item.true_name)
        out_dir.mkdir(parents=True, exist_ok=True)

        with open(url) as fh:
            lines = fh.read().strip().split('\n')
        frequency = []
        raw = []
        for line in lines:
            if re.match(r'-?\d+(,\d+)?;-?\d+(,\d+)?', line):
                # floats with comma as decimal point, separated by semicolon
                line = line.replace(',', '.')
                floats = re.findall(r'-?\d+\.?\d*', line)
                frequency.append(float(floats[0]))  # Assume first to be frequency
                raw.append(float(floats[1]))  # Assume second to be raw
            # Discard all lines which don't match data pattern

        if len(set(frequency)) != len(frequency):
            # Not all are unique, remove duplicates
            uniqf = set()
            frequency2 = []
            raw2 = []
            for i in range(len(frequency)):
                if frequency[i] not in uniqf:
                    uniqf.add(frequency[i])
                    frequency2.append(frequency[i])
                    raw2.append(raw[i])
            frequency = frequency2
            raw = raw2

        fr = FrequencyResponse(name=item.true_name, frequency=frequency, raw=raw)
        fr.interpolate()
        fr.center()
        fr.write_to_csv(out_dir.joinpath(item.true_name))
        print(f'Saved "{item.true_name}" to "{out_dir.joinpath(item.true_name)}"')

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
                p = Path(url)
                if p.parts[-2] == 'In-Ear':
                    form = 'inear'
                elif p.parts[-2] == 'Over-Ear':
                    form = 'onear'
                else:
                    raise ValueError('File path "{url}" doesn\'t have directory indicating form')
                # Name doesn't exist in the name index
                intermediate_name = self.intermediate_name(false_name)
                manufacturer, manufacturer_match = self.manufacturers.find(intermediate_name)
                if manufacturer:
                    model = re.sub(re.escape(manufacturer_match), '', intermediate_name,
                                   flags=re.IGNORECASE).strip()
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
                    form=form,
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

