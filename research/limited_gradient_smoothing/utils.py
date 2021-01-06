# -*- coding: utf-8 -*-

import sys
from pathlib import Path
if str(Path().resolve().parent.parent) not in sys.path:
    sys.path.insert(1, str(Path().resolve().parent.parent))
import numpy as np
import scipy
from frequency_response import FrequencyResponse


def limited_slope_plots(fr, limit, limit_decay=0.0):
    fr.equalization = -fr.error
    limited, smoothed, limited_forward, clipped_forward, limited_backward, clipped_backward, peak_inds, dip_inds, \
        backward_start, protection_mask = limited_slope(fr.frequency, fr.equalization, limit, limit_decay=limit_decay)

    x = fr.frequency.copy()
    y = smoothed

    # Plot graphs
    fig, ax = fr.plot_graph(
        show=False, raw=False, error=False, target=False, equalization_plot_kwargs={
            'color': 'C2', 'linewidth': 1, 'label': 'Raw equalization', 'linestyle': 'dashed'
        })
    fig.set_size_inches(20, 9)
    ax.plot(x, y, label='Smoothed equalization', color='C2')
    ax.plot(x, limited, label='Limited', color='C1')
    ax.fill_between(x, clipped_forward * -5, clipped_forward * 10, label='Limited left to right', color='blue',
                    alpha=0.1)
    ax.fill_between(x, clipped_backward * -10, clipped_backward * 5, label='Limited right to left', color='red',
                    alpha=0.1)
    ax.fill_between(x, protection_mask * -12, protection_mask * 12, label='Limitation-safe zone', color='limegreen',
                    alpha=0.2)
    ax.scatter(x[peak_inds], y[peak_inds], color='red')
    ax.scatter(x[backward_start], y[backward_start], 200, marker='<', label='Backward start', color='black')
    ax.scatter(x[dip_inds], y[dip_inds], color='limegreen')
    ax.legend()

    return fig, ax


def limited_slope(x, y, limit, limit_decay=0.0):
    """Bi-directional slope limitation for a frequency response curve

    Args:
        x: frequencies
        y: amplitudes
        limit: Maximum slope in dB per octave
        limit_decay: Decay coefficient (per octave) for the limit. Value of 0.5 would reduce limit by 50% in an octave
            when traversing a single limitation zone.

    Returns:

    """
    fr = FrequencyResponse(name='fr', frequency=x, raw=y)
    # Smoothen data, heavily on treble to avoid problems in +10 kHz region
    fr.smoothen_fractional_octave(window_size=1 / 12, treble_window_size=2, treble_f_lower=9000, treble_f_upper=11500)

    # Copy data
    x = fr.frequency.copy()
    y = fr.smoothed.copy()

    # Find peaks and notches
    # TODO: these affect which regions are rejected
    peak_inds, peak_props = scipy.signal.find_peaks(y, prominence=1)
    dip_inds, dip_props = scipy.signal.find_peaks(-y, prominence=1)

    limit_free_mask = protection_mask(y, peak_inds, dip_inds)
    # TODO: 8 kHz - 11.5 kHz should not be limit free zone

    # Find backward start index
    backward_start = find_backward_start(y, peak_inds, dip_inds)

    # Find forward and backward limitations
    # limited_forward is y but with slopes limited when traversing left to right
    # clipped_forward is boolean mask for limited samples when traversing left to right
    # limited_backward is found using forward algorithm but with flipped data
    limited_forward, clipped_forward, regions_forward = limited_forward_slope(
        x, y, limit, limit_decay=limit_decay, start_index=0, peak_inds=peak_inds, limit_free_mask=limit_free_mask)
    limited_backward, clipped_backward, regions_backward = limited_backward_slope(
        x, y, limit, limit_decay=limit_decay, start_index=backward_start, peak_inds=peak_inds, limit_free_mask=limit_free_mask)

    # Forward and backward limited curves are combined with min function
    # Combination function is smoothed to get rid of hard kinks
    limiter = FrequencyResponse(
        name='limiter', frequency=x.copy(), raw=np.min(np.vstack([limited_forward, limited_backward]), axis=0))
    limiter.smoothen_fractional_octave(window_size=1 / 5, treble_window_size=1 / 5)
    #limiter.smoothed = limiter.raw.copy()

    return limiter.smoothed.copy(), fr.smoothed.copy(), limited_forward, clipped_forward, limited_backward,\
           clipped_backward, peak_inds, dip_inds, backward_start, limit_free_mask


def protection_mask(y, peak_inds, dip_inds):
    """Finds zones around dips which are lower than their adjacent dips. Zones extend to the lower level of the adjacent
    dips.

    Args:
        y: amplitudes
        peak_inds: Indices of peaks
        dip_inds: Indices of dips

    Returns:
        Boolean mask for limitation-free indices
    """
    if peak_inds[-1] > dip_inds[-1]:
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


def limited_backward_slope(x, y, limit, limit_decay=0.0, start_index=0, peak_inds=None, limit_free_mask=None):
    """Limits forwards slope of a frequency response curve while traversing backwards

        Args:
            x: frequencies
            y: amplitudes
            limit: maximum slope in dB / oct
            limit_decay: Limit decay coefficient per octave
            start_index: Index where to start traversing, no limitations apply before this
            peak_inds: Peak indexes. Regions will require to touch one of these if given.
            limit_free_mask: Boolean mask for indices where limitation must not be applied

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
    limited_backward, clipped_backward, regions_backward = limited_forward_slope(
        x, np.flip(y), limit, limit_decay=limit_decay, start_index=start_index, peak_inds=peak_inds,
        limit_free_mask=limit_free_mask)
    limited_backward = np.flip(limited_backward)
    clipped_backward = np.flip(clipped_backward)
    regions_backward = len(x) - regions_backward - 1
    return limited_backward, clipped_backward, regions_backward


def limited_forward_slope(x, y, limit, limit_decay=0.0, start_index=0, peak_inds=None, limit_free_mask=None):
    """Limits forwards slope of a frequency response curve

    Args:
        x: frequencies
        y: amplitudes
        limit: maximum slope in dB / oct
        limit_decay: Limit decay coefficient per octave
        start_index: Index where to start traversing, no limitations apply before this
        peak_inds: Peak indexes. Regions will require to touch one of these if given.
        limit_free_mask: Boolean mask for indices where limitation must not be applied

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

        if clipped[-1]:
            # Previous sample clipped, reduce limit
            #print(f'{x[i]} -> {x[regions[-1][0]]} = {(1 - limit_decay) ** np.log2(x[i] / x[regions[-1][0]])}')
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
