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
    for file_path in glob(os.path.join(input_dir, '*.csv'), recursive=True):
        model = os.path.split(file_path)[-1].replace('.csv', '')
        if not re.search(MOD_REGEX, model, re.IGNORECASE):
            continue
        normalized_name = re.sub(MOD_REGEX, '', model, 0, flags=re.IGNORECASE)
        if normalized_name not in models:
            models[normalized_name] = []
        models[normalized_name].append(model)

    for normalized_name, original_name_models in models.items():
        if len(original_name_models) > 1:  # Not averaging with just one sample
            f = FrequencyResponse.generate_frequencies()
            avg = np.zeros(len(f))
            for model in original_name_models:
                fr = FrequencyResponse.read_from_csv(os.path.join(input_dir, model + '.csv'))
                fr.interpolate()
                fr.center()
                avg += fr.raw
            avg /= len(original_name_models)
            fr = FrequencyResponse(name=normalized_name, frequency=f, raw=avg)
            file_path = os.path.join(output_dir, normalized_name + '.csv')
            fr.write_to_csv(file_path)
            print(f'Saved {normalized_name} to {file_path}')


def create_cli():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir', type=str, required=True, help='Path to input directory.')
    arg_parser.add_argument('--output_dir', type=str, required=False, default=argparse.SUPPRESS,
                            help='Path to output directory.')
    cli_args = arg_parser.parse_args()
    return vars(cli_args)


if __name__ == '__main__':
    average_measurements(**create_cli())
