# -*- coding: utf-8 -*-

import sys
from pathlib import Path
ROOT_PATH = Path().resolve().parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
import numpy as np
import scipy
from frequency_response import FrequencyResponse
from research.limited_gradient_smoothing.utils import log_log_gradient


class FR(FrequencyResponse):
    @staticmethod
    def limited_forward_delta(x, y, limit, start_index=0):
        limited = []
        for i in range(len(x)):
            if i < start_index:
                limited.append(y[i])
            else:
                gradient = log_log_gradient(x[i], x[i - 1], y[i], limited[-1])
                if limit >= 0.0:
                    gradient = np.min([gradient, limit])
                else:
                    gradient = np.max([gradient, limit])
                octaves = np.log(x[i] / x[i - 1]) / np.log(2)
                limited.append(limited[-1] + gradient * octaves)
        return np.array(limited)

    @classmethod
    def limited_delta(cls, x, y, limit):
        peak_finder = cls(name='peak_finder', frequency=x, raw=y)
        peak_finder.smoothen_fractional_octave(window_size=1 / 12, treble_window_size=1 / 3, treble_f_lower=9000,
                                               treble_f_upper=11000)
        peaks = scipy.signal.find_peaks(-peak_finder.smoothed)[0]
        forward_start = peaks[0]
        backward_start = len(x) - peaks[-1] - 1

        limited_forward = cls.limited_forward_delta(x, y, limit, start_index=forward_start)
        limited_backward = cls.limited_forward_delta(np.flip(x), np.flip(y), -limit, start_index=backward_start)
        limited_backward = np.flip(limited_backward)

        _fr = FrequencyResponse(name='limiter', frequency=x.copy(),
                                raw=np.min(np.vstack([limited_forward, limited_backward]), axis=0))
        _fr.smoothen_fractional_octave(window_size=1 / 6, treble_window_size=1 / 6)
        return _fr.smoothed.copy()

    def equalize(self,
                 max_gain=6.0,
                 smoothen=True,
                 treble_f_lower=5000,
                 treble_f_upper=10000,
                 treble_max_gain=6.0,
                 treble_gain_k=1.0):
        """Creates equalization curve and equalized curve.

        Args:
            max_gain: Maximum positive gain in dB
            smoothen: Smooth kinks caused by clipping gain to max gain?
            treble_f_lower: Lower frequency boundary for transition region between normal parameters and treble parameters
            treble_f_upper: Upper frequency boundary for transition reqion between normal parameters and treble parameters
            treble_max_gain: Maximum positive gain in dB in treble region
            treble_gain_k: Coefficient for treble gain, positive and negative. Useful for disbling or reducing \
                           equalization power in treble region. Defaults to 1.0 (not limited).
        """
        # Limit gain
        eq_target = np.clip(self.error * -1, None, max_gain)

        # Limit delta
        limited = self.limited_delta(self.frequency, eq_target, 6.0)
        self.equalization = limited
        self.parametric_eq = eq_target

        # Equalized
        self.equalized_raw = self.raw + self.equalization
        if len(self.smoothed):
            self.equalized_smoothed = self.smoothed + self.equalization