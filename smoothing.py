# -*- coding: utf-8 -*-

import os
from copy import deepcopy
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from frequency_response import FrequencyResponse


def main():
    for file_path in glob('results/innerfidelity/sbaf-serious/*/*.csv'):
        fr = FrequencyResponse.read_from_csv(file_path)
        fr.smoothen()

        light = fr.copy()
        light.name = 'Light'
        light.smoothen(
            window_size=1 / 6,
            iterations=1,
            treble_f_lower=100,
            treble_f_upper=10000,
            treble_window_size=1 / 3,
            treble_iterations=1
        )

        heavy = fr.copy()
        heavy.name = 'Heavy'
        heavy.smoothen(
            window_size=1 / 3,
            iterations=1,
            treble_f_lower=1000,
            treble_f_upper=6000,
            treble_window_size=1 / 2,
            treble_iterations=100
        )

        combination = fr.copy()
        combination.name = 'Combination'
        combination.error = np.max(np.vstack([light.error_smoothed, heavy.error_smoothed]), axis=0)
        combination.smoothen(
            window_size=1 / 3,
            iterations=1,
            treble_f_lower=100,
            treble_f_upper=10000,
            treble_window_size=1 / 3,
            treble_iterations=1
        )

        fig, ax = fr.plot_graph(
            show=False,
            close=False,
            raw=False,
            smoothed=False,
            error=False,
            error_smoothed=False,
            equalization=False,
            parametric_eq=False,
            target=False,
            equalized=False
        )
        fig.set_size_inches(15, 10)
        legend = []
        ax.plot(fr.frequency, fr.error)
        legend.append('Raw error')
        #ax.plot(fr.frequency, fr.error_smoothed)
        #legend.append('Default smoothing')
        #ax.plot(light.frequency, light.error_smoothed)
        #legend.append('Light smoothing')
        ax.plot(heavy.frequency, heavy.error_smoothed)
        legend.append('Heavy smoothing')
        ax.plot(combination.frequency, combination.error_smoothed)
        legend.append('Combination')
        ax.plot(combination.frequency, -combination.error_smoothed)
        legend.append('Equalization')
        ax.plot(light.frequency, fr.error - combination.error_smoothed)
        legend.append('Equalized')
        ax.set_ylim([-20, 20])

        ax.legend(legend)
        plt.show(fig)
        #fig.savefig(os.path.join('smoothing', fr.name + '.png'), dpi=150)
        #plt.close(fig)


if __name__ == '__main__':
    main()
