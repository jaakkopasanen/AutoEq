# -*- coding: utf-8 -*-

import os
from frequency_response import FrequencyResponse
import matplotlib.pyplot as plt


def main():
    stock = FrequencyResponse.read_from_csv('data/HE400S stock.csv')
    focus = FrequencyResponse.read_from_csv('data/HE400S focus.csv')
    base = FrequencyResponse.read_from_csv('innerfidelity/data/HiFiMAN HE400S/HiFiMAN HE400S.csv')

    stock.interpolate(f_min=20, f_max=20000)
    stock.center()
    focus.interpolate(f_min=20, f_max=20000)
    focus.center()
    base.interpolate(f=stock.frequency)
    base.center()
    diff = FrequencyResponse(name='Diff', frequency=stock.frequency, raw=focus.raw-stock.raw)
    fr = FrequencyResponse(name='HE400S with Focus Pads', frequency=stock.frequency, raw=base.raw+diff.raw)

    _fr = FrequencyResponse(name='debug', frequency=stock.frequency, raw=base.raw, smoothed=diff.raw, equalization=fr.raw)
    _fr.plot_graph()

    fr.smoothen(window_size=1 / 5, iterations=10, treble_window_size=1 / 2, treble_iterations=100)


    #stock.plot_graph()
    #focus.plot_graph()
    #diff.plot_graph()
    #base.plot_graph()
    #fr.plot_graph()
    os.makedirs('innerfidelity/data/HiFiMAN HE400S with Focus Pads', exist_ok=True)
    fr.write_to_csv(file_path='innerfidelity/data/HiFiMAN HE400S with Focus Pads/HiFiMAN HE400S with Focus Pads ORIG.csv')
    fr.equalize(max_gain=12, smoothen=True, window_size=1 / 5, bass_target=4)
    fr.write_to_csv(file_path='innerfidelity/data/HiFiMAN HE400S with Focus Pads/HiFiMAN HE400S with Focus Pads.csv')
    fig, ax = fr.plot_graph(show=False, file_path='innerfidelity/data/HiFiMAN HE400S with Focus Pads/HiFiMAN HE400S with Focus Pads.png')
    plt.close(fig)
    fr.write_eqapo_graphic_eq('innerfidelity/data/HiFiMAN HE400S with Focus Pads/HiFiMAN HE400S with Focus Pads EqAPO.txt')


if __name__ == '__main__':
    main()
