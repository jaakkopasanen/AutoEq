import warnings
from time import time
from abc import ABC, abstractmethod
import numpy as np
from matplotlib import pyplot as plt, ticker
from scipy.optimize import fmin_slsqp
from scipy.signal import find_peaks
from tabulate import tabulate

from autoeq.constants import DEFAULT_SHELF_FILTER_MIN_FC, DEFAULT_SHELF_FILTER_MAX_FC, DEFAULT_SHELF_FILTER_MIN_Q, \
    DEFAULT_SHELF_FILTER_MAX_Q, DEFAULT_SHELF_FILTER_MIN_GAIN, DEFAULT_SHELF_FILTER_MAX_GAIN, \
    DEFAULT_PEAKING_FILTER_MIN_FC, DEFAULT_PEAKING_FILTER_MAX_FC, DEFAULT_PEAKING_FILTER_MIN_Q, \
    DEFAULT_PEAKING_FILTER_MAX_Q, DEFAULT_PEAKING_FILTER_MIN_GAIN, DEFAULT_PEAKING_FILTER_MAX_GAIN, \
    DEFAULT_PEQ_OPTIMIZER_MIN_F, DEFAULT_PEQ_OPTIMIZER_MAX_F, DEFAULT_PEQ_OPTIMIZER_MAX_TIME, \
    DEFAULT_PEQ_OPTIMIZER_TARGET_LOSS, DEFAULT_PEQ_OPTIMIZER_MIN_CHANGE_RATE, DEFAULT_PEQ_OPTIMIZER_MIN_STD


class PEQFilter(ABC):
    def __init__(self, f, fs,
                 fc=None, optimize_fc=None, min_fc=None, max_fc=None,
                 q=None, optimize_q=None, min_q=None, max_q=None,
                 gain=None, optimize_gain=None, min_gain=None, max_gain=None):
        self.f = np.array(f)
        self._fs = fs

        if not optimize_fc and fc is None:
            raise TypeError('fc must be given when not optimizing it')
        self._fc = fc
        self.optimize_fc = optimize_fc
        self.min_fc = min_fc
        self.max_fc = max_fc

        if not optimize_fc and fc is None:
            raise TypeError('q must be given when not optimizing it')
        self._q = q
        self.optimize_q = optimize_q
        self.min_q = min_q
        self.max_q = max_q

        if not optimize_fc and fc is None:
            raise TypeError('gain must be given when not optimizing it')
        self._gain = gain
        self.optimize_gain = optimize_gain
        self.min_gain = min_gain
        self.max_gain = max_gain

        self._ix10k = None
        self._ix20k = None

        self._fr = None

    def __str__(self):
        return f'{self.__class__.__name__} {self.fc:.0f} Hz, {self.q:.2f} Q, {self.gain:.1f} dB'

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._ix10k = None
        self._ix20k = None
        self._fr = None
        self._f = value

    @property
    def fs(self):
        return self._fs

    @fs.setter
    def fs(self, value):
        self._fr = None
        self._fs = value

    @property
    def fc(self):
        return self._fc

    @fc.setter
    def fc(self, value):
        self._fr = None
        self._fc = value

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, value):
        self._fr = None
        self._q = value

    @property
    def gain(self):
        return self._gain

    @gain.setter
    def gain(self, value):
        self._fr = None
        self._gain = value

    @property
    def ix10k(self):
        if self._ix10k is not None:
            return self._ix10k
        return np.argmin(np.abs(self.f - self.fs))

    @property
    def fr(self):
        """Calculates frequency response"""
        if self._fr is not None:
            return self._fr

        w = 2 * np.pi * self.f / self.fs
        phi = 4 * np.sin(w / 2) ** 2

        a0, a1, a2, b0, b1, b2 = self.biquad_coefficients()

        a1 *= -1
        a2 *= -1

        self._fr = 10 * np.log10(
            (b0 + b1 + b2) ** 2 + (b0 * b2 * phi - (b1 * (b0 + b2) + 4 * b0 * b2)) * phi
        ) - 10 * np.log10(
            (a0 + a1 + a2) ** 2 + (a0 * a2 * phi - (a1 * (a0 + a2) + 4 * a0 * a2)) * phi
        )
        return self._fr

    @abstractmethod
    def init(self, target):
        """Initializes optimizable center frequency (fc), qualtiy (q) and gain

        Args:
            target: Equalizer target frequency response

        Returns:
            List of initialized optimizable parameter values for the optimizer
        """
        pass

    @abstractmethod
    def biquad_coefficients(self):
        pass

    @property
    @abstractmethod
    def sharpness_penalty(self):
        pass

    @property
    @abstractmethod
    def band_penalty(self):
        pass


class Peaking(PEQFilter):
    def __init__(self, f, fs, fc=None, optimize_fc=None, min_fc=DEFAULT_PEAKING_FILTER_MIN_FC,
                 max_fc=DEFAULT_PEAKING_FILTER_MAX_FC, q=None, optimize_q=None, min_q=DEFAULT_PEAKING_FILTER_MIN_Q,
                 max_q=DEFAULT_PEAKING_FILTER_MAX_Q, gain=None, optimize_gain=None,
                 min_gain=DEFAULT_PEAKING_FILTER_MIN_GAIN, max_gain=DEFAULT_PEAKING_FILTER_MAX_GAIN):
        super().__init__(f, fs, fc, optimize_fc, min_fc, max_fc, q, optimize_q, min_q, max_q, gain, optimize_gain,
                         min_gain, max_gain)

    def init(self, target):
        """Initializes optimizable center frequency (fc), qualtiy (q) and gain

        The operating principle is to find the biggest (by width AND height) peak of the target curve and set center
        frequency at the peak's location. Quality is set in such a way that the filter width matches the peak width
        and gain is set to the peak height.

        Args:
            target: Equalizer target frequency response

        Returns:
            List of initialized optimizable parameter values for the optimizer
        """
        # Finds positive and negative peaks
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            positive_peak_ixs, peak_props = find_peaks(np.clip(target, 0, None), width=0, prominence=0, height=0)
            negative_peak_ixs, dip_props = find_peaks(np.clip(-target, 0, None), width=0, prominence=0, height=0)

        # Indexes for minimum and maximum center frequency
        min_fc_ix = np.argmin(np.abs(self.f - self.min_fc))
        max_fc_ix = np.argmin(np.abs(self.f - self.max_fc))

        if len(positive_peak_ixs) == 0 and len(negative_peak_ixs) == 0:
            # No peaks found
            params = []
            if self.optimize_fc:
                self.fc = self.f[(min_fc_ix + max_fc_ix) // 2]
                params.append(np.log10(self.fc))
            if self.optimize_q:
                self.q = np.sqrt(2)
                params.append(self.q)
            if self.optimize_gain:
                self.gain = 0.0
                params.append(self.gain)
            return params

        # All peak indexes together
        peak_ixs = np.concatenate([positive_peak_ixs, negative_peak_ixs])
        # Exclude peak indexes which are outside of minimum and maximum center frequency
        mask = np.logical_and(peak_ixs >= min_fc_ix, peak_ixs <= max_fc_ix)
        peak_ixs = peak_ixs[mask]
        # Properties of included peaks together
        widths = np.concatenate([peak_props['widths'], dip_props['widths']])[mask]
        heights = np.concatenate([peak_props['peak_heights'], dip_props['peak_heights']])[mask]
        # Find the biggest peak, by height AND width
        sizes = widths * heights  # Size of each peak for ranking
        ixs_ix = np.argmax(sizes)  # Index to indexes array which point to the biggest peak
        ix = peak_ixs[ixs_ix]  # Index to f and target

        params = []
        if self.optimize_fc:
            self.fc = np.clip(self.f[ix], self.min_fc, self.max_fc)
            params.append(np.log10(self.fc))  # Convert to logarithmic scale for optimizer
        if self.optimize_q:
            width = widths[ixs_ix]
            # Find bandwidth which matches the peak width
            f_step = np.log2(self.f[1] / self.f[0])
            bw = np.log2((2 ** f_step) ** width)
            # Calculate quality with bandwidth
            self.q = np.sqrt(2 ** bw) / (2 ** bw - 1)
            self.q = np.clip(self.q, self.min_q, self.max_q)
            params.append(self.q)
        if self.optimize_gain:
            # Target value at center frequency
            self.gain = heights[ixs_ix] if target[ix] > 0 else -heights[ixs_ix]
            self.gain = np.clip(self.gain, self.min_gain, self.max_gain)
            params.append(self.gain)
        return params

    def biquad_coefficients(self):
        """Calculates 2nd order biquad filter coefficients"""
        a = 10 ** (self.gain / 40)
        w0 = 2 * np.pi * self.fc / self._fs
        alpha = np.sin(w0) / (2 * self.q)

        a0 = 1 + alpha / a
        a1 = -(-2 * np.cos(w0)) / a0
        a2 = -(1 - alpha / a) / a0

        b0 = (1 + alpha * a) / a0
        b1 = (-2 * np.cos(w0)) / a0
        b2 = (1 - alpha * a) / a0

        return 1.0, a1, a2, b0, b1, b2

    @property
    def sharpness_penalty(self):
        """Calculates penalty for having too steep slope

        Multiplies the filter frequency response with a penalty coefficient and calculates MSE from it

        The penalty coefficient is a sigmoid function which goes quickly from 0.0 to 1.0 around 18 dB / octave slope
        """
        # This polynomial function gives the gain for peaking filter which achieves 18 dB / octave max derivative
        # The polynomial estimate is accurate in the vicinity of 18 dB / octave
        gain_limit = -0.09503189270199464 + 20.575128011847003 * (1 / self.q)
        # Scaled sigmoid function as penalty coefficient
        x = self.gain / gain_limit - 1
        sharpness_penalty_coefficient = 1 / (1 + np.e ** (-x * 100))
        return np.mean(np.square(self.fr * sharpness_penalty_coefficient))

    @property
    def band_penalty(self):
        """Calculates penalty for transition band extending Nyquist frequency

        Biquad filter shape starts to get distorted when the transition band extends Nyquist frequency in such a way
        that the right side gets compressed (greater slope). This method calculates the RMSE between
        the left and right sides of the frequency response. If the right side is fully compressed, the penalty is the
        entire effect of frequency response thus negating the filter entirely. Right side is mirrored around vertical
        axis.
        """
        fc_ix = np.argmin(np.abs(self.f - self.fc))  # Index to frequency array closes to center frequency
        # Number of indexes on each side of center frequency, not extending outside, only up to 10 kHz
        n = min(fc_ix, self.ix10k - fc_ix)
        if n == 0:
            return 0.0
        return np.mean(np.square(self.fr[fc_ix - n:fc_ix] - self.fr[fc_ix + n - 1:fc_ix - 1:-1]))


class ShelfFilter(PEQFilter, ABC):
    def __init__(self, f, fs, fc=None, optimize_fc=None, min_fc=DEFAULT_SHELF_FILTER_MIN_FC,
                 max_fc=DEFAULT_SHELF_FILTER_MAX_FC, q=None, optimize_q=None, min_q=DEFAULT_SHELF_FILTER_MIN_Q,
                 max_q=DEFAULT_SHELF_FILTER_MAX_Q, gain=None, optimize_gain=None,
                 min_gain=DEFAULT_SHELF_FILTER_MIN_GAIN, max_gain=DEFAULT_SHELF_FILTER_MAX_GAIN):
        super().__init__(f, fs, fc, optimize_fc, min_fc, max_fc, q, optimize_q, min_q, max_q, gain, optimize_gain,
                         min_gain, max_gain)

    @property
    def sharpness_penalty(self):
        # Shelf filters start to overshoot hard before they get anywhere near 18 dB per octave slope
        return 0.0

    @property
    def band_penalty(self):
        """Calculates penalty for transition band extending Nyquist frequency

        Biquad filter shape starts to get distorted when the transition band extends Nyquist frequency in such a way
        that the right side gets compressed (greater slope). This method calculates the MSE between
        the left and right sides of the frequency response. If the right side is fully compressed, the penalty is the
        entire effect of frequency response thus negating the filter entirely. Right side is mirrored around both axes.
        """
        fc_ix = np.argmin(np.abs(self.f - self.fc))  # Index to frequency array closes to center frequency
        # Number of indexes on each side of center frequency, not extending outside, only up to 10 kHz
        n = min(fc_ix, self.ix10k - fc_ix)
        if n == 0:
            return 0.0
        return np.mean(np.square(self.fr[fc_ix - n:fc_ix] - (self.gain - self.fr[fc_ix + n - 1:fc_ix - 1:-1])))


class HighShelf(ShelfFilter):
    def init(self, target):
        """Initializes optimizable center frequency (fc), quality (q) and gain

        The operating principle is to find a point after which the average level is greatest and set the center
        frequency there. Gain is set to average level of the target after the transition band. Quality is always set to
        0.7.

        Args:
            target: Equalizer target frequency response

        Returns:
            List of initialized optimizable parameter values for the optimizer
        """
        params = []
        if self.optimize_fc:
            # Find point where the ratio of average level after the point and average level before the point is the
            # greatest
            min_ix = np.sum(self.f < max(40, self.min_fc))
            max_ix = np.sum(self.f < min(10000, self.max_fc))
            ix = np.argmax([np.abs(np.mean(target[ix:])) for ix in range(min_ix, max_ix)])
            self.fc = np.clip(self.f[ix], self.min_fc, self.max_fc)
            params.append(np.log10(self.fc))
        if self.optimize_q:
            self.q = np.clip(0.7, self.min_q, self.max_q)
            params.append(self.q)
        if self.optimize_gain:
            # Calculated weighted average from the target where the frequency response (dBs) of a 1 dB shelf is the
            # weight vector
            self.gain = 1
            self.gain = np.dot(target, self.fr) / np.sum(self.fr)  # Weighted average
            self.gain = np.clip(self.gain, self.min_gain, self.max_gain)
            params.append(self.gain)
        return params

    def biquad_coefficients(self):
        """Calculates 2nd order biquad filter coefficients"""
        a = 10 ** (self.gain / 40)
        w0 = 2 * np.pi * self.fc / self._fs
        alpha = np.sin(w0) / (2 * self.q)

        a0 = (a + 1) - (a - 1) * np.cos(w0) + 2 * np.sqrt(a) * alpha
        a1 = -(2 * ((a - 1) - (a + 1) * np.cos(w0))) / a0
        a2 = -((a + 1) - (a - 1) * np.cos(w0) - 2 * np.sqrt(a) * alpha) / a0

        b0 = (a * ((a + 1) + (a - 1) * np.cos(w0) + 2 * np.sqrt(a) * alpha)) / a0
        b1 = (-2 * a * ((a - 1) + (a + 1) * np.cos(w0))) / a0
        b2 = (a * ((a + 1) + (a - 1) * np.cos(w0) - 2 * np.sqrt(a) * alpha)) / a0

        return 1.0, a1, a2, b0, b1, b2


class LowShelf(ShelfFilter):
    def init(self, target):
        """Initializes optimizable center frequency (fc), qualtiy (q) and gain

        The operating principle is to find a point before which the average level is greatest and set the center
        frequency there. Gain is set to average level of the target before the transition band. Quality is always set to
        0.7.

        Args:
            target: Equalizer target frequency response

        Returns:
            List of initialized optimizable parameter values for the optimizer
        """
        params = []
        if self.optimize_fc:
            # Find point where the ratio of average level before the point and average level after the point is the
            # greatest
            min_ix = np.sum(self.f < max(40, self.min_fc))
            max_ix = np.sum(self.f < min(10000, self.max_fc))
            ix = np.argmax([np.abs(np.mean(target[:ix + 1])) for ix in range(min_ix, max_ix)])
            ix += min_ix
            self.fc = np.clip(self.f[ix], self.min_fc, self.max_fc)
            params.append(np.log10(self.fc))
        if self.optimize_q:
            self.q = np.clip(0.7, self.min_q, self.max_q)
            params.append(self.q)
        if self.optimize_gain:
            # Calculated weighted average from the target where the frequency response (dBs) of a 1 dB shelf is the
            # weight vector
            self.gain = 1
            self.gain = np.dot(target, self.fr) / np.sum(self.fr)  # Weighted average
            self.gain = np.clip(self.gain, self.min_gain, self.max_gain)
            params.append(self.gain)
        return params

    def biquad_coefficients(self):
        """Calculates 2nd order biquad filter coefficients"""
        a = 10 ** (self.gain / 40)
        w0 = 2 * np.pi * self.fc / self._fs
        alpha = np.sin(w0) / (2 * self.q)

        a0 = (a + 1) + (a - 1) * np.cos(w0) + 2 * np.sqrt(a) * alpha
        a1 = -(-2 * ((a - 1) + (a + 1) * np.cos(w0))) / a0
        a2 = -((a + 1) + (a - 1) * np.cos(w0) - 2 * np.sqrt(a) * alpha) / a0

        b0 = (a * ((a + 1) - (a - 1) * np.cos(w0) + 2 * np.sqrt(a) * alpha)) / a0
        b1 = (2 * a * ((a - 1) - (a + 1) * np.cos(w0))) / a0
        b2 = (a * ((a + 1) - (a - 1) * np.cos(w0) - 2 * np.sqrt(a) * alpha)) / a0

        return 1.0, a1, a2, b0, b1, b2


class OptimizationHistory:
    def __init__(self):
        self.start_time = time()
        self.time = []
        self.loss = []
        self.moving_avg_loss = []
        self.change_rate = []
        self.std = []
        self.params = []


class PEQ:
    def __init__(self, f, fs, filters=None, target=None,
                 min_f=DEFAULT_PEQ_OPTIMIZER_MIN_F, max_f=DEFAULT_PEQ_OPTIMIZER_MAX_F,
                 max_time=DEFAULT_PEQ_OPTIMIZER_MAX_TIME, target_loss=DEFAULT_PEQ_OPTIMIZER_TARGET_LOSS,
                 min_change_rate=DEFAULT_PEQ_OPTIMIZER_MIN_CHANGE_RATE, min_std=DEFAULT_PEQ_OPTIMIZER_MIN_STD):
        self.f = np.array(f)
        self.fs = fs
        self.filters = []
        if filters is not None:
            for filt in filters:
                self.add_filter(filt)
        self.target = np.array(target) if target is not None else None
        self._min_f = min_f
        self._max_f = max_f
        self._min_f_ix = np.argmin(np.abs(self.f - self._min_f))
        self._max_f_ix = np.argmin(np.abs(self.f - self._max_f))
        self._ix50 = np.argmin(np.abs(self.f - 50))
        self._10k_ix = np.argmin(np.abs(self.f - 10000))
        self._20k_ix = np.argmin(np.abs(self.f - 20000))
        self._max_time = max_time
        self._target_loss = target_loss
        self._min_change_rate = min_change_rate
        self._min_std = min_std
        self.history = None

    @classmethod
    def from_dict(cls, config, f, fs, target=None):
        """Initializes class instance with configuration dict and target

        Args:
            config: Configuration dict with sampling rate "fs", filters and optionally filter defaults. Filters and
                filter defaults are dicts with keys fc, q, gain, min_fc, max_fc, min_q, max_q, min_gain, max_gain and
                type. The filter fc, q and gain are optimized if they are not present in the filter dicts, separately
                for each filter. "type" can be "LOW_SHELF", "PEAKING" or "HIGH_SHELF". "filter_defaults" sets the
                default values for filters to avoid repetition. Be wary of setting fc, q and gain in filter defaults
                as these will disable optimization for all filters and there is no way to enable optimization for a
                single filter after that. See `constants.py` for examples.
            f: Frequency array
            fs: Sampling rate
            target: Equalizer frequency response target. Needed if optimization is to be performed.
        Returns:

        """
        if target is not None and len(f) != len(target):
            raise ValueError('f and target must be the same length')
        optimizer_kwargs = config['optimizer'] if 'optimizer' in config else {}
        peq = cls(f, fs, target=target, **optimizer_kwargs)
        filter_classes = {'LOW_SHELF': LowShelf, 'PEAKING': Peaking, 'HIGH_SHELF': HighShelf}
        keys = ['fc', 'q', 'gain', 'min_fc', 'max_fc', 'min_q', 'max_q', 'min_gain', 'max_gain', 'type']
        for filt in config['filters']:
            if 'filter_defaults' in config:
                for key in keys:
                    if key not in filt and key in config['filter_defaults']:
                        filt[key] = config['filter_defaults'][key]
            peq.add_filter(filter_classes[filt['type']](
                peq.f, peq.fs,
                **{key: filt[key] for key in keys if key in filt and key != 'type'},
                optimize_fc='fc' not in filt, optimize_q='q' not in filt, optimize_gain='gain' not in filt
            ))
        return peq

    def add_filter(self, filt):
        if filt.fs != self.fs:
            raise ValueError(f'Filter sampling rate ({filt.fs}) must match equalizer sampling rate ({self.fs})')
        if not np.array_equal(filt.f, self.f):
            raise ValueError('Filter frequency array (f) must match equalizer frequency array')
        self.filters.append(filt)

    def sort_filters(self):
        type_order = [LowShelf.__name__, Peaking.__name__, HighShelf.__name__]
        self.filters = sorted(
            self.filters,
            key=lambda filt: type_order.index(filt.__class__.__name__) + filt.fc / 1e6,
            reverse=False)

    @property
    def fr(self):
        """Calculates cascade frequency response"""
        return np.sum([filt.fr for filt in self.filters], axis=0)

    @property
    def max_gain(self):
        """Calculates maximum gain of frequency response"""
        return np.max(self.fr)

    def markdown_table(self):
        """Formats filters as a Markdown table string"""
        table_data = [
            [i + 1, filt.__class__.__name__, f'{filt.fc:.0f}', f'{filt.q:.2f}', f'{filt.gain:.1f}']
            for i, filt in enumerate(self.filters)
        ]
        return tabulate(
            table_data,
            headers=['#', 'Type', 'Fc (Hz)', 'Q', 'Gain (dB)'],
            tablefmt='github'
        )

    def _parse_optimizer_params(self, params):
        """Extracts fc, q and gain from optimizer params and updates filters

        Args:
            params: Parameter list/array passed by the optimizer. The values correspond to the initialized params
        """
        i = 0
        for filt in self.filters:
            if filt.optimize_fc:
                filt.fc = 10 ** params[i]
                i += 1
            if filt.optimize_q:
                filt.q = params[i]
                i += 1
            if filt.optimize_gain:
                filt.gain = params[i]
                i += 1

    def _optimizer_loss(self, params, parse=True):
        """Calculates optimizer loss value"""
        # Update filters with latest iteration params
        if parse:
            self._parse_optimizer_params(params)

        # Above 10 kHz only the total energy matters so we'll take the average
        fr = self.fr.copy()
        target = self.target.copy()
        target[self._10k_ix:] = np.mean(target[self._10k_ix:])
        fr[self._10k_ix:] = np.mean(self.fr[self._10k_ix:])
        #target[:self._ix50] = np.mean(target[:self._ix50])  # TODO: Is this good?
        #fr[:self._ix50] = np.mean(fr[:self._ix50])

        # Mean squared error as loss, between minimum and maximum frequencies
        loss_val = np.mean(np.square(target[self._min_f_ix:self._max_f_ix] - fr[self._min_f_ix:self._max_f_ix]))

        # Sum penalties from all filters to MSE
        for filt in self.filters:
            loss_val += filt.sharpness_penalty
            #loss_val += filt.band_penalty  # TODO

        return np.sqrt(loss_val)

    def _init_optimizer_params(self):
        """Creates a list of initial parameter values for the optimizer

        The list is fc, q and gain from each filter. Non-optimizable parameters are skipped.
        """
        order = [
            [Peaking.__name__, True, True],  # Peaking
            [LowShelf.__name__, True, True],  # Low shelfs
            [HighShelf.__name__, True, True],  # High shelfs
            [Peaking.__name__, True, False],  # Peaking with fixed q
            [LowShelf.__name__, True, False],  # Low shelfs with fixed q
            [HighShelf.__name__, True, False],  # High shelfs with fixed q
            [Peaking.__name__, False, True],  # Peaking with fixed fc
            [LowShelf.__name__, False, True],  # Low shelfs with fixed fc
            [HighShelf.__name__, False, True],  # High shelfs with fixed fc
            [Peaking.__name__, False, False],  # Peaking with fixed fc and q
            [LowShelf.__name__, False, False],  # Low shelfs with fixed fc and q
            [HighShelf.__name__, False, False],  # High shelfs with fixed fc and q
        ]

        def init_order(filter_ix):
            filt = self.filters[filter_ix]
            ix = order.index([filt.__class__.__name__, filt.optimize_fc, filt.optimize_q])
            val = ix * 100
            if filt.optimize_fc:
                val += 1 / np.log2(filt.max_fc / filt.min_fc)
            return val

        # Initialize filter params as list of empty lists, one per filter
        filter_params = [[]] * len(self.filters)
        # Indexes to self.filters sorted by filter init order
        filter_argsort = sorted(list(range(len(self.filters))), key=init_order, reverse=True)
        remaining_target = self.target.copy()
        for ix in filter_argsort:  # Iterate sorted filter indexes
            filt = self.filters[ix]  # Get filter
            filter_params[ix] = filt.init(remaining_target)  # Init filter and place params to list of lists
            remaining_target -= filt.fr  # Adjust target
        filter_params = np.concatenate(filter_params).flatten()  # Flatten params list
        return filter_params

    def _init_optimizer_bounds(self):
        """Creates optimizer bounds

        For each optimizable fc, q and gain a (min, max) tuple is added
        """
        bounds = []
        for filt in self.filters:
            if filt.optimize_fc:
                bounds.append((np.log10(filt.min_fc), np.log10(filt.max_fc)))
            if filt.optimize_q:
                bounds.append((filt.min_q, filt.max_q))
            if filt.optimize_gain:
                bounds.append((filt.min_gain, filt.max_gain))
        return bounds

    def _callback(self, params):
        """Optimization callback function"""
        n = 8
        t = time() - self.history.start_time
        loss = self._optimizer_loss(params, parse=False)

        self.history.time.append(t)
        self.history.loss.append(loss)

        # Standard deviation of the last N loss values
        std = np.std(np.array(self.history.loss[-n:]))
        # Standard deviation of the last N/2 loss values
        std_np2 = np.std(np.array(self.history.loss[-n//2:]))
        self.history.std.append(std)

        moving_avg_loss = np.mean(np.array(self.history.loss[-n:])) if len(self.history.loss) >= n else 0.0
        self.history.moving_avg_loss.append(moving_avg_loss)
        if len(self.history.moving_avg_loss) > 1:
            d_loss = loss - self.history.moving_avg_loss[-2]
            d_time = t - self.history.time[-2]
            change_rate = d_loss / d_time if len(self.history.moving_avg_loss) > n else 0.0
        else:
            change_rate = 0.0
        self.history.change_rate.append(change_rate)
        self.history.params.append(params)
        if self._max_time is not None and t >= self._max_time:
            raise OptimizationFinished('Maximum time reached')
        if self._target_loss is not None and loss <= self._target_loss:
            raise OptimizationFinished('Target loss reached')
        if (
                self._min_change_rate is not None
                and len(self.history.moving_avg_loss) > n
                and -change_rate < self._min_change_rate
        ):
            raise OptimizationFinished('Change too small')
        if self._min_std is not None and (
                # STD from last N loss values must be below min STD OR...
                (len(self.history.std) > n and std < self._min_std)
                # ...STD from the last N/2 loss values must be below half of the min STD
                or (len(self.history.std) > n // 2 and std_np2 < self._min_std / 2)
        ):
            raise OptimizationFinished('STD too small')

    def optimize(self):
        """Optimizes filter parameters"""
        self.history = OptimizationHistory()
        try:
            fmin_slsqp(  # Tested all of the scipy minimize methods, this is the best
                self._optimizer_loss,
                self._init_optimizer_params(),
                bounds=self._init_optimizer_bounds(),
                callback=self._callback,
                iprint=0)
        except OptimizationFinished as err:
            # Restore best params
            self._parse_optimizer_params(self.history.params[np.argmin(self.history.loss)])
            #print(err)

    def plot(self, fig=None, ax=None):
        if fig is None:
            fig, ax = plt.subplots()
            fig.set_size_inches(12, 8)
            fig.set_facecolor('white')
            ax.set_facecolor('white')
            ax.set_xlabel('Frequency (Hz)')
            ax.semilogx()
            ax.set_xlim([20, 20e3])
            ax.set_ylabel('Amplitude (dBr)')
            ax.grid(True, which='major')
            ax.grid(True, which='minor')
            ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
            ax.set_xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000])
        if self.target is not None:
            ax.plot(self.f, self.target, color='black', linestyle='--', linewidth=1, label='Target')
        for i, filt in enumerate(self.filters):
            ax.fill_between(filt.f, np.zeros(filt.fr.shape), filt.fr, alpha=0.3, color=f'C{i}')
            ax.plot(filt.f, filt.fr, color=f'C{i}', linewidth=1)
        ax.plot(self.f, self.fr, color='black', linewidth=1, label='FR')
        ax.legend()
        return fig, ax


class OptimizationFinished(Exception):
    pass
