# -*- coding: utf-8 -*-

import os
import argparse
from frequency_response import FrequencyResponse

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--new_only', action='store_true', help='Process only new measurements?')
    cli_args = arg_parser.parse_args()
    new_only = bool(cli_args.new_only)

    if_compensation = os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv')
    hp_compensation = os.path.join(ROOT_DIR, 'headphonecom', 'resources', 'headphonecom_compensation_sbaf-serious.csv')
    rtings_compensation = os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation_avg.csv')

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

    # Rtings earbud Avg
    print('\nProcessing Rtings inear measurements...')
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'earbud'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'avg'),
        new_only=new_only,
        compensation=rtings_compensation,
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5]
    )


if __name__ == '__main__':
    main()
