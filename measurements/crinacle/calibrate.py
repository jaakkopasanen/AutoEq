# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import re
import numpy as np
import requests
import matplotlib.pyplot as plt
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.name_index import NameIndex, NameItem
from measurements.crawler import Crawler
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def measurements(dir_path):
    frs = []
    for fp in glob(os.path.join(dir_path, '*', '*.csv')):
        frs.append(FrequencyResponse.read_from_csv(fp))
    return frs


def main():
    harman_nobass = FrequencyResponse.read_from_csv(os.path.join(
        DIR_PATH, os.pardir, os.pardir, 'compensation', 'harman_over-ear_2018_wo_bass.csv'
    ))
    oratory1990 = measurements(os.path.join(DIR_PATH, os.pardir, 'oratory1990', 'data', 'onear'))
    crinacle = measurements(os.path.join(DIR_PATH, 'data', 'onear'))
    pairs = []
    for fr in crinacle:
        for candidate in oratory1990:
            if fr.name.lower() == candidate.name.lower():
                pairs.append((fr, candidate))

    fig, axs = plt.subplots(1, 3)
    fig.set_size_inches(25, 10)
    fig.suptitle('Crinacle Over-ear Calibration')
    description = 'Calibrated against oratory1990 measurements with headphones: '
    line_len = len(description)
    for fr, _ in pairs:
        if line_len > 240:
            description += '\n'
            line_len = 0
        description += f'{fr.name}, '
        line_len += len(fr.name) + 2
    description = description[:-2]
    fig.text(0.5, 0.93, description, ha='center')

    errors = []
    i = 0
    for fr, target in pairs:
        fr.compensate(target, min_mean_error=True)
        errors.append(fr.error)
        fr.raw = fr.error.copy()
        fr.error = []
        fr.target = []
        fr.plot_graph(fig=fig, ax=axs[0], show=False, color=f'C{i}')
        i += 1
    axs[0].set_ylim([-15, 15])
    axs[0].set_title('Individual Errors')
    errors = np.vstack(errors)
    mean = np.mean(errors, axis=0)
    std = np.std(errors, axis=0)

    fr = FrequencyResponse(name='Mean and Standard Deviation')
    fr.raw = mean
    fr.smoothen_heavy_light()
    fr.raw = fr.smoothed.copy()
    fr.smoothed = []
    fr.plot_graph(fig=fig, ax=axs[1], color='C0', show=False)
    axs[1].fill_between(fr.frequency, mean - std, mean + std, facecolor='#c1dff5')
    axs[1].set_ylim([-15, 15])

    harman_nobass.plot_graph(fig=fig, ax=axs[2], show=False, color='C0')
    crinacle_nobass = harman_nobass.copy()
    crinacle_nobass.raw += fr.raw
    crinacle_nobass.plot_graph(fig=fig, ax=axs[2], show=False, color='C1')
    axs[2].legend([
        'Harman over-ear 2018 w/o bass',
        'Crinacle over-ear w/o bass'
    ])
    axs[2].set_title('Crinacle Over-ear Target')
    axs[2].set_ylim([-15, 15])

    resources_dir = os.path.join(DIR_PATH, 'resources')
    os.makedirs(resources_dir, exist_ok=True)
    fig.savefig(os.path.join(DIR_PATH, 'resources', 'calibration.png'), bbox_inches='tight')
    crinacle_nobass.name = 'Crinacle Over-ear Target'
    crinacle_nobass.plot_graph(show=False, file_path=os.path.join(resources_dir, 'crinacle_over-ear.png'), color='C0')
    crinacle_nobass.write_to_csv(file_path=os.path.join(resources_dir, 'crinacle_over-ear.csv'))
    # plt.show()


if __name__ == '__main__':
    main()
