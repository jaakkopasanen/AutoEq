# -*- coding: utf-8 -*-

import numpy as np
from frequency_response import FrequencyResponse


def numpyfy(f_center, Q, gain, fs):
    # Cast lists to Numpy arrays
    if type(f_center) == list:
        f_center = np.array(f_center)
    if type(Q) == list:
        Q = np.array(Q)
    if type(gain) == list:
        gain = np.array(gain)
    if type(fs) == list:
        fs = np.array(fs)
    return f_center, Q, gain, fs


def peaking(f_center, Q, gain, fs=48000):
    """Peaking filter designer.

    Args:
        f_center: Center frequency
        Q: Q factor
        gain: Gain
        fs: Sampling frequency

    Returns:
        Biquad filter coefficients a0, a1, a2, b0, b1 and b2 as tuple
    """
    # Turn lists into numpy arrays
    f_center, Q, gain, fs = numpyfy(f_center, Q, gain, fs)

    A = 10 ** (gain / 40)
    w0 = 2 * np.pi * f_center / fs
    alpha = np.sin(w0) / (2 * Q)

    a0 = 1 + alpha / A
    a1 = -(-2 * np.cos(w0)) / a0
    a2 = -(1 - alpha / A) / a0

    b0 = (1 + alpha * A) / a0
    b1 = (-2 * np.cos(w0)) / a0
    b2 = (1 - alpha * A) / a0

    return 1.0, a1, a2, b0, b1, b2


def low_shelf(f_center, Q, gain, fs=48000):
    """Low shelf filter designer.

    Args:
        f_center: Center frequency
        Q: Q factor
        gain: Gain
        fs: Sampling frequency

    Returns:
        Biquad filter coefficients a0, a1, a2, b0, b1 and b2 as tuple
    """
    # Turn lists into numpy arrays
    f_center, Q, gain, fs = numpyfy(f_center, Q, gain, fs)

    A = 10 ** (gain / 40)
    w0 = 2 * np.pi * f_center / fs
    alpha = np.sin(w0) / (2 * Q)

    a0 = (A + 1) + (A - 1) * np.cos(w0) + 2 * np.sqrt(A) * alpha
    a1 = -(-2 * ((A - 1) + (A + 1) * np.cos(w0))) / a0
    a2 = -((A + 1) + (A - 1) * np.cos(w0) - 2 * np.sqrt(A) * alpha) / a0

    b0 = (A * ((A + 1) - (A - 1) * np.cos(w0) + 2 * np.sqrt(A) * alpha)) / a0
    b1 = (2 * A * ((A - 1) - (A + 1) * np.cos(w0))) / a0
    b2 = (A * ((A + 1) - (A - 1) * np.cos(w0) - 2 * np.sqrt(A) * alpha)) / a0

    return 1.0, a1, a2, b0, b1, b2


def high_shelf(f_center, Q, gain, fs=48000):
    """High shelf filter designer.

    Args:
        f_center: Center frequency
        Q: Q factor
        gain: Gain
        fs: Sampling frequency

    Returns:
        Biquad filter coefficients a0, a1, a2, b0, b1 and b2 as tuple
    """
    # Turn lists into numpy arrays
    f_center, Q, gain, fs = numpyfy(f_center, Q, gain, fs)

    A = 10 ** (gain / 40)
    w0 = 2 * np.pi * f_center / fs
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
    f_center = [200, 1000]
    Q = [2, 2]
    gain = [5, 3]
    fs = 48000

    a0, a1, a2, b0, b1, b2 = high_shelf(f_center, Q, gain, fs=fs)

    fr = FrequencyResponse(name='Biquad')
    f = fr.frequency
    f = np.repeat(np.expand_dims(f, 1), len(f_center), axis=1)

    c = digital_coeffs(f, fs, a0, a1, a2, b0, b1, b2)

    #fr.raw = np.sum(c, axis=1)
    fr.raw = c
    fr.plot_graph()


if __name__ == '__main__':
    main()
