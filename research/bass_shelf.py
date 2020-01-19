# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
from frequency_response import FrequencyResponse
from biquad import low_shelf, digital_coeffs


def main():
    oe18 = FrequencyResponse.read_from_csv('compensation/harman_over-ear_2018.csv')
    oe18_nobass = FrequencyResponse.read_from_csv('compensation/harman_over-ear_2018_wo_bass.csv')
    oe18_bass = oe18_nobass.copy()
    oe18_bass.raw += digital_coeffs(oe18_bass.frequency, 48000, *low_shelf(100, 0.65, 6, 48000))

    iem19 = FrequencyResponse.read_from_csv('compensation/harman_in-ear_2019v2.csv')
    iem19_nobass = FrequencyResponse.read_from_csv('compensation/harman_in-ear_2019v2_wo_bass.csv')
    iem19_bass = iem19_nobass.copy()
    iem19_bass.raw += digital_coeffs(iem19_bass.frequency, 48000, *low_shelf(100, 0.65, 9.5, 48000))

    usound = FrequencyResponse.read_from_csv('compensation/usound.csv')
    usound_nobass = FrequencyResponse.read_from_csv('compensation/usound_wo_bass.csv')
    usound_bass = usound_nobass.copy()
    usound_bass.raw += digital_coeffs(usound_bass.frequency, 48000, *low_shelf(150, 0.65, 9.4, 48000))

    fig, ax = oe18.plot_graph(show=False, color='C0')
    oe18_nobass.plot_graph(show=False, color='C1', fig=fig, ax=ax)
    oe18_bass.plot_graph(show=False, color='C2', fig=fig, ax=ax)
    ax.legend(['Original', 'Without bass', 'Shelf bass'])

    fig, ax = iem19.plot_graph(show=False, color='C0')
    iem19_nobass.plot_graph(show=False, color='C1', fig=fig, ax=ax)
    iem19_bass.plot_graph(show=False, color='C2', fig=fig, ax=ax)
    ax.legend(['Original', 'Without bass', 'Shelf bass'])

    fig, ax = usound.plot_graph(show=False, color='C0')
    usound_nobass.plot_graph(show=False, color='C1', fig=fig, ax=ax)
    usound_bass.plot_graph(show=False, color='C2', fig=fig, ax=ax)
    ax.legend(['Original', 'Without bass', 'Shelf bass'])

    plt.show()


if __name__ == '__main__':
    main()
