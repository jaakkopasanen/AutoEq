# -*- coding: utf-8 -*-

import os
from frequency_response import FrequencyResponse

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    if_compensation = os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv')
    hp_compensation = os.path.join(ROOT_DIR, 'headphonecom', 'resources', 'headphonecom_compensation_sbaf-serious.csv')

    # Innerfidelity on-ear SBAF-Serious
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'rename', 'onear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
        compensation=if_compensation,
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        bass_boost=4.0
    )

    # Innerfidelity in-ear SBAF-Serious
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'rename', 'inear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
        compensation=if_compensation,
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        iem_bass_boost=6.0
    )
    #
    # # Innerfidelity earbud SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'earbud'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
    #     compensation=if_compensation,
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    # )
    #
    # # Headphone.com on-ear SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'onear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
    #     compensation=hp_compensation,
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=4.0
    # )
    #
    # # Headphone.com in-ear SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'inear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
    #     compensation=hp_compensation,
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     iem_bass_boost=6.0
    # )
    #
    # # Headphone.com earbud SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'earbud'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
    #     compensation=hp_compensation,
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    # )
    #
    # # Oratory1990 on-ear
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'oratory1990', 'data', 'onear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'harman_over-ear_2018'),
    #     compensation=os.path.join(ROOT_DIR, 'compensation', 'harman_over-ear_2018_wo_bass.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=4.0
    # )
    #
    # # Oratory1990 in-ear
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'oratory1990', 'data', 'inear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'harman_in-ear_2017-1'),
    #     compensation=os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2017-1_wo_bass.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     iem_bass_boost=6.0
    # )
    #
    # # Oratory1990 earbud
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'oratory1990', 'data', 'earbud'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'oratory1990', 'harman_in-ear_2017-1'),
    #     compensation=os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2017-1_wo_bass.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    # )

    # Rtings on-ear native
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'rename', 'onear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'rtings'),
        compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation.csv'),
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        bass_boost=4.0
    )

    # Rtings in-ear native
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'rename', 'inear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'rtings'),
        compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation.csv'),
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        iem_bass_boost=6.0
    )

    # # Rtings earbud native
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'earbud'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'rtings'),
    #     compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5]
    # )

    # Rtings on-ear SBAF Serious
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'rename', 'onear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'sbaf-serious'),
        compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation_sbaf-serious.csv'),
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        bass_boost=4.0
    )

    # Rtings in-ear SBAF Serious
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'rename', 'inear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'sbaf-serious'),
        compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation_sbaf-serious.csv'),
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        iem_bass_boost=6.0
    )

    # # Rtings earbud SBAF Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'earbud'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'sbaf-serious'),
    #     compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation_sbaf-serious.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5]
    # )

    # Rtings on-ear Avg
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'rename', 'onear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'avg'),
        compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation_avg.csv'),
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        bass_boost=4.0
    )

    # Rtings in-ear Avg
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'rename', 'inear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'avg'),
        compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation_avg.csv'),
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        iem_bass_boost=6.0
    )

    # # Rtings earbud Avg
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'rtings', 'data', 'earbud'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'rtings', 'avg'),
    #     compensation=os.path.join(ROOT_DIR, 'rtings', 'resources', 'rtings_compensation_avg.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5]
    # )


if __name__ == '__main__':
    main()
