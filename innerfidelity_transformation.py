# -*- coding: utf-8 -*-

"""Finds transformation function from old compensation function to new compensation function.
Reads *_after and *_before images from innerfidelity/transformation directory, calculates differences between
measurements done with old and new compensation curves. Final transfomation function is smoothed mean over these
individual differences."""

import os
from glob import glob
from PIL import Image, ImageDraw
import colorsys
from frequency_response import FrequencyResponse
from image_graph_parser import ImageGraphParser
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main():
    models = dict()
    for file_path in glob('innerfidelity\\transformation\\*'):
        file_path = os.path.abspath(file_path)
        file_name = os.path.split(file_path)[-1]
        file_name = file_name.split('.')[0]
        name, kind = file_name.split('_')
        if name not in models:
            models[name] = dict()

        with open(file_path, 'rb') as f:
            model = os.path.split(file_path)[-1].split('.')[0]
            im = Image.open(file_path)

        px_top = 50  # Pixels from top to +30dB
        px_bottom = 50  # Pixels from bottom to -30dB
        px_left = 50  # Pixels from left to 10Hz
        px_right = 20  # Pixels from right edge

        fr = ImageGraphParser.parse_innerfidelity(
            im,
            model=model,
            px_top=px_top,
            px_bottom=px_bottom,
            px_left=px_left,
            px_right=px_right
        )
        #fr.plot_graph(a_min=-50, a_max=20)
        fr.interpolate()
        models[name][kind] = fr

    diffs = []
    names = []
    for model, frs in models.items():
        diffs.append(frs['after'].raw - frs['before'].raw)
        names.append(model)
    diffs = np.vstack(diffs)
    diff = np.mean(diffs, axis=0)
    f = models[list(models.keys())[0]]['before'].frequency
    diff = FrequencyResponse(name='Diff', frequency=f, raw=diff)
    diff.smooth(1/5)
    #diff.plot_graph(a_min=-10, a_max=10)

    fig, ax = plt.subplots()
    legend = []

    # for i, d in enumerate(diffs):
    #     fr = FrequencyResponse(name=names[i], frequency=f, raw=d)
    #     fr.smooth()
    #     plt.plot(f, fr.raw)
    #     legend.append(names[i])

    plt.plot(f, diff.raw)
    legend.append('Mean smoothed')

    plt.xlabel('Frequency (Hz)')
    plt.semilogx()
    plt.xlim([10, 30000])
    plt.ylabel('Amplitude (dBr)')
    plt.ylim([-5, 15])
    plt.legend(legend)
    plt.grid(which='major')
    plt.grid(which='minor')
    plt.title('Innerfidelity Transformation Function')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
    fig.savefig('innerfidelity\\transformation\\transformation.png', dpi=240)
    plt.show()
    diff.write_to_csv('innerfidelity\\transformation\\transformation.csv')


if __name__ == '__main__':
    main()
