import numpy as np
from scipy.fft import fft


def magnitude_response(x, fs):
    """Calculates frequency magnitude response

    Args:
        x: Audio data
        fs: Sampling rate

    Returns:
        - **f:** Frequencies
        - **X:** Magnitudes
    """
    nfft = len(x)
    df = fs / nfft
    f = np.arange(0, fs - df, df)
    y = fft(x)
    y_mag = 20 * np.log10(np.abs(y))
    return f[0:int(np.ceil(nfft/2))], y_mag[0:int(np.ceil(nfft/2))]
