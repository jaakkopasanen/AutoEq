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
import shutil
from time import time


class FrequencyResponse:
    def __init__(self,
                 name=None,
                 frequency=None,
                 raw=None,
                 error=None,
                 smoothed=None,
                 equalization=None,
                 equalized_raw=None,
                 equalized_smoothed=None):
        self.name = name.strip()

        self.frequency = frequency if frequency is not None else self.generate_frequencies()
        self.frequency = [None if x is None or math.isnan(x) else x for x in self.frequency]
        self.frequency = np.array(self.frequency)

        self.raw = raw if raw is not None else []
        self.raw = [None if x is None or math.isnan(x) or x is None else x for x in self.raw]
        self.raw = np.array(self.raw)

        self.error = error if error is not None else []
        self.error = [None if x is None or math.isnan(x) or x is None else x for x in self.error]
        self.error = np.array(self.error)

        self.smoothed = smoothed if smoothed is not None else []
        self.smoothed = np.array(self.smoothed)

        self.equalization = equalization if equalization is not None else []
        self.equalization = [None if x is None or math.isnan(x) or x is None else x for x in self.equalization]
        self.equalization = np.array(self.equalization)

        self.equalized_raw = equalized_raw if equalized_raw is not None else []
        self.equalized_raw = [None if x is None or math.isnan(x) else x for x in self.equalized_raw]
        self.equalized_raw = np.array(self.equalized_raw)

        self.equalized_smoothed = equalized_smoothed if equalized_smoothed is not None else []
        self.equalized_smoothed = [None if x is None or math.isnan(x) else x for x in self.equalized_smoothed]
        self.equalized_smoothed = np.array(self.equalized_smoothed)

        self.target = np.array([])
        self.rounded_frequencies = np.array([])
        self.rounded_equalization = np.array([])

        self._sort()

    def _sort(self):
        sorted_inds = self.frequency.argsort()
        self.frequency = self.frequency[sorted_inds]
        if len(self.raw):
            self.raw = self.raw[sorted_inds]
        if len(self.error):
            self.error = self.error[sorted_inds]
        if len(self.smoothed):
            self.smoothed = self.smoothed[sorted_inds]
        if len(self.equalization):
            self.equalization = self.equalization[sorted_inds]
        if len(self.equalized_raw):
            self.equalized_raw = self.equalized_raw[sorted_inds]
        if len(self.equalized_smoothed):
            self.equalized_smoothed = self.equalized_smoothed[sorted_inds]

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

        return cls(
            name=name,
            frequency=frequency,
            raw=raw,
            error=error,
            smoothed=smoothed,
            equalization=equalization,
            equalized_raw=equalized_raw,
            equalized_smoothed=equalized_smoothed
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
        if len(self.equalization):
            df['equalization'] = [x if x is not None else 'NaN' for x in self.equalization]
        if len(self.equalized_raw):
            df['equalized_raw'] = [x if x is not None else 'NaN' for x in self.equalized_raw]
        if len(self.equalized_smoothed):
            df['equalized_smoothed'] = [x if x is not None else 'NaN' for x in self.equalized_smoothed]
        df.to_csv(file_path, header=True, index=False)

    def write_eqapo_graphic_eq(self, file_path):
        """Writes equalization graph to a file as Equalizer APO config."""
        file_path = os.path.abspath(file_path)

        fr = FrequencyResponse(name='hack', frequency=self.frequency, raw=self.equalization)
        fr.interpolate(f_min=20, f_max=20000, f_step=1.07)

        with open(file_path, 'w') as f:
            s = '; '.join(['{f} {a:.1f}'.format(f=f, a=a) for f, a in zip(fr.frequency, fr.raw)])
            s = 'GraphicEQ: 10 -84; ' + s
            f.write(s)
        return s

    @staticmethod
    def generate_frequencies(f_min=20, f_max=20000, f_step=1.01):
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

    def interpolate(self, f=None, f_step=1.01, pol_order=1, f_min=20, f_max=20000):
        """Interpolates missing values from previous and next value."""
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

    def center(self):
        """Removed bias from frequency response."""
        interpolator = InterpolatedUnivariateSpline(np.log10(self.frequency), self.raw, k=1)
        diff = interpolator(np.log10(1000))
        self.raw -= diff
        self.error -= diff
        self.smoothed -= diff
        self.equalization -= diff
        self.equalized_raw -= diff
        self.equalized_smoothed -= diff

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

    def smooth(self,
               window_size=1/5,
               iterations=1,
               treble_window_size=None,
               treble_iterations=None,
               treble_f_lower=6000,
               treble_f_upper=10000):
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

        # Use error data if available
        data = self.error if len(self.error) else self.raw

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
        self.smoothed = y_normal * k_normal + y_treble * k_treble

    def compensate(self, compensation):
        """Calibrates raw frequency response data with compensation array. Doesn't change raw data."""
        error_new = self.raw - compensation.raw
        if len(self.error):
            # Already error, calculate difference between new and old compensation
            diff = error_new - self.error
            self.smoothed -= diff
            self.equalization -= diff
            self.equalized_raw -= diff
            self.equalized_smoothed -= diff
        self.error = error_new

    def calibrate(self, calibration):
        """Calibrates measurement to match calibration. Changes raw data."""
        error_new = self.raw - calibration.raw
        if len(self.error):
            # Already error, calculate difference between new and old compensation
            diff = error_new - self.error
            self.error = error_new
            self.smoothed -= diff
            self.equalization -= diff
            self.equalized_raw -= diff
            self.equalized_smoothed -= diff
        self.raw -= calibration.raw

    def _target(self, bass_boost=4):
        """Creates target curve with bass boost as described by harman target response.

        Args:
            bass_boost: Bass boost in dB

        Returns:
            Target for equalization
        """
        f_bass = self.frequency[self.frequency < 60]
        f_highs = self.frequency[200 <= self.frequency]
        f_bm = np.concatenate([f_bass, f_highs], axis=0)

        a_bass = np.ones([len(f_bass)]) * bass_boost
        a_mids = np.zeros([len(f_highs)])
        a_bm = np.concatenate([a_bass, a_mids], axis=0)

        interpolator = InterpolatedUnivariateSpline(np.log10(f_bm), a_bm, k=3)
        return interpolator(np.log10(self.frequency))

    def equalize(self,
                 max_gain=12,
                 smooth=True,
                 window_size=1/3,
                 bass_target=4,
                 treble_f_lower=6000,
                 treble_f_upper=10000,
                 treble_max_gain=0,
                 treble_gain_k=1.0):
        """Creates equalization curve and equalized curve.

        Args:
            max_gain: Maximum positive gain in dB
            smooth: Smooth kinks caused by clipping gain to max gain?
            window_size: Smoothing average window size in octaves
            bass_target: Target value in dB for bass boost
            treble_f_lower: Lower frequency boundary for transition region between normal parameters and treble parameters
            treble_f_upper: Upper frequency boundary for transition reqion between normal parameters and treble parameters
            treble_max_gain: Maximum positive gain in dB in treble region
            treble_gain_k: Coefficient for treble gain, positive and negative. Useful for disbling or reducing \
                           equalization power in treble region. Defaults to 1.0 (not limited).
        """
        self.equalization = []
        self.equalized_raw = []

        if len(self.smoothed):
            data = self.smoothed
        elif len(self.error):
            data = self.error
        else:
            data = self.raw

        if None in data or None in self.equalization or None in self.equalized_raw:
            # Must not contain None values
            self.interpolate()

        # Invert with max gain clipping
        previous_clipped = False
        kink_inds = []
        self.target = self._target(bass_boost=bass_target)
        # Max gain at each frequency
        max_gain = self._sigmoid(treble_f_lower, treble_f_upper, a_normal=max_gain, a_treble=treble_max_gain)
        gain_k = self._sigmoid(treble_f_lower, treble_f_upper, a_normal=1.0, a_treble=treble_gain_k)
        for i, a in enumerate(data):
            gain = (self.target[i] - a) * gain_k[i]
            clipped = gain > max_gain[i]
            if previous_clipped != clipped:
                kink_inds.append(i)
            previous_clipped = clipped
            if clipped:
                gain = max_gain[i]
            self.equalization.append(gain)

        if len(kink_inds) and kink_inds[0] == 0:
            del kink_inds[0]

        if smooth:
            # Smooth out kinks
            window_size = self._window_size(window_size)
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
            self.rounded_frequencies = self.frequency[doomed_inds]
            self.rounded_equalization = self.equalization[doomed_inds]
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
                   equalization=True,
                   equalized=True,
                   target=True,
                   file_path=None,
                   f_min=20,
                   f_max=20000,
                   a_min=None,
                   a_max=None):
        """Plots frequency response graph."""
        if fig is None:
            fig, ax = plt.subplots()
        legend = []
        if not len(self.frequency):
            raise ValueError('\'frequency\' has no data!')
        if target and len(self.target):
            plt.plot(self.frequency, self.target, linewidth=2)
            legend.append('Target')
        if raw and len(self.raw):
            plt.plot(self.frequency, self.raw, linewidth=1)
            legend.append('Raw')
        if error and len(self.error) and not (smoothed and len(self.smoothed)):
            plt.plot(self.frequency, self.error, linewidth=1)
            legend.append('Error')
        if smoothed and len(self.smoothed):
            plt.plot(self.frequency, self.smoothed, linewidth=1)
            if len(self.error):
                legend.append('Error Smoothed')
            else:
                legend.append('Smoothed')
        if equalization and len(self.equalization):
            plt.plot(self.frequency, self.equalization, linewidth=1)
            legend.append('Equalization')
        if equalized and len(self.equalized_raw) and not len(self.equalized_smoothed):
            plt.plot(self.frequency, self.equalized_raw, linewidth=1)
            legend.append('Equalized raw')
        if equalized and len(self.equalized_smoothed):
            plt.plot(self.frequency, self.equalized_smoothed, linewidth=1)
            legend.append('Equalized smoothed')

        plt.xlabel('Frequency (Hz)')
        plt.semilogx()
        plt.xlim([f_min, f_max])
        plt.ylabel('Amplitude (dBr)')
        if a_min is None:
            a_min = max(np.min(self.raw) - 10, -40)
        if a_max is None:
            a_max = min(np.max(self.raw) + 10, 20)
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
        arg_parser.add_argument('--input_dir', type=str, default=os.path.abspath('data'),
                                help='Path to data directory. Will look for csv files in the data directory and '
                                     'recursively in sub-directories.')
        arg_parser.add_argument('--output_dir', type=str, default=os.path.abspath('results'),
                                help='Path to results directory. Will keep the same relative paths for files found'
                                     'in input_dir. Compilation results are produced in directory root.')
        arg_parser.add_argument('--calibration', type=str, required=False, default=argparse.SUPPRESS,
                                help='File path to CSV containing calibration curve.')
        arg_parser.add_argument('--compensation', type=str, required=False, default=argparse.SUPPRESS,
                                help='File path to CSV containing compensation curve.')
        arg_parser.add_argument('--equalize', action='store_true', default=False,
                                help='Run equalization?')
        arg_parser.add_argument('--bass_target', type=float, default=4,
                                help='Target gain for sub-bass. Defaults to +6dB as per Harman on-ear 2017 target '
                                     'response.')
        arg_parser.add_argument('--max_gain', type=float, default=12,
                                help='Maximum gain in equalization. Higher max gain allows to equalize deeper dips in '
                                     'frequency response but will limit output volume if no analog gain is available.')
        arg_parser.add_argument('--treble_f_lower', type=float, default=5000,
                                help='Lower bound for transition region between normal and treble frequencies. Treble '
                                     'frequencies are smoothed heavier and have lower max gain.')
        arg_parser.add_argument('--treble_f_upper', type=float, default=9000,
                                help='Upper bound for transition region between normal and treble frequencies. Treble '
                                     'frequencies are smoothed heavier and have lower max gain.')
        arg_parser.add_argument('--treble_max_gain', type=float, default=0,
                                help='Maximum gain in equalization in treble region.')
        arg_parser.add_argument('--treble_gain_k', type=float, default=1.0,
                                help='Coefficient for treble gain, positive and negative. Useful for disbling or'
                                     'reducing equalization power in treble region. Defaults to 1.0 (not limited).')
        arg_parser.add_argument('--show_plot', action='store_true', default=False,
                                help='Show plots? Requires the user to close each plot before next file can be '
                                     'processed.')
        return vars(arg_parser.parse_args())

    @staticmethod
    def main(input_dir=None,
             output_dir=None,
             calibration=None,
             compensation=None,
             equalize=False,
             bass_target=4,
             max_gain=6,
             treble_f_lower=3000,
             treble_f_upper=8000,
             treble_max_gain=0,
             treble_gain_k=1.0,
             show_plot=False):
        """Parses files in input directory and produces equalization results in output directory."""
        if calibration:
            # Creates FrequencyReponse for compensation data
            file_path = os.path.abspath(calibration)
            calibration = FrequencyResponse.read_from_csv(file_path)
            calibration.interpolate()
            calibration.center()

        if compensation:
            # Creates FrequencyReponse for compensation data
            file_path = os.path.abspath(compensation)
            compensation = FrequencyResponse.read_from_csv(file_path)
            compensation.interpolate()
            compensation.center()

        # Dir paths to absolute
        input_dir = os.path.abspath(input_dir)
        output_dir = os.path.abspath(output_dir)

        t = time()
        eq_apo_str = ''  # Compilation EqualizerAPO string
        for file_path in glob(os.path.join(input_dir, '**', '*.csv'), recursive=True):
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

            if compensation is not None:
                # Compensate
                fr.compensate(compensation)

            # Center by 1kHz
            fr.center()

            # Smooth data
            fr.smooth(
                window_size=1/7,
                iterations=10,
                treble_window_size=1/5,
                treble_iterations=100,
                treble_f_lower=treble_f_lower,
                treble_f_upper=treble_f_upper
            )

            # Equalize
            if equalize:
                fr.equalize(
                    max_gain=max_gain,
                    smooth=True,
                    window_size=1/5,
                    bass_target=bass_target,
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
                    _eq_apo_str = fr.write_eqapo_graphic_eq(file_path.replace('.csv', ' EqAPO.txt'))
                    print('Equalized "{}"'.format(fr.name))
                    # Add to compilation EqAPO string
                    eq_apo_str += '# ' + fr.name + '\n'
                    eq_apo_str += '#' + _eq_apo_str + '\n\n'
            elif show_plot:
                fig, ax = fr.plot_graph(show=show_plot)
                plt.close(fig)

        if equalize:
            # Write compilation EqAPO to file
            file_name = 'EqApo Bass +{b}dB, Max +{m}dB.txt'.format(b=bass_target, m=max_gain)
            with open(os.path.join(output_dir, file_name), 'w') as f:
                f.write(eq_apo_str)
            print('Equalized all in {:.2f}s'.format(time()-t))


if __name__ == '__main__':
    FrequencyResponse.main(**FrequencyResponse.cli_args())
