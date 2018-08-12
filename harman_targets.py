# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from frequency_response import FrequencyResponse


def save(df, column, name):
    fr = FrequencyResponse(name=name, frequency=df['Frequency'], raw=df[column])
    fr.interpolate()
    fr.center()
    name = name.lower().replace(' ', '_')
    fr.write_to_csv('compensation/{}.csv'.format(name))
    fr.plot_graph(file_path='compensation/{}.png'.format(name), show=False, color=None)

    ind = np.argmin(fr.raw[:400])
    fr.raw[:ind] = fr.raw[ind]
    fr.write_to_csv('compensation/{}_wo_bass.csv'.format(name))
    fr.plot_graph(file_path='compensation/{}_wo_bass.png'.format(name), show=False, color=None)


def main():
    df = pd.read_csv('compensation/harman.csv')
    save(df, 'Over-Ear (2013)', 'Harman Over-Ear 2013')
    save(df, 'Over-Ear (2015)', 'Harman Over-Ear 2015')
    save(df, 'Over-Ear (2018)', 'Harman Over-Ear 2018')
    save(df, 'In-Ear (2016)', 'Harman In-Ear 2016')
    save(df, 'In-Ear_2 (2017)', 'Harman In-Ear 2017-2')
    save(df, 'In-Ear_1 (2017)', 'Harman In-Ear 2017-1')
    save(df, 'Loudspeaker equalized to flat in-room response (2013)', 'Loudspeaker In-Room Flat 2013')


if __name__ == '__main__':
    main()
