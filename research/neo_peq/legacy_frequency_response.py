# -*- coding: utf-8 -*_

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import pandas as pd
from io import StringIO
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.signal import savgol_filter, find_peaks, minimum_phase, firwin2
from scipy.special import expit
from scipy.stats import linregress
from scipy.fftpack import next_fast_len
import numpy as np
import urllib
from time import time
from tabulate import tabulate
from PIL import Image
import re
import warnings
import biquad
from constants import DEFAULT_F_MIN, DEFAULT_F_MAX, DEFAULT_STEP, DEFAULT_MAX_GAIN, DEFAULT_TREBLE_F_LOWER, \
    DEFAULT_TREBLE_F_UPPER, DEFAULT_TREBLE_GAIN_K, DEFAULT_SMOOTHING_WINDOW_SIZE, \
    DEFAULT_SMOOTHING_ITERATIONS, DEFAULT_TREBLE_SMOOTHING_F_LOWER, DEFAULT_TREBLE_SMOOTHING_F_UPPER, \
    DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE, DEFAULT_TREBLE_SMOOTHING_ITERATIONS, DEFAULT_TILT, DEFAULT_FS, \
    DEFAULT_F_RES, DEFAULT_BASS_BOOST_GAIN, DEFAULT_BASS_BOOST_FC, \
    DEFAULT_BASS_BOOST_Q, DEFAULT_GRAPHIC_EQ_STEP, HARMAN_INEAR_PREFENCE_FREQUENCIES, \
    HARMAN_ONEAR_PREFERENCE_FREQUENCIES, PREAMP_HEADROOM, DEFAULT_MAX_SLOPE

DEFAULT_FBEQ_FILTER_MAX_GAIN = 12
DEFAULT_PEQ_FILTER_MAX_GAIN = 20

warnings.filterwarnings("ignore", message="Values in x were outside bounds during a minimize step, clipping to bounds")


class LegacyFrequencyResponse:
    def __init__(self,
                 name=None,
                 frequency=None,
                 raw=None,
                 error=None,
                 smoothed=None,
                 error_smoothed=None,
                 equalization=None,
                 parametric_eq=None,
                 fixed_band_eq=None,
                 equalized_raw=None,
                 equalized_smoothed=None,
                 target=None):
        if not name:
            raise TypeError('Name must not be a non-empty string.')
        self.name = name.strip()

        self.frequency = self._init_data(frequency)
        if not len(self.frequency):
            self.frequency = self.generate_frequencies()

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

    def copy(self, name=None):
        return self.__class__(
            name=self.name + '_copy' if name is None else name,
            frequency=self._init_data(self.frequency),
            raw=self._init_data(self.raw),
            error=self._init_data(self.error),
            smoothed=self._init_data(self.smoothed),
            error_smoothed=self._init_data(self.error_smoothed),
            equalization=self._init_data(self.equalization),
            parametric_eq=self._init_data(self.parametric_eq),
            fixed_band_eq=self._init_data(self.fixed_band_eq),
            equalized_raw=self._init_data(self.equalized_raw),
            equalized_smoothed=self._init_data(self.equalized_smoothed),
            target=self._init_data(self.target)
        )

    def _init_data(self, data):
        """Initializes data to a clean format. If None is passed and empty array is created. Non-numbers are removed."""
        if data is None:
            # None means empty array
            data = []
        elif type(data) == float or type(data) == int:
            # Scalar means all values are that, same shape as frequency
            data = np.ones(self.frequency.shape) * data
        # Replace nans with Nones
        data = [None if x is None or math.isnan(x) else x for x in data]
        # Wrap in Numpy array
        data = np.array(data)
        return data

    def _sort(self):
        sorted_inds = self.frequency.argsort()
        self.frequency = self.frequency[sorted_inds]
        for i in range(1, len(self.frequency)):
            if self.frequency[i] == self.frequency[i-1]:
                raise ValueError('Duplicate values found at frequency {}. Remove duplicates manually.'.format(
                    self.frequency[i])
                )
        if len(self.raw):
            self.raw = self.raw[sorted_inds]
        if len(self.error):
            self.error = self.error[sorted_inds]
        if len(self.smoothed):
            self.smoothed = self.smoothed[sorted_inds]
        if len(self.error_smoothed):
            self.error_smoothed = self.error_smoothed[sorted_inds]
        if len(self.equalization):
            self.equalization = self.equalization[sorted_inds]
        if len(self.parametric_eq):
            self.parametric_eq = self.parametric_eq[sorted_inds]
        if len(self.fixed_band_eq):
            self.fixed_band_eq = self.fixed_band_eq[sorted_inds]
        if len(self.equalized_raw):
            self.equalized_raw = self.equalized_raw[sorted_inds]
        if len(self.equalized_smoothed):
            self.equalized_smoothed = self.equalized_smoothed[sorted_inds]
        if len(self.target):
            self.target = self.target[sorted_inds]

    def reset(self,
              raw=False,
              smoothed=True,
              error=True,
              error_smoothed=True,
              equalization=True,
              fixed_band_eq=True,
              parametric_eq=True,
              equalized_raw=True,
              equalized_smoothed=True,
              target=True):
        """Resets data."""
        if raw:
            self.raw = self._init_data(None)
        if smoothed:
            self.smoothed = self._init_data(None)
        if error:
            self.error = self._init_data(None)
        if error_smoothed:
            self.error_smoothed = self._init_data(None)
        if equalization:
            self.equalization = self._init_data(None)
        if parametric_eq:
            self.parametric_eq = self._init_data(None)
        if fixed_band_eq:
            self.fixed_band_eq = self._init_data(None)
        if equalized_raw:
            self.equalized_raw = self._init_data(None)
        if equalized_smoothed:
            self.equalized_smoothed = self._init_data(None)
        if target:
            self.target = self._init_data(None)

    @classmethod
    def read_from_csv(cls, file_path):
        """Reads data from CSV file and constructs class instance."""
        name = '.'.join(os.path.split(file_path)[1].split('.')[:-1])

        # Read file
        f = open(file_path, 'r', encoding='utf-8')
        s = f.read()

        # Regex for AutoEq style CSV
        header_pattern = r'frequency(,(raw|smoothed|error|error_smoothed|equalization|parametric_eq|fixed_band_eq|equalized_raw|equalized_smoothed|target))+'
        float_pattern = r'-?\d+\.?\d+'
        data_2_pattern = r'{fl}[ ,;:\t]+{fl}?'.format(fl=float_pattern)
        data_n_pattern = r'{fl}([ ,;:\t]+{fl})+?'.format(fl=float_pattern)
        autoeq_pattern = r'^{header}(\n{data})+\n*$'.format(header=header_pattern, data=data_n_pattern)

        if re.match(autoeq_pattern, s):
            # Known AutoEq CSV format
            df = pd.read_csv(StringIO(s), sep=',', header=0)
            frequency = list(df['frequency'])
            raw = list(df['raw']) if 'raw' in df else None
            smoothed = list(df['smoothed']) if 'smoothed' in df else None
            error = list(df['error']) if 'error' in df else None
            error_smoothed = list(df['error_smoothed']) if 'error_smoothed' in df else None
            equalization = list(df['equalization']) if 'equalization' in df else None
            parametric_eq = list(df['parametric_eq']) if 'parametric_eq' in df else None
            fixed_band_eq = list(df['fixed_band_eq']) if 'fixed_band_eq' in df else None
            equalized_raw = list(df['equalized_raw']) if 'equalized_raw' in df else None
            equalized_smoothed = list(df['equalized_smoothed']) if 'equalized_smoothed' in df else None
            target = list(df['target']) if 'target' in df else None
            return cls(
                name=name,
                frequency=frequency,
                raw=raw,
                smoothed=smoothed,
                error=error,
                error_smoothed=error_smoothed,
                equalization=equalization,
                parametric_eq=parametric_eq,
                fixed_band_eq=fixed_band_eq,
                equalized_raw=equalized_raw,
                equalized_smoothed=equalized_smoothed,
                target=target
            )
        else:
            # Unknown format, try to guess
            lines = s.split('\n')
            frequency = []
            raw = []
            for line in lines:
                if re.match(data_2_pattern, line):  # float separator float
                    floats = re.findall(float_pattern, line)
                    frequency.append(float(floats[0]))  # Assume first to be frequency
                    raw.append(float(floats[1]))  # Assume second to be raw
                # Discard all lines which don't match data pattern
            return cls(name=name, frequency=frequency, raw=raw)

    def to_dict(self):
        d = dict()
        if len(self.frequency):
            d['frequency'] = self.frequency.tolist()
        if len(self.raw):
            d['raw'] = [x if x is not None else 'NaN' for x in self.raw]
        if len(self.error):
            d['error'] = [x if x is not None else 'NaN' for x in self.error]
        if len(self.smoothed):
            d['smoothed'] = [x if x is not None else 'NaN' for x in self.smoothed]
        if len(self.error_smoothed):
            d['error_smoothed'] = [x if x is not None else 'NaN' for x in self.error_smoothed]
        if len(self.equalization):
            d['equalization'] = [x if x is not None else 'NaN' for x in self.equalization]
        if len(self.parametric_eq):
            d['parametric_eq'] = [x if x is not None else 'NaN' for x in self.parametric_eq]
        if len(self.fixed_band_eq):
            d['fixed_band_eq'] = [x if x is not None else 'NaN' for x in self.fixed_band_eq]
        if len(self.equalized_raw):
            d['equalized_raw'] = [x if x is not None else 'NaN' for x in self.equalized_raw]
        if len(self.equalized_smoothed):
            d['equalized_smoothed'] = [x if x is not None else 'NaN' for x in self.equalized_smoothed]
        if len(self.target):
            d['target'] = [x if x is not None else 'NaN' for x in self.target]
        return d

    def write_to_csv(self, file_path=None):
        """Writes data to files as CSV."""
        file_path = os.path.abspath(file_path)
        df = pd.DataFrame(self.to_dict())
        df.to_csv(file_path, header=True, index=False, float_format='%.2f')

    def eqapo_graphic_eq(self, normalize=True, f_step=DEFAULT_GRAPHIC_EQ_STEP):
        """Generates EqualizerAPO GraphicEQ string from equalization curve."""
        fr = self.__class__(name='hack', frequency=self.frequency, raw=self.equalization)
        n = np.ceil(np.log(20000 / 20) / np.log(f_step))
        f = 20 * f_step**np.arange(n)
        f = np.sort(np.unique(f.astype('int')))
        fr.interpolate(f=f)
        if normalize:
            fr.raw -= np.max(fr.raw) + PREAMP_HEADROOM
            if fr.raw[0] > 0.0:
                # Prevent bass boost below lowest frequency
                fr.raw[0] = 0.0

        s = '; '.join(['{f} {a:.1f}'.format(f=f, a=a) for f, a in zip(fr.frequency, fr.raw)])
        s = 'GraphicEQ: ' + s
        return s

    def write_eqapo_graphic_eq(self, file_path, normalize=True):
        """Writes equalization graph to a file as Equalizer APO config."""
        file_path = os.path.abspath(file_path)
        s = self.eqapo_graphic_eq(normalize=normalize)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(s)
        return s

    @classmethod
    def optimize_biquad_filters(cls, frequency, target, max_time=5, max_filters=None, fs=DEFAULT_FS, fc=None, q=None):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        import tensorflow.compat.v1 as tf
        tf.get_logger().setLevel('ERROR')
        tf.disable_v2_behavior()

        if fc is not None or q is not None:
            if fc is None:
                raise TypeError('"fc" must be given if "q" is given.')
            if q is None:
                raise TypeError('"q" must be give nif "fc" is given.')
            if max_filters is not None:
                raise TypeError('"max_filters" must not be given when "fc" and "q" are given.')
            fc = np.array(fc, dtype='float32')
            q = np.array(q, dtype='float32')

        parametric = fc is None

        # Reset graph to be able to run this again
        tf.reset_default_graph()
        # Sampling frequency
        fs_tf = tf.constant(fs, name='f', dtype='float32')

        # Smoothen heavily
        fr_target = cls(name='Filter Initialization', frequency=frequency, raw=target)
        fr_target.smoothen_fractional_octave(window_size=1 / 7, iterations=1000)

        # Equalization target
        eq_target = tf.constant(target, name='eq_target', dtype='float32')

        n_ls = n_hs = 0

        if parametric:
            # Fc and Q not given, parametric equalizer, find initial estimation of peaks and gains
            fr_target_pos = np.clip(fr_target.smoothed, a_min=0.0, a_max=None)
            peak_inds = find_peaks(fr_target_pos)[0]
            fr_target_neg = np.clip(-fr_target.smoothed, a_min=0.0, a_max=None)
            peak_inds = np.concatenate((peak_inds, find_peaks(fr_target_neg)[0]))
            peak_inds.sort()
            peak_inds = peak_inds[np.abs(fr_target.smoothed[peak_inds]) > 0.1]

            # Peak center frequencies and gains
            peak_fc = frequency[peak_inds].astype('float32')

            if peak_fc[0] > 80:
                # First peak is beyond 80Hz, add peaks to 20Hz and 60Hz
                peak_fc = np.concatenate((np.array([20, 60], dtype='float32'), peak_fc))
            elif peak_fc[0] > 40:
                # First peak is beyond 40Hz, add peak to 20Hz
                peak_fc = np.concatenate((np.array([20], dtype='float32'), peak_fc))

            # Gains at peak center frequencies
            interpolator = InterpolatedUnivariateSpline(np.log10(frequency), fr_target.smoothed, k=1)
            peak_g = interpolator(np.log10(peak_fc)).astype('float32')

            def remove_small_filters(min_gain):
                # Remove peaks with too little gain
                nonlocal peak_fc, peak_g
                peak_fc = peak_fc[np.abs(peak_g) > min_gain]
                peak_g = peak_g[np.abs(peak_g) > min_gain]

            def merge_filters():
                # Merge two filters which have small integral between them
                nonlocal peak_fc, peak_g
                # Form filter pairs, select only filters with equal gain sign
                pair_inds = []
                for j in range(len(peak_fc) - 1):
                    if np.sign(peak_g[j]) == np.sign(peak_g[j + 1]):
                        pair_inds.append(j)

                min_err = None
                min_err_ind = None
                for pair_ind in pair_inds:
                    # Interpolate between the two points
                    f_0 = peak_fc[pair_ind]
                    g_0 = peak_g[pair_ind]
                    i_0 = np.argmin(np.abs(frequency - f_0))
                    f_1 = peak_fc[pair_ind + 1]
                    i_1 = np.argmin(np.abs(frequency - f_1))
                    g_1 = peak_g[pair_ind]
                    interp = InterpolatedUnivariateSpline(np.log10([f_0, f_1]), [g_0, g_1], k=1)
                    line = interp(frequency[i_0:i_1 + 1])
                    err = line - fr_target.smoothed[i_0:i_1 + 1]
                    err = np.sqrt(np.mean(np.square(err)))  # Root mean squared error
                    if min_err is None or err < min_err:
                        min_err = err
                        min_err_ind = pair_ind

                if min_err is None:
                    # No pairs detected
                    return False

                # Select smallest error if err < threshold
                if min_err < 0.3:
                    # New filter
                    c = peak_fc[min_err_ind] * np.sqrt(peak_fc[min_err_ind + 1] / peak_fc[min_err_ind])
                    c = frequency[np.argmin(np.abs(frequency - c))]
                    g = np.mean([peak_g[min_err_ind], peak_g[min_err_ind + 1]])
                    # Remove filters
                    peak_fc = np.delete(peak_fc, [min_err_ind, min_err_ind + 1])
                    peak_g = np.delete(peak_g, [min_err_ind, min_err_ind + 1])
                    # Add filter in-between
                    peak_fc = np.insert(peak_fc, min_err_ind, c)
                    peak_g = np.insert(peak_g, min_err_ind, g)
                    return True
                return False  # No prominent filter pairs

            # Remove insignificant filters
            remove_small_filters(0.1)
            if len(peak_fc) == 0:
                # All filters were insignificant, exit
                return np.zeros(frequency.shape), 0.0, np.array([]), np.array([]), np.array([])

            # Limit filter number to max_filters by removing least significant filters and merging close filters
            if max_filters is not None:
                if len(peak_fc) > max_filters:
                    # Remove too small filters
                    remove_small_filters(0.2)

                if len(peak_fc) > max_filters:
                    # Try to remove some more
                    remove_small_filters(0.33)

                # Merge filters if needed
                while merge_filters() and len(peak_fc) > max_filters:
                    pass

                if len(peak_fc) > max_filters:
                    # Remove smallest filters
                    sorted_inds = np.flip(np.argsort(np.abs(peak_g)))
                    sorted_inds = sorted_inds[:max_filters]
                    peak_fc = peak_fc[sorted_inds]
                    peak_g = peak_g[sorted_inds]

            sorted_inds = np.argsort(peak_fc)
            peak_fc = peak_fc[sorted_inds]
            peak_g = peak_g[sorted_inds]

            n = n_pk = len(peak_fc)

            # Frequencies
            f = tf.constant(np.repeat(np.expand_dims(frequency, axis=0), n, axis=0), name='f', dtype='float32')

            # Center frequencies
            fc = tf.get_variable('fc', initializer=np.expand_dims(np.log10(peak_fc), axis=1), dtype='float32')

            # Q
            Q_init = np.ones([n, 1], dtype='float32') * np.ones([n_pk, 1], dtype='float32')
            Q = tf.get_variable('Q', initializer=Q_init, dtype='float32')

        else:
            # Fc and Q given, fixed band equalizer
            Q = tf.get_variable(
                'Q',
                initializer=np.expand_dims(q, axis=1),
                dtype='float32',
                trainable=False
            )

            # Gains at peak center frequencies
            interpolator = InterpolatedUnivariateSpline(np.log10(frequency), fr_target.smoothed, k=1)
            peak_g = interpolator(np.log10(fc)).astype('float32')

            # Number of filters
            n = n_pk = len(fc)

            # Frequencies
            f = tf.constant(np.repeat(np.expand_dims(frequency, axis=0), n, axis=0), name='f', dtype='float32')

            # Center frequencies
            fc = tf.get_variable(
                'fc',
                initializer=np.expand_dims(np.log10(fc), axis=1),
                dtype='float32',
                trainable=False
            )

        # Gain
        gain = tf.get_variable('gain', initializer=np.expand_dims(peak_g, axis=1), dtype='float32')

        # Filter design

        # Low shelf filter
        # This is not used at the moment but is kept for future
        A = 10 ** (gain[:n_ls, :] / 40)
        w0 = 2 * np.pi * tf.pow(10.0, fc[:n_ls, :]) / fs_tf
        alpha = tf.sin(w0) / (2 * Q[:n_ls, :])

        a0_ls = ((A + 1) + (A - 1) * tf.cos(w0) + 2 * tf.sqrt(A) * alpha)
        a1_ls = (-(-2 * ((A - 1) + (A + 1) * tf.cos(w0))) / a0_ls)
        a2_ls = (-((A + 1) + (A - 1) * tf.cos(w0) - 2 * tf.sqrt(A) * alpha) / a0_ls)

        b0_ls = ((A * ((A + 1) - (A - 1) * tf.cos(w0) + 2 * tf.sqrt(A) * alpha)) / a0_ls)
        b1_ls = ((2 * A * ((A - 1) - (A + 1) * tf.cos(w0))) / a0_ls)
        b2_ls = ((A * ((A + 1) - (A - 1) * tf.cos(w0) - 2 * tf.sqrt(A) * alpha)) / a0_ls)

        # Peak filter
        A = 10 ** (gain[n_ls:n_ls+n_pk, :] / 40)
        w0 = 2 * np.pi * tf.pow(10.0, fc[n_ls:n_ls+n_pk, :]) / fs_tf
        alpha = tf.sin(w0) / (2 * Q[n_ls:n_ls+n_pk, :])

        a0_pk = (1 + alpha / A)
        a1_pk = -(-2 * tf.cos(w0)) / a0_pk
        a2_pk = -(1 - alpha / A) / a0_pk

        b0_pk = (1 + alpha * A) / a0_pk
        b1_pk = (-2 * tf.cos(w0)) / a0_pk
        b2_pk = (1 - alpha * A) / a0_pk

        # High self filter
        # This is not kept at the moment but kept for future
        A = 10 ** (gain[n_ls+n_pk:, :] / 40)
        w0 = 2 * np.pi * tf.pow(10.0, fc[n_ls+n_pk:, :]) / fs_tf
        alpha = tf.sin(w0) / (2 * Q[n_ls+n_pk:, :])

        a0_hs = (A + 1) - (A - 1) * tf.cos(w0) + 2 * tf.sqrt(A) * alpha
        a1_hs = -(2 * ((A - 1) - (A + 1) * tf.cos(w0))) / a0_hs
        a2_hs = -((A + 1) - (A - 1) * tf.cos(w0) - 2 * tf.sqrt(A) * alpha) / a0_hs

        b0_hs = (A * ((A + 1) + (A - 1) * tf.cos(w0) + 2 * tf.sqrt(A) * alpha)) / a0_hs
        b1_hs = (-2 * A * ((A - 1) + (A + 1) * tf.cos(w0))) / a0_hs
        b2_hs = (A * ((A + 1) + (A - 1) * tf.cos(w0) - 2 * tf.sqrt(A) * alpha)) / a0_hs

        # Concatenate all
        a0 = tf.concat([a0_ls, a0_pk, a0_hs], axis=0)
        a1 = tf.concat([a1_ls, a1_pk, a1_hs], axis=0)
        a2 = tf.concat([a2_ls, a2_pk, a2_hs], axis=0)
        b0 = tf.concat([b0_ls, b0_pk, b0_hs], axis=0)
        b1 = tf.concat([b1_ls, b1_pk, b1_hs], axis=0)
        b2 = tf.concat([b2_ls, b2_pk, b2_hs], axis=0)

        w = 2 * np.pi * f / fs_tf
        phi = 4 * tf.sin(w / 2) ** 2

        a0 = 1.0
        a1 *= -1
        a2 *= -1

        # Equalizer frequency response
        eq_op = 10 * tf.log(
            (b0 + b1 + b2) ** 2 + (b0 * b2 * phi - (b1 * (b0 + b2) + 4 * b0 * b2)) * phi
        ) / tf.log(10.0) - 10 * tf.log(
            (a0 + a1 + a2) ** 2 + (a0 * a2 * phi - (a1 * (a0 + a2) + 4 * a0 * a2)) * phi
        ) / tf.log(10.0)
        eq_op = tf.reduce_sum(eq_op, axis=0)

        # RMSE as loss
        loss = tf.reduce_mean(tf.square(eq_op - eq_target))
        learning_rate_value = 0.1
        decay = 0.9995
        learning_rate = tf.placeholder('float32', shape=(), name='learning_rate')
        train_step = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

        # Optimization loop
        min_loss = None
        threshold = 0.01
        momentum = 100
        bad_steps = 0

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            t = time()
            while time() - t < max_time:
                step_loss, _ = sess.run([loss, train_step], feed_dict={learning_rate: learning_rate_value})
                if min_loss is None or step_loss < min_loss:
                    # Improvement, update model
                    _eq, _fc, _Q, _gain = sess.run([eq_op, fc, Q, gain])
                    _fc = 10**_fc

                if min_loss is None or min_loss - step_loss > threshold:
                    # Loss improved
                    min_loss = step_loss
                    bad_steps = 0
                else:
                    # No improvement, increment bad step counter
                    bad_steps += 1
                if bad_steps > momentum:
                    # Bad steps exceed maximum number of bad steps, break
                    break
                learning_rate_value = learning_rate_value * decay

        rmse = np.sqrt(min_loss)  # RMSE

        # Fold center frequencies back to normal
        _fc = np.abs(np.round(_fc / fs) * fs - _fc)

        # Squeeze to rank-1 arrays
        _fc = np.squeeze(_fc)
        _Q = np.squeeze(_Q)
        _gain = np.squeeze(_gain)

        if parametric:
            # Filter selection slice
            sl = np.logical_and(np.abs(_gain) > 0.1, _fc > 10)
            _fc = _fc[sl]
            _Q = np.abs(_Q[sl])
            _gain = _gain[sl]

        # Sort filters by center frequency
        sorted_inds = np.argsort(_fc)
        _fc = _fc[sorted_inds]
        _Q = _Q[sorted_inds]
        _gain = _gain[sorted_inds]

        # Expand dimensionality for biquad
        _fc = np.expand_dims(_fc, axis=1)
        _Q = np.expand_dims(np.abs(_Q), axis=1)
        _gain = np.expand_dims(_gain, axis=1)
        # Re-compute eq
        a0, a1, a2, b0, b1, b2 = biquad.peaking(_fc, _Q, _gain, fs=fs)
        _eq = np.sum(biquad.digital_coeffs(frequency, fs, a0, a1, a2, b0, b1, b2), axis=0)

        coeffs_a = np.hstack((np.tile(a0, a1.shape), a1, a2))
        coeffs_b = np.hstack((b0, b1, b2))
        return _eq, rmse, np.squeeze(_fc, axis=1), np.squeeze(_Q, axis=1), np.squeeze(_gain, axis=1), coeffs_a, coeffs_b

    def optimize_parametric_eq(self, max_filters=None, fs=DEFAULT_FS):
        """Fits multiple biquad filters to equalization curve. If max_filters is a list with more than one element, one
        optimization run will be ran for each element. Each optimization run will continue from the previous. Each
        optimization run results must be combined with results of all the previous runs but can be used independently of
        the preceeding runs' results. If max_filters is [5, 5, 5] the first 5, 10 and 15 filters can be used
        independently.

        Args:
            max_filters: List of maximum number of filters available for each filter group optimization.
            fs: Sampling frequency

        Returns:
            - **filters:** Numpy array of filters where each row contains one filter fc, Q and gain
            - **n_produced:** Actual number of filters produced for each filter group. Calling with [5, 5] max_filters
                              might actually produce [4, 5] filters meaning that first 4 filters can be used
                              independently.
            - **max_gains:** Maximum gain value of the equalizer frequency response after each filter group
                             optimization. When using sub-set of filters independently the actual max gain of that
                             sub-set's frequency response must be applied as a negative digital preamp to avoid
                             clipping.
        """
        if not len(self.equalization):
            raise ValueError('Equalization has not been done yet.')

        if type(max_filters) != list:
            max_filters = [max_filters]

        self.parametric_eq = np.zeros(self.frequency.shape)
        fc = Q = gain = np.array([])
        coeffs_a = coeffs_b = np.empty((0, 3))
        n_produced = []
        max_gains = []
        for n in max_filters:
            _eq, rmse, _fc, _Q, _gain, _coeffs_a, _coeffs_b = self.optimize_biquad_filters(
                frequency=self.frequency,
                target=self.equalization - self.parametric_eq,
                max_filters=n,
                fs=fs
            )
            n_produced.append(len(_fc))
            # print('RMSE: {:.2f}dB'.format(rmse))
            self.parametric_eq += _eq
            max_gains.append(np.max(self.parametric_eq))
            fc = np.concatenate((fc, _fc))
            Q = np.concatenate((Q, _Q))
            gain = np.concatenate((gain, _gain))
            coeffs_a = np.vstack((coeffs_a, _coeffs_a))
            coeffs_b = np.vstack((coeffs_b, _coeffs_b))

        filters = np.transpose(np.vstack([fc, Q, gain]))
        return filters, n_produced, max_gains

    def optimize_fixed_band_eq(self, fc=None, q=None, fs=DEFAULT_FS):
        """Fits multiple fixed Fc and Q biquad filters to equalization curve.

        Args:
            fc: List of center frequencies for the filters
            q: List of Q values for the filters
            fs: Sampling frequency

        Returns:
            - **filters:** Numpy array of filters where each row contains one filter fc, Q and gain
            - **n_produced:** Number of filters. Equals to length or inputs.
            - **max_gains:** Maximum gain value of the equalizer frequency response.
        """
        eq, rmse, fc, Q, gain, coeffs_a, coeffs_b = self.optimize_biquad_filters(
            frequency=self.frequency,
            target=self.equalization,
            fc=fc,
            q=q,
            fs=fs
        )
        self.fixed_band_eq = eq
        filters = np.transpose(np.vstack([fc, Q, gain]))
        return filters, len(fc), np.max(self.fixed_band_eq)

    def write_eqapo_parametric_eq(self, file_path, filters, preamp=None):
        """Writes EqualizerAPO Parameteric eq settings to a file."""
        file_path = os.path.abspath(file_path)

        if preamp is None:
            # Calculate preamp from the cascade frequency response
            fr = np.zeros(self.frequency.shape)
            for filt in filters:
                a0, a1, a2, b0, b1, b2 = biquad.peaking(filt[0], filt[1], filt[2], fs=44100)
                fr += biquad.digital_coeffs(self.frequency, 44100, a0, a1, a2, b0, b1, b2)
            preamp = np.min([0.0, -(np.max(fr) + PREAMP_HEADROOM)])

        with open(file_path, 'w', encoding='utf-8') as f:
            s = f'Preamp: {preamp:.1f} dB\n'
            for i, filt in enumerate(filters):
                s += f'Filter {i+1}: ON PK Fc {filt[0]:.0f} Hz Gain {filt[2]:.1f} dB Q {filt[1]:.2f}\n'
            f.write(s)

    def write_rockbox_10_band_fixed_eq(self, file_path, filters, preamp=None):
        """Writes Rockbox 10 band eq settings to a file."""
        file_path = os.path.abspath(file_path)

        if preamp is None:
            # Calculate preamp from the cascade frequency response
            fr = np.zeros(self.frequency.shape)
            for filt in filters:
                a0, a1, a2, b0, b1, b2 = biquad.peaking(filt[0], filt[1], filt[2], fs=44100)
                fr += biquad.digital_coeffs(self.frequency, 44100, a0, a1, a2, b0, b1, b2)
            preamp = np.min([0.0, -(np.max(fr) + PREAMP_HEADROOM)])

        with open(file_path, 'w', encoding='utf-8') as f:
            s = f'eq enabled: on\neq precut: {round(abs(preamp), 1) * 10:.0f}\n'
            for i, filt in enumerate(filters):
                if i == 0:
                    s += f'eq low shelf filter: {filt[0]:.0f}, {round(filt[1], 1) * 10:.0f}, {round(filt[2], 1) * 10:.0f}\n'
                elif i == len(filters) - 1:
                    s += f'eq high shelf filter: {filt[0]:.0f}, {round(filt[1], 1) * 10:.0f}, {round(filt[2], 1) * 10:.0f}\n'
                else:
                    s += f'eq peak filter {i}: {filt[0]:.0f}, {round(filt[1], 1) * 10:.0f}, {round(filt[2], 1) * 10:.0f}\n'
            f.write(s)

    @staticmethod
    def _split_path(path):
        """Splits file system path into components."""
        folders = []
        while 1:
            path, folder = os.path.split(path)

            if folder != "":
                folders.append(folder)
            else:
                if path != "":
                    folders.append(path)

                break

        folders.reverse()
        return folders

    def minimum_phase_impulse_response(self, fs=DEFAULT_FS, f_res=DEFAULT_F_RES, normalize=True):
        """Generates minimum phase impulse response

        Inspired by:
        https://sourceforge.net/p/equalizerapo/code/HEAD/tree/tags/1.2/filters/GraphicEQFilter.cpp#l45

        Args:
            fs: Sampling frequency in Hz
            f_res: Frequency resolution as sampling interval. 20 would result in sampling at 0 Hz, 20 Hz, 40 Hz, ...
            normalize: Normalize gain to -0.2 dB

        Returns:
            Minimum phase impulse response
        """
        # Double frequency resolution because it will be halved when converting linear phase IR to minimum phase
        f_res /= 2
        # Interpolate to even sample interval
        fr = self.__class__(name='fr_data', frequency=self.frequency.copy(), raw=self.equalization.copy())
        # Save gain at lowest available frequency
        f_min = np.max([fr.frequency[0], f_res])
        interpolator = InterpolatedUnivariateSpline(np.log10(fr.frequency), fr.raw, k=1)
        gain_f_min = interpolator(np.log10(f_min))
        # Filter length, optimized for FFT speed
        n = round(fs // 2 / f_res)
        n = next_fast_len(n)
        f = np.linspace(0.0, fs // 2, n)
        # Run interpolation
        fr.interpolate(f, pol_order=1)
        # Set gain for all frequencies below original minimum frequency to match gain at the original minimum frequency
        fr.raw[fr.frequency <= f_min] = gain_f_min
        if normalize:
            # Reduce by max gain to avoid clipping with 1 dB of headroom
            fr.raw -= np.max(fr.raw)
            fr.raw -= PREAMP_HEADROOM
        # Minimum phase transformation by scipy's homomorphic method halves dB gain
        fr.raw *= 2
        # Convert amplitude to linear scale
        fr.raw = 10**(fr.raw / 20)
        # Zero gain at Nyquist frequency
        fr.raw[-1] = 0.0
        # Calculate response
        ir = firwin2(len(fr.frequency)*2, fr.frequency, fr.raw, fs=fs)
        # Convert to minimum phase
        ir = minimum_phase(ir, n_fft=len(ir))
        return ir

    def linear_phase_impulse_response(self, fs=DEFAULT_FS, f_res=DEFAULT_F_RES, normalize=True):
        """Generates impulse response implementation of equalization filter."""
        # Interpolate to even sample interval
        fr = self.__class__(name='fr_data', frequency=self.frequency, raw=self.equalization)
        # Save gain at lowest available frequency
        f_min = np.max([fr.frequency[0], f_res])
        interpolator = InterpolatedUnivariateSpline(np.log10(fr.frequency), fr.raw, k=1)
        gain_f_min = interpolator(np.log10(f_min))
        # Run interpolation
        fr.interpolate(np.arange(0.0, fs // 2, f_res), pol_order=1)
        # Set gain for all frequencies below original minimum frequency to match gain at the original minimum frequency
        fr.raw[fr.frequency <= f_min] = gain_f_min
        if normalize:
            # Reduce by max gain to avoid clipping with 1 dB of headroom
            fr.raw -= np.max(fr.raw)
            fr.raw -= PREAMP_HEADROOM
        # Convert amplitude to linear scale
        fr.raw = 10**(fr.raw / 20)
        # Calculate response
        fr.frequency = np.append(fr.frequency, fs // 2)
        fr.raw = np.append(fr.raw, 0.0)
        ir = firwin2(len(fr.frequency)*2, fr.frequency, fr.raw, fs=fs)
        return ir

    def write_readme(self, file_path, max_filters=None, max_gains=None):
        """Writes README.md with picture and Equalizer APO settings."""
        file_path = os.path.abspath(file_path)
        dir_path = os.path.dirname(file_path)
        model = self.name

        # Write model
        s = '# {}\n'.format(model)
        s += 'See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and ' \
             'info.\n'

        # Add parametric EQ settings
        parametric_eq_path = os.path.join(dir_path, model + ' ParametricEQ.txt')
        if os.path.isfile(parametric_eq_path) and self.parametric_eq is not None and len(self.parametric_eq):

            # Read Parametric eq
            with open(parametric_eq_path, 'r', encoding='utf-8') as f:
                parametric_eq_str = f.read().strip()

            # Filters as Markdown table
            filters = []
            for line in parametric_eq_str.split('\n'):
                if line == '' or line.split()[0] != 'Filter':
                    continue
                filter_type = line[line.index('ON')+3:line.index('Fc')-1]
                if filter_type == 'PK':
                    filter_type = 'Peaking'
                if filter_type == 'LS':
                    filter_type = 'Low Shelf'
                if filter_type == 'HS':
                    filter_type = 'High Shelf'
                fc = line[line.index('Fc')+3:line.index('Gain')-1]
                gain = line[line.index('Gain')+5:line.index('Q')-1]
                q = line[line.index('Q')+2:]
                filters.append([filter_type, fc, q, gain])
            filters_table_str = tabulate(
                filters,
                headers=['Type', 'Fc', 'Q', 'Gain'],
                tablefmt='orgtbl'
            ).replace('+', '|').replace('|-', '|:')

            max_filters_str = ''
            if type(max_filters) == list and len(max_filters) > 1:
                n = [0]
                for x in max_filters:
                    n.append(n[-1] + x)
                del n[0]
                if len(max_filters) > 3:
                    max_filters_str = ', '.join([str(x) for x in n[:-2]]) + f' or {n[-2]}'
                if len(max_filters) == 3:
                    max_filters_str = f'{n[0]} or {n[1]}'
                if len(max_filters) == 2:
                    max_filters_str = str(n[0])
                max_filters_str = f'The first {max_filters_str} filters can be used independently.'

            preamp_str = ''
            if type(max_gains) == list and len(max_gains) > 1:
                if len(max_gains) > 3:
                    strs = f', '.join([f'{-(x + PREAMP_HEADROOM):.1f} dB' for x in max_gains[:-2]]) + f' or -{max_gains[-2]:.1f} dB'
                    preamp_str = f'When using independent subset of filters, apply preamp of {strs}, respectively.'
                elif len(max_gains) == 3:
                    preamp_str = f'When using independent subset of filters, apply preamp of ' \
                                 f'{-(max_gains[0] + PREAMP_HEADROOM):.1f} dB ' \
                                 f'or {-(max_gains[1] + PREAMP_HEADROOM):.1f} dB, respectively.'
                elif len(max_gains) == 2:
                    preamp_str = f'When using independent subset of filters, apply preamp of ' \
                                 f'**{-(max_gains[0] + PREAMP_HEADROOM):.1f} dB**.'

            s += '''
            ### Parametric EQs
            In case of using parametric equalizer, apply preamp of **{preamp:.1f}dB** and build filters manually
            with these parameters. {max_filters_str}
            {preamp_str}

            {filters_table}
            '''.format(
                model=model,
                preamp=-(max_gains[-1] + PREAMP_HEADROOM),
                max_filters_str=max_filters_str,
                preamp_str=preamp_str,
                filters_table=filters_table_str
            )

        # Add fixed band eq
        fixed_band_eq_path = os.path.join(dir_path, model + ' FixedBandEQ.txt')
        if os.path.isfile(fixed_band_eq_path) and self.fixed_band_eq is not None and len(self.fixed_band_eq):
            preamp = np.min([0.0, -np.max(self.fixed_band_eq) - PREAMP_HEADROOM])

            # Read Parametric eq
            with open(fixed_band_eq_path, 'r', encoding='utf-8') as f:
                fixed_band_eq_str = f.read().strip()

            # Filters as Markdown table
            filters = []
            for line in fixed_band_eq_str.split('\n'):
                if line == '' or line.split()[0] != 'Filter':
                    continue
                filter_type = line[line.index('ON') + 3:line.index('Fc') - 1]
                if filter_type == 'PK':
                    filter_type = 'Peaking'
                if filter_type == 'LS':
                    filter_type = 'Low Shelf'
                if filter_type == 'HS':
                    filter_type = 'High Shelf'
                fc = line[line.index('Fc') + 3:line.index('Gain') - 1]
                gain = line[line.index('Gain') + 5:line.index('Q') - 1]
                q = line[line.index('Q') + 2:]
                filters.append([filter_type, fc, q, gain])
            filters_table_str = tabulate(
                filters,
                headers=['Type', 'Fc', 'Q', 'Gain'],
                tablefmt='orgtbl'
            ).replace('+', '|').replace('|-', '|:')

            s += '''
            ### Fixed Band EQs
            In case of using fixed band (also called graphic) equalizer, apply preamp of **{preamp:.1f}dB**
            (if available) and set gains manually with these parameters.

            {filters_table}
            '''.format(
                model=model,
                preamp=preamp,
                filters_table=filters_table_str
            )

        # Write image link
        img_path = os.path.join(dir_path, model + '.png')
        if os.path.isfile(img_path):
            img_url = f'./{os.path.split(img_path)[1]}'
            img_url = urllib.parse.quote(img_url, safe="%/:=&?~#+!$,;'@()*[]")
            s += '''
            ### Graphs
            ![]({})
            '''.format(img_url)

        # Write file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(re.sub('\n[ \t]+', '\n', s).strip())

    @staticmethod
    def generate_frequencies(f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, f_step=DEFAULT_STEP):
        freq = []
        f = f_min
        while f <= f_max:
            freq.append(f)
            f *= f_step
        return np.array(freq)

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

        # Interpolation functions
        keys = 'raw error error_smoothed equalization equalized_raw equalized_smoothed target'.split()
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

        # Run interpolators
        log_f = np.log10(self.frequency)
        for key in keys:
            if len(self.__dict__[key]) and key in interpolators:
                self.__dict__[key] = interpolators[key](log_f)

        if zero_freq_fix:
            # Restore zero frequency
            self.frequency[0] = 0

        # Everything but the interpolated data is affected by interpolating, reset them
        self.reset(**{key: False for key in keys})

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
        self.reset(raw=False, smoothed=False, error=False, error_smoothed=False, target=False)

        return -diff

    def _tilt(self, tilt=DEFAULT_TILT):
        """Creates a tilt for equalization.

        Args:
            tilt: Slope steepness in dB/octave

        Returns:
            Tilted data
        """
        # Center in logarithmic scale
        c = DEFAULT_F_MIN * np.sqrt(DEFAULT_F_MAX / DEFAULT_F_MIN)
        # N octaves above center
        n_oct = np.log2(self.frequency / c)
        return n_oct * tilt

    def create_target(self,
                      bass_boost_gain=DEFAULT_BASS_BOOST_GAIN,
                      bass_boost_fc=DEFAULT_BASS_BOOST_FC,
                      bass_boost_q=DEFAULT_BASS_BOOST_Q,
                      tilt=None):
        """Creates target curve with bass boost as described by harman target response.

        Args:
            bass_boost_gain: Bass boost amount in dB
            bass_boost_fc: Bass boost low shelf center frequency
            bass_boost_q: Bass boost low shelf quality
            tilt: Frequency response tilt (slope) in dB per octave, positive values make it brighter

        Returns:
            Target for equalization
        """
        bass_boost = biquad.digital_coeffs(
            self.frequency,
            DEFAULT_FS,
            *biquad.low_shelf(bass_boost_fc, bass_boost_q, bass_boost_gain, DEFAULT_FS)
        )
        if tilt is not None:
            tilt = self._tilt(tilt=tilt)
        else:
            tilt = np.zeros(len(self.frequency))
        return bass_boost + tilt

    def compensate(self,
                   compensation,
                   bass_boost_gain=DEFAULT_BASS_BOOST_GAIN,
                   bass_boost_fc=DEFAULT_BASS_BOOST_FC,
                   bass_boost_q=DEFAULT_BASS_BOOST_Q,
                   tilt=None,
                   sound_signature=None,
                   min_mean_error=False):
        """Sets target and error curves."""
        # Copy and center compensation data
        compensation = self.__class__(name='compensation', frequency=compensation.frequency, raw=compensation.raw)
        compensation.center()

        # Set target
        self.target = compensation.raw + self.create_target(
            bass_boost_gain=bass_boost_gain,
            bass_boost_fc=bass_boost_fc,
            bass_boost_q=bass_boost_q,
            tilt=tilt
        )
        if sound_signature is not None:
            # Sound signature give, add it to target curve
            if not np.all(sound_signature.frequency == self.frequency):
                # Interpolate sound signature to match self on the frequency axis
                sound_signature.interpolate(self.frequency)
            self.target += sound_signature.raw

        # Set error
        self.error = self.raw - self.target
        if min_mean_error:
            # Shift error by it's mean in range 100 Hz to 10 kHz
            delta = np.mean(self.error[np.logical_and(self.frequency >= 100, self.frequency <= 10000)])
            self.error -= delta
            self.target += delta

        # Smoothed error and equalization results are affected by compensation, reset them
        self.reset(
            raw=False,
            smoothed=False,
            error=False,
            error_smoothed=True,
            equalization=True,
            parametric_eq=True,
            fixed_band_eq=True,
            equalized_raw=True,
            equalized_smoothed=True,
            target=False
        )

    def _window_size(self, octaves):
        """Calculates moving average window size in indices from octaves."""
        # Octaves to coefficient
        k = 2 ** octaves
        # Calculate average step size in frequencies
        steps = []
        for i in range(1, len(self.frequency)):
            steps.append(self.frequency[i] / self.frequency[i - 1])
        step_size = sum(steps) / len(steps)
        # Calculate window size in indices
        # step_size^x = k  --> x = ...
        window_size = math.log(k) / math.log(step_size)
        # Half window size
        window_size = window_size
        # Round to integer to be usable as index
        window_size = round(window_size)
        if not window_size % 2:
            window_size += 1
        return window_size

    def _sigmoid(self, f_lower, f_upper, a_normal=0.0, a_treble=1.0):
        f_center = np.sqrt(f_upper / f_lower) * f_lower
        half_range = np.log10(f_upper) - np.log10(f_center)
        f_center = np.log10(f_center)
        a = expit((np.log10(self.frequency) - f_center) / (half_range / 4))
        a = a * -(a_normal - a_treble) + a_normal
        return a

    def _smoothen_fractional_octave(self,
                                    data,
                                    window_size=DEFAULT_SMOOTHING_WINDOW_SIZE,
                                    iterations=DEFAULT_SMOOTHING_ITERATIONS,
                                    treble_window_size=None,
                                    treble_iterations=None,
                                    treble_f_lower=DEFAULT_TREBLE_SMOOTHING_F_LOWER,
                                    treble_f_upper=DEFAULT_TREBLE_SMOOTHING_F_UPPER):
        """Smooths data.

        Args:
            window_size: Filter window size in octaves.
            iterations: Number of iterations to run the filter. Each new iteration is using output of previous one.
            treble_window_size: Filter window size for high frequencies.
            treble_iterations: Number of iterations for treble filter.
            treble_f_lower: Lower boundary of transition frequency region. In the transition region normal filter is \
                        switched to treble filter with sigmoid weighting function.
            treble_f_upper: Upper boundary of transition frequency reqion. In the transition region normal filter is \
                        switched to treble filter with sigmoid weighting function.
        """
        if None in self.frequency or None in data:
            # Must not contain None values
            raise ValueError('None values present, cannot smoothen!')

        # Normal filter
        y_normal = data
        with warnings.catch_warnings():
            # Savgol filter uses array indexing which is not future proof, ignoring the warning and trusting that this
            # will be fixed in the future release
            warnings.simplefilter('ignore')
            for i in range(iterations):
                y_normal = savgol_filter(y_normal, self._window_size(window_size), 2)

            # Treble filter
            y_treble = data
            for _ in range(treble_iterations):
                y_treble = savgol_filter(y_treble, self._window_size(treble_window_size), 2)

        # Transition weighted with sigmoid
        k_treble = self._sigmoid(treble_f_lower, treble_f_upper)
        k_normal = k_treble * -1 + 1
        return y_normal * k_normal + y_treble * k_treble

    def smoothen_fractional_octave(self,
                                   window_size=DEFAULT_SMOOTHING_WINDOW_SIZE,
                                   iterations=DEFAULT_SMOOTHING_ITERATIONS,
                                   treble_window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
                                   treble_iterations=DEFAULT_TREBLE_SMOOTHING_ITERATIONS,
                                   treble_f_lower=DEFAULT_TREBLE_SMOOTHING_F_LOWER,
                                   treble_f_upper=DEFAULT_TREBLE_SMOOTHING_F_UPPER):
        """Smooths data.

        Args:
            window_size: Filter window size in octaves.
            iterations: Number of iterations to run the filter. Each new iteration is using output of previous one.
            treble_window_size: Filter window size for high frequencies.
            treble_iterations: Number of iterations for treble filter.
            treble_f_lower: Lower boundary of transition frequency region. In the transition region normal filter is \
                        switched to treble filter with sigmoid weighting function.
            treble_f_upper: Upper boundary of transition frequency reqion. In the transition region normal filter is \
                        switched to treble filter with sigmoid weighting function.
        """
        if treble_f_upper <= treble_f_lower:
            raise ValueError('Upper transition boundary must be greater than lower boundary')

        # Smoothen raw data
        self.smoothed = self._smoothen_fractional_octave(
            self.raw,
            window_size=window_size,
            iterations=iterations,
            treble_window_size=treble_window_size,
            treble_iterations=treble_iterations,
            treble_f_lower=treble_f_lower,
            treble_f_upper=treble_f_upper
        )

        if len(self.error):
            # Smoothen error data
            self.error_smoothed = self._smoothen_fractional_octave(
                self.error,
                window_size=window_size,
                iterations=iterations,
                treble_window_size=treble_window_size,
                treble_iterations=treble_iterations,
                treble_f_lower=treble_f_lower,
                treble_f_upper=treble_f_upper
            )

        # Equalization is affected by smoothing, reset equalization results
        self.reset(
            raw=False,
            smoothed=False,
            error=False,
            error_smoothed=False,
            equalization=True,
            parametric_eq=True,
            fixed_band_eq=True,
            equalized_raw=True,
            equalized_smoothed=True,
            target=False
        )

    def equalize(self,
                 max_gain=DEFAULT_MAX_GAIN,
                 limit=DEFAULT_MAX_SLOPE,
                 limit_decay=0.0,
                 concha_interference=False,
                 window_size=1 / 12,
                 treble_window_size=2,
                 treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                 treble_f_upper=DEFAULT_TREBLE_F_UPPER,
                 treble_gain_k=DEFAULT_TREBLE_GAIN_K):
        """Creates equalization curve and equalized curve.

        Args:
            max_gain: Maximum positive gain in dB
            limit: Maximum slope in dB per octave
            limit_decay: Decay coefficient (per octave) for the limit. Value of 0.5 would reduce limit by 50% in an octave
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
        fr.smoothen_fractional_octave(
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
            return y, fr.smoothed.copy(), np.array([]), np.array([False] * len(y)), np.array([]),\
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
                x, y, limit, limit_decay=limit_decay, start_index=0, peak_inds=peak_inds,
                limit_free_mask=limit_free_mask, concha_interference=concha_interference)
            limited_rtl, clipped_rtl, regions_rtl = self.limited_rtl_slope(
                x, y, limit, limit_decay=limit_decay, start_index=rtl_start, peak_inds=peak_inds,
                limit_free_mask=limit_free_mask, concha_interference=concha_interference)

            # ltr and rtl limited curves are combined with min function
            combined = self.__class__(
                name='limiter', frequency=x, raw=np.min(np.vstack([limited_ltr, limited_rtl]), axis=0))

            # Limit treble gain
            gain_k = self._sigmoid(treble_f_lower, treble_f_upper, a_normal=1.0, a_treble=treble_gain_k)
            combined.raw *= gain_k

            # Gain can be reduced in the treble region
            # Clip positive gain to max gain
            combined.raw = np.min(np.vstack([combined.raw, np.ones(combined.raw.shape) * max_gain]), axis=0)
            # Smoothen the curve to get rid of hard kinks
            combined.smoothen_fractional_octave(window_size=1 / 5, treble_window_size=1 / 5)

            # Equalization curve
            self.equalization = combined.smoothed

        # Equalized
        self.equalized_raw = self.raw + self.equalization
        if len(self.smoothed):
            self.equalized_smoothed = self.smoothed + self.equalization

        return combined.smoothed.copy(), fr.smoothed.copy(), limited_ltr, clipped_ltr, limited_rtl,\
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
    def limited_rtl_slope(cls, x, y, limit, limit_decay=0.0, start_index=0, peak_inds=None, limit_free_mask=None,
                          concha_interference=False):
        """Limits right to left slope of an equalization curve.

            Args:
                x: frequencies
                y: amplitudes
                limit: maximum slope in dB / oct
                limit_decay: Limit decay coefficient per octave
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
            x, np.flip(y), limit, limit_decay=limit_decay, start_index=start_index, peak_inds=peak_inds,
            limit_free_mask=limit_free_mask, concha_interference=concha_interference)
        limited_rtl = np.flip(limited_rtl)
        clipped_rtl = np.flip(clipped_rtl)
        regions_rtl = len(x) - regions_rtl - 1
        return limited_rtl, clipped_rtl, regions_rtl

    @classmethod
    def limited_ltr_slope(cls, x, y, limit, limit_decay=0.0, start_index=0, peak_inds=None, limit_free_mask=None,
                          concha_interference=False):
        """Limits left to right slope of a equalization curve.

        Args:
            x: frequencies
            y: amplitudes
            limit: maximum slope in dB / oct
            limit_decay: Limit decay coefficient per octave
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
            slope = cls.log_log_gradient(x[i], x[i - 1], y[i], limited[-1])
            # Local limit is 25% of the limit between 8 kHz and 10 kHz
            local_limit = limit / 4 if 8000 <= x[i] <= 11500 and concha_interference else limit

            if clipped[-1]:
                # Previous sample clipped, reduce limit
                # print(f'{x[i]} -> {x[regions[-1][0]]} = {(1 - limit_decay) ** np.log2(x[i] / x[regions[-1][0]])}')
                local_limit *= (1 - limit_decay) ** np.log2(x[i] / x[regions[-1][0]])

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
    def log_log_gradient(f0, f1, g0, g1):
        """Calculates gradient (derivative) in dB per octave."""
        octaves = np.log(f1 / f0) / np.log(2)
        gain = g1 - g0
        return gain / octaves

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
    def kwarg_defaults(kwargs, **defaults):
        if kwargs is None:
            kwargs = {}
        else:
            kwargs = {key: val for key, val in kwargs.items()}
        for key, val in defaults.items():
            if key not in kwargs:
                kwargs[key] = val
        return kwargs

    @staticmethod
    def init_plot(fig=None, ax=None, f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, a_min=None, a_max=None, ):
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

    def plot_graph(self,
                   fig=None,
                   ax=None,
                   show=True,
                   raw=True,
                   error=True,
                   smoothed=True,
                   error_smoothed=True,
                   equalization=True,
                   parametric_eq=True,
                   fixed_band_eq=True,
                   equalized=True,
                   target=True,
                   file_path=None,
                   f_min=DEFAULT_F_MIN,
                   f_max=DEFAULT_F_MAX,
                   a_min=None,
                   a_max=None,
                   color='black',
                   raw_plot_kwargs=None,
                   smoothed_plot_kwargs=None,
                   error_plot_kwargs=None,
                   error_smoothed_plot_kwargs=None,
                   equalization_plot_kwargs=None,
                   parametric_eq_plot_kwargs=None,
                   fixed_band_eq_plot_kwargs=None,
                   equalized_plot_kwargs=None,
                   target_plot_kwargs=None,
                   close=False):
        """Plots frequency response graph."""
        if not len(self.frequency):
            raise ValueError('\'frequency\' has no data!')

        fig, ax = self.__class__.init_plot(fig=fig, ax=ax, f_min=f_min, f_max=f_max, a_min=a_min, a_max=a_max)

        if target and len(self.target):
            ax.plot(
                self.frequency, self.target,
                **self.kwarg_defaults(target_plot_kwargs, label='Target', linewidth=5, color='lightblue')
            )

        if smoothed and len(self.smoothed):
            ax.plot(
                self.frequency, self.smoothed,
                **self.kwarg_defaults(smoothed_plot_kwargs, label='Raw Smoothed', linewidth=5, color='lightgrey')
            )

        if error_smoothed and len(self.error_smoothed):
            ax.plot(
                self.frequency, self.error_smoothed,
                **self.kwarg_defaults(error_smoothed_plot_kwargs, label='Error Smoothed', linewidth=5, color='pink')
            )

        if raw and len(self.raw):
            ax.plot(
                self.frequency, self.raw,
                **self.kwarg_defaults(raw_plot_kwargs, label='Raw', linewidth=1, color=color)
            )

        if error and len(self.error):
            ax.plot(
                self.frequency, self.error,
                **self.kwarg_defaults(error_plot_kwargs, label='Error', linewidth=1, color='red')
            )

        if equalization and len(self.equalization):
            ax.plot(
                self.frequency, self.equalization,
                **self.kwarg_defaults(equalization_plot_kwargs, label='Equalization', linewidth=5, color='lightgreen')
            )

        if parametric_eq and len(self.parametric_eq):
            ax.plot(
                self.frequency, self.parametric_eq,
                **self.kwarg_defaults(parametric_eq_plot_kwargs, label='Parametric Eq', linewidth=1, color='darkgreen')
            )

        if fixed_band_eq and len(self.fixed_band_eq):
            ax.plot(
                self.frequency, self.fixed_band_eq,
                **self.kwarg_defaults(
                    fixed_band_eq_plot_kwargs,
                    label='Fixed Band Eq', linewidth=1, color='darkgreen', linestyle='--'
                )
            )

        if equalized and len(self.equalized_raw):
            ax.plot(
                self.frequency, self.equalized_raw,
                **self.kwarg_defaults(equalized_plot_kwargs, label='Equalized', linewidth=1, color='blue')
            )

        ax.set_title(self.name)
        if len(ax.lines) > 0:
            ax.legend(fontsize=8)

        if file_path is not None:
            file_path = os.path.abspath(file_path)
            fig.savefig(file_path, dpi=120)
            im = Image.open(file_path)
            im = im.convert('P', palette=Image.ADAPTIVE, colors=60)
            im.save(file_path, optimize=True)
        if show:
            plt.show()
        elif close:
            plt.close(fig)
        return fig, ax

    def harman_onear_preference_score(self):
        """Calculates Harman preference score for over-ear and on-ear headphones.

        Returns:
            - score: Preference score
            - std: Standard deviation of error
            - slope: Slope of linear regression of error
        """
        fr = self.copy()
        fr.interpolate(HARMAN_ONEAR_PREFERENCE_FREQUENCIES)
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

    def process(self,
                compensation=None,
                min_mean_error=False,
                equalize=False,
                parametric_eq=False,
                fixed_band_eq=False,
                fc=None,
                q=None,
                ten_band_eq=None,
                max_filters=None,
                bass_boost_gain=None,
                bass_boost_fc=None,
                bass_boost_q=None,
                tilt=None,
                sound_signature=None,
                max_gain=DEFAULT_MAX_GAIN,
                fs=DEFAULT_FS,
                concha_interference=False,
                window_size=DEFAULT_SMOOTHING_WINDOW_SIZE,
                treble_window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
                treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                treble_f_upper=DEFAULT_TREBLE_F_UPPER,
                treble_gain_k=DEFAULT_TREBLE_GAIN_K,
                parametric_eq_filter_max_gain=DEFAULT_PEQ_FILTER_MAX_GAIN,
                fixed_band_eq_filter_max_gain=DEFAULT_FBEQ_FILTER_MAX_GAIN):
        """Runs processing pipeline with interpolation, centering, compensation and equalization.

        Args:
            compensation: Compensation FrequencyResponse. Must be interpolated and centered.
            min_mean_error: Minimize mean error. Normally all curves cross at 1 kHz but this makes it possible to shift
                            error curve so that mean between 100 Hz and 10 kHz is at minimum. Target curve is shifted
                            accordingly. Useful for avoiding large bias caused by a narrow notch or peak at 1 kHz.
            equalize: Run equalization?
            parametric_eq: Optimize peaking filters for parametric eq?
            fixed_band_eq: Optimize peaking filters for fixed band (graphic) eq?
            fc: List of center frequencies for fixed band eq
            q: List of Q values for fixed band eq
            ten_band_eq: Optimize filters for standard ten band eq?
            max_filters: List of maximum number of peaking filters for each additive filter optimization run.
            bass_boost_gain: Bass boost amount in dB.
            bass_boost_fc: Bass boost low shelf center frequency.
            bass_boost_q: Bass boost low shelf quality.
            tilt: Target frequency response tilt in db / octave
            sound_signature: Sound signature as FrequencyResponse instance. Raw data will be used.
            max_gain: Maximum positive gain in dB
            fs: Sampling frequency
            concha_interference: Do measurements include concha interference which produced a narrow dip around 9 kHz?
            window_size: Smoothing window size in octaves.
            treble_window_size: Smoothing window size in octaves in the treble region.
            treble_f_lower: Lower boundary of transition frequency region. In the transition region normal filter is
                            switched to treble filter with sigmoid weighting function.
            treble_f_upper: Upper boundary of transition frequency region. In the transition region normal filter is
                            switched to treble filter with sigmoid weighting function.
            treble_gain_k: Coefficient for treble gain, positive and negative. Useful for disabling or reducing
                           equalization power in treble region. Defaults to 1.0 (not limited).
            parametric_eq_filter_max_gain: Maximum gain range for parametric equalizer filters
            fixed_band_eq_filter_max_gain: Maximum gain range for fixed band equalizer filters

        Returns:
            - **peq_filters:** Numpy array of produced parametric eq peaking filters. Each row contains Fc, Q and gain
            - **n_peq_filters:** Number of produced parametric eq peaking filters for each group.
            - **peq_max_gains:** Maximum positive gains in each parametric eq peaking filter group.
            - **fbeq_filters:** Numpy array of produced fixed band peaking filters. Each row contains Fc, Q and gain
            - **n_fbeq_filters:** Number of produced fixed band peaking filters.
            - **fbeq_max_gains:** Maximum positive gain for fixed band eq.
        """
        if parametric_eq and not equalize:
            raise ValueError('equalize must be True when parametric_eq is True.')

        if ten_band_eq:
            # Ten band eq is a shortcut for setting Fc and Q values to standard 10-band equalizer filters parameters
            fixed_band_eq = True
            fc = np.array([31.25, 62.5, 125, 250, 500, 1000, 2000, 4000, 8000, 16000], dtype='float32')
            q = np.ones(10, dtype='float32') * np.sqrt(2)

        if fixed_band_eq:
            if fc is None or q is None:
                raise ValueError('"fc" and "q" must be given when "fixed_band_eq" is given.')
            # Center frequencies are given but Q is a single value
            # Repeat Q to length of Fc
            if type(q) in [list, np.ndarray]:
                if len(q) == 1:
                    q = np.repeat(q[0], len(fc))
                elif len(q) != len(fc):
                    raise ValueError('q must have one elemet or the same number of elements as fc.')
            elif type(q) not in [list, np.ndarray]:
                q = np.repeat(q, len(fc))

        if fixed_band_eq and not equalize:
            raise ValueError('equalize must be True when fixed_band_eq or ten_band_eq is True.')

        if max_filters is not None and type(max_filters) != list:
            max_filters = [max_filters]

        # Interpolate to standard frequency vector
        self.interpolate()

        # Center by 1kHz
        self.center()

        if compensation is not None:
            # Compensate
            self.compensate(
                compensation,
                bass_boost_gain=bass_boost_gain,
                bass_boost_fc=bass_boost_fc,
                bass_boost_q=bass_boost_q,
                tilt=tilt,
                sound_signature=sound_signature,
                min_mean_error=min_mean_error
            )

        # Smooth data
        self.smoothen_fractional_octave(
            window_size=window_size,
            treble_window_size=treble_window_size,
            treble_f_lower=treble_f_lower,
            treble_f_upper=treble_f_upper
        )

        peq_filters = n_peq_filters = peq_max_gains = fbeq_filters = n_fbeq_filters = fbeq_max_gains = None
        # Equalize
        if equalize:
            self.equalize(
                max_gain=max_gain, concha_interference=concha_interference, treble_f_lower=treble_f_lower,
                treble_f_upper=treble_f_upper, treble_gain_k=treble_gain_k)
            if parametric_eq:
                # Get the filters
                peq_filters, n_peq_filters, peq_max_gains = self.optimize_parametric_eq(
                    max_filters=max_filters, filter_max_gain=parametric_eq_filter_max_gain, fs=fs)
            if fixed_band_eq:
                fbeq_filters, n_fbeq_filters, fbeq_max_gains = self.optimize_fixed_band_eq(
                    fc=fc, q=q, filter_max_gain=fixed_band_eq_filter_max_gain, fs=fs)

        return peq_filters, n_peq_filters, peq_max_gains, fbeq_filters, n_fbeq_filters, fbeq_max_gains
