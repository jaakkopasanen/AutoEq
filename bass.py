# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from frequency_response import FrequencyResponse


def main(oe, ie):
    oe18 = FrequencyResponse.read_from_csv('compensation/harman_over-ear_2018.csv')
    oe18wob = FrequencyResponse.read_from_csv('compensation/harman_over-ear_2018_wo_bass.csv')
    ie17 = FrequencyResponse.read_from_csv('compensation/harman_in-ear_2017-1.csv')
    ie17wob = FrequencyResponse.read_from_csv('compensation/harman_in-ear_2017-1_wo_bass.csv')

    if oe:
        bass = FrequencyResponse(name='Bass', frequency=oe18.frequency)
        bass.raw = bass._sigmoid(35, 280, 4, -2.0)
        fig, ax = oe18.plot_graph(show=False, color=None)
        oe18wob.plot_graph(fig=fig, ax=ax, show=False, color=None)
        bass.plot_graph(fig=fig, ax=ax, show=False, color=None)
        boost = FrequencyResponse(name='Boost', frequency=bass.frequency, raw=bass.raw)
        boost.center()
        oe18wob_boosted = FrequencyResponse(name='Boosted OE18', frequency=oe18.frequency, raw=oe18wob.raw + boost.raw)
        oe18wob_boosted.plot_graph(fig=fig, ax=ax, show=False, color=None)
        ax.legend(['OE18', 'OE18 w/o bass', 'Bass', 'Boosted'])
        plt.show()

    if ie:
        bass = FrequencyResponse(name='Bass', frequency=ie17.frequency)
        bass.raw = bass._sigmoid(25, 350, 8, -1.7)
        fig, ax = ie17.plot_graph(show=False, color=None)
        ie17wob.plot_graph(fig=fig, ax=ax, show=False, color=None)
        bass.plot_graph(fig=fig, ax=ax, show=False, color=None)
        boost = FrequencyResponse(name='Boost', frequency=bass.frequency, raw=bass.raw)
        boost.center()
        ie17wob_boosted = FrequencyResponse(name='Boosted IE17', frequency=ie17.frequency, raw=ie17wob.raw + boost.raw)
        ie17wob_boosted.plot_graph(fig=fig, ax=ax, show=False, color=None)
        ax.legend(['IE17', 'IE17 w/o bass', 'Bass', 'Boosted'])
        plt.show()


if __name__ == '__main__':
    main(True, True)
