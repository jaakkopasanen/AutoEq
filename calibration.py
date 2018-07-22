# -*- coding: utf-8 -*-

import os
from glob import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from frequency_response import FrequencyResponse


def normalize(s):
    return ''.join(ch for ch in s if ch.isalnum())


def main():
    # Filenames
    if_files = list(glob(os.path.join('innerfidelity', 'data', '**', '*.csv'), recursive=True))
    if_file_names = [os.path.split(os.path.abspath(f))[-1] for f in if_files]
    normalized_if_files = [normalize(s) for s in if_file_names]
    hp_files = list(glob(os.path.join('headphonecom', 'data', '**', '*.csv'), recursive=True))

    # Find matching files
    matching_if_files = []
    matching_hp_files = []
    for hp_file in hp_files:
        file_name = os.path.split(os.path.abspath(hp_file))[-1]
        for i in range(len(normalized_if_files)):
            if normalized_if_files[i] == normalize(file_name):
                matching_hp_files.append(hp_file)
                matching_if_files.append(if_files[i])

    # Write mathces to file for manual inspection
    df = pd.DataFrame(np.array([matching_hp_files, matching_if_files]).transpose())
    df.to_csv('matches.csv', index=False, header=False)

    fig, ax = plt.subplots()
    diffs = []
    # Calculate differences for all models
    if_compensation = FrequencyResponse.read_from_csv(os.path.join('innerfidelity', 'resources', 'innerfidelity_compensation_2017.csv'))
    if_compensation.interpolate()
    hp_compensation = FrequencyResponse.read_from_csv(os.path.join('headphonecom', 'resources', 'headphonecom_compensation.csv'))
    hp_compensation.interpolate()
    for i in range(len(matching_if_files)):
        if_fr = FrequencyResponse.read_from_csv(matching_if_files[i])
        if_fr.interpolate()
        if_fr.center()
        if_fr.compensate(if_compensation)
        hp_fr = FrequencyResponse.read_from_csv(matching_hp_files[i])
        hp_fr.interpolate()
        hp_fr.center()
        hp_fr.compensate(hp_compensation)
        diff = FrequencyResponse(name=if_fr.name, frequency=if_fr.frequency, raw=hp_fr.error - if_fr.error)
        plt.plot(diff.frequency, diff.raw)
        diffs.append(diff.raw)

    # Average and smooth difference
    f = FrequencyResponse.generate_frequencies()
    diffs = np.vstack(diffs)
    diff = np.mean(diffs, axis=0)
    std = np.std(diffs, axis=0)
    diff = FrequencyResponse(name='Headphone.com to Innerfidelity', frequency=f, raw=diff)
    diff.smooth(window_size=1 / 9, iterations=10)
    diff.raw = diff.smoothed
    diff.smoothed = np.array([])

    plt.xlabel('Frequency (Hz)')
    plt.semilogx()
    plt.xlim([20, 20000])
    plt.ylabel('Amplitude (dBr)')
    plt.ylim([-15, 15])
    plt.grid(which='major')
    plt.grid(which='minor')
    plt.title('Headphone.com to Innerfidelity')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
    plt.show()

    fig, ax = diff.plot_graph(f_min=10, f_max=20000, show=False)
    ax.fill_between(diff.frequency, diff.raw+std, diff.raw-std, facecolor='lightblue')
    plt.legend(['Headphone.com to Innerfidelity', 'Standard Deviation'])
    fig.savefig(os.path.join('calibration', 'headphonecom_to_innerfidelity.png'), dpi=240)
    plt.show()
    diff.write_to_csv(os.path.join('calibration', 'headphonecom_to_innerfidelity.csv'))

    diff.raw *= -1
    diff.name = 'Innerfidelity to Headphone.com'
    fig, ax = diff.plot_graph(f_min=10, f_max=20000, show=False)
    ax.fill_between(diff.frequency, diff.raw + std, diff.raw - std, facecolor='lightblue')
    plt.legend(['Innerfidelity to Headphone.com', 'Standard Deviation'])
    fig.savefig(os.path.join('calibration', 'innerfidelity_to_headphonecom.png'), dpi=240)
    plt.show()
    diff.write_to_csv(os.path.join('calibration', 'innerfidelity_to_headphonecom.csv'))


if __name__ == '__main__':
    main()
