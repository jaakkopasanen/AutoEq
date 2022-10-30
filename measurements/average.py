# -*- coding: utf-8 -*-

import os
import re
import argparse
from glob import glob
import numpy as np
from autoeq.frequency_response import FrequencyResponse
from autoeq.constants import MOD_REGEX


def average_measurements(input_dir=None, output_dir=None):
    if input_dir is None:
        raise TypeError('Input directory path is required!')
    if output_dir is None:
        output_dir = os.path.abspath(input_dir)
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    models = {}
    for file_path in glob(os.path.join(input_dir, '**', '*.csv'), recursive=True):
        model = os.path.split(file_path)[-1].replace('.csv', '')
        if not re.search(MOD_REGEX, model, re.IGNORECASE):
            continue
        norm = re.sub(MOD_REGEX, '', model, 0, flags=re.IGNORECASE)
        if norm not in models:
            models[norm] = []
        models[norm].append(model)

    for norm, origs in models.items():
        if len(origs) > 1:
            f = FrequencyResponse.generate_frequencies()
            avg = np.zeros(len(f))
            for model in origs:
                fr = FrequencyResponse.read_from_csv(os.path.join(input_dir, model, model + '.csv'))
                fr.interpolate()
                fr.center()
                avg += fr.raw
            avg /= len(origs)
            fr = FrequencyResponse(name=norm, frequency=f, raw=avg)
            d = os.path.join(output_dir, norm)
            os.makedirs(d, exist_ok=True)
            file_path = os.path.join(d, norm + '.csv')
            fr.write_to_csv(file_path)
            print(f'Saved {norm} to {file_path}')


def create_cli():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir', type=str, required=True, help='Path to input directory.')
    arg_parser.add_argument('--output_dir', type=str, required=False, default=argparse.SUPPRESS,
                            help='Path to output directory.')
    cli_args = arg_parser.parse_args()
    return vars(cli_args)


if __name__ == '__main__':
    average_measurements(**create_cli())
