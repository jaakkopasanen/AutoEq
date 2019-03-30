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
    f_res = 40
    input_dir = os.path.join('oratory1990', 'data', 'onear')
    glob_files = glob(os.path.join(input_dir, '**', '*.csv'), recursive=True)
    for input_file_path in glob_files:
        fr = FrequencyResponse.read_from_csv(input_file_path)
        fr.equalization = fr.raw
        fr.raw = np.array([])

        mp = fr.minimum_phase_impulse_response(fs=fs, f_res=f_res/2)
        f_mp, mp = fft(mp, fs)
        f_mp[0] = 0.1
        mp = FrequencyResponse(name='Minimum phase', frequency=f_mp, raw=mp)
        mp.center()

        lp = fr.linear_phase_impulse_response(fs=fs, f_res=f_res)
        f_lp, lp = fft(lp, fs)
        f_lp[0] = 0.1
        lp = FrequencyResponse(name='Linear phase', frequency=f_lp, raw=lp)
        lp.center()

        plt.plot(fr.frequency, fr.equalization)
        plt.plot(lp.frequency, lp.raw)
        plt.plot(mp.frequency, mp.raw)
        plt.legend(['Raw', 'Linear phase', 'Minimum phase'])
        plt.semilogx()
        plt.xlabel('Frequency (Hz)')
        plt.xlim([20, 20000])
        plt.ylabel('Gain (dBr)')
        plt.ylim([-20, 20])
        plt.title(fr.name)
        plt.grid(True, which='major')
        plt.grid(True, which='minor')
        plt.show()


if __name__ == '__main__':
    main()
