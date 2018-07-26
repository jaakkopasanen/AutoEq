# -*- coding: utf-8 -*_

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import argparse
import math
import pandas as pd
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.signal import savgol_filter
from scipy.special import expit
import numpy as np
from glob import glob
import urllib
from warnings import warn
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_F_MIN = 20
DEFAULT_F_MAX = 20000
DEFAULT_STEP = 1.01
DEFAULT_MAX_GAIN = 6.0
DEFAULT_TREBLE_F_LOWER = 6000.0
DEFAULT_TREBLE_F_UPPER = 8000.0
DEFAULT_TREBLE_MAX_GAIN = 0.0
DEFAULT_TREBLE_GAIN_K = 1.0
DEFAULT_BASS_BOOST = 0.0
DEFAULT_SMOOTHING_WINDOW_SIZE = 1/7
DEFAULT_SMOOTHING_ITERATIONS = 10
DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE = 1/5
DEFAULT_TREBLE_SMOOTHING_ITERATIONS = 100
DEFAULT_TILT = 0.0
DEFAULT_COMPENSATION_FILE_PATH = os.path.join(
    'innerfidelity',
    'resources',
    'innerfidelity_compensation_SBAF-Serious.brighter.csv'
)
BASS_BOOST_F_LOWER = 60
BASS_BOOST_F_UPPER = 200
GRAPHIC_EQ_STEP = 1.07


class FrequencyResponse:
    def __init__(self,
                 name=None,
                 frequency=None,
                 raw=None,
                 error=None,
                 smoothed=None,
                 error_smoothed=None,
                 equalization=None,
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
        self.equalized_raw = self._init_data(equalized_raw)
        self.equalized_smoothed = self._init_data(equalized_smoothed)
        self.target = self._init_data(target)

        self._sort()

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
              equalized_raw=True,
              equalized_smoothed=True,
              target=True):
        """Resets data."""
        if (
                (raw and len(self.raw)) or
                (smoothed and len(self.smoothed)) or
                (error and len(self.error)) or
                (error_smoothed and len(self.error_smoothed)) or
                (equalization and len(self.equalization)) or
                (equalized_raw and len(self.equalized_raw)) or
                (equalized_smoothed and len(self.equalized_smoothed)) or
                (target and len(self.target))
        ):
            warn('Resetting data, existing results will be affected!')
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

        df = pd.read_csv(file_path, sep=',', header=0)
        frequency = list(df['frequency']) if 'frequency' in df else None
        raw = list(df['raw']) if 'raw' in df else None
        error = list(df['error']) if 'error' in df else None
        smoothed = list(df['smoothed']) if 'smoothed' in df else None
        equalization = list(df['equalization']) if 'equalization' in df else None
        equalized_raw = list(df['equalized_raw']) if 'equalized_raw' in df else None
        equalized_smoothed = list(df['equalized_smoothed']) if 'equalized_smoothed' in df else None
        target = list(df['target']) if 'target' in df else None

        return cls(
            name=name,
            frequency=frequency,
            raw=raw,
            error=error,
            smoothed=smoothed,
            equalization=equalization,
            equalized_raw=equalized_raw,
            equalized_smoothed=equalized_smoothed,
            target=target
        )

    def write_to_csv(self, file_path=None):
        """Writes data to files as CSV."""
        file_path = os.path.abspath(file_path)
        df = pd.DataFrame()
        if len(self.frequency):
            df['frequency'] = self.frequency
        if len(self.raw):
            df['raw'] = [x if x is not None else 'NaN' for x in self.raw]
        if len(self.error):
            df['error'] = [x if x is not None else 'NaN' for x in self.error]
        if len(self.smoothed):
            df['smoothed'] = [x if x is not None else 'NaN' for x in self.smoothed]
        if len(self.error_smoothed):
            df['error_smoothed'] = [x if x is not None else 'NaN' for x in self.error_smoothed]
        if len(self.equalization):
            df['equalization'] = [x if x is not None else 'NaN' for x in self.equalization]
        if len(self.equalized_raw):
            df['equalized_raw'] = [x if x is not None else 'NaN' for x in self.equalized_raw]
        if len(self.equalized_smoothed):
            df['equalized_smoothed'] = [x if x is not None else 'NaN' for x in self.equalized_smoothed]
        if len(self.target):
            df['target'] = [x if x is not None else 'NaN' for x in self.target]
        df.to_csv(file_path, header=True, index=False)

    def write_eqapo_graphic_eq(self, file_path):
        """Writes equalization graph to a file as Equalizer APO config."""
        file_path = os.path.abspath(file_path)

        fr = FrequencyResponse(name='hack', frequency=self.frequency, raw=self.equalization)
        fr.interpolate(f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, f_step=GRAPHIC_EQ_STEP)

        with open(file_path, 'w') as f:
            s = '; '.join(['{f} {a:.1f}'.format(f=f, a=a) for f, a in zip(fr.frequency, fr.raw)])
            s = 'GraphicEQ: 10 -84; ' + s
            f.write(s)
        return s

    def _split_path(self, path):
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

    def write_readme(self, file_path):
        """Writes README.md with picture and Equalizer APO settings."""
        file_path = os.path.abspath(file_path)
        dir_path = os.path.dirname(file_path)
        model = os.path.split(dir_path)[-1]

        lines = ['# ' + model]

        # Write GraphicEQ settings
        graphic_eq_path = os.path.join(dir_path, model + ' GraphicEQ.txt')
        if os.path.isfile(graphic_eq_path):
            preamp = min(0.0, float(-np.max(self.equalization)))
            with open(graphic_eq_path, 'r') as f:
                eq_str = f.read().strip()

            lines.append('### EqualizerAPO GraphicEQ')
            lines.append('If you are using HeSuVi, replace contents of HeSuVi\'s eq file '
                         '`C:\\Program Files\\EqualizerAPO\\config\\HeSuVi\\eq.txt` with this line and set global '
                         'volume for both channels from HeSuVi UI to {:.0f}.'.format(preamp*10))
            lines.append('```')
            lines.append(eq_str)
            lines.append('```')

            lines.append('If you are not using HeSuVi, copy this to end of EqualizerAPO configuration file '
                         '`C:\\Program Files\\EqualizerAPO\\config\\config.txt`.')
            lines.append('```')
            lines.append(eq_str)
            lines.append('Copy: L={preamp:.1f}dB*l, R={preamp:.1f}dB*R'.format(preamp=preamp))
            lines.append('```')
            lines.append('EqualizerAPO Peace GUI does not work with GraphicEQ so you have to disable parametric '
                         'equalization configured by Peace if you are already using Peace.')

        # Write image link
        img_path = os.path.join(dir_path, model + '.png')
        if os.path.isfile(img_path):
            img_rel_path = os.path.relpath(img_path, ROOT_DIR)
            img_url = '/'.join(self._split_path(img_rel_path))
            img_url = 'https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/{}'.format(img_url)
            img_url = urllib.parse.quote(img_url, safe="%/:=&?~#+!$,;'@()*[]")
            lines.append('![]({})'.format(img_url))

        # Write file
        with open(file_path, 'w') as f:
            f.write('\n'.join(lines) + '\n')

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
        self.raw = interpolator(np.log10(self.frequency))
        # Everything but raw data is affected by interpolating, reset them
        self.reset(raw=False)

    def calibrate(self, calibration):
        """Calibrates measurement to match calibration. Changes raw data."""
        self.raw -= calibration.raw
        # Everything but raw data is affected by calibrating, reset them
        self.reset(raw=False)

    def center(self):
        """Removed bias from frequency response."""
        interpolator = InterpolatedUnivariateSpline(np.log10(self.frequency), self.raw, k=1)
        diff = interpolator(np.log10(1000))
        self.raw -= diff
        if len(self.smoothed):
            self.smoothed -= diff
        # Everything but raw, smoothed and target is affected by centering, reset them
        self.reset(raw=False, smoothed=False, target=False)

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

    def _target(self, bass_boost=DEFAULT_BASS_BOOST, tilt=DEFAULT_TILT):
        """Creates target curve with bass boost as described by harman target response.

        Args:
            bass_boost: Bass boost in dB

        Returns:
            Target for equalization
        """
        bass_boost = self._sigmoid(
            f_lower=BASS_BOOST_F_LOWER,
            f_upper=BASS_BOOST_F_UPPER,
            a_normal=bass_boost,
            a_treble=0.0
        )
        tilt = self._tilt(tilt=tilt)
        return bass_boost + tilt

    def compensate(self, compensation, bass_boost=DEFAULT_BASS_BOOST, tilt=DEFAULT_TILT):
        """Calibrates raw frequency response data with compensation array. Doesn't change raw data."""
        # Copy and center compensation data
        compensation = FrequencyResponse(name='compensation', frequency=compensation.frequency, raw=compensation.raw)
        compensation.smoothen(
            window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
            iterations=DEFAULT_TREBLE_SMOOTHING_ITERATIONS
        )
        compensation.center()
        compensation.raw = compensation.smoothed
        compensation.smoothed = np.array([])
        # Set target
        self.target = compensation.raw + self._target(bass_boost=bass_boost, tilt=tilt)
        # Set error
        self.error = self.raw - self.target
        # Smoothed error and equalization results are affected by compensation, reset them
        self.reset(
            raw=False,
            smoothed=False,
            error=False,
            error_smoothed=True,
            equalization=True,
            equalized_raw=True,
            equalized_smoothed=True,
            target=False
        )

    def _window_size(self, octaves):
        """Calculates moving average window size in indices from octaves."""
        # Octaves to coefficient
        k = 2**octaves
        # Calculate average step size in frequencies
        steps = []
        for i in range(1, len(self.frequency)):
            steps.append(self.frequency[i] / self.frequency[i-1])
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

    def _smoothen_data(self,
                       data,
                       window_size=DEFAULT_SMOOTHING_WINDOW_SIZE,
                       iterations=DEFAULT_SMOOTHING_ITERATIONS,
                       treble_window_size=None,
                       treble_iterations=None,
                       treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                       treble_f_upper=DEFAULT_TREBLE_F_UPPER):
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
        for _ in range(iterations):
            y_normal = savgol_filter(y_normal, self._window_size(window_size), 2)

        # Treble filter
        y_treble = data
        for _ in range(treble_iterations):
            y_treble = savgol_filter(y_treble, self._window_size(treble_window_size), 2)

        # Transition weighted with sigmoid
        k_treble = self._sigmoid(treble_f_lower, treble_f_upper)
        k_normal = k_treble * -1 + 1
        return y_normal * k_normal + y_treble * k_treble

    def smoothen(self,
                 window_size=DEFAULT_SMOOTHING_WINDOW_SIZE,
                 iterations=DEFAULT_SMOOTHING_ITERATIONS,
                 treble_window_size=None,
                 treble_iterations=None,
                 treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                 treble_f_upper=DEFAULT_TREBLE_F_UPPER):
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

        # Use normal filter parameters for treble filter if treble filter parameters are not given
        if treble_window_size is None:
            treble_window_size = window_size
        if treble_iterations is None:
            treble_iterations = iterations

        # Smoothen raw data
        self.smoothed = self._smoothen_data(
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
            self.error_smoothed = self._smoothen_data(
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
            window_size: Smoothing average window size in octaves
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
            warn('None values detected during equalization, interpolating data with default parameters.')
            self.interpolate()

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
            window_size = self._window_size(1/12)
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
                   equalized=True,
                   target=True,
                   file_path=None,
                   f_min=DEFAULT_F_MIN,
                   f_max=DEFAULT_F_MAX,
                   a_min=None,
                   a_max=None,
                   color='black'):
        """Plots frequency response graph."""
        if fig is None:
            fig, ax = plt.subplots()
        legend = []
        if not len(self.frequency):
            raise ValueError('\'frequency\' has no data!')
        if target and len(self.target):
            plt.plot(self.frequency, self.target, linewidth=5, color='lightblue')
            legend.append('Target')
        if smoothed and len(self.smoothed):
            plt.plot(self.frequency, self.smoothed, linewidth=5, color='lightgrey')
            legend.append('Raw Smoothed')
        if error_smoothed and len(self.error_smoothed):
            plt.plot(self.frequency, self.error_smoothed, linewidth=5, color='pink')
            legend.append('Error Smoothed')
        if raw and len(self.raw):
            plt.plot(self.frequency, self.raw, linewidth=1, color=color)
            legend.append('Raw')
        if error and len(self.error):
            plt.plot(self.frequency, self.error, linewidth=1, color='red')
            legend.append('Error')
        if equalization and len(self.equalization):
            plt.plot(self.frequency, self.equalization, linewidth=2, color='limegreen')
            legend.append('Equalization')
        if equalized and len(self.equalized_raw) and not len(self.equalized_smoothed):
            plt.plot(self.frequency, self.equalized_raw, linewidth=1, color='magenta')
            legend.append('Equalized raw')
        if equalized and len(self.equalized_smoothed):
            plt.plot(self.frequency, self.equalized_smoothed, linewidth=1, color='darkblue')
            legend.append('Equalized smoothed')

        plt.xlabel('Frequency (Hz)')
        plt.semilogx()
        plt.xlim([f_min, f_max])
        plt.ylabel('Amplitude (dBr)')
        plt.ylim([a_min, a_max])
        plt.title(self.name)
        plt.legend(legend, fontsize=8)
        plt.grid(True, which='major')
        plt.grid(True, which='minor')
        ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
        if file_path is not None:
            file_path = os.path.abspath(file_path)
            fig.savefig(file_path, dpi=240)
        if show:
            plt.show()
        return fig, ax

    @staticmethod
    def cli_args():
        """Parses command line arguments."""
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--input_dir', type=str, required=True,
                                help='Path to data directory. Will look for csv files in the data directory and '
                                     'recursively in sub-directories.')
        arg_parser.add_argument('--output_dir', type=str, required=True,
                                help='Path to results directory. Will keep the same relative paths for files found'
                                     'in input_dir.')
        arg_parser.add_argument('--calibration', type=str, required=False, default=argparse.SUPPRESS,
                                help='File path to CSV containing calibration curve.')
        arg_parser.add_argument('--compensation', type=str, required=False, default=DEFAULT_COMPENSATION_FILE_PATH,
                                help='File path to CSV containing compensation curve. Compensation is necessary when '
                                     'equalizing because all input data is raw microphone data. See '
                                     'innerfidelity/resources and headphonecom/resources. '
                                     'Defaults to "{}"'.format(DEFAULT_COMPENSATION_FILE_PATH))
        arg_parser.add_argument('--equalize', action='store_true',
                                help='Will run equalization if this parameter exists, no value needed.')
        arg_parser.add_argument('--bass_boost', type=float, default=DEFAULT_BASS_BOOST,
                                help='Target gain for sub-bass in dB. Flat response from 20 Hz to 60 Hz and a sigmoid '
                                     'slope down to 200 Hz. Defaults to {}'.format(DEFAULT_BASS_BOOST))
        arg_parser.add_argument('--tilt', type=float, default=DEFAULT_TILT,
                                help='Target tilt in dB/octave. Positive value (upwards slope) will result in brighter '
                                     'frequency response and negative value (downwards slope) will result in darker '
                                     'frequency response. 1 dB/octave will produce nearly 10 dB difference between '
                                     'desired value between 20 Hz and 20 kHz. Tilt is applied with bass boost and both '
                                     'will affect the bass gain. Defaults to {}'.format(DEFAULT_TILT))
        arg_parser.add_argument('--max_gain', type=float, default=DEFAULT_MAX_GAIN,
                                help='Maximum positive gain in equalization. Higher max gain allows to equalize deeper '
                                     'dips in  frequency response but will limit output volume if no analog gain is '
                                     'available because positive gain requires negative digital preamp equal to '
                                     'maximum positive gain. Defaults to {}'.format(DEFAULT_MAX_GAIN))
        arg_parser.add_argument('--treble_f_lower', type=float, default=DEFAULT_TREBLE_F_LOWER,
                                help='Lower bound for transition region between normal and treble frequencies. Treble '
                                     'frequencies can have different smoothing, max gain and gain K. Defaults to '
                                     '{}'.format(DEFAULT_TREBLE_F_LOWER))
        arg_parser.add_argument('--treble_f_upper', type=float, default=DEFAULT_TREBLE_F_UPPER,
                                help='Upper bound for transition region between normal and treble frequencies. Treble '
                                     'frequencies can have different smoothing, max gain and gain K. Defaults to '
                                     '{}'.format(DEFAULT_TREBLE_F_UPPER))
        arg_parser.add_argument('--treble_max_gain', type=float, default=DEFAULT_TREBLE_MAX_GAIN,
                                help='Maximum positive gain for equalization in treble region. Defaults to '
                                     '{}'.format(DEFAULT_TREBLE_MAX_GAIN))
        arg_parser.add_argument('--treble_gain_k', type=float, default=DEFAULT_TREBLE_GAIN_K,
                                help='Coefficient for treble gain, affects both positive and negative gain. Useful for '
                                     'disbling or reducing equalization power in treble region. Defaults to '
                                     '{}.'.format(DEFAULT_TREBLE_GAIN_K))
        arg_parser.add_argument('--show_plot', action='store_true', default=False,
                                help='Plot will be shown if this parameter exists, no value needed.')
        return vars(arg_parser.parse_args())

    @staticmethod
    def main(input_dir=None,
             output_dir=None,
             calibration=None,
             compensation=None,
             equalize=False,
             bass_boost=DEFAULT_BASS_BOOST,
             tilt=DEFAULT_TILT,
             max_gain=DEFAULT_MAX_GAIN,
             treble_f_lower=DEFAULT_TREBLE_F_LOWER,
             treble_f_upper=DEFAULT_TREBLE_F_UPPER,
             treble_max_gain=DEFAULT_TREBLE_MAX_GAIN,
             treble_gain_k=DEFAULT_TREBLE_GAIN_K,
             show_plot=False):
        """Parses files in input directory and produces equalization results in output directory."""
        if calibration:
            # Creates FrequencyReponse for compensation data
            calibration_path = os.path.abspath(calibration)
            calibration = FrequencyResponse.read_from_csv(calibration_path)
            calibration.interpolate()
            calibration.center()

        if compensation:
            # Creates FrequencyReponse for compensation data
            compensation_path = os.path.abspath(compensation)
            compensation = FrequencyResponse.read_from_csv(compensation_path)
            compensation.interpolate()
            compensation.center()

        # Dir paths to absolute
        input_dir = os.path.abspath(input_dir)
        output_dir = os.path.abspath(output_dir)
        glob_files = glob(os.path.join(input_dir, '**', '*.csv'), recursive=True)
        if len(glob_files) == 0:
            warn('No CSV files found in "{}"'.format(input_dir))
            return

        readme_path = os.path.join(output_dir, 'README.md')
        readme_occupied = False

        for file_path in glob_files:
            # Read data from input file
            fr = FrequencyResponse.read_from_csv(file_path)

            # Copy relative path to output directory
            relative_path = os.path.relpath(file_path, input_dir)
            file_path = os.path.join(output_dir, relative_path)
            dir_path = os.path.dirname(file_path)
            if not os.path.isdir(dir_path):
                os.makedirs(dir_path, exist_ok=True)

            # Interpolate to standard frequency vector
            fr.interpolate()

            if calibration is not None:
                # Calibrate
                fr.calibrate(calibration)

            # Center by 1kHz
            fr.center()

            if compensation is not None:
                # Compensate
                fr.compensate(compensation, bass_boost=bass_boost, tilt=tilt)

            # Smooth data
            fr.smoothen(
                window_size=DEFAULT_SMOOTHING_WINDOW_SIZE,
                iterations=DEFAULT_SMOOTHING_ITERATIONS,
                treble_window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
                treble_iterations=DEFAULT_TREBLE_SMOOTHING_ITERATIONS,
                treble_f_lower=treble_f_lower,
                treble_f_upper=treble_f_upper
            )

            # Equalize
            if equalize:
                fr.equalize(
                    max_gain=max_gain,
                    smoothen=True,
                    treble_f_lower=treble_f_lower,
                    treble_f_upper=treble_f_upper,
                    treble_max_gain=treble_max_gain,
                    treble_gain_k=treble_gain_k
                )

            if output_dir:
                # Write results to CSV file
                fr.write_to_csv(file_path)
                # Write plots to file and optionally display them
                fig, ax = fr.plot_graph(
                    show=show_plot,
                    file_path=file_path.replace('.csv', '.png'),
                )
                plt.close(fig)

                if equalize:
                    # Write EqualizerAPO settings to file
                    fr.write_eqapo_graphic_eq(file_path.replace('.csv', ' GraphicEQ.txt'))
                    print('Equalized "{}"'.format(fr.name))

                # Write README.md
                _readme_path = os.path.join(dir_path, 'README.md')
                fr.write_readme(_readme_path)
                if _readme_path == readme_path:
                    readme_occupied = True

            elif show_plot:
                fig, ax = fr.plot_graph(show=show_plot)
                plt.close(fig)

        lines = ['# Run {}'.format(datetime.now().isoformat())]
        lines.append('There results were obtained with parameters:')
        lines.append('* `--input_dir="{}"`'.format(os.path.relpath(input_dir, ROOT_DIR)))
        lines.append('* `--output_dir="{}"`'.format(os.path.relpath(output_dir, ROOT_DIR)))
        if calibration is not None:
            lines.append('* `--calibration="{}"`'.format(os.path.relpath(calibration_path, ROOT_DIR)))
        if compensation is not None:
            lines.append('* `--compensation="{}"`'.format(os.path.relpath(compensation_path, ROOT_DIR)))
        lines.append('* `--bass_boost={}`'.format(bass_boost))
        lines.append('* `--tilt={}`'.format(tilt))
        lines.append('* `--max_gain={}`'.format(max_gain))
        lines.append('* `--treble_f_lower={}`'.format(treble_f_lower))
        lines.append('* `--treble_f_upper={}`'.format(treble_f_upper))
        lines.append('* `--treble_max_gain={}`'.format(treble_max_gain))
        lines.append('* `--treble_gain_k={}`'.format(treble_gain_k))

        # Write parameters to run README.md
        if readme_occupied:
            print('append')
            # Directory already contains a README.md written for a single headphone
            # Add to the end of the README
            with open(readme_path, 'a') as f:
                f.write('\n' + '\n'.join(lines))
        else:
            print('write')
            # README.md doesn't exist or old README.md from previous run, safe to overwrite
            with open(readme_path, 'w') as f:
                f.write('\n'.join(lines))


if __name__ == '__main__':
    FrequencyResponse.main(**FrequencyResponse.cli_args())
