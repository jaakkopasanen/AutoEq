# -*- coding: utf-8 -*-

import os
from glob import glob
import argparse
import soundfile as sf
from time import time
import numpy as np
from constants import DEFAULT_MAX_GAIN, DEFAULT_TREBLE_F_LOWER, DEFAULT_TREBLE_F_UPPER, DEFAULT_TREBLE_MAX_GAIN, \
    DEFAULT_TREBLE_GAIN_K, DEFAULT_FS, DEFAULT_BIT_DEPTH, DEFAULT_PHASE, DEFAULT_F_RES, DEFAULT_BASS_BOOST_GAIN, \
    DEFAULT_BASS_BOOST_FC, DEFAULT_BASS_BOOST_Q
from frequency_response import FrequencyResponse


def batch_processing(input_dir=None, output_dir=None, new_only=False, standardize_input=False, compensation=None,
                     equalize=False, parametric_eq=False, fixed_band_eq=False, fc=None, q=None, ten_band_eq=False,
                     max_filters=None, convolution_eq=False, fs=DEFAULT_FS, bit_depth=DEFAULT_BIT_DEPTH,
                     phase=DEFAULT_PHASE, f_res=DEFAULT_F_RES, bass_boost_gain=DEFAULT_BASS_BOOST_GAIN,
                     bass_boost_fc=DEFAULT_BASS_BOOST_FC, bass_boost_q=DEFAULT_BASS_BOOST_Q, tilt=None,
                     sound_signature=None, max_gain=DEFAULT_MAX_GAIN, treble_f_lower=DEFAULT_TREBLE_F_LOWER,
                     treble_f_upper=DEFAULT_TREBLE_F_UPPER, treble_max_gain=DEFAULT_TREBLE_MAX_GAIN,
                     treble_gain_k=DEFAULT_TREBLE_GAIN_K, show_plot=False):
    """Parses files in input directory and produces equalization results in output directory."""
    start_time = time()

    if convolution_eq and not equalize:
        raise ValueError('equalize must be True when convolution_eq is True.')

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

    # Add files
    n_total = 0
    file_paths = []
    for input_file_path in glob_files:
        relative_path = os.path.relpath(input_file_path, input_dir)
        output_file_path = os.path.join(output_dir, relative_path) if output_dir else None
        output_file_dir = os.path.split(output_file_path)[0]
        if not new_only or not os.path.isdir(output_file_dir) or not len(os.listdir(output_file_dir)):
            # Not looking for only new ones or the output directory doesn't exist or it's empty
            file_paths.append((input_file_path, output_file_path))
            n_total += 1

    n = 0
    for input_file_path, output_file_path in file_paths:
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
            bass_boost_gain=bass_boost_gain,
            bass_boost_fc=bass_boost_fc,
            bass_boost_q=bass_boost_q,
            tilt=tilt,
            sound_signature=sound_signature,
            max_gain=max_gain,
            treble_f_lower=treble_f_lower,
            treble_f_upper=treble_f_upper,
            treble_max_gain=treble_max_gain,
            treble_gain_k=treble_gain_k,
            fs=fs[0] if type(fs) == list else fs
        )

        if output_file_path is not None:
            # Copy relative path to output directory
            output_dir_path, _ = os.path.split(output_file_path)
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
                if convolution_eq:
                    for _fs in fs:
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
        print(f'{n}/{n_total} ({n / n_total * 100:.1f}%) {time() - start_time:.0f}s: {fr.name}')


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
    arg_parser.add_argument('--q', type=str,
                            help='Comma separated list of Q values for fixed band eq. If only one '
                                 'value is passed it is used for all bands. Q value can be '
                                 'calculated from bandwidth in N octaves by Q = 2^(N/2)/(2^N-1).')
    arg_parser.add_argument('--ten_band_eq', action='store_true',
                            help='Shortcut parameter for activating standard ten band eq optimization.')
    arg_parser.add_argument('--max_filters', type=str, default=argparse.SUPPRESS,
                            help='Maximum number of filters for parametric EQ. Multiple cumulative optimization '
                                 'runs can be done by giving multiple filter counts separated by "+". "5+5" would '
                                 'create 10 filters where the first 5 are usable independently from the rest 5 and '
                                 'the last 5 can only be used with the first 5. This allows to have muliple '
                                 'configurations for equalizers with different number of bands available. '
                                 'Not limited by default.')
    arg_parser.add_argument('--convolution_eq', action='store_true',
                            help='Will produce impulse response for convolution equalizers if this parameter exists, '
                                 'no value needed.')
    arg_parser.add_argument('--fs', type=str, default=str(DEFAULT_FS),
                            help='Sampling frequency in Hertz for impulse response and parametric eq filters. Single '
                                 'value or multiple values separated by commas eg 44100,48000. When multiple values '
                                 'are given only the first one will be used for parametric eq. '
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
    arg_parser.add_argument('--bass_boost', type=str, default=argparse.SUPPRESS,
                            help='Bass boost shelf. Sub-bass frequencies will be boosted by this amount. Can be '
                                 'either a single value for a gain in dB or a comma separated list of three values '
                                 'for parameters of a low shelf filter, where the first is gain in dB, second is '
                                 'center frequency (Fc) in Hz and the last is quality (Q). When only a single '
                                 'value (gain) is given, default values for Fc and Q are used which are '
                                 f'{DEFAULT_BASS_BOOST_FC} Hz and {DEFAULT_BASS_BOOST_Q}, '
                                 'respectively. For example "--bass_boost=6" or "--bass_boost=9.5,150,0.69".')
    arg_parser.add_argument('--iem_bass_boost', type=float, default=argparse.SUPPRESS,
                            help='iem_bass_boost argument has been removed, use "--bass_boost" instead!')
    arg_parser.add_argument('--tilt', type=float, default=argparse.SUPPRESS,
                            help='Target tilt in dB/octave. Positive value (upwards slope) will result in brighter '
                                 'frequency response and negative value (downwards slope) will result in darker '
                                 'frequency response. 1 dB/octave will produce nearly 10 dB difference in '
                                 'desired value between 20 Hz and 20 kHz. Tilt is applied with bass boost and both '
                                 'will affect the bass gain.')
    arg_parser.add_argument('--sound_signature', type=str,
                            help='File path to a sound signature CSV file. Sound signature is added to the '
                                 'compensation curve. Error data will be used as the sound signature target if '
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
    if 'iem_bass_boost' in args:
        raise TypeError('iem_bass_boost argument has been removed, use "--bass_boost" instead!')
    if 'bass_boost' in args:
        bass_boost = args['bass_boost'].split(',')
        if len(bass_boost) == 1:
            args['bass_boost_gain'] = float(bass_boost[0])
            args['bass_boost_fc'] = DEFAULT_BASS_BOOST_FC
            args['bass_boost_q'] = DEFAULT_BASS_BOOST_Q
        elif len(bass_boost) == 3:
            args['bass_boost_gain'] = float(bass_boost[0])
            args['bass_boost_fc'] = float(bass_boost[1])
            args['bass_boost_q'] = float(bass_boost[2])
        else:
            raise ValueError('"--bass_boost" must have one value or three values separated by commas!')
        del args['bass_boost']
    if 'max_filters' in args:
        args['max_filters'] = [int(x) for x in args['max_filters'].split('+')]
    if 'fc' in args and args['fc'] is not None:
        args['fc'] = [float(x) for x in args['fc'].split(',')]
    if 'q' in args and args['q'] is not None:
        args['q'] = [float(x) for x in args['q'].split(',')]
    if 'fs' in args and args['fs'] is not None:
        args['fs'] = [int(x) for x in args['fs'].split(',')]
    return args


if __name__ == '__main__':
    batch_processing(**cli_args())
