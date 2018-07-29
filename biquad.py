# -*- coding: utf-8 -*-

import numpy as np
from frequency_response import FrequencyResponse


def numpyfy(fc, Q, gain, fs):
    # Cast lists to Numpy arrays
    if type(fc) == list:
        fc = np.array(fc)
    if type(Q) == list:
        Q = np.array(Q)
    if type(gain) == list:
        gain = np.array(gain)
    if type(fs) == list:
        fs = np.array(fs)
    return fc, Q, gain, fs


def peaking(fc, Q, gain, fs=48000):
    """Peaking filter designer.

    Args:
        fc: Center frequency
        Q: Q factor
        gain: Gain
        fs: Sampling frequency

    Returns:
        Biquad filter coefficients a0, a1, a2, b0, b1 and b2 as tuple
    """
    # Turn lists into numpy arrays
    fc, Q, gain, fs = numpyfy(fc, Q, gain, fs)

    A = 10 ** (gain / 40)
    w0 = 2 * np.pi * fc / fs
    alpha = np.sin(w0) / (2 * Q)

    a0 = 1 + alpha / A
    a1 = -(-2 * np.cos(w0)) / a0
    a2 = -(1 - alpha / A) / a0

    b0 = (1 + alpha * A) / a0
    b1 = (-2 * np.cos(w0)) / a0
    b2 = (1 - alpha * A) / a0

    return 1.0, a1, a2, b0, b1, b2


def low_shelf(fc, Q, gain, fs=48000):
    """Low shelf filter designer.

    Args:
        fc: Center frequency
        Q: Q factor
        gain: Gain
        fs: Sampling frequency

    Returns:
        Biquad filter coefficients a0, a1, a2, b0, b1 and b2 as tuple
    """
    # Turn lists into numpy arrays
    fc, Q, gain, fs = numpyfy(fc, Q, gain, fs)

    A = 10 ** (gain / 40)
    w0 = 2 * np.pi * fc / fs
    alpha = np.sin(w0) / (2 * Q)

    a0 = (A + 1) + (A - 1) * np.cos(w0) + 2 * np.sqrt(A) * alpha
    a1 = -(-2 * ((A - 1) + (A + 1) * np.cos(w0))) / a0
    a2 = -((A + 1) + (A - 1) * np.cos(w0) - 2 * np.sqrt(A) * alpha) / a0

    b0 = (A * ((A + 1) - (A - 1) * np.cos(w0) + 2 * np.sqrt(A) * alpha)) / a0
    b1 = (2 * A * ((A - 1) - (A + 1) * np.cos(w0))) / a0
    b2 = (A * ((A + 1) - (A - 1) * np.cos(w0) - 2 * np.sqrt(A) * alpha)) / a0

    return 1.0, a1, a2, b0, b1, b2


def high_shelf(fc, Q, gain, fs=48000):
    """High shelf filter designer.

    Args:
        fc: Center frequency
        Q: Q factor
        gain: Gain
        fs: Sampling frequency

    Returns:
        Biquad filter coefficients a0, a1, a2, b0, b1 and b2 as tuple
    """
    # Turn lists into numpy arrays
    fc, Q, gain, fs = numpyfy(fc, Q, gain, fs)

    A = 10 ** (gain / 40)
    w0 = 2 * np.pi * fc / fs
    alpha = np.sin(w0) / (2 * Q)

    a0 = (A + 1) - (A - 1) * np.cos(w0) + 2 * np.sqrt(A) * alpha
    a1 = -(2 * ((A - 1) - (A + 1) * np.cos(w0))) / a0
    a2 = -((A + 1) - (A - 1) * np.cos(w0) - 2 * np.sqrt(A) * alpha) / a0

    b0 = (A * ((A + 1) + (A - 1) * np.cos(w0) + 2 * np.sqrt(A) * alpha)) / a0
    b1 = (-2 * A * ((A - 1) + (A + 1) * np.cos(w0))) / a0
    b2 = (A * ((A + 1) + (A - 1) * np.cos(w0) - 2 * np.sqrt(A) * alpha)) / a0

    return 1.0, a1, a2, b0, b1, b2


def digital_coeffs(f, fs, a0, a1, a2, b0, b1, b2):
    w = 2 * np.pi * f / fs
    phi = 4 * np.sin(w / 2) ** 2

    a1 *= -1
    a2 *= -1

    c = 10 * np.log10(
        (b0 + b1 + b2) ** 2 + (b0 * b2 * phi - (b1 * (b0 + b2) + 4 * b0 * b2)) * phi
    ) - 10 * np.log10(
        (a0 + a1 + a2) ** 2 + (a0 * a2 * phi - (a1 * (a0 + a2) + 4 * a0 * a2)) * phi
    )
    return c


def main():
    fc = [20, 220, 450, 1280, 2200, 3000, 5700, 6600, 7600]
    Q = [1.1, 0.9, 1.0, 1.5, 4.0, 2.0, 6.0, 7.0, 5.0]
    gain = [2.1, -3.8, -2.0, 4.0, -3.5, 4.5, -5.0, 0.4, -2.4]
    fs = 48000

    a0, a1, a2, b0, b1, b2 = peaking(fc, Q, gain, fs=fs)

    fr = FrequencyResponse(name='Biquad')
    f = fr.frequency
    f = np.repeat(np.expand_dims(f, 1), len(fc), axis=1)

    c_peaking = digital_coeffs(f, fs, a0, a1, a2, b0, b1, b2)

    a0, a1, a2, b0, b1, b2 = low_shelf(55, 0.7, 2.4, fs=fs)
    c_low_shelf = digital_coeffs(fr.frequency, fs, a0, a1, a2, b0, b1, b2)

    #fr.raw = c_peaking
    #fr.raw = c_low_shelf
    fr.raw = np.sum(c_peaking, axis=1) + np.sum(np.expand_dims(c_low_shelf, axis=1), axis=1)
    fr.plot_graph()


if __name__ == '__main__':
    main()
