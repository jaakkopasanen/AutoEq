# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import signal


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


def digital_coeffs(f, fs, a0, a1, a2, b0, b1, b2, reduce=False):
    f = np.array(f)

    shape = None
    coeffs = [a0, a1, a2, b0, b1, b2]
    for i in range(len(coeffs)):
        if not np.isscalar(coeffs[i]):
            # Lists are made arrays
            coeffs[i] = np.array(coeffs[i]).flatten()

            if coeffs[i].size == 1:
                # Len 1 arrays are made scalars
                coeffs[i] = coeffs[i][0]
            else:
                # Make into column array
                coeffs[i] = np.expand_dims(coeffs[i], axis=1)
                # Record shape
                if shape is not None and coeffs[i].shape != shape:
                    raise ValueError('All coefficient shapes must be the same or scalar')
                shape = coeffs[i].shape
    a0, a1, a2, b0, b1, b2 = coeffs

    if shape is not None:
        # Coefficients are arrays, replicate frequency array for multiplications
        f = np.tile(f, shape)

    w = 2 * np.pi * f / fs
    phi = 4 * np.sin(w / 2) ** 2

    a1 *= -1
    a2 *= -1

    c = 10 * np.log10(
        (b0 + b1 + b2) ** 2 + (b0 * b2 * phi - (b1 * (b0 + b2) + 4 * b0 * b2)) * phi
    ) - 10 * np.log10(
        (a0 + a1 + a2) ** 2 + (a0 * a2 * phi - (a1 * (a0 + a2) + 4 * a0 * a2)) * phi
    )

    if shape is not None and reduce:
        return np.sum(c, axis=0)

    return c


def impulse_response(a0, a1, a2, b0, b1, b2, n=250):
    raise NotImplemented('biquad.impulse_response is not correctly implemented!')
    ir = signal.unit_impulse(n)
    for _a0, _a1, _a2, _b0, _b1, _b2 in zip(a0, a1, a2, b0, b1, b2):
        ir = signal.lfilter(np.concatenate([_b0, _b1, _b2]), np.concatenate([_a0, _a1, _a2]), ir)
    ir = np.concatenate(([0.0], ir))
    return ir


def main():
    fc = [20, 220, 450, 1280, 2200, 3000, 5700, 6600, 7600]
    Q = [1.1, 0.9, 1.0, 1.5, 4.0, 2.0, 6.0, 7.0, 5.0]
    gain = [2.1, -3.8, -2.0, 4.0, -3.5, 4.5, -5.0, 0.4, -2.4]

    fs = 48000

    a0, a1, a2, b0, b1, b2 = peaking(fc, Q, gain, fs=fs)

    f = [20]
    while f[-1] < fs:
        f.append(f[-1]*2**(1/16))
    f = np.repeat(np.expand_dims(f, 1), len(fc), axis=1)

    c = digital_coeffs(f, fs, a0, a1, a2, b0, b1, b2)
    a0 = [a0] * len(a1)
    ir = impulse_response(a0, a1, a2, b0, b1, b2, n=250)

    fig, ax = plt.subplots()
    #plt.plot(f, np.sum(c, axis=1), linewidth=3)
    plt.plot(f, c)
    plt.xlabel('Frequency (Hz)')
    plt.semilogx()
    plt.xlim([20, 20000])
    plt.ylabel('Amplitude (dBr)')
    plt.grid(True, which='major')
    plt.grid(True, which='minor')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
    plt.show()

    fig, ax = plt.subplots()
    plt.plot(np.arange(0, len(ir)) / fs, ir)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.ylim([-0.01, 0.01])
    plt.show()


if __name__ == '__main__':
    main()
