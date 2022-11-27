import os
import argparse
import multiprocessing
import warnings

from autoeq.constants import DEFAULT_MAX_GAIN, DEFAULT_TREBLE_F_LOWER, DEFAULT_TREBLE_F_UPPER, \
    DEFAULT_TREBLE_GAIN_K, DEFAULT_FS, DEFAULT_BIT_DEPTH, DEFAULT_PHASE, DEFAULT_F_RES, DEFAULT_BASS_BOOST_FC, \
    DEFAULT_BASS_BOOST_Q, DEFAULT_SMOOTHING_WINDOW_SIZE, DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE, DEFAULT_TREBLE_BOOST_FC, \
    DEFAULT_TREBLE_BOOST_Q, DEFAULT_PREAMP
from autoeq.batch_processing import batch_processing


def cli_args():
    """Parses command line arguments."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input-dir', type=str, required=True,
                            help='Path to input data directory. Will look for CSV files in the data directory and '
                                 'recursively in sub-directories.')
    arg_parser.add_argument('--output-dir', type=str, required=True,
                            help='Path to results directory. Will keep the same relative paths for files found '
                                 'in input-dir.')
    arg_parser.add_argument('--standardize-input', action='store_true',
                            help='Overwrite input data in standardized sampling and bias?')
    arg_parser.add_argument('--new-only', action='store_true',
                            help='Only process input files which don\'t have results in output directory.')
    arg_parser.add_argument('--compensation', type=str,
                            help='File path to CSV containing compensation (target) curve. Compensation is '
                                 'necessary when equalizing because all input data is raw microphone data. See '
                                 '"compensation", "innerfidelity/resources" and "headphonecom/resources".')
    arg_parser.add_argument('--equalize', action='store_true',
                            help='Will run equalization if this parameter exists, no value needed.')
    arg_parser.add_argument('--parametric-eq', action='store_true',
                            help='Will produce parametric eq settings if this parameter exists, no value needed.')
    arg_parser.add_argument('--fixed-band-eq', action='store_true',
                            help='Will produce fixed band eq settings if this parameter exists, no value needed.')
    arg_parser.add_argument('--rockbox', action='store_true',
                            help='Will produce a Rockbox .cfg file with 10 band eq settings if this parameter exists,'
                                 'no value needed.')
    arg_parser.add_argument('--ten-band-eq', action='store_true',
                            help='Shortcut parameter for activating standard ten band eq optimization.')
    arg_parser.add_argument('--parametric-eq-config', type=str,
                            default='4_PEAKING_WITH_LOW_SHELF,4_PEAKING_WITH_HIGH_SHELF',
                            help='Name of parametric equalizer configuration or a path to a configuration file. '
                                 'Available named configurations are "10_PEAKING" for 10 peaking filters, '
                                 '"8_PEAKING_WITH_SHELVES" for 8 peaking filters and a low shelf at 105 Hz for bass '
                                 'adjustment and a high shelf at 10 kHz for treble adjustment, '
                                 '"4_PEAKING_WITH_LOW_SHELF" for 4 peaking filters and a low shelf at 105 Hz for bass '
                                 'adjustment, "4_PEAKING_WITH_HIGH_SHELF" for 4 peaking filters and a high shelf '
                                 'at 10 kHz for treble adjustments. You can give multiple named configurations by '
                                 'separating the names with commas and filter sets will be built on top of each other. '
                                 'When the value is a file path, the file will be read and used as a configuration. '
                                 'The file needs to be a YAML file with "filters" field as a list of filter '
                                 'configurations, each of which can define "fc", "min_fc", "max_fc", "q", "min_q", '
                                 '"max_q", "gain", "min_gain", "max_gain" and "type" fields. When the fc, q or gain '
                                 'value is given, the parameter won\'t be optimized for the filter. "type" needs to '
                                 'be either "LOW_SHELF", "PEAKING" or "HIGH_SHELF". Also "filter_defaults" field is '
                                 'supported on the top level and it can have the same fields as the filters do. '
                                 'All fields missing from the filters will be read from "filter_defaults". '
                                 'Defaults to "4_PEAKING_WITH_LOW_SHELF,4_PEAKING_WITH_HIGH_SHELF". '
                                 'Optimizer behavior can be adjusted by defining "optimizer" field which has fields '
                                 '"min_f" and "max_f" for lower and upper bounds of the optimization range, "max_time" '
                                 'for maximum optimization duration in seconds, "target_loss" for RMSE target level '
                                 'upon reaching which the optimization is ended, "min_change_rate" for minimum rate '
                                 'of improvement in db/s and "min_std" for minimum standard deviation of the last few '
                                 'loss values. "min_change_rate" and "min_std" end the optimization when further time '
                                 'spent optimizing can\'t be expected to improve the results dramatically. See '
                                 'peq.yaml for an example.'),
    arg_parser.add_argument('--fixed-band-eq-config', type=str, default='10_BAND_GRAPHIC_EQ',
                            help='Path to fixed band equalizer configuration. The file format is the same YAML as '
                                 'for parametric equalizer.')
    arg_parser.add_argument('--convolution-eq', action='store_true',
                            help='Will produce impulse response for convolution equalizers if this parameter exists, '
                                 'no value needed.')
    arg_parser.add_argument('--fs', type=str, default=str(DEFAULT_FS),
                            help='Sampling frequency in Hertz for impulse response and parametric eq filters. Single '
                                 'value or multiple values separated by commas eg 44100,48000. When multiple values '
                                 'are given only the first one will be used for parametric eq. '
                                 f'Defaults to {DEFAULT_FS}.')
    arg_parser.add_argument('--bit-depth', type=int, default=DEFAULT_BIT_DEPTH,
                            help='Number of bits for every sample in impulse response. '
                                 f'Defaults to {DEFAULT_BIT_DEPTH}.')
    arg_parser.add_argument('--phase', type=str, default=DEFAULT_PHASE,
                            help='Impulse response phase characteristic. "minimum", "linear" or "both". '
                                 f'Defaults to "{DEFAULT_PHASE}"')
    arg_parser.add_argument('--f-res', type=float, default=DEFAULT_F_RES,
                            help='Frequency resolution for impulse responses. If this is 20 then impulse response '
                                 'frequency domain will be sampled every 20 Hz. Filter length for '
                                 f'impulse responses will be fs/f_res. Defaults to {DEFAULT_F_RES}.')
    arg_parser.add_argument('--bass-boost', type=str, default=argparse.SUPPRESS,
                            help='Bass boost shelf. Sub-bass frequencies will be boosted by this amount. Can be '
                                 'either a single value for a gain in dB or a comma separated list of three values '
                                 'for parameters of a low shelf filter, where the first is gain in dB, second is '
                                 'center frequency (Fc) in Hz and the last is quality (Q). When only a single '
                                 'value (gain) is given, default values for Fc and Q are used which are '
                                 f'{DEFAULT_BASS_BOOST_FC} Hz and {DEFAULT_BASS_BOOST_Q}, '
                                 'respectively. For example "--bass-boost=6" or "--bass-boost=9.5,150,0.69".')
    arg_parser.add_argument('--treble-boost', type=str, default=argparse.SUPPRESS,
                            help='Treble boost shelf. > 10 kHz frequencies will be boosted by this amount. Can be '
                                 'either a single value for a gain in dB or a comma separated list of three values '
                                 'for parameters of a high shelf filter, where the first is gain in dB, second is '
                                 'center frequency (Fc) in Hz and the last is quality (Q). When only a single '
                                 'value (gain) is given, default values for Fc and Q are used which are '
                                 f'{DEFAULT_TREBLE_BOOST_FC} Hz and {DEFAULT_TREBLE_BOOST_Q}, '
                                 'respectively. For example "--treble-boost=3" or "--treble-boost=-4,12000,0.69".')
    arg_parser.add_argument('--tilt', type=float, default=argparse.SUPPRESS,
                            help='Target tilt in dB/octave. Positive value (upwards slope) will result in brighter '
                                 'frequency response and negative value (downwards slope) will result in darker '
                                 'frequency response. 1 dB/octave will produce nearly 10 dB difference in '
                                 'desired value between 20 Hz and 20 kHz. Tilt is applied with bass boost and both '
                                 'will affect the bass gain.')
    arg_parser.add_argument('--sound-signature', type=str,
                            help='File path to a sound signature CSV file. Sound signature is added to the '
                                 'compensation curve. Error data will be used as the sound signature target if '
                                 'the CSV file contains an error column and otherwise the raw column will be used. '
                                 'This means there are two different options for using sound signature: 1st is '
                                 'pointing it to a result CSV file of a previous run and the 2nd is to create a '
                                 'CSV file with just frequency and raw columns by hand (or other means). The Sound '
                                 'signature graph will be interpolated so any number of point at any frequencies '
                                 'will do, making it easy to create simple signatures with as little as two or '
                                 'three points.')
    arg_parser.add_argument('--max-gain', type=float, default=DEFAULT_MAX_GAIN,
                            help='Maximum positive gain in equalization. Higher max gain allows to equalize deeper '
                                 'dips in  frequency response but will limit output volume if no analog gain is '
                                 'available because positive gain requires negative digital preamp equal to '
                                 f'maximum positive gain. Defaults to {DEFAULT_MAX_GAIN}.')
    arg_parser.add_argument('--window-size', type=float, default=DEFAULT_SMOOTHING_WINDOW_SIZE,
                            help='Smoothing window size in octaves.')
    arg_parser.add_argument('--treble-window-size', type=float, default=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
                            help='Smoothing window size in octaves in the treble region.')
    arg_parser.add_argument('--treble-f-lower', type=float, default=DEFAULT_TREBLE_F_LOWER,
                            help='Lower bound for transition region between normal and treble frequencies. Treble '
                                 'frequencies can have different max gain and gain K. Defaults to '
                                 f'{DEFAULT_TREBLE_F_LOWER}.')
    arg_parser.add_argument('--treble-f-upper', type=float, default=DEFAULT_TREBLE_F_UPPER,
                            help='Upper bound for transition region between normal and treble frequencies. Treble '
                                 'frequencies can have different max gain and gain K. Defaults to '
                                 f'{DEFAULT_TREBLE_F_UPPER}.')
    arg_parser.add_argument('--treble-gain-k', type=float, default=DEFAULT_TREBLE_GAIN_K,
                            help='Coefficient for treble gain, affects both positive and negative gain. Useful for '
                                 'disabling or reducing equalization power in treble region. Defaults to '
                                 f'{DEFAULT_TREBLE_GAIN_K}.')
    arg_parser.add_argument('--thread-count', default=1,
                            help='Amount of threads to use for processing results. If set to "max" all the threads '
                                 'available will be used. Using more threads result in higher memory usage. '
                                 'Defaults to 1.')
    arg_parser.add_argument('--preamp', type=float, default=DEFAULT_PREAMP,
                            help='Extra pre-amplification to be applied to equalizer settings in dB')
    args = vars(arg_parser.parse_args())

    # Replace hyphens with underscores to be compatible with the batch_processing method signature
    args = {key.replace('-', '_'): val for key, val in args.items()}

    if 'equalize' in args and args['equalize']:
        warnings.warn(
            '"equalize" parameter is no longer supported. The equalization target is created automatically every time.')
    del args['equalize']

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
            raise ValueError('"--bass-boost" must have one value or three values separated by commas!')
        del args['bass_boost']
        
    if 'treble_boost' in args:
        treble_boost = args['treble_boost'].split(',')
        if len(treble_boost) == 1:
            args['treble_boost_gain'] = float(treble_boost[0])
            args['treble_boost_fc'] = DEFAULT_TREBLE_BOOST_FC
            args['treble_boost_q'] = DEFAULT_TREBLE_BOOST_Q
        elif len(treble_boost) == 3:
            args['treble_boost_gain'] = float(treble_boost[0])
            args['treble_boost_fc'] = float(treble_boost[1])
            args['treble_boost_q'] = float(treble_boost[2])
        else:
            raise ValueError('"--treble-boost" must have one value or three values separated by commas!')
        del args['treble_boost']

    if 'parametric_eq_config' in args:
        if not os.path.isfile(args['parametric_eq_config']):
            # Named configurations, split by commas
            args['parametric_eq_config'] = args['parametric_eq_config'].split(',')

    if 'fs' in args and args['fs'] is not None:
        args['fs'] = [int(x) for x in args['fs'].split(',')]

    if thread_count := args.get('thread_count'):
        if thread_count == 'max':
            args['thread_count'] = multiprocessing.cpu_count()
        else:
            try:
                thread_count = int(thread_count)
            except ValueError:
                raise ValueError('"--thread_count" must have a value greater than 0 or equal to "max"!')
            if thread_count <= 0:
                raise ValueError('"--thread_count" must have a value greater than 0 or equal to "max"!')
            args['thread_count'] = thread_count
    return args


if __name__ == '__main__':
    batch_processing(**cli_args())
