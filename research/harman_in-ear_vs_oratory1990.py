# -*- coding: utf-8 -*-

import os
import sys
from tabulate import tabulate
import matplotlib.pyplot as plt
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))


def main():
    harman = FrequencyResponse.read_from_csv(os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2019v2.csv'))
    harman.name = 'oratory1990 vs Harman in-ear 2019'
    oratory1990 = FrequencyResponse.read_from_csv(os.path.join(ROOT_DIR, 'compensation', 'usound.csv'))
    harman.compensate(oratory1990)
    harman.smoothen_fractional_octave(window_size=1/6, treble_window_size=1/6)
    harman.equalize()
    filters, _, _ = harman.optimize_parametric_eq(max_filters=2, fs=48000)
    filters_formatted = []
    for i in range(len(filters)):
        filters_formatted.append(['Peaking'] + [f'{x:.2f}' for x in filters[i]])
    filters_table_str = tabulate(
        filters_formatted,
        headers=['Type', 'Fc', 'Q', 'Gain'],
        tablefmt='orgtbl'
    ).replace('+', '|').replace('|-', '|:')
    print(filters_table_str)
    fig, ax = harman.plot_graph(show=False)
    ax.legend(['oratory1990', 'Harman in-ear 2019 1/6 oct smoothed', 'Difference 1/6 oct smoothed',
               'Harman ine-ear 2019', 'Difference 1/6 oct smoothed', 'Parametric EQ with 2 filters',
               'Equalization target', 'Equalized'])
    plt.show()


if __name__ == '__main__':
    main()
