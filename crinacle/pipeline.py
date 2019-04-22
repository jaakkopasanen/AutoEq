# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import numpy as np
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse
import warnings

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main():
    data = dict()
    for file_path in glob(os.path.join(DIR_PATH, 'raw_data', '*.txt')):
        # Read name of the IEM from file path
        _, file_name = os.path.split(file_path)
        name = '.'.join(file_name.split('.')[:-1])
        name = name[:-2]  # Remove channel from name
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

    if os.path.exists(os.path.join(DIR_PATH, 'inspection')):
        os.makedirs(os.path.join(DIR_PATH, 'inspection'))

    # Iterate all models
    for name, frs in data.items():
        # Average SPL data from all measurements for this model (so Left and Right)
        raw = np.mean([fr.raw for fr in frs], axis=0)
        # Save as CSV
        fr = FrequencyResponse(name=name, frequency=frs[0].frequency, raw=raw)
        fr.write_to_csv(os.path.join(DIR_PATH, 'data', name + '.csv'))
        # Save inspection image
        fr.plot_graph(show=False, file_path=os.path.join(DIR_PATH, 'inspection', name + '.png'))


if __name__ == '__main__':
    main()
