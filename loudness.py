# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from frequency_response import FrequencyResponse


def equal_loudness_contour(phon):
    f = [20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500,
         3150, 4000, 5000, 6300, 8000, 10000, 12500]
    af = [0.532, 0.506, 0.480, 0.455, 0.432, 0.409, 0.387, 0.367, 0.349, 0.330, 0.315, 0.301, 0.288, 0.276, 0.267,
          0.259, 0.253, 0.250, 0.246, 0.244, 0.243, 0.243, 0.243, 0.242, 0.242, 0.245, 0.254, 0.271, 0.301]
    Lu = [-31.6, -27.2, -23.0, -19.1, -15.9, -13.0, -10.3, -8.1, -6.2, -4.5, -3.1, -2.0, -1.1, -0.4, 0.0, 0.3, 0.5, 0.0,
          -2.7, -4.1, -1.0, 1.7, 2.5, 1.2, -2.1, -7.1, -11.2, -10.7, -3.1]
    Tf = [78.5, 68.7, 59.5, 51.1, 44.0, 37.5, 31.5, 26.5, 22.1, 17.9, 14.4, 11.4, 8.6, 6.2, 4.4, 3.0, 2.2, 2.4, 3.5,
          1.7, -1.3, -4.2, -6.0, -5.4, -1.5, 6.0, 12.6, 13.9, 12.3]

    Ln = phon
    Lps = []
    for i in range(0, len(f)):
        Af = 0.00447 * (10.0 ** (Ln / 40.0) - 1.15) + (10.0 ** (((Tf[i] + Lu[i]) / 10.0) - 9.0) / 2.5) ** af[i]
        Lp = ((10.0 / af[i]) * math.log10(Af)) - Lu[i] + 94.0
        Lps.append(Lp)
    Lps = np.array(Lps)

    fr = FrequencyResponse(name='{} phon Equal Loudness Contour'.format(phon), frequency=f, raw=Lps)
    fr.interpolate(pol_order=3, f_min=20, f_max=12500)
    fr.center()
    return fr


def pop_frequency_distribution():
    # Approximation of pop music frequency distribution
    fr = FrequencyResponse(
        name='Pop Music Frequency Distribution',
        frequency=[20, 100, 100*math.sqrt(10), 1000, 1000*math.sqrt(10), 10000, 20000],
        raw=[-30, 0, -3, -6, -10, -20, -50]
    )
    fr.raw += 80
    fr.interpolate(pol_order=3, f_min=20, f_max=12500)
    #fr.center()
    return fr


def main():
    pop = pop_frequency_distribution()

    elc = equal_loudness_contour(80)
    elc.center()
    elc.raw = -elc.raw

    loudness = FrequencyResponse('Loudness', frequency=pop.frequency, raw=pop.raw+elc.raw)
    #loudness.center()

    fig, ax = pop.plot_graph(show=False)
    #elc.plot_graph(fig=fig, ax=ax, show=False)
    loudness.plot_graph(fig=fig, ax=ax, show=False)

    v = FrequencyResponse(name='V', frequency=[20, 1000, 20000], raw=[10, -10, 10])
    v.interpolate(pol_order=2)
    v.interpolate(f=loudness.frequency)
    v.plot_graph(fig=fig, ax=ax, show=False)

    v_l = FrequencyResponse(name='V Loudness', frequency=v.frequency, raw=v.raw+loudness.raw)
    v_l.plot_graph(fig=fig, ax=ax, show=False)

    a = FrequencyResponse(name='A', frequency=[20, 1000, 20000], raw=[-10, 5, -10])
    a.interpolate(pol_order=2)
    a.interpolate(f=loudness.frequency)
    a.plot_graph(fig=fig, ax=ax, show=False)

    a_l = FrequencyResponse(name='A Loudness', frequency=a.frequency, raw=a.raw+loudness.raw)
    a_l.plot_graph(fig=fig, ax=ax, show=False, a_min=-20, a_max=90)

    plt.legend(['Pop Music Frequency Distribution', 'Loudness',
                'V', 'V+L', 'A', 'A+L'])
    print('V: {}'.format(20*np.log10(np.mean(np.power(v.raw/20, 10)))))
    print('V loudness: {}'.format(20*np.log10(np.mean(np.power(v_l.raw/20, 10)))))
    print('A: {}'.format(20*np.log10(np.mean(np.power(a.raw/20, 10)))))
    print('A loudness: {}'.format(20*np.log10(np.mean(np.power(a_l.raw/20, 10)))))
    plt.show()
    loudness.write_to_csv('music_loudness_contour.csv')
    plt.close(fig)


if __name__ == '__main__':
    main()
