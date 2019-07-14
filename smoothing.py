# -*- coding: utf-8 -*-

import os
from copy import deepcopy
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from frequency_response import FrequencyResponse


def main():
    os.makedirs('smoothing', exist_ok=True)
    for file_path in glob('results/innerfidelity/sbaf-serious/*/*.csv'):
        fr = FrequencyResponse.read_from_csv(file_path)
        fr.smoothen_fractional_octave()

        light = fr.copy()
        light.name = 'Light'
        light.smoothen_fractional_octave(
            window_size=1 / 6,
            iterations=1,
            treble_f_lower=100,
            treble_f_upper=10000,
            treble_window_size=1 / 3,
            treble_iterations=1
        )

        heavy = fr.copy()
        heavy.name = 'Heavy'
        heavy.smoothen_fractional_octave(
            window_size=1 / 3,
            iterations=1,
            treble_f_lower=1000,
            treble_f_upper=6000,
            treble_window_size=1.3,
            treble_iterations=1
        )

        combination = fr.copy()
        combination.name = 'Combination'
        combination.error = np.max(np.vstack([light.error_smoothed, heavy.error_smoothed]), axis=0)
        combination.smoothen_fractional_octave(
            window_size=1 / 3,
            iterations=1,
            treble_f_lower=100,
            treble_f_upper=10000,
            treble_window_size=1 / 3,
            treble_iterations=1
        )

        window = fr.copy()
        window.name = 'Window'
        window.smoothen_fractional_octave(
            window_size=1.0,
            iterations=1,
            treble_window_size=1.0,
            treble_iterations=1
        )

        iterations = fr.copy()
        iterations.name = 'Iterations'
        iterations.smoothen_fractional_octave(
            window_size=1/3,
            iterations=100,
            treble_window_size=1/3,
            treble_iterations=60
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
        # ax.plot(fr.frequency, fr.error_smoothed)
        # legend.append('Default smoothed error')
        # ax.plot(light.frequency, light.error_smoothed)
        # legend.append('Ligthly smoothed error)
        ax.plot(heavy.frequency, heavy.error_smoothed)
        legend.append('Heavily smoothed error')
        ax.plot(combination.frequency, combination.error_smoothed)
        legend.append('Combination smoothed error')
        # ax.plot(combination.frequency, -combination.error_smoothed)
        # legend.append('Equalization')
        ax.plot(light.frequency, fr.error - combination.error_smoothed)
        legend.append('Equalized')
        # ax.plot(window.frequency, window.error_smoothed)
        # legend.append(window.name)
        # ax.plot(iterations.frequency, iterations.error_smoothed)
        # legend.append(iterations.name)
        ax.set_ylim([-20, 20])

        ax.legend(legend)
        #plt.show(fig)
        fig.savefig(os.path.join('smoothing', fr.name + '.png'), dpi=150)
        plt.close(fig)


if __name__ == '__main__':
    main()
