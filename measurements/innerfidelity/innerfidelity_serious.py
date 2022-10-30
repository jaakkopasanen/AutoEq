# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from autoeq.frequency_response import FrequencyResponse


def main():
    trans = FrequencyResponse.read_from_csv('resources\innerfidelity_transformation_SBAF-Serious.csv')
    comp16 = FrequencyResponse.read_from_csv('resources\innerfidelity_compensation_2016.csv')
    comp17 = FrequencyResponse.read_from_csv('resources\innerfidelity_compensation_2017.csv')

    trans.interpolate()
    trans.center()
    comp = FrequencyResponse(name='Serious Compensation', frequency=comp16.frequency, raw=comp16.raw + trans.raw)

    fig, ax = trans.plot_graph(show=False)
    comp16.plot_graph(fig=fig, ax=ax, show=False)
    comp.plot_graph(fig=fig, ax=ax, show=False)
    comp17.plot_graph(fig=fig, ax=ax, show=False)
    fig.legend(['Serious', '2016', '2016+Serious', '2017'])
    plt.show()

    comp.write_to_csv('resources\innerfidelity_compensation_SBAF-Serious.csv')
    comp.plot_graph(show=False, close=True, file_path='resources\innerfidelity_compensation_SBAF_Serious.png')


if __name__ == '__main__':
    main()
