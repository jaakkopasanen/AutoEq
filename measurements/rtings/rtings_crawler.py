# -*- coding: utf-8 -*-

import os
import requests
import json
import numpy as np
from glob import glob
from bs4 import BeautifulSoup
from measurements.downloader import download
from measurements.index import Index, Item
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))

# Compensation
ONEAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(DIR_PATH, 'resources', 'rtings_compensation_w_bass.csv')
)
INEAR_TARGET = FrequencyResponse.read_from_csv(
    os.path.join(DIR_PATH, 'resources', 'rtings_inear_compensation_w_bass.csv')
)


def get_links():
    res = requests.get('https://www.rtings.com/headphones/1-2/graph')
    document = BeautifulSoup(res.content, 'html.parser')

    links = {}
    for child in document.find(id='product_select').find_all('option'):
        name = child.text.strip()
        links[name] = f'https://www.rtings.com/images/graphs/{child["data-urlpart"]}/graph-frequency-response.json'

    return links


def get_existing():
    existing = dict()
    for fp in glob(os.path.join(DIR_PATH, 'data', '*', '*')):
        directory, name = os.path.split(fp)
        form = os.path.split(directory)[1]
        existing[name] = form
    return existing


def prompt_type():
    types = ['onear', 'inear', 'earbud']
    print(f'What is it\'s type?\n' + '\n'.join(f'[{i}] {t}' for i, t in enumerate(types)))
    while True:
        form = input('> ')
        try:
            return types[int(form)]
        except:
            print('That didn\'t work, try again.')


def parse_json(json_data):
    header = json_data['header']
    data = np.array(json_data['data'])
    frequency = data[:, header.index('Frequency')]
    left = data[:, header.index('Left')]
    right = data[:, header.index('Right')]
    target = data[:, header.index('Target Response')]
    raw = np.mean([left, right], axis=0)
    if np.std(target) > 0:
        raw += target
    fr = FrequencyResponse(name='', frequency=frequency, raw=raw)
    target = FrequencyResponse(name='', frequency=frequency, raw=target)
    return fr, target


def process(json_data, item):
    fr, target = parse_json(json_data)
    fr.name = item.true_name
    fr.interpolate()
    if np.std(fr.raw) == 0:
        # Frequency response data has non-zero target response, use that
        target.interpolate()
        target = target
        print(f'Using target for {fr.name}')
    elif item.form == 'inear':
        # Using in-ear target response
        target = INEAR_TARGET
    else:
        # Using on-ear or earbud target response
        target = ONEAR_TARGET
    target.center()
    fr.raw += target.raw
    fr.center()

    # Create directory
    dir_path = os.path.join(DIR_PATH, 'data', item.form, fr.name)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    # Write to CSV
    hp_file_path = os.path.join(dir_path, fr.name + '.csv')
    fr.write_to_csv(hp_file_path)
    print(f'Saved "{fr.name}" to "{hp_file_path}"')


def main():
    links = get_links()
    name_index = Index.read(os.path.join(DIR_PATH, 'name_index.tsv'))
    existing = get_existing()

    for false_name, link in links.items():
        try:
            item = name_index.find_by_false_name(false_name)
            if item:
                # Name index contains the entry
                if item.true_name in existing:
                    # Exists already, skip
                    continue
            else:
                print(f'"{false_name}" is not known. What is it\'s true name? Leave empty to accept that.')
                true_name = input('> ')
                form = prompt_type()
                item = Item(false_name, true_name, form)
                name_index.add(item)
            download({item.true_name: link}, os.path.join(DIR_PATH, 'json'))
            with open(os.path.join(DIR_PATH, 'json', f'{item.true_name}.json'), 'r') as fh:
                process(json.load(fh), item)

        except Exception as err:
            raise err
            print(f'Failed to process {false_name}: {str(err)}')

    name_index.write(os.path.join(DIR_PATH, 'name_index.tsv'))


if __name__ == '__main__':
    main()
