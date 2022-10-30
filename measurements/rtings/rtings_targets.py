# -*- coding: utf-8 -*-

import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
from autoeq.frequency_response import FrequencyResponse


def measurements_avg():
    stack = []
    for file in glob('data/*/*/*.csv'):
        stack.append(FrequencyResponse.read_from_csv(file).raw)
    return FrequencyResponse(name='AVG', raw=np.mean(np.vstack(stack), axis=0))


def main():
    serious = FrequencyResponse.read_from_csv('resources/rtings_compensation_sbaf-serious.csv')
    native = FrequencyResponse.read_from_csv('resources/rtings_compensation.csv')
    avg = measurements_avg()
    hd650 = FrequencyResponse.read_from_csv('data/onear/Sennheiser HD 650/Sennheiser HD 650.csv')

    fig, ax = native.plot_graph(show=False, color=None)
    serious.plot_graph(fig=fig, ax=ax, show=False, color=None)
    avg.plot_graph(fig=fig, ax=ax, show=False, color=None)
    hd650.plot_graph(fig=fig, ax=ax, show=False, color=None)

    plt.legend(['Rtings native', 'SBAF Serious', 'Measurements Avg', 'Sennheiser HD 650'])
    plt.title('Rtings Targets')
    plt.ylim([-10.0, 12.0])
    plt.show()
    fig.savefig('resources/rtings_targets_comparison.png', dpi=120)

    avg.raw[avg.frequency < 2500] = native.raw[native.frequency < 2500]
    avg.write_to_csv('resources/rtings_compensation_avg.csv')
    avg.plot_graph(show=False, file_path='resources/rtings_compensation_avg.png', color=None)


if __name__ == '__main__':
    main()
