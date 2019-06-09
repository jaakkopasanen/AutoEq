# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import warnings
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main():
    # Read name index
    name_index = dict()
    df = pd.read_csv(os.path.join(DIR_PATH, 'name_index.tsv'), sep='\t', header=None)
    # Replace empty cells with empty strings
    df = df.fillna('')
    df.columns = ['name', 'full_name', 'comment']
    records = df.to_dict('records')
    full_names = set()
    for record in records:
        if record['full_name'] in full_names:
            warnings.warn('Duplicate entry in name index with full name: "{}".'.format(record['full_name']))
            continue
        name_index[record['name']] = record

    data = dict()
    for file_path in glob(os.path.join(DIR_PATH, 'raw_data', '*.txt')):
        name = os.path.split(file_path)[1]
        # Remove ".txt" and " R" or " L" suffix
        name = re.sub('\.txt$', '', name)
        name = re.sub(' (L|R)', '', name)
        if name not in name_index:
            warnings.warn('"{}" missing from name index, skipping.'.format(name))
            continue
        if name_index[name]['comment'] in ['ignore', 'onear'] or not name_index[name]['full_name']:
            warnings.warn('Skipping "{}".'.format(name))
            continue
        name = name_index[name]['full_name']
        if name not in data:
            data[name] = []

        # Read file
        with open(file_path, 'r') as f:
            s = f.read()

        freq = []
        raw = []
        for line in s.split('\n'):
            if len(line) == 0 or line[0] == '*':
                # Skip empty lines and comments
                if 'C-weighting compensation: On' in line:
                    warnings.warn('C-weighted measurement: ' + name)
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
        fr = FrequencyResponse(name=name, frequency=freq, raw=raw)
        fr.interpolate()
        fr.center()
        data[name].append(fr)

    if not os.path.isdir(os.path.join(DIR_PATH, 'inspection')):
        os.makedirs(os.path.join(DIR_PATH, 'inspection'))

    # Iterate all models
    for name, frs in data.items():
        # Average SPL data from all measurements for this model (so Left and Right)
        raw = np.mean([fr.raw for fr in frs], axis=0)
        # Save as CSV
        fr = FrequencyResponse(name=name, frequency=frs[0].frequency, raw=raw)
        dir_path = os.path.join(DIR_PATH, 'data', 'inear', name)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        fr.write_to_csv(os.path.join(dir_path, name + '.csv'))
        # Save inspection image
        fr.plot_graph(show=False, close=True, file_path=os.path.join(DIR_PATH, 'inspection', name + '.png'))


if __name__ == '__main__':
    main()
