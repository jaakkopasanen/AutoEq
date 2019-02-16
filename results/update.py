# -*- coding: utf-8 -*-

import os
import sys
import argparse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--new_only', action='store_true', help='Process only new measurements?')
    arg_parser.add_argument('--innerfidelity', action='store_true', help='Process Innerfidelity measurements?')
    arg_parser.add_argument('--headphonecom', action='store_true', help='Process Headphone.com measurements?')
    arg_parser.add_argument('--oratory1990', action='store_true', help='Process oratory1990 measurements?')
    arg_parser.add_argument('--rtings', action='store_true', help='Process Rtings measurements?')
    arg_parser.add_argument('--referenceaudioanalyzer', action='store_true',
                            help='Process Reference Audio Analyzer measurements?')
    arg_parser.add_argument('--onear', action='store_true', help='Process on-ear measurements?')
    arg_parser.add_argument('--inear', action='store_true', help='Process in-ear measurements?')
    arg_parser.add_argument('--earbud', action='store_true', help='Process ear bud measurements?')
    cli_args = arg_parser.parse_args()

    new_only = bool(cli_args.new_only)
    innerfidelity = bool(cli_args.innerfidelity)
    headphonecom = bool(cli_args.headphonecom)
    oratory1990 = bool(cli_args.oratory1990)
    rtings = bool(cli_args.rtings)
    referenceaudioanalyzer = bool(cli_args.referenceaudioanalyzer)
    onear = bool(cli_args.onear)
    inear = bool(cli_args.inear)
    earbud = bool(cli_args.earbud)

    if not innerfidelity and not headphonecom and not oratory1990 and not rtings and not referenceaudioanalyzer:
        innerfidelity = True
        headphonecom = True
        oratory1990 = True
        rtings = True
        referenceaudioanalyzer = True
    if not onear and not inear and not earbud:
        onear = True
        inear = True
        earbud = True

    if_compensation = os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv')
    hp_compensation = os.path.join(ROOT_DIR, 'headphonecom', 'resources', 'headphonecom_compensation_sbaf-serious.csv')
    rtings_compensation = os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation_avg.csv')

    if innerfidelity:
        if onear:
            # Innerfidelity on-ear SBAF-Serious
            print('\nProcessing Innerfidelity on-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
                new_only=new_only,
                compensation=if_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                bass_boost=4.0
            )

        if inear:
            # Innerfidelity in-ear SBAF-Serious
            print('\nProcessing Innerfidelity in-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
                new_only=new_only,
                compensation=if_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                iem_bass_boost=6.0
            )

        if earbud:
            # Innerfidelity earbud SBAF-Serious
            print('\nProcessing Innerfidelity earbud measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
                new_only=new_only,
                compensation=if_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
            )

    if headphonecom:
        if onear:
            # Headphone.com on-ear SBAF-Serious
            print('\nProcessing Headphone.com on-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
                new_only=new_only,
                compensation=hp_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                bass_boost=4.0
            )

        if inear:
            # Headphone.com in-ear SBAF-Serious
            print('\nProcessing Headphone.com in-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
                new_only=new_only,
                compensation=hp_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                iem_bass_boost=6.0
            )

        if earbud:
            # Headphone.com earbud SBAF-Serious
            print('\nProcessing Headphone.com earbud measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
                new_only=new_only,
                compensation=hp_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
            )

    if oratory1990:
        if onear:
            # Oratory1990 on-ear
            print('\nProcessing oratory1990 on-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'oratory1990', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'harman_over-ear_2018'),
                new_only=new_only,
                compensation=os.path.join(ROOT_DIR, 'compensation', 'harman_over-ear_2018_wo_bass.csv'),
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                bass_boost=4.0
            )

        if inear:
            # Oratory1990 in-ear Harman in-ear 2017-1
            print('\nProcessing oratory1990 in-ear measurements with Harman in-ear 2017-1 target...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'oratory1990', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'harman_in-ear_2017-1'),
                new_only=new_only,
                compensation=os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2017-1_wo_bass.csv'),
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                iem_bass_boost=6.0
            )

            # Oratory1990 in-ear Usound
            print('\nProcessing oratory1990 in-ear measurements with Usound target...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'oratory1990', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'usound'),
                new_only=new_only,
                compensation=os.path.join(ROOT_DIR, 'compensation', 'usound_wo_bass.csv'),
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                iem_bass_boost=6.0
            )

        if earbud:
            # Oratory1990 earbud
            print('\nProcessing oratory1990 ear bud measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'oratory1990', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'harman_in-ear_2017-1'),
                new_only=new_only,
                compensation=os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2017-1_wo_bass.csv'),
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
            )

    if rtings:
        if onear:
            # Rtings on-ear Avg
            print('\nProcessing Rtings on-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'avg'),
                new_only=new_only,
                compensation=rtings_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                bass_boost=4.0
            )

        if inear:
            # Rtings in-ear Avg
            print('\nProcessing Rtings in-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'avg'),
                new_only=new_only,
                compensation=rtings_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                iem_bass_boost=6.0
            )

        if earbud:
            # Rtings earbud Avg
            print('\nProcessing Rtings in-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'avg'),
                new_only=new_only,
                compensation=rtings_compensation,
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5]
            )

    if onear:
        if referenceaudioanalyzer:
            # Reference Audio Analyzer on-ear
            print('\nProcessing Reference Audio Analyzer on-ear measurements...')
            FrequencyResponse.main(
                input_dir=os.path.join(ROOT_DIR, 'referenceaudioanalyzer', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results', 'referenceaudioanalyzer', 'zero'),
                new_only=new_only,
                compensation=os.path.join(ROOT_DIR, 'compensation', 'zero.csv'),
                equalize=True,
                parametric_eq=True,
                max_filters=[5, 5],
                bass_boost=4.0
            )


if __name__ == '__main__':
    main()
