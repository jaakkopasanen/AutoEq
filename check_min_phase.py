# -*- coding: utf-8 -*-

import os
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from frequency_response import FrequencyResponse


def fft(x, fs):
    nfft = len(x)
    df = fs / nfft
    f = np.arange(0, fs - df, df)
    X = np.fft.fft(x)
    X_mag = 20 * np.log10(np.abs(X))
    return f[0:int(np.ceil(nfft/2))], X_mag[0:int(np.ceil(nfft/2))]


def main():
    fs = 48000
    f_res = 5
    input_dir = os.path.join('oratory1990', 'data', 'onear')
    glob_files = glob(os.path.join(input_dir, '**', '*.csv'), recursive=True)
    for input_file_path in glob_files:
        fr = FrequencyResponse.read_from_csv(input_file_path)
        fr.equalization = fr.raw
        fr.raw = np.array([])

        mp = fr.minimum_phase_impulse_response(fs=fs, f_res=f_res)
        f_mp, mp = fft(mp, fs)

        lp = fr.linear_phase_impulse_response(fs=fs, f_res=f_res)
        f_lp, lp = fft(lp, fs)

        plt.plot(f_lp, lp)
        plt.plot(f_mp, mp)
        plt.legend(['Linear phase', 'Minimum phase'])
        plt.semilogx()
        plt.xlabel('Frequency (Hz)')
        plt.xlim([20, 20000])
        plt.ylabel('Gain (dBr)')
        plt.ylim([-40, 0])
        plt.title(fr.name)
        plt.show()


if __name__ == '__main__':
    main()
