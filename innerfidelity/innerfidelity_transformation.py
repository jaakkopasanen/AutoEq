# -*- coding: utf-8 -*-

"""Finds transformation function from old compensation function to new compensation function.
Reads *_after and *_before images from innerfidelity/transformation directory, calculates differences between
measurements done with old and new compensation curves. Final transfomation function is smoothed mean over these
individual differences."""

import os
from glob import glob
from PIL import Image
from frequency_response import FrequencyResponse
from image_graph_parser import ImageGraphParser
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main():
    models = dict()
    for file_path in glob(os.path.join('transformation', '*.jpg')):
        print(file_path)
        file_path = os.path.abspath(file_path)
        file_name = os.path.split(file_path)[-1]
        file_name = file_name.split('.')[0]
        name, kind = file_name.split('_')
        if name not in models:
            models[name] = dict()

        with open(file_path, 'rb') as f:
            model = os.path.split(file_path)[-1].split('.')[0]
            im = Image.open(file_path)

        # Add -1px to left and top, +1px to right and bottom of tight crop box in parse_innerfidelity
        fr = ImageGraphParser.parse_cropped(
            im,
            name=model,
            f_min=10,
            f_max=20000,
            a_min=-50,
            a_max=20
        )
        fr.interpolate()
        models[name][kind] = fr

    diffs = []
    names = []
    for model, frs in models.items():
        diffs.append(frs['before'].raw - frs['after'].raw)
        names.append(model)
    diffs = np.vstack(diffs)
    diff = np.mean(diffs, axis=0)
    f = models[list(models.keys())[0]]['before'].frequency
    diff = FrequencyResponse(name='Innerfidelity Transformation', frequency=f, raw=diff)
    diff.smooth(window_size=1/9, iterations=10)
    diff.raw = diff.smoothed
    diff.smoothed = np.array([])

    fig, ax = plt.subplots()
    legend = []

    for i, d in enumerate(diffs):
        fr = FrequencyResponse(name=names[i], frequency=f, raw=d)
        plt.plot(f, fr.raw)
        legend.append(names[i])

    plt.xlabel('Frequency (Hz)')
    plt.semilogx()
    plt.xlim([10, 20000])
    plt.ylabel('Amplitude (dBr)')
    plt.ylim([-15, 5])
    plt.legend(legend)
    plt.grid(which='major')
    plt.grid(which='minor')
    plt.title('Innerfidelity Transformation Function')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
    plt.show()
    diff.write_to_csv('innerfidelity_transformation.csv')

    diff.plot_graph(f_min=10, f_max=20000, file_path='innerfidelity_transformation.png')


if __name__ == '__main__':
    main()
