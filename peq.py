from abc import ABC, abstractmethod
import numpy as np
from scipy.optimize import fmin_slsqp
from scipy.signal import find_peaks
from tabulate import tabulate


class PEQFilter(ABC):
    def __init__(self, f, fs,
                 fc=None, optimize_fc=None, min_fc=None, max_fc=None,
                 q=None, optimize_q=None, min_q=None, max_q=None,
                 gain=None, optimize_gain=None, min_gain=None, max_gain=None):
        self.f = np.array(f)
        self.fs = fs

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

        self._fr = None

    def __str__(self):
        return f'{self.__class__.__name__} {self.fc:.0f} Hz, {self.q:.2f} Q, {self.gain:.1f} dB'

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
    def bandwidth(self):
        return np.log2(1 + 1 / (2 * self.q**2) + np.sqrt(((2 * self.q**2 + 1) / self.q**2)**2 / 4 - 1))

    @property
    def fr(self):
        if self._fr is not None:
            return self._fr
        w = 2 * np.pi * self.f / self.fs
        phi = 4 * np.sin(w / 2) ** 2

        a0, a1, a2, b0, b1, b2 = self.biquad_coefficients()

        a1 *= -1
        a2 *= -1

        return 10 * np.log10(
            (b0 + b1 + b2) ** 2 + (b0 * b2 * phi - (b1 * (b0 + b2) + 4 * b0 * b2)) * phi
        ) - 10 * np.log10(
            (a0 + a1 + a2) ** 2 + (a0 * a2 * phi - (a1 * (a0 + a2) + 4 * a0 * a2)) * phi
        )

    @abstractmethod
    def init(self, target):
        pass

    @abstractmethod
    def biquad_coefficients(self):
        pass

    @property
    @abstractmethod
    def sharpness_penalty(self):
        pass


class Peaking(PEQFilter):
    def __init__(self, f, fs,
                 fc=None, optimize_fc=None, min_fc=20, max_fc=20e3,
                 q=None, optimize_q=None, min_q=0.18248, max_q=6,
                 gain=None, optimize_gain=None, min_gain=-20, max_gain=20):
        super().__init__(f, fs, fc, optimize_fc, min_fc, max_fc, q, optimize_q, min_q, max_q, gain, optimize_gain,
                         min_gain, max_gain)

    def init(self, target):
        """Initializes optimizable fc, q and gain"""
        peak_ixs, peak_props = find_peaks(np.clip(target, 0, None), width=0, prominence=0, height=0)
        dip_ixs, dip_props = find_peaks(np.clip(-target, 0, None), width=0, prominence=0, height=0)

        min_fc_ix = np.sum(self.f < self.min_fc)
        max_fc_ix = np.sum(self.f < self.max_fc)

        ixs = np.concatenate([peak_ixs, dip_ixs])
        mask = np.logical_and(ixs >= min_fc_ix, ixs <= max_fc_ix)
        ixs = ixs[mask]
        widths = np.concatenate([peak_props['widths'], dip_props['widths']])[mask]
        heights = np.concatenate([peak_props['peak_heights'], dip_props['peak_heights']])[mask]
        sizes = widths * heights
        ixs_ix = np.argmax(sizes)  # Index to indexes array which point to the peak with greatest size
        ix = ixs[ixs_ix]  # Index to f and target

        params = []
        if self.optimize_fc:
            self.fc = self.f[ix]
            params.append(np.log10(self.fc))
        if self.optimize_q:
            width = widths[ixs_ix]
            f_step = np.log2(self.f[1] / self.f[0])
            bw = np.log2((2 ** f_step) ** width)
            self.q = np.sqrt(2 ** bw) / (2 ** bw - 1)
            params.append(self.q)
        if self.optimize_gain:
            self.gain = heights[ixs_ix] if target[ix] > 0 else - heights[ixs_ix]
            params.append(self.gain)
        return params

    def biquad_coefficients(self):
        a = 10 ** (self.gain / 40)
        w0 = 2 * np.pi * self.fc / self.fs
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
        # This polynomial function gives the gain for peaking filter which achieves 18 dB / octave max derivative
        # The polynomial estimate is accurate in the vicinity of 18 dB / octave
        gain_limit = -0.09503189270199464 + 20.575128011847003 * (1 / self.q)
        # Scaled sigmoid function as penalty coefficient
        x = self.gain / gain_limit - 1
        sharpness_penalty_coefficient = 1 / (1 + np.e ** (-x * 100))
        return np.mean(np.square(self.fr * sharpness_penalty_coefficient))


class ShelfFilter(PEQFilter, ABC):
    def __init__(self, f, fs,
                 fc=None, optimize_fc=None, min_fc=20, max_fc=20e3,
                 q=None, optimize_q=None, min_q=0.4, max_q=0.7,
                 gain=None, optimize_gain=None, min_gain=-20, max_gain=20):
        super().__init__(f, fs, fc, optimize_fc, min_fc, max_fc, q, optimize_q, min_q, max_q, gain, optimize_gain,
                         min_gain, max_gain)

    @property
    def sharpness_penalty(self):
        # Shelf filters start to overshoot hard before they get anywhere near 18 dB per octave slope
        return 0.0


class HighShelf(ShelfFilter):
    def init(self, target):
        params = []
        if self.optimize_fc:
            # Find point where the ratio of average level after the point and average level before the point is the
            # greatest
            ix = np.argmax([np.mean(target[ix:]) / np.mean(target[:ix + 1]) for ix in range(1, len(self.f))])
            self.fc = self.f[ix]
            params.append(np.log10(self.fc))
        if self.optimize_q:
            self.q = 0.7
            params.append(self.q)
        if self.optimize_gain:
            ix = np.argmin(np.abs(self.f - self.fc))
            self.gain = np.mean(target[ix:])
            params.append(self.gain)
        return params

    def biquad_coefficients(self):
        a = 10 ** (self.gain / 40)
        w0 = 2 * np.pi * self.fc / self.fs
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
        params = []
        if self.optimize_fc:
            # Find point where the ratio of average level before the point and average level after the point is the
            # greatest
            ix = np.argmax([np.mean(np.mean(target[:ix + 1] / target[ix:])) for ix in range(1, len(self.f))])
            self.fc = self.f[ix]
            params.append(np.log10(self.fc))
        if self.optimize_q:
            self.q = 0.7
            params.append(self.q)
        if self.optimize_gain:
            ix = np.argmin(np.abs(self.f - self.fc))
            self.gain = np.mean(target[:ix + 1])
            params.append(self.gain)
        return params

    def biquad_coefficients(self):
        a = 10 ** (self.gain / 40)
        w0 = 2 * np.pi * self.fc / self.fs
        alpha = np.sin(w0) / (2 * self.q)

        a0 = (a + 1) + (a - 1) * np.cos(w0) + 2 * np.sqrt(a) * alpha
        a1 = -(-2 * ((a - 1) + (a + 1) * np.cos(w0))) / a0
        a2 = -((a + 1) + (a - 1) * np.cos(w0) - 2 * np.sqrt(a) * alpha) / a0

        b0 = (a * ((a + 1) - (a - 1) * np.cos(w0) + 2 * np.sqrt(a) * alpha)) / a0
        b1 = (2 * a * ((a - 1) - (a + 1) * np.cos(w0))) / a0
        b2 = (a * ((a + 1) - (a - 1) * np.cos(w0) - 2 * np.sqrt(a) * alpha)) / a0

        return 1.0, a1, a2, b0, b1, b2


class PEQ:
    def __init__(self, f, fs, filters=None, target=None):
        self.f = np.array(f)
        self.fs = fs
        self.filters = []
        if filters is not None:
            for filt in filters:
                self.add_filter(filt)
        self.target = np.array(target) if target is not None else None
        self._ix50 = np.sum(self.f < 50)
        self._ix10k = np.sum(self.f < 10e3)  # Index for ~10 kHz
        self._ix20k = np.sum(self.f < 20e3)  # Index for ~20 kHz

    @classmethod
    def from_dict(cls, config, target=None):
        freq = []
        f = 20
        while f <= 20e3:
            freq.append(f)
            f *= 1.01
        peq = cls(freq, config['fs'], target=target)
        filter_classes = {'LOW_SHELF': LowShelf, 'PEAKING': Peaking, 'HIGH_SHELF': HighShelf}
        keys = ['fc', 'q', 'gain', 'min_fc', 'max_fc', 'min_q', 'max_q', 'min_gain', 'max_gain', 'type']
        for filt in config['filters']:
            if 'filter_defaults' in config:
                for key in keys:
                    if key not in filt and key in config['filter_defaults']:
                        filt[key] = config['filter_defaults'][key]
            peq.add_filter(filter_classes[filt['type']](
                peq.f.copy(), peq.fs,
                **{key: filt[key] for key in keys if key in filt and key != 'type'},
                optimize_fc='fc' not in filt, optimize_q='q' not in filt, optimize_gain='gain' not in filt
            ))
        return peq

    def add_filter(self, filt):
        if filt.fs != self.fs:
            raise ValueError('Filter sampling rate (fs) must match equalizer sampling rate')
        if not np.array_equal(filt.f, self.f):
            raise ValueError('Filter frequency array (f) must match equalizer frequency array')
        self.filters.append(filt)

    @property
    def fr(self):
        return np.sum([filt.fr for filt in self.filters], axis=0)

    def markdown_table(self):
        type_order = [LowShelf.__name__, Peaking.__name__, HighShelf.__name__]

        def filter_sorter(filt):
            return type_order.index(filt.__class__.__name__) + filt.fc / 1e6

        table_data = [
            [filt.__class__.__name__, f'{filt.fc:.0f}', f'{filt.q:.2f}', f'{filt.gain:.1f}']
            for filt in sorted(self.filters, key=filter_sorter, reverse=False)
        ]
        return tabulate(
            table_data,
            headers=['Type', 'Fc (Hz)', 'Q', 'Gain (dB)'],
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
                filt.fc = 10**params[i]
                i += 1
            if filt.optimize_q:
                filt.q = params[i]
                i += 1
            if filt.optimize_gain:
                filt.gain = params[i]
                i += 1

    def _optimizer_loss(self, params):
        """Calculates optimizer loss value"""
        # Update filters with latest iteration params
        self._parse_optimizer_params(params)

        # Above 10 kHz only the total energy matters so we'll take mean of values between 10 kHz and 20 kHz
        fr = self.fr.copy()
        target = self.target.copy()
        target[self._ix10k:self._ix20k] = np.mean(target[self._ix10k:self._ix20k])
        target[:self._ix50] = np.mean(target[:self._ix50])  # TODO: Is this good?
        fr[self._ix10k:self._ix20k] = np.mean(self.fr[self._ix10k:self._ix20k])
        fr[:self._ix50] = np.mean(fr[:self._ix50])

        # Mean squared error as loss, only up to 20 kHz
        loss_val = np.mean(np.square(self.target[:self._ix20k] - fr[:self._ix20k]))
        #loss_val = np.mean(np.square(self.target[:self._ix10k] - fr[:self._ix10k]))

        # Sum penalties from all filters to MSE
        for filt in self.filters:
            loss_val += filt.sharpness_penalty

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
        filter_params = np.concatenate(filter_params).flatten().tolist()  # Flatten params list
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

    def optimize(self):
        """Optimizes filter parameters"""
        params = fmin_slsqp(
            self._optimizer_loss,
            self._init_optimizer_params(),
            iter=1000,
            bounds=self._init_optimizer_bounds(),
            iprint=1,
            full_output=False)
        self._parse_optimizer_params(params)
