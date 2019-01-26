# -*- coding: utf-8 -*-

from frequency_response import FrequencyResponse


def main():
    fr = FrequencyResponse.read_from_csv('my_data/HiFiMAN HE400S/HiFiMAN HE400S.csv')
    fr.compensate(
        FrequencyResponse.read_from_csv('innerfidelity/resources/innerfidelity_compensation_sbaf-serious.csv'),
        bass_boost=4.0,
        bass_boost_f_lower=35,
        bass_boost_f_upper=280
    )
    fr.equalize()
    ir = fr.minimum_phase_impulse_response(fs=48000, filter_length=2 ** 14)


if __name__ == '__main__':
    main()
