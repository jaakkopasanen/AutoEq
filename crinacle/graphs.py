# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse
import warnings

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))
FREQ_LOCS = [20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800,
             900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000]
FREQ_NAMES = ['20', '30', '40', '50', '60', '70', '80', '90', '100', '200', '300', '400', '500', '600', '700', '800',
              '900', '1k', '2k', '3k', '4k', '5k', '6k', '7k', '8k', '9k', '10k', '20k']


def main():
    data = dict()
    i = 0
    for file_path in glob(os.path.join(DIR_PATH, 'raw_data', '*.txt')):
        # Read name of the IEM from file path
        _, file_name = os.path.split(file_path)
        name = '.'.join(file_name.split('.')[:-1])
        channel = name[-1]
        name = name[:-2]  # Remove channel from name
        if name not in data:
            data[name] = dict()

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
        data[name][channel] = fr
        i += 1
        if i > 11:
            break

    bg = Image.open('crinacle.png')
    bg = bg.convert('RGBA')

    for name, frs in data.items():
        file_path = 'images/{}.png'.format(name)
        fig, ax = plt.subplots()
        fig.set_size_inches(20, 10)
        #ax.imshow(img, aspect='equal', extent=[100, 2000, 40, 75], alpha=0.3)
        plt.plot(frs['L'].frequency, frs['L'].raw, color='blue')
        plt.plot(frs['R'].frequency, frs['R'].raw, color='red')
        plt.xlabel('Frequency (Hz)')
        plt.semilogx()
        plt.xlim([20, 20000])
        plt.ylabel('SPL (dB)')
        plt.ylim([30, 85])
        plt.title(name)
        plt.grid(True, which='major', color=(0.7, 0.7, 0.7), alpha=0.35, linewidth=1)
        plt.xticks(FREQ_LOCS, FREQ_NAMES, rotation=30)
        plt.yticks(np.arange(30, 90, 5))
        fig.savefig(file_path, bbox_inches='tight', transparent=True, dpi=120)
        graph = Image.open(file_path)
        graph = graph.convert('RGBA')
        im = bg.copy()
        im.paste(graph, (0, 0), mask=graph)
        #im = graph.copy()
        im = im.convert('P', palette=Image.ADAPTIVE, colors=60)
        im.save(file_path, optimize=True)


if __name__ == '__main__':
    main()
