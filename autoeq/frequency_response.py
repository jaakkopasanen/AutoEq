# -*- coding: utf-8 -*_

import os
from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
from pathlib import Path
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.signal import savgol_filter, find_peaks, minimum_phase, firwin2
from scipy.stats import linregress
from scipy.fftpack import next_fast_len
import numpy as np
import urllib
from time import time
from PIL import Image
import warnings
from autoeq.constants import DEFAULT_F_MIN, DEFAULT_F_MAX, DEFAULT_STEP, DEFAULT_MAX_GAIN, DEFAULT_TREBLE_F_LOWER, \
    DEFAULT_TREBLE_F_UPPER, DEFAULT_TREBLE_GAIN_K, DEFAULT_SMOOTHING_WINDOW_SIZE, \
    DEFAULT_TREBLE_SMOOTHING_F_LOWER, DEFAULT_TREBLE_SMOOTHING_F_UPPER, \
    DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE, DEFAULT_TILT, DEFAULT_FS, \
    DEFAULT_F_RES, DEFAULT_BASS_BOOST_GAIN, DEFAULT_BASS_BOOST_FC, \
    DEFAULT_BASS_BOOST_Q, DEFAULT_GRAPHIC_EQ_STEP, HARMAN_INEAR_PREFENCE_FREQUENCIES, \
    HARMAN_OVEREAR_PREFERENCE_FREQUENCIES, PREAMP_HEADROOM, DEFAULT_MAX_SLOPE, \
    DEFAULT_BIQUAD_OPTIMIZATION_F_STEP, DEFAULT_TREBLE_BOOST_GAIN, DEFAULT_TREBLE_BOOST_FC, DEFAULT_TREBLE_BOOST_Q, \
    DEFAULT_PREAMP, DEFAULT_SOUND_SIGNATURE_SMOOTHING_WINDOW_SIZE
from autoeq.csv import parse_csv, create_csv
from autoeq.peq import PEQ, LowShelf, HighShelf, Peaking
from autoeq.utils import generate_frequencies, log_tilt, smoothing_window_size, log_f_sigmoid, log_log_gradient

warnings.filterwarnings("ignore", message="Values in x were outside bounds during a minimize step, clipping to bounds")


class FrequencyResponse:
    _cols = [
        'frequency', 'raw', 'smoothed', 'error', 'error_smoothed', 'equalization', 'parametric_eq', 'fixed_band_eq',
        'equalized_raw', 'equalized_smoothed', 'target']

    def __init__(self, name=None, frequency=None, raw=None, error=None, smoothed=None, error_smoothed=None,
                 equalization=None, parametric_eq=None, fixed_band_eq=None, equalized_raw=None, equalized_smoothed=None,
                 target=None):
        if not name:
            raise TypeError('Name must not be a non-empty string.')
        self.name = name.strip()
        self.frequency = self._init_data(frequency)
        if not len(self.frequency):
            self.frequency = self.generate_frequencies()
        self._check_duplicate_frequencies()
        self.raw = self._init_data(raw)
        self.smoothed = self._init_data(smoothed)
        self.error = self._init_data(error)
        self.error_smoothed = self._init_data(error_smoothed)
        self.equalization = self._init_data(equalization)
        self.parametric_eq = self._init_data(parametric_eq)
        self.fixed_band_eq = self._init_data(fixed_band_eq)
        self.equalized_raw = self._init_data(equalized_raw)
        self.equalized_smoothed = self._init_data(equalized_smoothed)
        self.target = self._init_data(target)
        self._sort()

    def _init_data(self, data):
        """Initializes data to a clean format. If None is passed and empty array is created. Non-numbers are removed."""
        if data is None:
            data = []
        elif type(data) == float or type(data) == int:
            data = np.ones(self.frequency.shape) * data
        return np.array([None if x is None or math.isnan(x) else x for x in data])

    def _check_duplicate_frequencies(self):
        """Checks if frequency array contains duplicate values and raises an error if it does."""
        unique_frequencies = set()
        duplicate_frequencies = set()
        for f in self.frequency:
            if f in unique_frequencies:
                duplicate_frequencies.add(f)
            unique_frequencies.add(f)
        if duplicate_frequencies:
            raise ValueError(f'Duplicate frequencies found {duplicate_frequencies}. Remove duplicates manually.')

    def _sort(self):
        """Sorts all columns in place in ascending order by frequency."""
        sorted_inds = self.frequency.argsort()
        self.frequency = self.frequency[sorted_inds]
        for col in self._cols:
            if len(self.__dict__[col]):
                self.__dict__[col] = self.__dict__[col][sorted_inds]

    def copy(self, name=None):
        return self.__class__(
            name=self.name + '_copy' if name is None else name,
            **{col: self._init_data(self.__dict__[col]) for col in self._cols})

    def reset(self, raw=False, smoothed=False, error=False, error_smoothed=False, equalization=False,
              fixed_band_eq=False, parametric_eq=False, equalized_raw=False, equalized_smoothed=False, target=False):
        """Resets data."""
        args = locals()
        for key in args:
            if args[key]:
                self.__dict__[key] = self._init_data(None)

    def to_dict(self):
        return {key: [x if x is not None else 'NaN' for x in self.__dict__[key]] for key in self._cols if len(self.__dict__[key])}

    @classmethod
    def read_csv(cls, file_path):
        """Reads data from CSV file and constructs class instance."""
        name = '.'.join(Path(file_path).name.split('.')[:-1])
        with open(file_path, 'r', encoding='utf-8') as fh:
            csv_str = fh.read().strip()
        return cls(name=name, **parse_csv(csv_str))

    def write_csv(self, file_path):
        """Writes data to files as CSV."""
        with open(file_path, 'w') as fh:
            fh.write(create_csv(self.to_dict()) + '\n')

    def eqapo_graphic_eq(self, normalize=True, preamp=DEFAULT_PREAMP, f_step=DEFAULT_GRAPHIC_EQ_STEP):
        """Generates EqualizerAPO GraphicEQ string from equalization curve."""
        fr = self.__class__(name='hack', frequency=self.frequency, raw=self.equalization)
        n = np.ceil(np.log(20000 / 20) / np.log(f_step))
        f = 20 * f_step ** np.arange(n)
        f = np.sort(np.unique(f.astype('int')))
        fr.interpolate(f=f)
        if normalize:
            fr.raw -= np.max(fr.raw) + PREAMP_HEADROOM
        if preamp:
            fr.raw += preamp
        if fr.raw[0] > 0.0:
            # Prevent bass boost below lowest frequency
            fr.raw[0] = 0.0
        s = '; '.join(['{f} {a:.1f}'.format(f=f, a=a) for f, a in zip(fr.frequency, fr.raw)])
        s = 'GraphicEQ: ' + s
        return s

    def write_eqapo_graphic_eq(self, file_path, normalize=True, preamp=DEFAULT_PREAMP):
        """Writes equalization graph to a file as Equalizer APO config."""
        file_path = os.path.abspath(file_path)
        s = self.eqapo_graphic_eq(normalize=normalize, preamp=preamp)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(s)
        return s

    def _optimize_peq_filters(self, configs, fs, max_time=None, preamp=DEFAULT_PREAMP):
        """Creates optimal set of parametric eq filters to match the equalization data"""
        if type(configs) != list:
            configs = [configs]
        peqs = []
        fr = self.__class__(name='optimizer', frequency=self.frequency, equalization=self.equalization)
        if preamp:
            fr.equalization += preamp
        fr.interpolate(f_step=DEFAULT_BIQUAD_OPTIMIZATION_F_STEP)
        start_time = time()
        for config in configs:
            if 'optimizer' in config and max_time is not None:
                config['optimizer']['max_time'] = max_time
            peq = PEQ.from_dict(config, fr.frequency, fs, target=fr.equalization)
            peq.optimize()
            fr.equalization -= peq.fr
            peqs.append(peq)
            if max_time is not None:
                max_time = max_time - (time() - start_time)
        return peqs

    def optimize_parametric_eq(self, configs, fs, max_time=None, preamp=DEFAULT_PREAMP):
        """Creates optimal set of parametric eq filters to match the equalization data"""
        peqs = self._optimize_peq_filters(configs, fs, max_time=max_time, preamp=preamp)
        fr = FrequencyResponse(
            name='PEQ', frequency=self.generate_frequencies(f_step=DEFAULT_BIQUAD_OPTIMIZATION_F_STEP),
            raw=np.sum(np.vstack([peq.fr for peq in peqs]), axis=0))
        fr.interpolate(f=self.frequency)
        self.parametric_eq = fr.raw
        return peqs

    def optimize_fixed_band_eq(self, configs, fs, max_time=None, preamp=DEFAULT_PREAMP, gain_range=None):
        """Creates optimal set of fixed eq filters to match the equalization data"""
        if type(configs) != list:
            configs = [configs]
        if gain_range is not None:
            fc_fr = self.copy()
            fcs = np.array([[filt['fc'] for filt in config['filters']] for config in configs]).flatten()
            fc_fr.interpolate(f=fcs)
            for config in configs:
                for filt in config['filters']:
                    target = fc_fr.equalization[np.argmin(np.abs(fc_fr.frequency - filt['fc']))]
                    filt['min_gain'] = target - gain_range
                    filt['max_gain'] = target + gain_range
        peqs = self._optimize_peq_filters(configs, fs, max_time=max_time, preamp=preamp)
        fr = FrequencyResponse(
            name='PEQ', frequency=self.generate_frequencies(f_step=DEFAULT_BIQUAD_OPTIMIZATION_F_STEP),
            raw=np.sum(np.vstack([peq.fr for peq in peqs]), axis=0))
        fr.interpolate(f=self.frequency)
        self.fixed_band_eq = fr.raw
        return peqs

    def write_eqapo_parametric_eq(self, file_path, peqs):
        """Writes EqualizerAPO Parametric eq settings to a file."""
        file_path = os.path.abspath(file_path)
        f = self.generate_frequencies(f_step=DEFAULT_BIQUAD_OPTIMIZATION_F_STEP)
        compound = PEQ(f, peqs[0].fs, [])
        for peq in peqs:
            for filt in peq.filters:
                compound.add_filter(filt)

        types = {Peaking.__name__: 'PK', LowShelf.__name__: 'LSC', HighShelf.__name__: 'HSC'}

        with open(file_path, 'w', encoding='utf-8') as f:
            s = f'Preamp: {-compound.max_gain:.1f} dB\n'
            for i, filt in enumerate(compound.filters):
                s += f'Filter {i + 1}: ON {types[filt.__class__.__name__]} Fc {filt.fc:.0f} Hz Gain {filt.gain:.1f} dB Q {filt.q:.2f}\n'
            f.write(s)

    def minimum_phase_impulse_response(self, fs=DEFAULT_FS, f_res=DEFAULT_F_RES, normalize=True, preamp=DEFAULT_PREAMP):
        """Generates minimum phase impulse response

        Inspired by:
        https://sourceforge.net/p/equalizerapo/code/HEAD/tree/tags/1.2/filters/GraphicEQFilter.cpp#l45

        Args:
            fs: Sampling frequency in Hz
            f_res: Frequency resolution as sampling interval. 20 would result in sampling at 0 Hz, 20 Hz, 40 Hz, ...
            normalize: Normalize gain to -0.2 dB
            preamp: Extra pre-amplification in dB

        Returns:
            Minimum phase impulse response
        """
        # Double frequency resolution because it will be halved when converting linear phase IR to minimum phase
        f_res /= 2
        # Interpolate to even sample interval
        fr = self.__class__(name='fr_data', frequency=self.frequency.copy(), raw=self.equalization.copy())
        f_min = np.max([fr.frequency[0], f_res])  # Save gain at lowest available frequency
        interpolator = InterpolatedUnivariateSpline(np.log10(fr.frequency), fr.raw, k=1)
        gain_f_min = interpolator(np.log10(f_min))
        # Filter length, optimized for FFT speed
        n = round(fs // 2 / f_res)
        n = next_fast_len(n)
        f = np.linspace(0.0, fs // 2, n)
        fr.interpolate(f, pol_order=1)
        # Set gain for all frequencies below original minimum frequency to match gain at the original minimum frequency
        fr.raw[fr.frequency <= f_min] = gain_f_min
        if normalize:
            # Reduce by max gain to avoid clipping with 1 dB of headroom
            fr.raw -= np.max(fr.raw)
            fr.raw -= PREAMP_HEADROOM
        if preamp:
            fr.raw += preamp
        fr.raw *= 2  # Minimum phase transformation by scipy's homomorphic method halves dB gain
        fr.raw = 10 ** (fr.raw / 20)  # Convert amplitude to linear scale
        fr.raw[-1] = 0.0  # Zero gain at Nyquist frequency
        ir = firwin2(len(fr.frequency) * 2, fr.frequency, fr.raw, fs=fs)  # Calculate linear phase FIR filter
        ir = minimum_phase(ir, n_fft=len(ir))  # Convert FIR filter to minimum phase
        return ir

    def linear_phase_impulse_response(self, fs=DEFAULT_FS, f_res=DEFAULT_F_RES, normalize=True, preamp=DEFAULT_PREAMP):
        """Generates impulse response implementation of equalization filter."""
        # Interpolate to even sample interval
        fr = self.__class__(name='fr_data', frequency=self.frequency, raw=self.equalization)
        f_min = np.max([fr.frequency[0], f_res])  # Save gain at lowest available frequency
        interpolator = InterpolatedUnivariateSpline(np.log10(fr.frequency), fr.raw, k=1)
        gain_f_min = interpolator(np.log10(f_min))
        fr.interpolate(np.arange(0.0, fs // 2, f_res), pol_order=1)
        # Set gain for all frequencies below original minimum frequency to match gain at the original minimum frequency
        fr.raw[fr.frequency <= f_min] = gain_f_min
        if normalize:
            # Reduce by max gain to avoid clipping with 1 dB of headroom
            fr.raw -= np.max(fr.raw)
            fr.raw -= PREAMP_HEADROOM
        if preamp:
            fr.raw += preamp
        fr.raw = 10 ** (fr.raw / 20)  # Convert amplitude to linear scale
        fr.frequency = np.append(fr.frequency, fs // 2)  # Nyquist frequency
        fr.raw = np.append(fr.raw, 0.0)  # Zero gain at Nyquist frequency
        return firwin2(len(fr.frequency) * 2, fr.frequency, fr.raw, fs=fs)

    def write_readme(self, file_path, parametric_peqs=None, fixed_band_peq=None):
        """Writes README.md with picture and Equalizer APO settings."""
        model = self.name

        # Write model
        s = '# {}\n'.format(model)
        s += 'See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.\n\n'

        # Add parametric EQ settings
        if parametric_peqs is not None:
            s += '### Parametric EQs\n'
            f = self.generate_frequencies(f_step=DEFAULT_BIQUAD_OPTIMIZATION_F_STEP)
            if len(parametric_peqs) > 1:
                compound = PEQ(f, parametric_peqs[0].fs)
                n = 0
                filter_ranges = ''
                preamps = ''
                for i, peq in enumerate(parametric_peqs):
                    peq = deepcopy(peq)
                    peq.sort_filters()
                    for filt in peq.filters:
                        compound.add_filter(filt)
                    filter_ranges += f'1-{len(peq.filters) + n}'
                    preamps += f'{-compound.max_gain - 0.1:.1f} dB'
                    if i < len(parametric_peqs) - 2:
                        filter_ranges += ', '
                        preamps += ', '
                    elif i == len(parametric_peqs) - 2:
                        filter_ranges += ' or '
                        preamps += ' or '
                    n += len(peq.filters)
                s += f'You can use filters {filter_ranges}. Apply preamp of {preamps}, respectively.\n\n'
            else:
                compound = PEQ(f, parametric_peqs[0].fs, [])
                for peq in parametric_peqs:
                    peq = deepcopy(peq)
                    peq.sort_filters()
                    for filt in peq.filters:
                        compound.add_filter(filt)
                s += f'Apply preamp of -{compound.max_gain + 0.1:.1f} dB when using parametric equalizer.\n\n'
            s += compound.markdown_table() + '\n\n'

        # Add fixed band eq
        if fixed_band_peq is not None:
            s += f'### Fixed Band EQs\nWhen using fixed band (also called graphic) equalizer, apply preamp of ' \
                 f'**-{fixed_band_peq.max_gain + 0.1:.1f} dB** (if available) and set gains manually with these ' \
                 f'parameters.\n\n{fixed_band_peq.markdown_table()}\n\n'

        # Write image link
        file_path = Path(file_path)
        img_path = os.path.join(file_path.parent, model + '.png')
        if os.path.isfile(img_path):
            img_url = f'./{os.path.split(img_path)[1]}'
            img_url = urllib.parse.quote(img_url, safe="%/:=&?~#+!$,;'@()*[]")
            s += f'### Graphs\n![]({img_url})\n'

        # Write file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(s)

    @staticmethod
    def generate_frequencies(f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, f_step=DEFAULT_STEP):
        """Moved to autoeq.utils but retaining method to avoid breaking changes."""
        return generate_frequencies(f_min, f_max, f_step)

    def interpolate(self, f=None, f_step=DEFAULT_STEP, pol_order=1, f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX):
        """Interpolates missing values from previous and next value. Resets all but raw data."""
        # Remove None values
        i = 0
        while i < len(self.raw):
            if self.raw[i] is None:
                self.raw = np.delete(self.raw, i)
                self.frequency = np.delete(self.frequency, i)
            else:
                i += 1
        keys = 'raw smoothed error error_smoothed equalization equalized_raw equalized_smoothed target'.split()
        interpolators = dict()
        log_f = np.log10(self.frequency)
        for key in keys:
            if len(self.__dict__[key]):
                interpolators[key] = InterpolatedUnivariateSpline(log_f, self.__dict__[key], k=pol_order)
        if f is None:
            self.frequency = self.generate_frequencies(f_min=f_min, f_max=f_max, f_step=f_step)
        else:
            self.frequency = np.array(f)
        # Prevent log10 from exploding by replacing zero frequency with small value
        zero_freq_fix = False
        if self.frequency[0] == 0:
            self.frequency[0] = 0.001
            zero_freq_fix = True
        log_f = np.log10(self.frequency)
        for key in keys:
            if len(self.__dict__[key]) and key in interpolators:
                self.__dict__[key] = interpolators[key](log_f)
        if zero_freq_fix:
            # Restore zero frequency
            self.frequency[0] = 0
        # Everything but the interpolated data is affected by interpolating, reset them
        self.reset(fixed_band_eq=True, parametric_eq=True)

    def center(self, frequency=1000):
        """Removed bias from frequency response.

        Args:
            frequency: Frequency which is set to 0 dB. If this is a list with two values then an average between the two
                       frequencies is set to 0 dB.

        Returns:
            Gain shifted
        """
        equal_energy_fr = self.__class__(name='equal_energy', frequency=self.frequency.copy(), raw=self.raw.copy())
        equal_energy_fr.interpolate()
        interpolator = InterpolatedUnivariateSpline(np.log10(equal_energy_fr.frequency), equal_energy_fr.raw, k=1)
        if type(frequency) in [list, np.ndarray] and len(frequency) > 1:
            # Use the average of the gain values between the given frequencies as the difference to be subtracted
            diff = np.mean(equal_energy_fr.raw[np.logical_and(
                equal_energy_fr.frequency >= frequency[0],
                equal_energy_fr.frequency <= frequency[1]
            )])
        else:
            if type(frequency) in [list, np.ndarray]:
                # List or array with only one element
                frequency = frequency[0]
            # Use the gain value at the given frequency as the difference to be subtracted
            diff = interpolator(np.log10(frequency))

        self.raw -= diff
        if len(self.smoothed):
            self.smoothed -= diff
        if len(self.error):
            self.error += diff
        if len(self.error_smoothed):
            self.error_smoothed += diff

        # Everything but raw, smoothed, errors and target is affected by centering, reset them
        self.reset(
            equalization=True, fixed_band_eq=True, parametric_eq=True, equalized_raw=True, equalized_smoothed=True)
        return -diff

    def create_target(
            self, bass_boost_gain=DEFAULT_BASS_BOOST_GAIN, bass_boost_fc=DEFAULT_BASS_BOOST_FC,
            bass_boost_q=DEFAULT_BASS_BOOST_Q, treble_boost_gain=DEFAULT_TREBLE_BOOST_GAIN,
            treble_boost_fc=DEFAULT_TREBLE_BOOST_FC, treble_boost_q=DEFAULT_TREBLE_BOOST_Q,
            tilt=DEFAULT_TILT, fs=DEFAULT_FS):
        """Creates target curve with bass boost as described by harman target response.

        Args:
            bass_boost_gain: Bass boost amount in dB
            bass_boost_fc: Bass boost low shelf center frequency
            bass_boost_q: Bass boost low shelf quality
            treble_boost_gain: Treble boost amount in dB
            treble_boost_fc: Treble boost high shelf center frequency
            treble_boost_q: Treble boost high shelf quality
            tilt: Frequency response tilt (slope) in dB per octave, positive values make it brighter
            fs: Sampling frequency

        Returns:
            Target for equalization
        """
        bass_boost = LowShelf(self.frequency, fs, fc=bass_boost_fc, q=bass_boost_q, gain=bass_boost_gain)
        treble_boost = HighShelf(
            self.frequency, fs, fc=treble_boost_fc, q=treble_boost_q, gain=treble_boost_gain)
        if tilt is not None:
            tilt = log_tilt(self.frequency, tilt)
        else:
            tilt = np.zeros(len(self.frequency))
        return bass_boost.fr + treble_boost.fr + tilt

    def compensate(
            self, target, bass_boost_gain=DEFAULT_BASS_BOOST_GAIN, bass_boost_fc=DEFAULT_BASS_BOOST_FC,
            bass_boost_q=DEFAULT_BASS_BOOST_Q, treble_boost_gain=DEFAULT_TREBLE_BOOST_GAIN,
            treble_boost_fc=DEFAULT_TREBLE_BOOST_FC, treble_boost_q=DEFAULT_TREBLE_BOOST_Q,
            tilt=DEFAULT_TILT, fs=DEFAULT_FS,
            sound_signature=None, sound_signature_smoothing_window_size=DEFAULT_SOUND_SIGNATURE_SMOOTHING_WINDOW_SIZE,
            min_mean_error=False):
        """Sets target and error curves."""
        target = target.copy()
        target.interpolate()
        target.center()

        self.target = target.raw + self.create_target(
            bass_boost_gain=bass_boost_gain, bass_boost_fc=bass_boost_fc, bass_boost_q=bass_boost_q,
            treble_boost_gain=treble_boost_gain, treble_boost_fc=treble_boost_fc, treble_boost_q=treble_boost_q,
            tilt=tilt, fs=fs)

        if sound_signature is not None:
            # Sound signature given, add it to target curve
            if not np.all(sound_signature.frequency == self.frequency):
                # Interpolate sound signature to match self on the frequency axis
                sound_signature.interpolate(self.frequency)
            if sound_signature_smoothing_window_size:
                sound_signature.smoothen(
                    window_size=sound_signature_smoothing_window_size,
                    treble_window_size=sound_signature_smoothing_window_size)
                self.target += sound_signature.smoothed
            else:
                self.target += sound_signature.raw

        self.error = self.raw - self.target
        if min_mean_error:
            # Shift error by it's mean in range 100 Hz to 10 kHz
            delta = np.mean(self.error[np.logical_and(self.frequency >= 100, self.frequency <= 10000)])
            self.error -= delta
            self.target += delta

        # Smoothed error and equalization results are affected by error calculation, reset them
        self.reset(
            error_smoothed=True, equalization=True, parametric_eq=True, fixed_band_eq=True, equalized_raw=True,
            equalized_smoothed=True)

    def _smoothen(
            self, data, window_size=DEFAULT_SMOOTHING_WINDOW_SIZE,
            treble_window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE, treble_f_lower=DEFAULT_TREBLE_SMOOTHING_F_LOWER,
            treble_f_upper=DEFAULT_TREBLE_SMOOTHING_F_UPPER):
        """Smooths data.

        Args:
            window_size: Filter window size in octaves.
            treble_window_size: Filter window size for high frequencies.
            treble_f_lower: Lower boundary of transition frequency region. In the transition region normal filter is
                            switched to treble filter with sigmoid weighting function.
            treble_f_upper: Upper boundary of transition frequency reqion. In the transition region normal filter is
                            switched to treble filter with sigmoid weighting function.
        """
        if None in self.frequency or None in data:
            # Must not contain None values
            raise ValueError('None values present, cannot smoothen!')
        # Savgol filter uses array indexing which is not future proof, ignoring the warning and trusting that this
        # will be fixed in the future release
        y_normal = savgol_filter(data, smoothing_window_size(self.frequency, window_size), 2)
        y_treble = savgol_filter(data, smoothing_window_size(self.frequency, treble_window_size), 2)
        # Transition weighted with sigmoid
        k_treble = log_f_sigmoid(self.frequency, treble_f_lower, treble_f_upper)
        k_normal = k_treble * -1 + 1
        return y_normal * k_normal + y_treble * k_treble

    def smoothen(
            self, window_size=DEFAULT_SMOOTHING_WINDOW_SIZE,
            treble_window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
            treble_f_lower=DEFAULT_TREBLE_SMOOTHING_F_LOWER,
            treble_f_upper=DEFAULT_TREBLE_SMOOTHING_F_UPPER):
        """Smooths data.

        Args:
            window_size: Filter window size in octaves.
            treble_window_size: Filter window size for high frequencies.
            treble_f_lower: Lower boundary of transition frequency region. In the transition region normal filter is \
                        switched to treble filter with sigmoid weighting function.
            treble_f_upper: Upper boundary of transition frequency reqion. In the transition region normal filter is \
                        switched to treble filter with sigmoid weighting function.
        """
        if treble_f_upper <= treble_f_lower:
            raise ValueError('Upper transition boundary must be greater than lower boundary')
        self.smoothed = self._smoothen(
            self.raw, window_size=window_size, treble_window_size=treble_window_size,
            treble_f_lower=treble_f_lower, treble_f_upper=treble_f_upper)
        if len(self.error):
            self.error_smoothed = self._smoothen(
                self.error, window_size=window_size, treble_window_size=treble_window_size,
                treble_f_lower=treble_f_lower, treble_f_upper=treble_f_upper)
        self.reset(
            equalization=True, parametric_eq=True, fixed_band_eq=True, equalized_raw=True, equalized_smoothed=True)

    def equalize(
            self, max_gain=DEFAULT_MAX_GAIN, max_slope=DEFAULT_MAX_SLOPE, max_slope_decay=0.0,
            concha_interference=False, window_size=1 / 12, treble_window_size=2, treble_f_lower=DEFAULT_TREBLE_F_LOWER,
            treble_f_upper=DEFAULT_TREBLE_F_UPPER, treble_gain_k=DEFAULT_TREBLE_GAIN_K):
        """Creates equalization curve and equalized curve.

        Args:
            max_gain: Maximum positive gain in dB
            max_slope: Maximum slope in dB per octave
            max_slope_decay: Decay coefficient (per octave) for the limit. Value of 0.5 would reduce limit by 50% in an octave
                when traversing a single limitation zone.
            concha_interference: Do measurements include concha interference which produced a narrow dip around 9 kHz?
            window_size: Smoothing window size in octaves.
            treble_window_size: Smoothing window size in octaves in the treble region.
            treble_f_lower: Lower boundary of transition frequency region. In the transition region normal filter is \
                            switched to treble filter with sigmoid weighting function.
            treble_f_upper: Upper boundary of transition frequency reqion. In the transition region normal filter is \
                            switched to treble filter with sigmoid weighting function.
            treble_gain_k: Coefficient for treble gain, positive and negative. Useful for disabling or reducing \
                           equalization power in treble region. Defaults to 1.0 (not limited).

        Returns:

        """
        fr = FrequencyResponse(name='fr', frequency=self.frequency, raw=self.error)
        # Smoothen data heavily in the treble region to avoid problems caused by peakiness
        fr.smoothen(
            window_size=window_size, treble_window_size=treble_window_size, treble_f_lower=treble_f_lower,
            treble_f_upper=treble_f_upper)

        # Copy data
        x = np.array(fr.frequency)
        y = np.array(-fr.smoothed)  # Inverse of the smoothed error

        # Find peaks and notches
        peak_inds, peak_props = find_peaks(y, prominence=1)
        dip_inds, dip_props = find_peaks(-y, prominence=1)

        if not len(peak_inds) and not len(dip_inds):
            # No peaks or dips, it's a flat line
            # Use the inverse error as the equalization target
            self.equalization = y
            # Equalized
            self.equalized_raw = self.raw + self.equalization
            if len(self.smoothed):
                self.equalized_smoothed = self.smoothed + self.equalization
            return y, fr.smoothed.copy(), np.array([]), np.array([False] * len(y)), np.array([]), \
                np.array([False] * len(y)), np.array([]), np.array([]), len(y) - 1, np.array([False] * len(y))

        else:
            limit_free_mask = self.protection_mask(y, peak_inds, dip_inds)
            if concha_interference:
                # 8 kHz - 11.5 kHz should not be limit free zone
                limit_free_mask[np.logical_and(x >= 8000, x <= 11500)] = False

            # Find rtl start index
            rtl_start = self.find_rtl_start(y, peak_inds, dip_inds)

            # Find ltr and rtl limitations
            # limited_ltr is y but with slopes limited when traversing left to right
            # clipped_ltr is boolean mask for limited samples when traversing left to right
            # limited_rtl is found using ltr algorithm but with flipped data
            limited_ltr, clipped_ltr, regions_ltr = self.limited_ltr_slope(
                x, y, max_slope, max_slope_decay=max_slope_decay, start_index=0, peak_inds=peak_inds,
                limit_free_mask=limit_free_mask, concha_interference=concha_interference)
            limited_rtl, clipped_rtl, regions_rtl = self.limited_rtl_slope(
                x, y, max_slope, max_slope_decay=max_slope_decay, start_index=rtl_start, peak_inds=peak_inds,
                limit_free_mask=limit_free_mask, concha_interference=concha_interference)

            # ltr and rtl limited curves are combined with min function
            combined = self.__class__(
                name='limiter', frequency=x, raw=np.min(np.vstack([limited_ltr, limited_rtl]), axis=0))

            # Limit treble gain
            gain_k = log_f_sigmoid(self.frequency, treble_f_lower, treble_f_upper, a_normal=1.0, a_treble=treble_gain_k)
            combined.raw *= gain_k

            # Gain can be reduced in the treble region
            # Clip positive gain to max gain
            combined.raw = np.min(np.vstack([combined.raw, np.ones(combined.raw.shape) * max_gain]), axis=0)
            # Smoothen the curve to get rid of hard kinks
            combined.smoothen(window_size=1 / 5, treble_window_size=1 / 5)

            # Equalization curve
            self.equalization = combined.smoothed

        # Equalized
        self.equalized_raw = self.raw + self.equalization
        if len(self.smoothed):
            self.equalized_smoothed = self.smoothed + self.equalization

        return combined.smoothed.copy(), fr.smoothed.copy(), limited_ltr, clipped_ltr, limited_rtl, \
            clipped_rtl, peak_inds, dip_inds, rtl_start, limit_free_mask

    @staticmethod
    def protection_mask(y, peak_inds, dip_inds):
        """Finds zones around dips which are lower than their adjacent dips.

        Args:
            y: amplitudes
            peak_inds: Indices of peaks
            dip_inds: Indices of dips

        Returns:
            Boolean mask for limitation-free indices
        """
        if len(peak_inds) and (not len(dip_inds) or peak_inds[-1] > dip_inds[-1]):
            # Last peak is after last dip, add new dip after the last peak at the minimum
            last_dip_ind = np.argmin(y[peak_inds[-1]:]) + peak_inds[-1]
            dip_inds = np.concatenate([dip_inds, [last_dip_ind]])
            dip_levels = y[dip_inds]
        else:
            dip_inds = np.concatenate([dip_inds, [-1]])
            dip_levels = y[dip_inds]
            dip_levels[-1] = np.min(y)

        mask = np.zeros(len(y)).astype(bool)
        if len(dip_inds) < 3:
            return mask

        for i in range(1, len(dip_inds) - 1):
            dip_ind = dip_inds[i]
            target_left = dip_levels[i - 1]
            target_right = dip_levels[i + 1]
            left_ind = np.argwhere(y[:dip_ind] >= target_left)[-1, 0] + 1
            right_ind = np.argwhere(y[dip_ind:] >= target_right)[0, 0] + dip_ind - 1
            mask[left_ind:right_ind + 1] = np.ones(right_ind - left_ind + 1).astype(bool)
        return mask

    @classmethod
    def limited_rtl_slope(cls, x, y, max_slope, max_slope_decay=0.0, start_index=0, peak_inds=None, limit_free_mask=None,
                          concha_interference=False):
        """Limits right to left slope of an equalization curve.

            Args:
                x: frequencies
                y: amplitudes
                max_slope: maximum slope in dB / oct
                max_slope_decay: Max slope decay coefficient per octave
                start_index: Index where to start traversing, no limitations apply before this
                peak_inds: Peak indexes. Regions will require to touch one of these if given.
                limit_free_mask: Boolean mask for indices where limitation must not be applied
                concha_interference: Do measurements include concha interference which produced a narrow dip around 9 kHz?

            Returns:
                limited: Limited curve
                mask: Boolean mask for clipped indexes
                regions: Clipped regions, one per row, 1st column is the start index, 2nd column is the end index (exclusive)
        """
        start_index = len(x) - start_index - 1
        if peak_inds is not None:
            peak_inds = len(x) - peak_inds - 1
        if limit_free_mask is not None:
            limit_free_mask = np.flip(limit_free_mask)
        limited_rtl, clipped_rtl, regions_rtl = cls.limited_ltr_slope(
            x, np.flip(y), max_slope, max_slope_decay=max_slope_decay, start_index=start_index, peak_inds=peak_inds,
            limit_free_mask=limit_free_mask, concha_interference=concha_interference)
        limited_rtl = np.flip(limited_rtl)
        clipped_rtl = np.flip(clipped_rtl)
        regions_rtl = len(x) - regions_rtl - 1
        return limited_rtl, clipped_rtl, regions_rtl

    @classmethod
    def limited_ltr_slope(cls, x, y, max_slope, max_slope_decay=0.0, start_index=0, peak_inds=None, limit_free_mask=None,
                          concha_interference=False):
        """Limits left to right slope of a equalization curve.

        Args:
            x: frequencies
            y: amplitudes
            max_slope: maximum slope in dB / oct
            max_slope_decay: Max slope decay coefficient per octave
            start_index: Index where to start traversing, no limitations apply before this
            peak_inds: Peak indexes. Regions will require to touch one of these if given.
            limit_free_mask: Boolean mask for indices where limitation must not be applied
            concha_interference: Do measurements include concha interference which produced a narrow dip around 9 kHz?

        Returns:
            limited: Limited curve
            mask: Boolean mask for clipped indexes
            regions: Clipped regions, one per row, 1st column is the start index, 2nd column is the end index (exclusive)
        """
        if peak_inds is not None:
            peak_inds = np.array(peak_inds)

        limited = []
        clipped = []
        regions = []
        for i in range(len(x)):
            if i <= start_index:
                # No clipping before start index
                limited.append(y[i])
                clipped.append(False)
                continue

            # Calculate slope and local limit
            slope = log_log_gradient(x[i], x[i - 1], y[i], limited[-1])
            # Local limit is 25% of the limit between 8 kHz and 10 kHz
            local_limit = max_slope / 4 if 8000 <= x[i] <= 11500 and concha_interference else max_slope

            if clipped[-1]:
                # Previous sample clipped, reduce limit
                local_limit *= (1 - max_slope_decay) ** np.log2(x[i] / x[regions[-1][0]])

            if slope > local_limit and (limit_free_mask is None or not limit_free_mask[i]):
                # Slope between the two samples is greater than the local maximum slope, clip to the max
                if not clipped[-1]:
                    # Start of clipped region
                    regions.append([i])
                clipped.append(True)
                # Add value with limited change
                octaves = np.log(x[i] / x[i - 1]) / np.log(2)
                limited.append(limited[-1] + local_limit * octaves)

            else:
                # Moderate slope, no need to limit
                limited.append(y[i])

                if clipped[-1]:
                    # Previous sample clipped but this one didn't, means it's the end of clipped region
                    # Add end index to the region
                    regions[-1].append(i + 1)

                    region_start = regions[-1][0]
                    if peak_inds is not None and not np.any(np.logical_and(peak_inds >= region_start, peak_inds < i)):
                        # None of the peak indices found in the current region, discard limitations
                        limited[region_start:i] = y[region_start:i]
                        clipped[region_start:i] = [False] * (i - region_start)
                        regions.pop()
                clipped.append(False)

        if len(regions) and len(regions[-1]) == 1:
            regions[-1].append(len(x) - 1)

        return np.array(limited), np.array(clipped), np.array(regions)

    @staticmethod
    def find_rtl_start(y, peak_inds, dip_inds):
        """Finds start index for right to left equalization curve traverse.

        Args:
            y: Gain data
            peak_inds: Indices of peaks in the gain data
            dip_inds: Indices of dips in the gain data

        Returns:
            Start index
        """
        # Find starting index for the rtl pass
        if len(peak_inds) and (not len(dip_inds) or peak_inds[-1] > dip_inds[-1]):
            # Last peak is a positive peak
            if len(dip_inds):
                # Find index on the right side of the peak where the curve crosses the last dip level
                rtl_start = np.argwhere(y[peak_inds[-1]:] <= y[dip_inds[-1]])
            else:
                # There are no dips, use the minimum of the first and the last value of y
                rtl_start = np.argwhere(y[peak_inds[-1]:] <= max(y[0], y[-1]))
            if len(rtl_start):
                rtl_start = rtl_start[0, 0] + peak_inds[-1]
            else:
                rtl_start = len(y) - 1
        else:
            # Last peak is a negative peak, start there
            rtl_start = dip_inds[-1]
        return rtl_start

    @staticmethod
    def init_plot(fig=None, ax=None, f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, a_min=None, a_max=None, ):
        """Configures figure and axis ready for frequency response plots"""
        if fig is None:
            fig, ax = plt.subplots()
            fig.set_size_inches(12, 8)
            fig.set_facecolor('white')
            ax.set_facecolor('white')
        ax.set_xlabel('Frequency (Hz)')
        ax.semilogx()
        ax.set_xlim([f_min, f_max])
        ax.set_ylabel('Amplitude (dBr)')
        if a_min is not None or a_max is not None:
            ax.set_ylim([a_min, a_max])
        ax.grid(True, which='major')
        ax.grid(True, which='minor')
        ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
        ax.set_xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000])
        return fig, ax

    def plot(
            self, fig=None, ax=None, show_fig=True, close_fig=False, file_path=None,
            raw=True, error=True, smoothed=True, error_smoothed=True, equalization=True, parametric_eq=True,
            fixed_band_eq=True, equalized=True, target=True,
            raw_plot_kwargs=None, smoothed_plot_kwargs=None, error_plot_kwargs=None, error_smoothed_plot_kwargs=None,
            equalization_plot_kwargs=None, parametric_eq_plot_kwargs=None, fixed_band_eq_plot_kwargs=None,
            equalized_plot_kwargs=None, target_plot_kwargs=None):
        """Plots frequency response graph."""
        if not len(self.frequency):
            raise ValueError('\'frequency\' has no data!')
        fig, ax = self.__class__.init_plot(fig=fig, ax=ax)
        if target and len(self.target):
            ax.plot(self.frequency, self.target, **{'label': 'Target', 'linewidth': 6, 'color': '#7bc8f6', **(target_plot_kwargs if target_plot_kwargs else {})})
        if smoothed and len(self.smoothed):
            ax.plot(self.frequency, self.smoothed, **{'label': 'Raw Smoothed', 'linewidth': 6, 'color': '#dbd3cd', **(smoothed_plot_kwargs if smoothed_plot_kwargs else {})})
        if error_smoothed and len(self.error_smoothed):
            ax.plot(self.frequency, self.error_smoothed, **{'label': 'Error Smoothed', 'linewidth': 6, 'color': '#ffcfc7', **(error_smoothed_plot_kwargs if error_smoothed_plot_kwargs else {})})
        if raw and len(self.raw):
            ax.plot(self.frequency, self.raw, **{'label': 'Raw', 'linewidth': 1.5, 'color': '#251f1b', **(raw_plot_kwargs if raw_plot_kwargs else {})})
        if error and len(self.error):
            ax.plot(self.frequency, self.error, **{'label': 'Error', 'linewidth': 1.5, 'color': '#ff5b3d', **(error_plot_kwargs if error_plot_kwargs else {})})
        if equalization and len(self.equalization):
            ax.plot(self.frequency, self.equalization, **{'label': 'Equalization', 'linewidth': 6, 'color': '#ded400', **(equalization_plot_kwargs if equalization_plot_kwargs else {})})
        if parametric_eq and len(self.parametric_eq):
            ax.plot(self.frequency, self.parametric_eq, **{'label': 'Parametric Eq', 'linewidth': 1.5, 'color': '#807900', **(parametric_eq_plot_kwargs if parametric_eq_plot_kwargs else {})})
        if fixed_band_eq and len(self.fixed_band_eq):
            ax.plot(self.frequency, self.fixed_band_eq, **{'label': 'Fixed Band Eq', 'linewidth': 1.5, 'color': '#a8a000', 'linestyle': '--', **(fixed_band_eq_plot_kwargs if fixed_band_eq_plot_kwargs else {})})
        if equalized and len(self.equalized_raw):
            ax.plot(self.frequency, self.equalized_raw, **{'label': 'Equalized', 'linewidth': 1.5, 'color': '#146899', **(equalized_plot_kwargs if equalized_plot_kwargs else {})})
        ax.set_title(self.name)
        if len(ax.lines) > 0:
            ax.legend(fontsize=8)
        if file_path is not None:
            file_path = os.path.abspath(file_path)
            fig.savefig(file_path, dpi=120)
            im = Image.open(file_path)
            im = im.convert('P', palette=Image.ADAPTIVE, colors=60)
            im.save(file_path, optimize=True)
        if show_fig:
            plt.show()
        elif close_fig:
            plt.close(fig)
        return fig, ax

    def harman_overear_preference_score(self):
        """Calculates Harman preference score for over-ear and on-ear headphones.

        Returns:
            - score: Preference score
            - std: Standard deviation of error
            - slope: Slope of linear regression of error
        """
        fr = self.copy()
        fr.interpolate(HARMAN_OVEREAR_PREFERENCE_FREQUENCIES)
        sl = np.logical_and(fr.frequency >= 50, fr.frequency <= 10000)
        x = fr.frequency[sl]
        y = fr.error[sl]
        std = np.std(y, ddof=1)  # ddof=1 is required to get the exact same numbers as the Excel from Listen Inc gives
        slope, _, _, _, _ = linregress(np.log(x), y)
        score = 114.490443008238 - 12.62 * std - 15.5163857197367 * np.abs(slope)
        return score, std, slope

    def harman_inear_preference_score(self):
        """Calculates Harman preference score for in-ear headphones.

        Returns:
            - score: Preference score
            - std: Standard deviation of error
            - slope: Slope of linear regression of error
            - mean: Mean of absolute error
        """
        fr = self.copy()
        fr.interpolate(HARMAN_INEAR_PREFENCE_FREQUENCIES)
        sl = np.logical_and(fr.frequency >= 20, fr.frequency <= 10000)
        x = fr.frequency[sl]
        y = fr.error[sl]
        std = np.std(y, ddof=1)  # ddof=1 is required to get the exact same numbers as the Excel from Listen Inc gives
        slope, _, _, _, _ = linregress(np.log(x), y)
        # Mean of absolute of error centered by 500 Hz
        delta = fr.error[np.where(fr.frequency == 500.0)[0][0]]
        y = fr.error[np.logical_and(fr.frequency >= 40, fr.frequency <= 10000)] - delta
        mean = np.mean(np.abs(y))
        # Final score
        score = 100.0795 - 8.5 * std - 6.796 * np.abs(slope) - 3.475 * mean
        return score, std, slope, mean

    def process(
            self, target=None, min_mean_error=False,
            bass_boost_gain=DEFAULT_BASS_BOOST_GAIN, bass_boost_fc=DEFAULT_BASS_BOOST_FC,
            bass_boost_q=DEFAULT_BASS_BOOST_Q, treble_boost_gain=DEFAULT_TREBLE_BOOST_GAIN,
            treble_boost_fc=DEFAULT_TREBLE_BOOST_FC, treble_boost_q=DEFAULT_TREBLE_BOOST_Q, tilt=DEFAULT_TILT,
            fs=DEFAULT_FS, sound_signature=None,
            sound_signature_smoothing_window_size=DEFAULT_SOUND_SIGNATURE_SMOOTHING_WINDOW_SIZE,
            max_gain=DEFAULT_MAX_GAIN, max_slope=DEFAULT_MAX_SLOPE, concha_interference=False,
            window_size=DEFAULT_SMOOTHING_WINDOW_SIZE, treble_window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
            treble_f_lower=DEFAULT_TREBLE_F_LOWER, treble_f_upper=DEFAULT_TREBLE_F_UPPER,
            treble_gain_k=DEFAULT_TREBLE_GAIN_K):
        """Runs processing pipeline with interpolation, centering, error calculation and equalization.

        Args:
            target: Target FrequencyResponse
            min_mean_error: Minimize mean error. Normally all curves cross at 1 kHz but this makes it possible to shift
                            error curve so that mean between 100 Hz and 10 kHz is at minimum. Target curve is shifted
                            accordingly. Useful for avoiding large bias caused by a narrow notch or peak at 1 kHz.
            bass_boost_gain: Bass boost amount in dB.
            bass_boost_fc: Bass boost low shelf center frequency.
            bass_boost_q: Bass boost low shelf quality.
            treble_boost_gain: Treble boost amount in dB.
            treble_boost_fc: Treble boost high shelf center frequency.
            treble_boost_q: Treble boost high shelf quality.
            fs: Sampling frequency
            tilt: Target frequency response tilt in db / octave
            sound_signature: Sound signature as FrequencyResponse instance. Raw data will be used.
            sound_signature_smoothing_window_size: Smoothing window size in octaves for sound signature
            max_gain: Maximum positive gain in dB
            max_slope: Maximum slope steepness for equalizer frequency response in db/oct.
            concha_interference: Do measurements include concha interference which produced a narrow dip around 9 kHz?
            window_size: Smoothing window size in octaves.
            treble_window_size: Smoothing window size in octaves in the treble region.
            treble_f_lower: Lower boundary of transition frequency region. In the transition region normal filter is
                            switched to treble filter with sigmoid weighting function.
            treble_f_upper: Upper boundary of transition frequency region. In the transition region normal filter is
                            switched to treble filter with sigmoid weighting function.
            treble_gain_k: Coefficient for treble gain, positive and negative. Useful for disabling or reducing
                           equalization power in treble region. Defaults to 1.0 (not limited).
        """
        self.interpolate()
        self.center()
        self.compensate(
            target, bass_boost_gain=bass_boost_gain, bass_boost_fc=bass_boost_fc, bass_boost_q=bass_boost_q,
            treble_boost_gain=treble_boost_gain, treble_boost_fc=treble_boost_fc, treble_boost_q=treble_boost_q,
            tilt=tilt, fs=fs, sound_signature=sound_signature,
            sound_signature_smoothing_window_size=sound_signature_smoothing_window_size,
            min_mean_error=min_mean_error
        )
        self.smoothen(
            window_size=window_size,
            treble_window_size=treble_window_size, treble_f_lower=treble_f_lower, treble_f_upper=treble_f_upper
        )
        self.equalize(
            max_slope=max_slope, max_gain=max_gain, concha_interference=concha_interference,
            treble_f_lower=treble_f_lower, treble_f_upper=treble_f_upper, treble_gain_k=treble_gain_k)
