# -*- coding: utf-8 -*-

import os
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))


def main():
    iem19 = FrequencyResponse.read_from_csv(os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2019v2_orig.csv'))
    iem19.interpolate()
    iem19.center()
    iem19.name = 'Harman in-ear 2019v2'
    iem19.write_to_csv(os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2019v2.csv'))

    iem19_wo_bass = iem19.copy()
    iem19_wo_bass.name = 'Harman in-ear 2019v2 without bass boost'
    ind = np.argmin(iem19_wo_bass.raw[iem19_wo_bass.frequency < 1000])
    iem19_wo_bass.raw[:ind] = iem19_wo_bass.raw[ind]
    iem19_wo_bass.plot_graph(
        show=False, color='C0',
        file_path=os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2019v2_wo_bass.png')
    )
    iem19_wo_bass.write_to_csv(os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2019v2_wo_bass.csv'))

    iem17 = FrequencyResponse.read_from_csv(os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2017-1.csv'))
    usound = FrequencyResponse.read_from_csv(os.path.join(ROOT_DIR, 'compensation', 'usound.csv'))
    oe18 = FrequencyResponse.read_from_csv(os.path.join(ROOT_DIR, 'compensation', 'harman_over-ear_2018.csv'))

    fig, ax = iem19.plot_graph(
        show=False, color='C0',
        file_path=os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2019v2.png')
    )
    iem17.plot_graph(fig=fig, ax=ax, show=False, color='C1')
    usound.plot_graph(fig=fig, ax=ax, color='C2', show=False)
    oe18.plot_graph(fig=fig, ax=ax, color='C3', show=False)

    ax.legend(['Harman in-ear 2019v2', 'Harman in-ear 2017-1', 'Usound', 'Harman over-ear 2018'])
    ax.set_title('In-ear Headphone Targets')
    plt.show()


if __name__ == '__main__':
    main()
