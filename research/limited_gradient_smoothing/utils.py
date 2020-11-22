# -*- coding: utf-8 -*-

import sys
from pathlib import Path
ROOT_PATH = Path().resolve().parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(str(ROOT_PATH))
import numpy as np
import scipy
from frequency_response import FrequencyResponse


def limited_slope_plots(fr, limit):
    # Smoothen data, heavily on treble to avoid problems in +10 kHz region
    fr.smoothen_fractional_octave(window_size=1 / 12, treble_window_size=2, treble_f_lower=9000, treble_f_upper=12000)

    # Copy data
    x = fr.frequency.copy()
    y = fr.smoothed.copy()

    # Find peaks and notches
    peak_inds, peak_props = scipy.signal.find_peaks(y, prominence=1)  # TODO: this affects which regions are rejected
    notch_inds, notch_props = scipy.signal.find_peaks(-y, prominence=1)  # TODO: this affects which regions are protected

    # Find backward start index
    backward_start = find_backward_start(y, peak_inds, notch_inds)  # TODO: backward start
    #backward_start = 0

    # Find forward and backward limitations
    # limited_forward is y but with slopes limited when traversing left to right
    # clipped_forward is boolean mask for limited samples when traversing left to right
    # limited_backward is found using forward algorithm but with flipped data
    limited_forward, clipped_forward, regions_forward = limited_forward_slope(
        x, y, limit, start_index=0, peak_inds=peak_inds)
    limited_backward, clipped_backward, regions_backward = limited_backward_slope(
        x, y, limit, start_index=backward_start, peak_inds=peak_inds)

    # TODO: Find notches which have backward region on left side, forward region on right side and are lower in level than adjacent notches

    # TODO: Set detected notches as slope clipping free zones up to levels of adjacent notches

    # Forward and backward limited curves are combined with min function
    # Combination function is smoothed to get rid of hard kinks
    limiter = FrequencyResponse(
        name='limiter', frequency=x.copy(), raw=np.min(np.vstack([limited_forward, limited_backward]), axis=0))
    limiter.smoothen_fractional_octave(window_size=1 / 3, treble_window_size=1 / 3)
    limited = limiter.smoothed

    # Plot graphs
    fig, ax = fr.plot_graph(show=False, raw_plot_kwargs={'color': 'C2'},
                            smoothed_plot_kwargs={'color': 'C2', 'linewidth': 1, 'linestyle': 'dashed'})
    fig.set_size_inches(20, 9)
    ax.plot(x, limited, label='Limited', color='C1')
    ax.fill_between(x, clipped_forward * -5, clipped_forward * 10, label='Clipped left to right', color='blue',
                    alpha=0.1)
    ax.fill_between(x, clipped_backward * -10, clipped_backward * 5, label='Clipped right to left', color='red',
                    alpha=0.1)
    ax.scatter(x[peak_inds], y[peak_inds], color='red')
    ax.scatter(x[notch_inds], y[notch_inds], color='blue')
    ax.scatter(x[backward_start], y[backward_start], 300, marker='X', label='Backward start',
               color='magenta', alpha=0.4)
    ax.legend()
    ax.set_xlim([300, 20000])

    return fig, ax


def limited_backward_slope(x, y, limit, start_index=0, peak_inds=None):
    """Limits forwards slope of a frequency response curve while traversing backwards

        Args:
            x: frequencies
            y: amplitudes
            limit: maximum slope in dB / oct
            start_index: Index where to start traversing, no limitations apply before this

        Returns:
            limited: Limited curve
            mask: Boolean mask for clipped indexes
            regions: Clipped regions, one per row, 1st column is the start index, 2nd column is the end index (exclusive)
    """
    start_index = len(x) - start_index - 1
    if peak_inds is not None:
        peak_inds = len(x) - peak_inds - 1
    limited_backward, clipped_backward, regions_backward = limited_forward_slope(
        x, np.flip(y), limit, start_index=start_index, peak_inds=peak_inds)
    limited_backward = np.flip(limited_backward)
    clipped_backward = np.flip(clipped_backward)
    regions_backward = len(x) - regions_backward - 1
    return limited_backward, clipped_backward, regions_backward


def limited_forward_slope(x, y, limit, start_index=0, peak_inds=None):
    """Limits forwards slope of a frequency response curve

    Args:
        x: frequencies
        y: amplitudes
        limit: maximum slope in dB / oct
        start_index: Index where to start traversing, no limitations apply before this
        peak_inds: Peak indexes. Regions will require to touch one of these if given.

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
        # TODO: limit 9 kHz notch 8 kHz to 11 kHz?
        local_limit = limit / 4 if 8000 <= x[i] <= 11500 else limit

        if slope > local_limit:
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

    return np.array(limited), np.array(clipped), np.array(regions)


def log_log_gradient(f0, f1, g0, g1):
    octaves = np.log(f1 / f0) / np.log(2)
    gain = g1 - g0
    return gain / octaves


def find_backward_start(y, peak_inds, notch_inds):
    # Find starting index for the backward pass
    if peak_inds[-1] > notch_inds[-1]:
        # Last peak is a positive peak
        # Find index on the right side of the peak where the curve crosses the left side minimum
        backward_start = np.argwhere(y[peak_inds[-1]:] <= y[notch_inds[-1]])
        if len(backward_start):
            backward_start = backward_start[0, 0] + peak_inds[-1]
        else:
            backward_start = len(y) - 1
    else:
        # Last peak is a negative peak, start there
        backward_start = notch_inds[-1]
    return backward_start
