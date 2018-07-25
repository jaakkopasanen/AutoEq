# -*- coding: utf-8 -*-

from frequency_response import FrequencyResponse
import matplotlib.pyplot as plt


def main():
    dt770 = FrequencyResponse.read_from_csv('headphonecom/data/onear/Beyerdynamic DT770/Beyerdynamic DT770.csv')
    dt770.interpolate()
    he400s = FrequencyResponse.read_from_csv('innerfidelity/data/onear/HiFiMAN HE400S/HiFiMAN HE400S.csv')
    he400s.interpolate()
    calibration = FrequencyResponse.read_from_csv('calibration/headphonecom_raw_to_innerfidelity_raw.csv')
    calibration.interpolate()
    compensation = FrequencyResponse.read_from_csv('innerfidelity/resources/innerfidelity_compensation_2017.csv')
    compensation.interpolate()

    dt770_calibrated = FrequencyResponse(name='DT 770 calibrated', frequency=dt770.frequency, raw=dt770.raw)
    dt770_calibrated.calibrate(calibration)
    dt770_calibrated.compensate(he400s)
    #dt770_calibrated.compensate(compensation)
    dt770_calibrated.center()
    dt770_calibrated.smoothen()
    dt770_calibrated.equalize(smoothen=True)
    dt770_calibrated.plot_graph(a_min=-20, a_max=20)


if __name__ == '__main__':
    main()
