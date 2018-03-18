# -*- coding: utf-8 -*-

from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from frequency_response import FrequencyResponse


def main():
    fr = FrequencyResponse.read_from_csv('innerfidelity\\transformation.csv')

    fig, ax = plt.subplots()
    legend = []
    plt.plot(fr.frequency, fr.raw)
    legend.append('Raw')

    pol_order = 2
    small_window = 1/5
    large_window = 1/2
    iterations = 100

    filtered = fr.raw
    for _ in range(iterations):
        filtered = savgol_filter(filtered, fr._window_size(small_window), pol_order)
    plt.plot(fr.frequency, filtered)
    legend.append('Filtered {i} times with {w} octaves'.format(i=iterations, w=small_window))

    filtered = fr.raw
    filtered = savgol_filter(filtered, fr._window_size(large_window), pol_order)
    plt.plot(fr.frequency, filtered)
    legend.append('Filtered {i} times with {w} octaves'.format(i=1, w=large_window))

    plt.xlabel('Frequency (Hz)')
    plt.semilogx()
    plt.xlim([10, 20000])
    plt.ylabel('Amplitude (dBr)')
    plt.ylim([-4, 12])
    plt.legend(legend)
    plt.grid(which='major')
    plt.grid(which='minor')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
    plt.show()


if __name__ == '__main__':
    main()
