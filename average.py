# -*- coding: utf-8 -*-

import os
import re
import argparse
from glob import glob
import numpy as np
import warnings
from frequency_response import FrequencyResponse


def main(input_dir=None, output_dir=None):
    if input_dir is None:
        raise TypeError('Input directory path is required!')
    if output_dir is None:
        raise TypeError('Output directory path is required!')
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    models = {}
    for file_path in glob(os.path.join(input_dir, '*')):
        model = os.path.split(file_path)[-1]
        if not (re.search(' sample [a-zA-Z0-9]$', model, re.IGNORECASE) or re.search(' sn[a-zA-Z0-9]+$', model, re.IGNORECASE)):
            continue
        norm = re.sub(' sample [a-zA-Z0-9]$', '', model, 0, re.IGNORECASE)
        norm = re.sub(' sn[a-zA-Z0-9]+$', '', norm, 0, re.IGNORECASE)
        try:
            models[norm].append(model)
        except KeyError as err:
            models[norm] = [model]

    for norm, origs in models.items():
        if len(origs) > 1:
            print(norm, origs)
            avg = np.zeros(613)
            f = FrequencyResponse.generate_frequencies()
            for model in origs:
                fr = FrequencyResponse.read_from_csv(os.path.join(input_dir, model, model + '.csv'))
                fr.interpolate()
                fr.center()
                avg += fr.raw
            avg /= len(origs)
            fr = FrequencyResponse(name=norm, frequency=f, raw=avg)
            d = os.path.join(output_dir, norm)
            if not os.path.isdir(d):
                os.makedirs(d)
            if os.path.isfile(os.path.join(d, norm + '.csv')):
                warnings.warn('Target file for "{}" already exists, skipping.'.format(norm))
            fr.write_to_csv(os.path.join(d, norm + '.csv'))
            #fr.plot_graph()


def create_cli():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir', type=str, required=True, help='Path to input directory.')
    arg_parser.add_argument('--output_dir', type=str, required=True, help='Path to output directory.')
    cli_args = arg_parser.parse_args()
    return vars(cli_args)


if __name__ == '__main__':
    main(**create_cli())
