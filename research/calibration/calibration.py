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
from constants import ROOT_DIR

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))
MEASUREMENTS = os.path.join(ROOT_DIR, 'measurements')


def get_measurements(dir_path):
    frs = []
    for fp in glob(os.path.join(dir_path, '**', '*.csv'), recursive=True):
        frs.append(FrequencyResponse.read_from_csv(fp))
    return frs


def main():
    harman_onear = FrequencyResponse.read_from_csv(os.path.join(ROOT_DIR, 'compensation', 'harman_over-ear_2018_wo_bass.csv'))
    harman_inear = FrequencyResponse.read_from_csv(os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2019v2_wo_bass.csv'))
    oratory1990_onear = get_measurements(os.path.join(MEASUREMENTS, 'oratory1990', 'data', 'onear'))
    oratory1990_inear = get_measurements(os.path.join(MEASUREMENTS, 'oratory1990', 'data', 'inear'))

    dbs = [
        ('crinacle_inear', get_measurements(os.path.join(MEASUREMENTS, 'crinacle', 'data', 'inear')), None),
        ('crinacle_onear', get_measurements(os.path.join(MEASUREMENTS, 'crinacle', 'data', 'onear')), None),
        (
            'headphonecom_onear',
            get_measurements(os.path.join(MEASUREMENTS, 'headphonecom', 'data', 'onear')),
            FrequencyResponse.read_from_csv(os.path.join(MEASUREMENTS, 'headphonecom', 'resources', 'headphonecom_compensation_sbaf-serious.csv'))
        ),
        (
            'headphonecom_inear',
            get_measurements(os.path.join(MEASUREMENTS, 'headphonecom', 'data', 'inear')),
            FrequencyResponse.read_from_csv(os.path.join(MEASUREMENTS, 'headphonecom', 'resources', 'headphonecom_compensation_sbaf-serious.csv'))
        ),
        (
            'innerfidelity_onear',
            get_measurements(os.path.join(MEASUREMENTS, 'innerfidelity', 'data', 'onear')),
            FrequencyResponse.read_from_csv(os.path.join(MEASUREMENTS, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'))
        ),
        (
            'innerfidelity_inear',
            get_measurements(os.path.join(MEASUREMENTS, 'innerfidelity', 'data', 'inear')),
            FrequencyResponse.read_from_csv(os.path.join(MEASUREMENTS, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'))
        ),
        (
            'referenceaudioanalyzer_onear-hdm-x',
            get_measurements(os.path.join(MEASUREMENTS, 'referenceaudioanalyzer', 'data', 'onear', 'HDM-X')),
            None
        ),
        (
            'referenceaudioanalyzer_onear-hdm1',
            get_measurements(os.path.join(MEASUREMENTS, 'referenceaudioanalyzer', 'data', 'onear', 'HDM1')),
            None
        ),
        (
            'referenceaudioanalyzer_inear-siec',
            get_measurements(os.path.join(MEASUREMENTS, 'referenceaudioanalyzer', 'data', 'inear', 'SIEC')),
            None
        ),
        (
            'rtings_onear',
            get_measurements(os.path.join(MEASUREMENTS, 'rtings', 'data', 'onear')),
            FrequencyResponse.read_from_csv(os.path.join(MEASUREMENTS, 'rtings', 'resources', 'rtings_compensation_avg.csv'))
        ),
        (
            'rtings_inear',
            get_measurements(os.path.join(MEASUREMENTS, 'rtings', 'data', 'inear')),
            FrequencyResponse.read_from_csv(os.path.join(MEASUREMENTS, 'rtings', 'resources', 'rtings_compensation_avg.csv'))
        ),
    ]

    stds = []
    for name, measurements, original_target in dbs:
        print(f'Calibrating {name}...')
        # Find matching pairs
        pairs = []
        for fr in measurements:
            ref = oratory1990_onear if 'onear' in name else oratory1990_inear
            for candidate in ref:
                if fr.name.lower() == candidate.name.lower():
                    pairs.append((fr, candidate))

        fig, axs = plt.subplots(1, 3)
        fig.set_size_inches(30, 8)
        fig.suptitle(name)
        description = 'Calibrated against oratory1990 measurements with headphones: '
        line_len = len(description)
        for fr, _ in pairs:
            if line_len > 240:
                description += '\n'
                line_len = 0
            description += f'{fr.name}, '
            line_len += len(fr.name) + 2
        description = description[:-2]
        fig.text(0.5, -0.05, description, ha='center')

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
        stds.append(FrequencyResponse(name=name, raw=std))

        fr = FrequencyResponse(name='Mean and Standard Deviation')
        fr.raw = mean
        fr.smoothen_heavy_light()
        fr.raw = fr.smoothed.copy()
        fr.smoothed = []
        fr.plot_graph(fig=fig, ax=axs[1], color='C0', show=False)
        axs[1].fill_between(fr.frequency, mean - std, mean + std, facecolor='#c1dff5')
        axs[1].set_ylim([-15, 15])

        ref_target = harman_onear if 'onear' in name else harman_inear
        ref_target.plot_graph(fig=fig, ax=axs[2], show=False, color='C0')
        target = ref_target.copy()
        target.name = name
        target.raw += fr.raw
        target.plot_graph(fig=fig, ax=axs[2], show=False, color='C1')
        if original_target is not None:
            original_target.plot_graph(fig=fig, ax=axs[2], show=False, color='C2')
            axs[2].legend([ref_target.name, target.name, original_target.name])
        else:
            axs[2].legend([ref_target.name, target.name])
        axs[2].set_title(f'{name} target')
        axs[2].set_ylim([-15, 15])


        fig.savefig(os.path.join(DIR_PATH, f'calibration_{name}.png'), bbox_inches='tight')

        target.plot_graph(show=False, file_path=os.path.join(DIR_PATH, f'target_{name}.png'), color='C0')
        target.write_to_csv(file_path=os.path.join(DIR_PATH, f'{name}.csv'))
        plt.close(fig)

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(20, 8)
    onear_labels = []
    inear_labels = []
    for fr in stds:
        if 'onear' in fr.name:
            fr.plot_graph(fig=fig, ax=axs[0], color=f'C{len(onear_labels)}', show=False)
            onear_labels.append(fr.name)
        else:
            fr.plot_graph(fig=fig, ax=axs[1], color=f'C{len(inear_labels)}', show=False)
            inear_labels.append(fr.name)
    axs[0].legend(onear_labels)
    axs[1].legend(inear_labels)
    axs[0].set_title('On-ear')
    axs[1].set_title('In-ear')
    axs[0].set_ylim([0, 15])
    axs[1].set_ylim([0, 15])
    fig.savefig(os.path.join(DIR_PATH, 'STDs.png'))
    plt.close(fig)


if __name__ == '__main__':
    main()
