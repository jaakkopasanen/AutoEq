# -*- coding: utf-8 -*-

import os
from frequency_response import FrequencyResponse

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    # # Innerfidelity SBAF-Serious
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'onear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'sbaf-serious'),
    #     compensation=os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_sbaf-serious.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=4.0
    # )

    # # Innerfidelity 2017
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'onear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'innerfidelity', 'innerfidelity2017'),
    #     compensation=os.path.join(ROOT_DIR, 'innerfidelity', 'resources', 'innerfidelity_compensation_2017.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=4.0
    # )

    # Headphone.com SBAF-Serious
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

    # # Headphone.com
    # FrequencyResponse.main(
    #     input_dir=os.path.join(ROOT_DIR, 'headphonecom', 'data', 'onear'),
    #     output_dir=os.path.join(ROOT_DIR, 'results', 'headphonecom', 'headphonecom'),
    #     compensation=os.path.join(ROOT_DIR, 'headphonecom', 'resources', 'headphonecom_compensation.csv'),
    #     equalize=True,
    #     parametric_eq=True,
    #     max_filters=[5, 5],
    #     bass_boost=4.0
    # )


if __name__ == '__main__':
    main()
