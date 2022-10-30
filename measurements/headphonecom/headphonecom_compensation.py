# -*- coding:utf-8 -*-

import os
from glob import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from autoeq.frequency_response import FrequencyResponse


def main():
    fig, ax = plt.subplots()
    diffs = []
    # Calculate differences for all models
    for file in glob(os.path.join('compensation', 'compensated', '**', '*.csv'), recursive=True):
        file = os.path.abspath(file)
        comp = FrequencyResponse.read_from_csv(file)
        comp.interpolate()
        comp.center()
        raw_data_path = file.replace('compensated', 'raw')
        raw = FrequencyResponse.read_from_csv(raw_data_path)
        raw.interpolate()
        raw.center()
        diff = FrequencyResponse(name=comp.name, frequency=comp.frequency, raw=raw.raw-comp.raw)
        plt.plot(diff.frequency, diff.raw)
        diffs.append(diff.raw)

    # Average and smoothen difference
    f = FrequencyResponse.generate_frequencies()
    diffs = np.vstack(diffs)
    diff = np.mean(diffs, axis=0)
    diff = FrequencyResponse(name='Headphone.com Compensation', frequency=f, raw=diff)
    diff.smoothen_fractional_octave(window_size=1 / 9, iterations=10)
    diff.raw = diff.smoothed
    diff.smoothed = np.array([])

    plt.xlabel('Frequency (Hz)')
    plt.semilogx()
    plt.xlim([20, 20000])
    plt.ylabel('Amplitude (dBr)')
    plt.ylim([-15, 15])
    plt.grid(which='major')
    plt.grid(which='minor')
    plt.title('Headphone.com Compensation Function')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
    plt.show()

    diff.write_to_csv('headphonecom_compensation.csv')
    diff.plot_graph(show=True, f_min=10, f_max=20000, file_path='headphonecom_compensation.png')


if __name__ == '__main__':
    main()
