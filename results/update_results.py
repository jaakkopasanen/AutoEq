# -*- coding: utf-8 -*-

import os
import sys
import argparse

from autoeq.constants import PEQ_CONFIGS

sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from autoeq.batch_processing import batch_processing

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main(
        new_only=True,
        innerfidelity=False,
        headphonecom=False,
        oratory1990=False,
        rtings=False,
        crinacle=False,
        overear=False,
        inear=False,
        earbud=False):
    innerfidelity_overear = os.path.join(ROOT_DIR, 'compensation', 'innerfidelity_harman_over-ear_2018_wo_bass.csv')
    innerfidelity_inear = os.path.join(ROOT_DIR, 'compensation', 'innerfidelity_autoeq_in-ear.csv')
    headphonecom_overear = os.path.join(ROOT_DIR, 'compensation', 'headphonecom_harman_over-ear_2018_wo_bass.csv')
    headphonecom_inear = os.path.join(ROOT_DIR, 'compensation', 'headphonecom_autoeq_in-ear.csv')
    rtings_overear = os.path.join(ROOT_DIR, 'compensation', 'rtings_harman_over-ear_2018_wo_bass.csv')
    rtings_inear = os.path.join(ROOT_DIR, 'compensation', 'rtings_autoeq_in-ear.csv')
    autoeq_inear = os.path.join(ROOT_DIR, 'compensation', 'autoeq_in-ear.csv')
    harman_overear = os.path.join(ROOT_DIR, 'compensation', 'harman_over-ear_2018_wo_bass.csv')
    crinacle_ears711_overear = os.path.join(ROOT_DIR, 'compensation', 'crinacle_harman_over-ear_2018_wo_bass.csv')
    diffuse_field_5128_tilted = os.path.join(ROOT_DIR, 'compensation', 'diffuse_field_5128_-1dBpoct.csv')
    eq_kwargs = {
        'new_only': new_only,
        'parametric_eq': True,
        'parametric_eq_config': [PEQ_CONFIGS['4_PEAKING_WITH_LOW_SHELF'], PEQ_CONFIGS['4_PEAKING_WITH_HIGH_SHELF']],
        'ten_band_eq': True,
        'convolution_eq': True,
        'fs': [44100, 48000],
        'thread_count': 0,
    }
    bass0 = {'bass_boost_fc': 105, 'bass_boost_q': 0.7, 'bass_boost_gain': 0.0}
    bass6 = {'bass_boost_fc': 105, 'bass_boost_q': 0.7, 'bass_boost_gain': 6.0}
    bass95 = {'bass_boost_fc': 105, 'bass_boost_q': 0.7, 'bass_boost_gain': 9.5}

    if innerfidelity:
        if overear:
            print('\nProcessing Innerfidelity over-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'innerfidelity', 'data', 'over-ear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Innerfidelity', 'over-ear'),
                compensation=innerfidelity_overear,
                **bass6, **eq_kwargs
            )

        if inear:
            print('\nProcessing Innerfidelity in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'innerfidelity', 'data', 'in-ear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Innerfidelity', 'in-ear'),
                compensation=innerfidelity_inear,
                **bass95, **eq_kwargs
            )

        if earbud:
            print('\nProcessing Innerfidelity earbud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'innerfidelity', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Innerfidelity', 'earbud'),
                compensation=innerfidelity_inear,
                **bass0, **eq_kwargs
            )

    if headphonecom:
        if overear:
            print('\nProcessing Headphone.com on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'headphonecom', 'data', 'over-ear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Headphone.com Legacy', 'over-ear'),
                compensation=headphonecom_overear,
                **bass6, **eq_kwargs
            )

        if inear:
            print('\nProcessing Headphone.com in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'headphonecom', 'data', 'in-ear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Headphone.com Legacy', 'in-ear'),
                compensation=headphonecom_inear,
                **bass95, **eq_kwargs
            )

        if earbud:
            print('\nProcessing Headphone.com earbud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'headphonecom', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Headphone.com Legacy', 'earbud'),
                compensation=headphonecom_inear,
                **bass0, **eq_kwargs
            )

    if oratory1990:
        if overear:
            print('\nProcessing oratory1990 on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'oratory1990', 'data', 'over-ear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'over-ear'),
                compensation=harman_overear,
                **bass6, **eq_kwargs
            )

        if inear:
            print('\nProcessing oratory1990 in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'oratory1990', 'data', 'in-ear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'in-ear'),
                compensation=autoeq_inear,
                **bass95, **eq_kwargs
            )

        if earbud:
            print('\nProcessing oratory1990 ear bud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'oratory1990', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'earbud'),
                compensation=autoeq_inear,
                **bass0, **eq_kwargs
            )

    if rtings:
        if overear:
            # Rtings on-ear Avg
            print('\nProcessing Rtings on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'rtings', 'data', 'over-ear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Rtings', 'over-ear'),
                compensation=rtings_overear,
                **bass6, **eq_kwargs
            )

        if inear:
            print('\nProcessing Rtings in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'rtings', 'data', 'in-ear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Rtings', 'in-ear'),
                compensation=rtings_inear,
                **bass95, **eq_kwargs
            )

        if earbud:
            print('\nProcessing Rtings earbud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'rtings', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'Rtings', 'earbud'),
                compensation=rtings_inear,
                **bass0, **eq_kwargs
            )

    if crinacle:
        if overear:
            print('\nProcessing Crinacle Ears-711 on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'crinacle', 'data', 'over-ear', 'EARS + 711'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'crinacle', 'EARS + 711 over-ear'),
                compensation=crinacle_ears711_overear,
                **bass6, **eq_kwargs
            )
            print('\nProcessing Crinacle GRAS 43AG-7 on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'crinacle', 'data', 'over-ear', 'GRAS 43AG-7'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'crinacle', 'GRAS 43AG-7 over-ear'),
                compensation=harman_overear,
                **bass6, **eq_kwargs
            )
        if inear:
            print('\nProcessing Crinacle 711 in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'crinacle', 'data', 'in-ear', '711'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'crinacle', '711 in-ear'),
                compensation=autoeq_inear,
                **bass95, **eq_kwargs
            )
            print('\nProcessing Crinacle 4620 in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'crinacle', 'data', 'in-ear', 'Bruel & Kjaer 4620'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'crinacle', 'Bruel & Kjaer 4620 in-ear'),
                compensation=diffuse_field_5128_tilted,
                **bass0, **eq_kwargs
            )


def _cli():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--new_only', action='store_true', help='Process only new measurements?')
    arg_parser.add_argument('--innerfidelity', action='store_true', help='Process Innerfidelity measurements?')
    arg_parser.add_argument('--headphonecom', action='store_true', help='Process Headphone.com measurements?')
    arg_parser.add_argument('--oratory1990', action='store_true', help='Process oratory1990 measurements?')
    arg_parser.add_argument('--rtings', action='store_true', help='Process Rtings measurements?')
    arg_parser.add_argument('--crinacle', action='store_true', help='Process Crinacle measurements?')
    arg_parser.add_argument('--overear', action='store_true', help='Process on-ear measurements?')
    arg_parser.add_argument('--inear', action='store_true', help='Process in-ear measurements?')
    arg_parser.add_argument('--earbud', action='store_true', help='Process ear bud measurements?')
    cli_args = arg_parser.parse_args()
    return vars(cli_args)


if __name__ == '__main__':
    main(**_cli())
