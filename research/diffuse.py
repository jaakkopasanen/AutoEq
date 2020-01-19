# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
from frequency_response import FrequencyResponse


def main():
    ht18 = FrequencyResponse.read_from_csv('compensation/harman_over-ear_2018_wo_bass.csv')
    df = FrequencyResponse.read_from_csv('compensation/diffuse_field.csv')
    df.raw += df._tilt(-1)
    eht = ht18.copy()
    eht.raw -= df.raw

    ifss = FrequencyResponse.read_from_csv('innerfidelity/resources/innerfidelity_compensation_sbaf-serious.csv')
    #ifdf = FrequencyResponse.read_from_csv('innerfidelity/resources/innerfidelity_compensation_2016.csv')
    ifdf = FrequencyResponse.read_from_csv('headphonecom/resources/headphonecom_compensation.csv')
    ifdf.raw += df._tilt(-1)
    #ifdf.raw -= 2.5
    eif = ifss.copy()
    eif.raw -= ifdf.raw

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(18, 9)

    ht18.plot_graph(fig=fig, ax=axs[0], show=False, color='blue')
    df.plot_graph(fig=fig, ax=axs[0], show=False, color='orange')
    eht.plot_graph(fig=fig, ax=axs[0], show=False, color='red')
    axs[0].legend(['Harman target 2018', 'Diffuse field (-1 dB/oct)', 'Difference'])
    axs[0].set_title('Harman target vs Diffuse field')

    ifss.plot_graph(fig=fig, ax=axs[1], show=False, color='blue')
    ifdf.plot_graph(fig=fig, ax=axs[1], show=False, color='orange')
    eif.plot_graph(fig=fig, ax=axs[1], show=False, color='red')
    #axs[1].legend(['SBAF-Serious', 'Innerfidelity diffuse field (-1 dB/oct)', 'Difference'])
    axs[1].legend(['SBAF-Serious', 'Headphonecom target (-1 dB/oct)', 'Difference'])
    axs[1].set_title('Innerfidelity SBAF-Serious vs Headphonecom')


    plt.show()

if __name__ == '__main__':
    main()
