# -*- coding: utf-8 -*-

import os
import sys
import argparse
from glob import glob
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
import warnings
import json
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def parse_json(json_data, name):
    header = json_data['header']
    data = np.array(json_data['data'])
    frequency = data[:, header.index('Frequency')]
    left = data[:, header.index('Left')]
    right = data[:, header.index('Right')]
    target = data[:, header.index('Target Response')]
    raw = np.mean([left, right], axis=0)
    if np.std(target) > 0:
        raw += target
    fr = FrequencyResponse(name=name, frequency=frequency, raw=raw)
    target = FrequencyResponse(name='', frequency=frequency, raw=target)
    return fr, target


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir', type=str, default=os.path.join(DIR_PATH, 'raw_data'),
                            help='Path to raw data directory.')
    arg_parser.add_argument('--inspection_dir', type=str, default=os.path.join(DIR_PATH, 'inspection'),
                            help='Path to inspection directory.')
    arg_parser.add_argument('--output_dir', type=str, default=os.path.join(DIR_PATH, 'data'),
                            help='Path to data directory.')
    arg_parser.add_argument('--name_index', type=str, default=os.path.join(DIR_PATH, 'name_index.tsv'),
                            help='Path to name index TSV file.')
    cli_args = arg_parser.parse_args()

    input_dir = os.path.abspath(cli_args.input_dir)
    inspection_dir = os.path.abspath(cli_args.inspection_dir)
    output_dir = os.path.abspath(cli_args.output_dir)
    name_index = os.path.abspath(cli_args.name_index)

    if not os.path.isdir(inspection_dir):
        os.makedirs(inspection_dir)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Compensation
    onear_target = FrequencyResponse.read_from_csv(
        os.path.join(DIR_PATH, 'resources', 'rtings_compensation_w_bass.csv')
    )
    inear_target = FrequencyResponse.read_from_csv(
        os.path.join(DIR_PATH, 'resources', 'rtings_inear_compensation_w_bass.csv')
    )

    df = pd.read_csv(name_index, sep='\t', header=0)
    df = df.fillna('')
    name_index = dict()
    for index, row in df.iterrows():
        name_index[row['name']] = row

    for file_path in glob(os.path.join(input_dir, '*.json')):
        name = os.path.split(file_path)[-1].replace('.json', '')
        if name not in name_index:
            warnings.warn('{} not in name index, skipping'.format(name))
            continue
        if name_index[name]['type'] not in ['onear', 'inear', 'earbud']:
            warnings.warn('Incorrect type "{t}" for "{hp}"'.format(t=name_index[name]['type'], hp=name))
            continue
        hp_type = name_index[name]['type']
        if name_index[name]['full_name']:
            name = name_index[name]['full_name']

        # Read and parse image
        with open(file_path) as f:
            json_data = json.loads(f.read())
        fr, target = parse_json(json_data, name)
        fr.interpolate()
        if np.std(fr.raw) == 0:
            # Frequency response data has non-zero target response, use that
            target.interpolate()
            target = target
            print('Using target for', name)
        elif hp_type == 'inear':
            # Using in-ear target response
            target = inear_target
        else:
            # Using on-ear or earbud target response
            target = onear_target
        target.center()
        fr.raw += target.raw
        fr.center()

        # Save inspection images
        fr.plot_graph(show=False, close=True, file_path=os.path.join(inspection_dir, name + '.png'))

        # Create directory
        dir_path = os.path.join(output_dir, hp_type, name)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

        # Write to CSV
        hp_file_path = os.path.join(dir_path, name + '.csv')
        fr.write_to_csv(hp_file_path)
        print('Saved "{hp}" to "{path}"'.format(hp=name, path=hp_file_path))


if __name__ == '__main__':
    main()
