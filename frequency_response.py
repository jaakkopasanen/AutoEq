# -*- coding: utf-8 -*_

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import argparse
import math
import pandas as pd
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.signal import savgol_filter, find_peaks, minimum_phase, firwin2
from scipy.special import expit
import soundfile as sf
import numpy as np
from glob import glob
import urllib
from warnings import warn
import tensorflow as tf
from time import time
from tabulate import tabulate
from PIL import Image
import re
import biquad
import warnings

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_F_MIN = 20
DEFAULT_F_MAX = 20000
DEFAULT_STEP = 1.01

DEFAULT_MAX_GAIN = 6.0
DEFAULT_TREBLE_F_LOWER = 6000.0
DEFAULT_TREBLE_F_UPPER = 8000.0
DEFAULT_TREBLE_MAX_GAIN = 0.0
DEFAULT_TREBLE_GAIN_K = 1.0

DEFAULT_SMOOTHING_METHOD = 'max'
DEFAULT_SMOOTHING_WINDOW_SIZE = 1 / 6
DEFAULT_SMOOTHING_ITERATIONS = 1
DEFAULT_TREBLE_SMOOTHING_F_LOWER = 100.0
DEFAULT_TREBLE_SMOOTHING_F_UPPER = 10000.0
DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE = 1 / 3
DEFAULT_TREBLE_SMOOTHING_ITERATIONS = 1
DEFAULT_TILT = 0.0
DEFAULT_FS = 44100
DEFAULT_BIT_DEPTH = 16
DEFAULT_PHASE = 'minimum'
DEFAULT_F_RES = 10

DEFAULT_OE_BASS_BOOST_F_LOWER = 35
DEFAULT_OE_BASS_BOOST_F_UPPER = 280
DEFAULT_IE_BASS_BOOST_F_LOWER = 25
DEFAULT_IE_BASS_BOOST_F_UPPER = 350

GRAPHIC_EQ_STEP = 1.1


class FrequencyResponse:
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
        return FrequencyResponse(
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

    @staticmethod
    def _init_data(data):
        """Initializes data to a clean format. If None is passed and empty array is created. Non-numbers are removed."""
        data = data if data is not None else []
        data = [None if x is None or math.isnan(x) else x for x in data]
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
        reset_data = []
        if raw and len(self.raw):
            reset_data.append('raw')
        if smoothed and len(self.smoothed):
            reset_data.append('smoothed')
        if error and len(self.error):
            reset_data.append('error')
        if error_smoothed and len(self.error_smoothed):
            reset_data.append('error_smoothed')
        if equalization and len(self.equalization):
            reset_data.append('equalization')
        if parametric_eq and len(self.parametric_eq):
            reset_data.append('parametric_eq')
        if fixed_band_eq and len(self.fixed_band_eq):
            reset_data.append('fixed_band_eq')
        if equalized_raw and len(self.equalized_raw):
            reset_data.append('equalized_raw')
        if equalized_smoothed and len(self.equalized_smoothed):
            reset_data.append('equalized_smoothed')
        if target and len(self.target):
            reset_data.append('target')
        if len(reset_data):
            warn('Resetting data of "{}". These need to be regenerated if they are still needed!'.format(
                '", "'.join(reset_data)
            ))
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
        file_path = os.path.abspath(file_path)
        name = os.path.split(file_path)[-1].split('.')[0]

        f = open(file_path)
        df = pd.read_csv(f, sep=',', header=0)
        if 'frequency' not in df:
            raise AttributeError('Column "frequency" missing from file "{fp}". Found columns are "{columns}".'.format(
                fp=file_path,
                columns='", "'.join(df.columns)
            ))
        frequency = list(df['frequency'])
        raw = list(df['raw']) if 'raw' in df else None
        smoothed = list(df['smoothed']) if 'smoothed' in df else None
        error = list(df['error']) if 'error' in df else None
        error_smoothed = list(df['error_smoothed']) if 'error_smoothed' in df else None
        equalization = list(df['equalization']) if 'equalization' in df else None
        parametric_eq = list(df['parametric_eq']) if 'parametric_eq' in df else None
        equalized_raw = list(df['equalized_raw']) if 'equalized_raw' in df else None
        equalized_smoothed = list(df['equalized_smoothed']) if 'equalized_smoothed' in df else None
        target = list(df['target']) if 'target' in df else None
        f.close()

        return cls(
            name=name,
            frequency=frequency,
            raw=raw,
            smoothed=smoothed,
            error=error,
            error_smoothed=error_smoothed,
            equalization=equalization,
            parametric_eq=parametric_eq,
            equalized_raw=equalized_raw,
            equalized_smoothed=equalized_smoothed,
            target=target
        )
    
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
            d['parametric_eq'] = [x if x is not None else 'NaN' for x in self.fixed_band_eq]
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

    def write_eqapo_graphic_eq(self, file_path, normalize=True):
        """Writes equalization graph to a file as Equalizer APO config."""
        file_path = os.path.abspath(file_path)

        fr = FrequencyResponse(name='hack', frequency=self.frequency, raw=self.equalization)
        fr.interpolate(f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, f_step=GRAPHIC_EQ_STEP)
        if normalize:
            fr.raw -= np.max(fr.raw) + 0.5
            if fr.raw[0] > 0.0:
                # Prevent bass boost below lowest frequency
                fr.raw[0] = 0.0

        # Remove leading zeros
        while np.abs(fr.raw[-1]) < 0.1 and np.abs(fr.raw[-2]) < 0.1:  # Last two are zeros
            fr.raw = fr.raw[:-1]

        with open(file_path, 'w') as f:
            s = '; '.join(['{f} {a:.1f}'.format(f=f, a=a) for f, a in zip(fr.frequency, fr.raw)])
            s = 'GraphicEQ: ' + s
            f.write(s)
        return s

    @staticmethod
    def optimize_biquad_filters(frequency, target, max_time=5, max_filters=None, fs=DEFAULT_FS, fc=None, q=None):
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
        fr_target = FrequencyResponse(name='Filter Initialization', frequency=frequency, raw=target)
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
                    i_0 = np.where(frequency == f_0)[0][0]
                    f_1 = peak_fc[pair_ind + 1]
                    i_1 = np.where(frequency == f_1)[0][0]
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
        frequency = np.repeat(np.expand_dims(frequency, axis=0), len(_fc), axis=0)
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

    @staticmethod
    def write_eqapo_parametric_eq(file_path, filters):
        """Writes EqualizerAPO Parameteric eq settings to a file."""
        file_path = os.path.abspath(file_path)

        with open(file_path, 'w') as f:
            f.write('\n'.join(['Filter {i}: ON {type} Fc {fc:.0f} Hz Gain {gain:.1f} dB Q {Q:.2f}'.format(
                i=i+1,
                type='PK',
                fc=filters[i, 0],
                Q=filters[i, 1],
                gain=filters[i, 2]
            ) for i in range(len(filters))]))

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
            normalize: Normalize gain to -0.5 dB

        Returns:
            Minimum phase impulse response
        """
        # Double frequency resolution because it will be halved when converting linear phase IR to minimum phase
        f_res /= 2
        # Interpolate to even sample interval
        fr = FrequencyResponse(name='fr_data', frequency=self.frequency.copy(), raw=self.equalization.copy())
        # Save gain at lowest available frequency
        f_min = np.max([fr.frequency[0], f_res])
        interpolator = InterpolatedUnivariateSpline(np.log10(fr.frequency), fr.raw, k=1)
        gain_f_min = interpolator(np.log10(f_min))
        # Run interpolation
        fr.interpolate(np.arange(0, fs // 2, f_res), pol_order=1)
        # Set gain for all frequencies below original minimum frequency to match gain at the original minimum frequency
        fr.raw[fr.frequency <= f_min] = gain_f_min
        if normalize:
            # Reduce by max gain to avoid clipping with 1 dB of headroom
            fr.raw -= np.max(fr.raw)
            fr.raw -= 0.5
        # Minimum phase transformation by scipy's homomorphic method halves dB gain
        fr.raw *= 2
        # Convert amplitude to linear scale
        fr.raw = 10**(fr.raw / 20)
        # Calculate response
        fr.frequency = np.append(fr.frequency, fs // 2)
        fr.raw = np.append(fr.raw, 0.0)
        ir = firwin2(len(fr.frequency)*2+1, fr.frequency, fr.raw, fs=fs)
        # Convert to minimum phase
        ir = minimum_phase(ir)
        return ir

    def linear_phase_impulse_response(self, fs=DEFAULT_FS, f_res=DEFAULT_F_RES, normalize=True):
        """Generates impulse response implementation of equalization filter."""
        # Interpolate to even sample interval
        fr = FrequencyResponse(name='fr_data', frequency=self.frequency, raw=self.equalization)
        # Save gain at lowest available frequency
        f_min = np.max([fr.frequency[0], f_res])
        interpolator = InterpolatedUnivariateSpline(np.log10(fr.frequency), fr.raw, k=1)
        gain_f_min = interpolator(np.log10(f_min))
        # Run interpolation
        fr.interpolate(np.arange(0, fs // 2, f_res))
        # Set gain for all frequencies below original minimum frequency to match gain at the original minimum frequency
        fr.raw[fr.frequency <= f_min] = gain_f_min
        if normalize:
            # Reduce by max gain to avoid clipping with 1 dB of headroom
            fr.raw -= np.max(fr.raw)
            fr.raw -= 0.5
        # Convert amplitude to linear scale
        fr.raw = 10**(fr.raw / 20)
        # Calculate response
        fr.frequency = np.append(fr.frequency, fs // 2)
        fr.raw = np.append(fr.raw, 0.0)
        ir = firwin2(len(fr.frequency)*2, fr.frequency, fr.raw, fs=fs)
        return ir

    def write_readme(self,
                     file_path,
                     max_filters=None,
                     max_gains=None):
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
            max_gains = [x + 0.5 for x in max_gains]

            # Read Parametric eq
            with open(parametric_eq_path, 'r') as f:
                parametric_eq_str = f.read().strip()

            # Filters as Markdown table
            filters = []
            for line in parametric_eq_str.split('\n'):
                if line == '':
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
                    max_filters_str = ', '.join([str(x) for x in n[:-2]]) + ' or {}'.format(n[-2])
                if len(max_filters) == 3:
                    max_filters_str = '{n0} or {n1}'.format(n0=n[0], n1=n[1])
                if len(max_filters) == 2:
                    max_filters_str = str(n[0])
                max_filters_str = 'The first {} filters can be used independently.'.format(max_filters_str)

            preamp_str = ''
            if type(max_gains) == list and len(max_gains) > 1:
                max_gains = [x + 0.1 for x in max_gains]
                if len(max_gains) > 3:
                    _s = 'When using independent subset of filters, apply preamp of {}, respectively.'
                    preamp_str = ', '.join(['-{:.1f}dB'.format(x) for x in max_gains[:-2]])
                    preamp_str += ' or -{:.1f}dB'.format(max_gains[-2])
                if len(max_gains) == 3:
                    _s = 'When using independent subset of filters, apply preamp of {}, respectively.'
                    preamp_str = '-{g0:.1f}dB or -{g1:.1f}dB'.format(g0=max_gains[0], g1=max_gains[1])
                if len(max_gains) == 2:
                    _s = 'When using independent subset of filters, apply preamp of **{}**.'
                    preamp_str = '-{:.1f}dB'.format(max_gains[0])
                preamp_str = _s.format(preamp_str)

            s += '''
            ### Parametric EQs
            In case of using parametric equalizer, apply preamp of **-{preamp:.1f}dB** and build filters manually
            with these parameters. {max_filters_str}
            {preamp_str}

            {filters_table}
            '''.format(
                model=model,
                preamp=max_gains[-1],
                max_filters_str=max_filters_str,
                preamp_str=preamp_str,
                filters_table=filters_table_str
            )

        # Add fixed band eq
        fixed_band_eq_path = os.path.join(dir_path, model + ' FixedBandEQ.txt')
        if os.path.isfile(fixed_band_eq_path) and self.fixed_band_eq is not None and len(self.fixed_band_eq):
            preamp = np.min([0.0, float(-np.max(self.fixed_band_eq))]) - 0.5

            # Read Parametric eq
            with open(fixed_band_eq_path, 'r') as f:
                fixed_band_eq_str = f.read().strip()

            # Filters as Markdown table
            filters = []
            for line in fixed_band_eq_str.split('\n'):
                if line == '':
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
            img_rel_path = os.path.relpath(img_path, ROOT_DIR)
            img_url = '/'.join(self._split_path(img_rel_path))
            img_url = 'https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/{}'.format(img_url)
            img_url = urllib.parse.quote(img_url, safe="%/:=&?~#+!$,;'@()*[]")
            s += '''
            ### Graphs
            ![]({})
            '''.format(img_url)

        # Write file
        with open(file_path, 'w') as f:
            f.write(re.sub('\n[ \t]+', '\n', s).strip())

    @staticmethod
    def generate_frequencies(f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, f_step=DEFAULT_STEP):
        freq_new = []
        # Frequencies from 20kHz down
        f = np.min([20000, f_max])
        while f > f_min:
            freq_new.append(int(round(f)))
            f = f / f_step
        # Frequencies from 20kHZ up
        f = np.min([20000, f_max])
        while f < f_max:
            freq_new.append(int(round(f)))
            f = f * f_step
        freq_new = sorted(set(freq_new))  # Remove duplicates and sort ascending
        return np.array(freq_new)

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
        interpolator = InterpolatedUnivariateSpline(np.log10(self.frequency), self.raw, k=pol_order)

        if f is None:
            self.frequency = self.generate_frequencies(f_min=f_min, f_max=f_max, f_step=f_step)
        else:
            self.frequency = f
        if self.frequency[0] == 0:
            self.frequency[0] = 1  # Prevent log10 from exploding
            self.raw = interpolator(np.log10(self.frequency))
            self.frequency[0] = 0
        else:
            self.raw = interpolator(np.log10(self.frequency))
        # Everything but raw data is affected by interpolating, reset them
        self.reset(raw=False)

    def center(self, frequency=1000):
        """Removed bias from frequency response.

        Args:
            frequency: Frequency which is set to 0 dB. If this is a list with two values then an average between the two
                       frequencies is set to 0 dB.

        Returns:
            Gain shifted
        """
        equal_energy_fr = FrequencyResponse(name='equal_energy', frequency=self.frequency.copy(), raw=self.raw.copy())
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

        # Everything but raw, smoothed and target is affected by centering, reset them
        self.reset(raw=False, smoothed=False, target=False)

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

    def _target(self,
                bass_boost=None,
                bass_boost_f_lower=None,
                bass_boost_f_upper=None,
                tilt=None):
        """Creates target curve with bass boost as described by harman target response.

        Args:
            bass_boost: Bass boost in dB

        Returns:
            Target for equalization
        """
        if bass_boost is not None:
            bass_boost = self._sigmoid(
                f_lower=bass_boost_f_lower,
                f_upper=bass_boost_f_upper,
                a_normal=bass_boost,
                a_treble=0.0
            )
        else:
            bass_boost = np.zeros(len(self.frequency))
        if tilt is not None:
            tilt = self._tilt(tilt=tilt)
        else:
            tilt = np.zeros(len(self.frequency))
        return bass_boost + tilt

    def compensate(self,
                   compensation,
                   bass_boost=None,
                   bass_boost_f_lower=None,
                   bass_boost_f_upper=None,
                   tilt=None,
                   sound_signature=None,
                   min_mean_error=False):
        """Sets target and error curves."""
        # Copy and center compensation data
        compensation = FrequencyResponse(name='compensation', frequency=compensation.frequency, raw=compensation.raw)
        compensation.smoothen_fractional_octave(
            window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
            iterations=DEFAULT_TREBLE_SMOOTHING_ITERATIONS
        )
        compensation.center()
        compensation.raw = compensation.smoothed
        compensation.smoothed = np.array([])

        # Set target
        self.target = compensation.raw + self._target(
            bass_boost=bass_boost,
            bass_boost_f_lower=bass_boost_f_lower,
            bass_boost_f_upper=bass_boost_f_upper,
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
            warnings.simplefilter("ignore")
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
                                   method='max',
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

    def smoothen_heavy_light(self):
        """Smoothens data by combining light and heavy smoothing and taking maximum.

        Returns:
            None
        """
        light = self.copy()
        light.name = 'Light'
        light.smoothen_fractional_octave(
            window_size=1 / 6,
            iterations=1,
            treble_f_lower=100,
            treble_f_upper=10000,
            treble_window_size=1 / 3,
            treble_iterations=1
        )

        heavy = self.copy()
        heavy.name = 'Heavy'
        heavy.smoothen_fractional_octave(
            window_size=1 / 3,
            iterations=1,
            treble_f_lower=1000,
            treble_f_upper=6000,
            treble_window_size=1.3,
            treble_iterations=1
        )

        combination = self.copy()
        combination.name = 'Combination'
        combination.error = np.max(np.vstack([light.error_smoothed, heavy.error_smoothed]), axis=0)
        combination.smoothen_fractional_octave(
            window_size=1 / 3,
            iterations=1,
            treble_f_lower=100,
            treble_f_upper=10000,
            treble_window_size=1 / 3,
            treble_iterations=1
        )

        self.smoothed = combination.smoothed.copy()
        self.error_smoothed = combination.error_smoothed.copy()

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
                 smoothen=True,
                 treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                 treble_f_upper=DEFAULT_TREBLE_F_UPPER,
                 treble_max_gain=DEFAULT_TREBLE_MAX_GAIN,
                 treble_gain_k=DEFAULT_TREBLE_GAIN_K):
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
        self.equalization = []
        self.equalized_raw = []

        if len(self.error_smoothed):
            error = self.error_smoothed
        elif len(self.error):
            error = self.error
        else:
            raise ValueError('Error data is missing. Call FrequencyResponse.compensate().')

        if None in error or None in self.equalization or None in self.equalized_raw:
            # Must not contain None values
            raise ValueError('None values detected during equalization, interpolating data with default parameters.')

        # Invert with max gain clipping
        previous_clipped = False
        kink_inds = []

        # Max gain at each frequency
        max_gain = self._sigmoid(treble_f_lower, treble_f_upper, a_normal=max_gain, a_treble=treble_max_gain)
        gain_k = self._sigmoid(treble_f_lower, treble_f_upper, a_normal=1.0, a_treble=treble_gain_k)
        for i in range(len(error)):
            gain = - error[i] * gain_k[i]
            clipped = gain > max_gain[i]
            if previous_clipped != clipped:
                kink_inds.append(i)
            previous_clipped = clipped
            if clipped:
                gain = max_gain[i]
            self.equalization.append(gain)

        if len(kink_inds) and kink_inds[0] == 0:
            del kink_inds[0]

        if smoothen:
            # Smooth out kinks
            window_size = self._window_size(1 / 12)
            doomed_inds = set()
            for i in kink_inds:
                start = i - min(i, (window_size - 1) // 2)
                end = i + 1 + min(len(self.equalization) - i - 1, (window_size - 1) // 2)
                doomed_inds.update(range(start, end))
            doomed_inds = sorted(doomed_inds)

            for i in range(1, 3):
                if len(self.frequency) - i in doomed_inds:
                    del doomed_inds[doomed_inds.index(len(self.frequency) - i)]

            f = np.array([x for i, x in enumerate(self.frequency) if i not in doomed_inds])
            e = np.array([x for i, x in enumerate(self.equalization) if i not in doomed_inds])
            interpolator = InterpolatedUnivariateSpline(np.log10(f), e, k=2)
            self.equalization = interpolator(np.log10(self.frequency))
        else:
            self.equalization = np.array(self.equalization)

        # Equalized
        self.equalized_raw = self.raw + self.equalization
        if len(self.smoothed):
            self.equalized_smoothed = self.smoothed + self.equalization

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
                   close=False):
        """Plots frequency response graph."""
        if fig is None:
            fig, ax = plt.subplots()
            fig.set_size_inches(12, 8)
        legend = []
        if not len(self.frequency):
            raise ValueError('\'frequency\' has no data!')
        if target and len(self.target):
            ax.plot(self.frequency, self.target, linewidth=5, color='lightblue')
            legend.append('Target')
        if smoothed and len(self.smoothed):
            ax.plot(self.frequency, self.smoothed, linewidth=5, color='lightgrey')
            legend.append('Raw Smoothed')
        if error_smoothed and len(self.error_smoothed):
            ax.plot(self.frequency, self.error_smoothed, linewidth=5, color='pink')
            legend.append('Error Smoothed')
        if raw and len(self.raw):
            ax.plot(self.frequency, self.raw, linewidth=1, color=color)
            legend.append('Raw')
        if error and len(self.error):
            ax.plot(self.frequency, self.error, linewidth=1, color='red')
            legend.append('Error')
        if parametric_eq and len(self.parametric_eq):
            ax.plot(self.frequency, self.parametric_eq, linewidth=5, color='lightgreen')
            legend.append('Parametric Eq')
        if fixed_band_eq and len(self.fixed_band_eq):
            ax.plot(self.frequency, self.fixed_band_eq, linewidth=5, color='limegreen')
            legend.append('Fixed Band Eq')
        if equalization and len(self.equalization):
            ax.plot(self.frequency, self.equalization, linewidth=1, color='darkgreen')
            legend.append('Equalization')
        if equalized and len(self.equalized_raw) and not len(self.equalized_smoothed):
            ax.plot(self.frequency, self.equalized_raw, linewidth=1, color='magenta')
            legend.append('Equalized raw')
        if equalized and len(self.equalized_smoothed):
            ax.plot(self.frequency, self.equalized_smoothed, linewidth=1, color='blue')
            legend.append('Equalized smoothed')

        ax.set_xlabel('Frequency (Hz)')
        ax.semilogx()
        ax.set_xlim([f_min, f_max])
        ax.set_ylabel('Amplitude (dBr)')
        ax.set_ylim([a_min, a_max])
        ax.set_title(self.name)
        ax.legend(legend, fontsize=8)
        ax.grid(True, which='major')
        ax.grid(True, which='minor')
        ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
        if file_path is not None:
            file_path = os.path.abspath(file_path)
            fig.savefig(file_path, dpi=120)
            im = Image.open(file_path)
            im = im.convert('P', palette=Image.ADAPTIVE, colors=60)
            im.save(file_path, optimize=True)
        if show:
            plt.show(fig)
        elif close:
            plt.close(fig)
        return fig, ax

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
                bass_boost=None,
                iem_bass_boost=None,
                tilt=None,
                sound_signature=None,
                max_gain=DEFAULT_MAX_GAIN,
                treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                treble_f_upper=DEFAULT_TREBLE_F_UPPER,
                treble_max_gain=DEFAULT_TREBLE_MAX_GAIN,
                treble_gain_k=DEFAULT_TREBLE_GAIN_K,
                fs=DEFAULT_FS):
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
            bass_boost: Bass boost amount in dB for over-ear headphones.
            iem_bass_boost: Bass boost amount in dB for in-ear headphones.
            tilt: Target frequency response tilt in db / octave
            sound_signature: Sound signature as FrequencyResponse instance. Raw data will be used.
            max_gain: Maximum positive gain in dB
            treble_f_lower: Lower bound for treble transition region
            treble_f_upper: Upper boud for treble transition region
            treble_max_gain: Maximum gain in treble region
            treble_gain_k: Gain coefficient in treble region
            fs: Sampling frequency

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

        # Use either normal bass boost (for on-ears) or iem bass boost
        if bass_boost is not None and iem_bass_boost is not None:
            raise TypeError('"bass_boost" or "iem_bass_boost" can be given but not both')
        elif bass_boost is not None and iem_bass_boost is None:
            bass_boost_f_lower = DEFAULT_OE_BASS_BOOST_F_LOWER
            bass_boost_f_upper = DEFAULT_OE_BASS_BOOST_F_UPPER
        elif iem_bass_boost is not None and bass_boost is None:
            bass_boost = iem_bass_boost
            bass_boost_f_lower = DEFAULT_IE_BASS_BOOST_F_LOWER
            bass_boost_f_upper = DEFAULT_IE_BASS_BOOST_F_UPPER
        else:
            bass_boost = None
            bass_boost_f_lower = None
            bass_boost_f_upper = None

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
                bass_boost=bass_boost,
                bass_boost_f_lower=bass_boost_f_lower,
                bass_boost_f_upper=bass_boost_f_upper,
                tilt=tilt,
                sound_signature=sound_signature,
                min_mean_error=min_mean_error
            )

        # Smooth data
        self.smoothen_heavy_light()

        peq_filters = n_peq_filters = peq_max_gains = fbeq_filters = n_fbeq_filters = nfbeq_max_gains = None
        # Equalize
        if equalize:
            self.equalize(
                max_gain=max_gain,
                smoothen=True,
                treble_f_lower=treble_f_lower,
                treble_f_upper=treble_f_upper,
                treble_max_gain=treble_max_gain,
                treble_gain_k=treble_gain_k
            )
            if parametric_eq:
                # Get the filters
                peq_filters, n_peq_filters, peq_max_gains = self.optimize_parametric_eq(max_filters=max_filters, fs=fs)
            if fixed_band_eq:
                fbeq_filters, n_fbeq_filters, nfbeq_max_gains = self.optimize_fixed_band_eq(fc=fc, q=q, fs=fs)

        return peq_filters, n_peq_filters, peq_max_gains, fbeq_filters, n_fbeq_filters, nfbeq_max_gains

    @staticmethod
    def main(input_dir=None,
             output_dir=None,
             new_only=False,
             standardize_input=False,
             compensation=None,
             equalize=False,
             parametric_eq=False,
             fixed_band_eq=False,
             fc=None,
             q=None,
             ten_band_eq=False,
             max_filters=None,
             fs=DEFAULT_FS,
             bit_depth=DEFAULT_BIT_DEPTH,
             phase=DEFAULT_PHASE,
             f_res=DEFAULT_F_RES,
             bass_boost=None,
             iem_bass_boost=None,
             tilt=None,
             sound_signature=None,
             max_gain=DEFAULT_MAX_GAIN,
             treble_f_lower=DEFAULT_TREBLE_F_LOWER,
             treble_f_upper=DEFAULT_TREBLE_F_UPPER,
             treble_max_gain=DEFAULT_TREBLE_MAX_GAIN,
             treble_gain_k=DEFAULT_TREBLE_GAIN_K,
             show_plot=False):
        """Parses files in input directory and produces equalization results in output directory."""

        start_time = time()

        # Dir paths to absolute
        input_dir = os.path.abspath(input_dir)
        glob_files = glob(os.path.join(input_dir, '**', '*.csv'), recursive=True)
        if len(glob_files) == 0:
            raise FileNotFoundError('No CSV files found in "{}"'.format(input_dir))

        if compensation:
            # Creates FrequencyResponse for compensation data
            compensation_path = os.path.abspath(compensation)
            compensation = FrequencyResponse.read_from_csv(compensation_path)
            compensation.interpolate()
            compensation.center()
        
        if bit_depth == 16:
            bit_depth = "PCM_16"
        elif bit_depth == 24:
            bit_depth = "PCM_24"
        elif bit_depth == 32:
            bit_depth = "PCM_32"
        else:
            raise ValueError('Invalid bit depth. Accepted values are 16, 24 e 32.')

        if sound_signature is not None:
            sound_signature = FrequencyResponse.read_from_csv(sound_signature)
            if len(sound_signature.error) > 0:
                # Error data present, replace raw data with it
                sound_signature.raw = sound_signature.error
            sound_signature.interpolate()
            sound_signature.center()

        n = 0
        n_total = len(list(glob_files))
        for input_file_path in glob_files:
            if output_dir:
                relative_path = os.path.relpath(input_file_path, input_dir)
                output_file_path = os.path.join(output_dir, relative_path)
                if os.path.isfile(output_file_path) and new_only:
                    # Skip file for which result already exists
                    continue
                output_dir_path = os.path.dirname(output_file_path)

            # Read data from input file
            fr = FrequencyResponse.read_from_csv(input_file_path)

            if standardize_input:
                # Overwrite input data in standard sampling and bias
                fr.interpolate()
                fr.center()
                fr.write_to_csv(input_file_path)

            # Process and equalize
            peq_filters, n_peq_filters, peq_max_gains, fbeq_filters, n_fbeq_filters, fbeq_max_gains = fr.process(
                compensation=compensation,
                min_mean_error=True,
                equalize=equalize,
                parametric_eq=parametric_eq,
                fixed_band_eq=fixed_band_eq,
                fc=fc,
                q=q,
                ten_band_eq=ten_band_eq,
                max_filters=max_filters,
                bass_boost=bass_boost,
                iem_bass_boost=iem_bass_boost,
                tilt=tilt,
                sound_signature=sound_signature,
                max_gain=max_gain,
                treble_f_lower=treble_f_lower,
                treble_f_upper=treble_f_upper,
                treble_max_gain=treble_max_gain,
                treble_gain_k=treble_gain_k,
                fs=fs
            )

            if output_dir:
                # Copy relative path to output directory
                if not os.path.isdir(output_dir_path):
                    os.makedirs(output_dir_path, exist_ok=True)

                if equalize:
                    # Write EqualizerAPO GraphicEq settings to file
                    fr.write_eqapo_graphic_eq(output_file_path.replace('.csv', ' GraphicEQ.txt'), normalize=True)
                    if parametric_eq:
                        # Write ParametricEq settings to file
                        fr.write_eqapo_parametric_eq(output_file_path.replace('.csv', ' ParametricEQ.txt'), peq_filters)

                    # Write fixed band eq
                    if fixed_band_eq or ten_band_eq:
                        # Write fixed band eq settings to file
                        fr.write_eqapo_parametric_eq(output_file_path.replace('.csv', ' FixedBandEQ.txt'), fbeq_filters)

                    # Write impulse response as WAV
                    fss = [44100, 48000] if fs in [44100, 48000] else [fs]
                    for _fs in fss:
                        if phase in ['linear', 'both']:
                            # Write linear phase impulse response
                            linear_phase_ir = fr.linear_phase_impulse_response(fs=_fs, f_res=f_res, normalize=True)
                            linear_phase_ir = np.tile(linear_phase_ir, (2, 1)).T
                            sf.write(
                                output_file_path.replace('.csv', ' linear phase {}Hz.wav'.format(_fs)),
                                linear_phase_ir,
                                _fs,
                                bit_depth
                            )
                        if phase in ['minimum', 'both']:
                            # Write minimum phase impulse response
                            minimum_phase_ir = fr.minimum_phase_impulse_response(fs=_fs, f_res=f_res, normalize=True)
                            minimum_phase_ir = np.tile(minimum_phase_ir, (2, 1)).T
                            sf.write(
                                output_file_path.replace('.csv', ' minimum phase {}Hz.wav'.format(_fs)),
                                minimum_phase_ir,
                                _fs,
                                bit_depth
                            )

                # Write results to CSV file
                fr.write_to_csv(output_file_path)

                # Write plots to file and optionally display them
                fr.plot_graph(
                    show=show_plot,
                    close=not show_plot,
                    file_path=output_file_path.replace('.csv', '.png'),
                )

                # Write README.md
                _readme_path = os.path.join(output_dir_path, 'README.md')
                fr.write_readme(
                    _readme_path,
                    max_filters=n_peq_filters,
                    max_gains=peq_max_gains
                )

            elif show_plot:
                fr.plot_graph(show=True, close=False)

            n += 1
            print(f'{n}/{n_total} ({n/n_total*100:.1f}%) {time()-start_time:.0f}s: {fr.name}')

    @staticmethod
    def cli_args():
        """Parses command line arguments."""
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--input_dir', type=str, required=True,
                                help='Path to input data directory. Will look for CSV files in the data directory and '
                                     'recursively in sub-directories.')
        arg_parser.add_argument('--output_dir', type=str, default=argparse.SUPPRESS,
                                help='Path to results directory. Will keep the same relative paths for files found '
                                     'in input_dir.')
        arg_parser.add_argument('--standardize_input', action='store_true',
                                help='Overwrite input data in standardized sampling and bias?')
        arg_parser.add_argument('--new_only', action='store_true',
                                help='Only process input files which don\'t have results in output directory.')
        arg_parser.add_argument('--compensation', type=str,
                                help='File path to CSV containing compensation (target) curve. Compensation is '
                                     'necessary when equalizing because all input data is raw microphone data. See '
                                     '"compensation", "innerfidelity/resources" and "headphonecom/resources".')
        arg_parser.add_argument('--equalize', action='store_true',
                                help='Will run equalization if this parameter exists, no value needed.')
        arg_parser.add_argument('--parametric_eq', action='store_true',
                                help='Will produce parametric eq settings if this parameter exists, no value needed.')
        arg_parser.add_argument('--fixed_band_eq', action='store_true',
                                help='Will produce fixed band eq settings if this parameter exists, no value needed.')
        arg_parser.add_argument('--fc', type=str, help='Comma separated list of center frequencies for fixed band eq.')
        arg_parser.add_argument('--q', type=str, help='Comma separated list of Q values for fixed band eq. If only one '
                                                      'value is passed it is used for all bands.')
        arg_parser.add_argument('--ten_band_eq', action='store_true',
                                help='Shortcut parameter for activating standard ten band eq optimization.')
        arg_parser.add_argument('--max_filters', type=str, default=argparse.SUPPRESS,
                                help='Maximum number of filters for parametric EQ. Multiple cumulative optimization '
                                     'runs can be done by giving multiple filter counts separated by "+". "5+5" would '
                                     'create 10 filters where the first 5 are usable independently from the rest 5 and '
                                     'the last 5 can only be used with the first 5. This allows to have muliple '
                                     'configurations for equalizers with different number of bands available. '
                                     'Not limited by default.')
        arg_parser.add_argument('--fs', type=int, default=DEFAULT_FS,
                                help='Sampling frequency for impulse response and parametric eq filters. '
                                     'Defaults to {}.'.format(DEFAULT_FS))
        arg_parser.add_argument('--bit_depth', type=int, default=DEFAULT_BIT_DEPTH,
                                help='Number of bits for every sample in impulse response. '
                                     'Defaults to {}.'.format(DEFAULT_BIT_DEPTH))
        arg_parser.add_argument('--phase', type=str, default=DEFAULT_PHASE,
                                help='Impulse response phase characteristic. "minimum", "linear" or "both". '
                                     'Defaults to "{}"'.format(DEFAULT_PHASE))
        arg_parser.add_argument('--f_res', type=float, default=DEFAULT_F_RES,
                                help='Frequency resolution for impulse responses. If this is 20 then impulse response '
                                     'frequency domain will be sampled every 20 Hz. Filter length for '
                                     'impulse responses will be fs/f_res. Defaults to {}.'.format(DEFAULT_F_RES))
        arg_parser.add_argument('--bass_boost', type=float, default=argparse.SUPPRESS,
                                help='Target gain for sub-bass in dB. Has sigmoid slope down from {f_min} Hz to '
                                     '{f_max} Hz. "--bass_boost" is mutually exclusive with "--iem_bass_boost".'.format(
                                        f_min=DEFAULT_OE_BASS_BOOST_F_LOWER,
                                        f_max=DEFAULT_OE_BASS_BOOST_F_UPPER
                                     )
                                )
        arg_parser.add_argument('--iem_bass_boost', type=float, default=argparse.SUPPRESS,
                                help='Target gain for sub-bass in dB. Has sigmoid slope down from {f_min} Hz to '
                                     '{f_max} Hz. "--iem_bass_boost" is mutually exclusive with "--bass_boost".'.format(
                                        f_min=DEFAULT_IE_BASS_BOOST_F_LOWER,
                                        f_max=DEFAULT_IE_BASS_BOOST_F_UPPER
                                     )
                                )
        arg_parser.add_argument('--tilt', type=float, default=argparse.SUPPRESS,
                                help='Target tilt in dB/octave. Positive value (upwards slope) will result in brighter '
                                     'frequency response and negative value (downwards slope) will result in darker '
                                     'frequency response. 1 dB/octave will produce nearly 10 dB difference in '
                                     'desired value between 20 Hz and 20 kHz. Tilt is applied with bass boost and both '
                                     'will affect the bass gain.')
        arg_parser.add_argument('--sound_signature', type=str,
                                help='File path to a sound signature CSV file. The CSV file must be in an AutoEQ '
                                     'understandable format. Error data will be used as the sound signature target if '
                                     'the CSV file contains an error column and otherwise the raw column will be used. '
                                     'This means there are two different options for using sound signature: 1st is '
                                     'pointing it to a result CSV file of a previous run and the 2nd is to create a '
                                     'CSV file with just frequency and raw columns by hand (or other means). The Sound '
                                     'signature graph will be interpolated so any number of point at any frequencies '
                                     'will do, making it easy to create simple signatures with as little as two or '
                                     'three points.')
        arg_parser.add_argument('--max_gain', type=float, default=DEFAULT_MAX_GAIN,
                                help='Maximum positive gain in equalization. Higher max gain allows to equalize deeper '
                                     'dips in  frequency response but will limit output volume if no analog gain is '
                                     'available because positive gain requires negative digital preamp equal to '
                                     'maximum positive gain. Defaults to {}.'.format(DEFAULT_MAX_GAIN))
        arg_parser.add_argument('--treble_f_lower', type=float, default=DEFAULT_TREBLE_F_LOWER,
                                help='Lower bound for transition region between normal and treble frequencies. Treble '
                                     'frequencies can have different max gain and gain K. Defaults to '
                                     '{}.'.format(DEFAULT_TREBLE_F_LOWER))
        arg_parser.add_argument('--treble_f_upper', type=float, default=DEFAULT_TREBLE_F_UPPER,
                                help='Upper bound for transition region between normal and treble frequencies. Treble '
                                     'frequencies can have different max gain and gain K. Defaults to '
                                     '{}.'.format(DEFAULT_TREBLE_F_UPPER))
        arg_parser.add_argument('--treble_max_gain', type=float, default=DEFAULT_TREBLE_MAX_GAIN,
                                help='Maximum positive gain for equalization in treble region. Defaults to '
                                     '{}.'.format(DEFAULT_TREBLE_MAX_GAIN))
        arg_parser.add_argument('--treble_gain_k', type=float, default=DEFAULT_TREBLE_GAIN_K,
                                help='Coefficient for treble gain, affects both positive and negative gain. Useful for '
                                     'disabling or reducing equalization power in treble region. Defaults to '
                                     '{}.'.format(DEFAULT_TREBLE_GAIN_K))
        arg_parser.add_argument('--show_plot', action='store_true',
                                help='Plot will be shown if this parameter exists, no value needed.')
        args = vars(arg_parser.parse_args())
        if 'bass_boost' in args and 'iem_bass_boost' in args:
            raise TypeError('"--bass_boost" or "--iem_bass_boost" can be given but not both')
        if 'max_filters' in args:
            args['max_filters'] = [int(x) for x in args['max_filters'].split('+')]
        if 'fc' in args and args['fc'] is not None:
            args['fc'] = [float(x) for x in args['fc'].split(',')]
        if 'q' in args and args['q'] is not None:
            args['q'] = [float(x) for x in args['q'].split(',')]
        return args


if __name__ == '__main__':
    FrequencyResponse.main(**FrequencyResponse.cli_args())
