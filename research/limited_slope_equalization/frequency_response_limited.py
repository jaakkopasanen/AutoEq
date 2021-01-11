# -*- coding: utf-8 -*-

import sys
from pathlib import Path
if str(Path().resolve().parent.parent) not in sys.path:
    sys.path.insert(1, str(Path().resolve().parent.parent))
import numpy as np
from scipy.signal import find_peaks
from constants import DEFAULT_MAX_GAIN, DEFAULT_TREBLE_F_LOWER, DEFAULT_TREBLE_F_UPPER, DEFAULT_TREBLE_MAX_GAIN,\
    DEFAULT_TREBLE_GAIN_K, DEFAULT_FS
from frequency_response import FrequencyResponse


class FrequencyResponseLimited(FrequencyResponse):
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
                window_size=1 / 12,
                treble_window_size=2,
                treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                treble_f_upper=DEFAULT_TREBLE_F_UPPER):
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
            treble_f_lower: Lower boundary of transition frequency region. In the transition region normal filter is \
                            switched to treble filter with sigmoid weighting function.
            treble_f_upper: Upper boundary of transition frequency reqion. In the transition region normal filter is \
                            switched to treble filter with sigmoid weighting function.

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
            window_size=1 / 12,
            treble_window_size=2,
            treble_f_lower=treble_f_lower,
            treble_f_upper=treble_f_upper
        )

        peq_filters = n_peq_filters = peq_max_gains = fbeq_filters = n_fbeq_filters = fbeq_max_gains = None
        # Equalize
        if equalize:
            self.equalize(
                max_gain=max_gain, concha_interference=concha_interference, treble_f_lower=treble_f_lower,
                treble_f_upper=treble_f_upper)
            if parametric_eq:
                # Get the filters
                peq_filters, n_peq_filters, peq_max_gains = self.optimize_parametric_eq(max_filters=max_filters, fs=fs)
            if fixed_band_eq:
                fbeq_filters, n_fbeq_filters, fbeq_max_gains = self.optimize_fixed_band_eq(fc=fc, q=q, fs=fs)

        return peq_filters, n_peq_filters, peq_max_gains, fbeq_filters, n_fbeq_filters, fbeq_max_gains

    def equalize(self,
                 max_gain=DEFAULT_MAX_GAIN,
                 limit=18,
                 limit_decay=0.0,
                 concha_interference=False,
                 window_size=1 / 12,
                 treble_window_size=2,
                 treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                 treble_f_upper=DEFAULT_TREBLE_F_UPPER):
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
            # Gain can be reduced in the treble region
            # Clip positive gain to max gain
            combined.raw = np.min(np.vstack([combined.raw, np.ones(combined.raw.shape) * max_gain]), axis=0)
            # Smoothen the curve to get rid of hard kinks
            combined.smoothen_fractional_octave(window_size=1 / 5, treble_window_size=1 / 5)

            # TODO: Fix trend by comparing super heavy smoothed equalizer frequency responses: limited vs unlimited

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
            # TODO: Should target be where gradient reduces below certain threshold?
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
