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
                 smoothed=None,
                 equalization=None,
                 equalized_raw=None,
                 equalized_smoothed=None):
        self.name = name.strip()

        self.frequency = frequency if frequency is not None else []
        self.frequency = [None if x is None or math.isnan(x) else x for x in self.frequency]
        self.frequency = np.array(self.frequency)

        self.raw = raw if raw is not None else []
        self.raw = [None if x is None or math.isnan(x) or x is None else x for x in self.raw]
        self.raw = np.array(self.raw)

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

    @classmethod
    def read_from_csv(cls, file_path):
        """Reads data from CSV file and constructs class instance."""
        file_path = os.path.abspath(file_path)
        name = os.path.split(file_path)[-1].split('.')[0]

        df = pd.read_csv(file_path, sep=',', header=0)
        frequency = list(df['frequency']) if 'frequency' in df else None
        raw = list(df['raw']) if 'raw' in df else None
        smoothed = list(df['smoothed']) if 'smoothed' in df else None
        equalization = list(df['equalization']) if 'equalization' in df else None
        equalized_raw = list(df['equalized_raw']) if 'equalized_raw' in df else None
        equalized_smoothed = list(df['equalized_smoothed']) if 'equalized_smoothed' in df else None

        return cls(
            name=name,
            frequency=frequency,
            raw=raw,
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
        if len(self.smoothed):
            df['smoothed'] = [x if x is not None else 'NaN' for x in self.smoothed]
        if len(self.equalization):
            df['equalization'] = [x if x is not None else 'NaN' for x in self.equalization]
        if len(self.equalized_raw):
            df['equalized_raw'] = [x if x is not None else 'NaN' for x in self.equalized_raw]
        if len(self.equalized_smoothed):
            df['equalized_smoothed'] = [x if x is not None else 'NaN' for x in self.equalized_smoothed]

        df.to_csv(file_path, header=True, index=False)

    def write_equalization_equalizerapo_graphic_eq(self, file_path):
        """Writes equalization graph to a file as Equalizer APO config."""
        file_path = os.path.abspath(file_path)
        freq = []
        eq = []
        for i, x in enumerate(self.frequency):
            if 20 <= x <= 20000:
                freq.append(x)
                eq.append(self.equalization[i])
        with open(file_path, 'w') as f:
            s = '; '.join(['{f} {a:.1f}'.format(f=round(f), a=a) for f, a in zip(freq, eq)])
            s = '# GraphicEQ: 10 -84; ' + s
            f.write(s)

    @staticmethod
    def generate_frequencies(f_min=10, f_max=30000, step=1.01):
        freq_new = []
        # Frequencies from 20kHz down
        f = np.min([20000, f_max])
        while f > f_min:
            freq_new.append(round(f))
            f = f / step
        # Frequencies from 20kHZ up
        f = np.min([20000, f_max])
        while f < f_max:
            freq_new.append(round(f))
            f = f * step
        freq_new = sorted(set(freq_new))  # Remove duplicates and sort ascending
        return np.array(freq_new)

    def interpolate(self, f=None, step=1.01, pol_order=1, f_min=10, f_max=30000):
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
            self.frequency = self.generate_frequencies(f_min=f_min, f_max=f_max, step=step)
        else:
            self.frequency = f
        self.raw = interpolator(np.log10(self.frequency))

    def center(self):
        """Removed bias from frequency response."""
        interpolator = InterpolatedUnivariateSpline(np.log10(self.frequency), self.raw, k=1)
        self.raw -= interpolator(np.log10(1000))

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

    def _sigmoid(self, f_lower, f_upper):
        f_center = np.sqrt(f_upper / f_lower) * f_lower
        half_range = np.log10(f_upper) - np.log10(f_center)
        f_center = np.log10(f_center)
        return expit((np.log10(self.frequency) - f_center) / (half_range / 4))

    def smooth(self,
               window_size=1/5,
               iterations=1,
               treble_window_size=None,
               treble_iterations=None,
               f_lower=6000,
               f_upper=10000):
        """Smooths data.

        Args:
            window_size: Filter window size in octaves.
            iterations: Number of iterations to run the filter. Each new iteration is using output of previous one.
            treble_window_size: Filter window size for high frequencies.
            treble_iterations: Number of iterations for treble filter.
            f_lower: Lower boundary of transition frequency region. In the transition region normal filter is \
                        switched to treble filter with sigmoid weighting function.
            f_upper: Upper boundary of transition frequency reqion. In the transition region normal filter is \
                        switched to treble filter with sigmoid weighting function.
        """
        if None in self.frequency or None in self.raw or None in self.equalization or None in self.equalized_raw:
            # Must not contain None values
            raise ValueError('None values present, cannot smoothen!')

        if f_upper <= f_lower:
            raise ValueError('Upper transition boundary must be greater than lower boundary')

        # Use normal filter parameters for treble filter if treble filter parameters are not given
        if treble_window_size is None:
            treble_window_size = window_size
        if treble_iterations is None:
            treble_iterations = iterations

        # Normal filter
        y_normal = self.raw
        for _ in range(iterations):
            y_normal = savgol_filter(y_normal, self._window_size(window_size), 2)

        # Treble filter
        y_treble = self.raw
        for _ in range(treble_iterations):
            y_treble = savgol_filter(y_treble, self._window_size(treble_window_size), 2)

        # Transition weighted with sigmoid
        k_treble = self._sigmoid(f_lower, f_upper)
        k_normal = k_treble * -1 + 1
        self.smoothed = y_normal * k_normal + y_treble * k_treble

    def calibrate(self, calibration):
        """Calibrates raw frequency response data with calibration array."""
        self.raw += calibration.raw

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

    def equalize(self, max_gain=12, smooth=True, window_size=1/3, bass_target=4):
        """Creates equalization curve and equalized curve.

        Args:
            max_gain: Maximum gain in dB
            smooth: Smooth kinks caused by clipping gain to max gain?
            window_size: Smoothing average window size in octaves
            bass_target: Target value in dB for bass boost
        """
        self.equalization = []
        self.equalized_raw = []

        data = self.smoothed if len(self.smoothed) else self.raw

        if None in data or None in self.equalization or None in self.equalized_raw:
            # Must not contain None values
            self.interpolate()

        if smooth:
            max_gain *= 0.9

        # Invert with max gain clipping
        previous_clipped = False
        kink_inds = []
        self.target = self._target(bass_boost=bass_target)
        k = self._sigmoid(6000, 10000) * -1 + 1  # Limit equalization power in high frequencies
        for i, a in enumerate(data):
            gain = self.target[i] - a
            #gain *= k[i]  # TODO: Restore?
            clipped = gain > max_gain
            if previous_clipped != clipped:
                kink_inds.append(i)
            previous_clipped = clipped
            if clipped:
                gain = max_gain
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
                   smoothed=True,
                   equalization=True,
                   equalized=True,
                   rounded=True,
                   target=True,
                   file_path=None,
                   f_min=10,
                   f_max=30000,
                   a_min=-40,
                   a_max=40):
        """Plots frequency response graph."""
        if fig is None:
            fig, ax = plt.subplots()
        legend = []
        if not len(self.frequency):
            raise ValueError('\'frequency\' has no data!')

        # if rounded and len(self.rounded_frequencies):
        #     plt.plot(self.rounded_frequencies, self.rounded_equalization, '.', color='r', linewidth=1)
        #     legend.append('Rounded')
        if target and len(self.target):
            plt.plot(self.frequency, self.target, linewidth=2)
            legend.append('Target')
        if raw and len(self.raw):
            plt.plot(self.frequency, self.raw, linewidth=1)
            legend.append('Raw')
        if smoothed and len(self.smoothed):
            plt.plot(self.frequency, self.smoothed, linewidth=1)
            legend.append('Smoothed')
        if equalization and len(self.equalization):
            plt.plot(self.frequency, self.equalization, linewidth=1)
            legend.append('Equalization')
        if equalized and len(self.equalized_raw):
            plt.plot(self.frequency, self.equalized_raw, linewidth=1)
            legend.append('Equalized raw')
        if equalized and len(self.equalized_smoothed):
            plt.plot(self.frequency, self.equalized_smoothed, linewidth=1)
            legend.append('Equalized smoothed')

        plt.xlabel('Frequency (Hz)')
        plt.semilogx()
        plt.xlim([f_min, f_max])
        plt.ylabel('Amplitude (dBr)')
        plt.ylim([a_min, a_max])
        plt.title(self.name)
        plt.legend(legend, loc='upper right', fontsize=8)
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
    def main():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--dir_path', type=str, default=os.path.join('innerfidelity', 'data'),
                                help='Path to data directory.')
        arg_parser.add_argument('--calibration', type=str,
                                default=os.path.join('innerfidelity', 'transformation.csv'),
                                help='File path to CSV containing calibration curve.')
        cli_args = arg_parser.parse_args()

        calibration = None
        if cli_args.calibration:
            file_path = os.path.abspath(cli_args.calibration)
            calibration = FrequencyResponse.read_from_csv(file_path)

        dir_path = os.path.abspath(cli_args.dir_path)
        t = time()
        for directory in glob(os.path.join(dir_path, '*')):
            for file_path in glob(os.path.join(directory, '*ORIG.csv')):
                for max_gain in [12]:
                    for bass_target in [4]:
                        fr = FrequencyResponse.read_from_csv(file_path)
                        s = ' (Max +{g}db, Bass +{b}dB)'.format(g=max_gain, b=bass_target)
                        fp = file_path.replace(' ORIG', s)
                        fr.name = fr.name.replace(' ORIG', s)
                        fr.interpolate()
                        if calibration is not None:
                            fr.calibrate(calibration)
                        fr.center()
                        fr.smooth(window_size=1/5, iterations=10, treble_window_size=1/2, treble_iterations=100)
                        fr.equalize(max_gain=max_gain, smooth=True, window_size=1/5, bass_target=bass_target)
                        fig, ax = fr.plot_graph(show=True, file_path=fp.replace('.csv', '.png'))
                        plt.close(fig)
                        fr.write_to_csv(fp)
                        fr.write_equalization_equalizerapo_graphic_eq(fp.replace('.csv', '.txt'))
                        print('Equalized "{}"'.format(fr.name))
                        fp = fp.replace('.csv', '.png')
                        shutil.copyfile(fp, os.path.join('inspect', os.path.split(fp)[-1]))
        print('Equalized all in {:.2f}s'.format(time()-t))


if __name__ == '__main__':
    FrequencyResponse.main()
