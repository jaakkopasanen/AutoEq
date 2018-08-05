# -*- coding: utf-8 -*-

import os
from frequency_response import FrequencyResponse

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    # # Innerfidelity on-ear SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'onear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
    #     compensation=os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=4.0
    # )
    #
    # # Innerfidelity in-ear SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'inear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
    #     compensation=os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=6.0
    # )
    #
    # # Innerfidelity earbud SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'earbud'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
    #     compensation=os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=0.0
    # )
    #
    # Headphone.com on-ear SBAF-Serious
    FrequencyResponse.main(
        input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'onear'),
        output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
        compensation=os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'),
        calibration=os.path.join(ROOT_DIR, 'calibration', 'headphonecom_to_innerfidelity.csv'),
        equalize=True,
        parametric_eq=True,
        max_filters=[5, 5],
        bass_boost=4.0
    )
    #
    # # Headphone.com in-ear SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'inear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
    #     compensation=os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'),
    #     calibration=os.path.join(ROOT_DIR, 'calibration', 'headphonecom_to_innerfidelity.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=6.0
    # )
    #
    # # Headphone.com earbud SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'earbud'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'sbaf-serious'),
    #     compensation=os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'),
    #     calibration=os.path.join(ROOT_DIR, 'calibration', 'headphonecom_to_innerfidelity.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=0.0
    # )


if __name__ == '__main__':
    main()
