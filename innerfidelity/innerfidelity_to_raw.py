# -*- coding: utf-8 -*-

"""This script transforms innerfidelity old compensated measurements into raw microphone data."""

import os
from glob import glob
from frequency_response import FrequencyResponse


def main():
    trans = FrequencyResponse.read_from_csv(os.path.join('resources', 'innerfidelity_transformation.csv'))
    trans.interpolate()
    trans.center()
    comp = FrequencyResponse.read_from_csv(os.path.join('resources', 'innerfidelity_compensation.csv'))
    comp.interpolate()
    comp.center()
    for file in glob(os.path.join('data', '**', '*.csv'), recursive=True):
        fr = FrequencyResponse.read_from_csv(file)
        print(fr.name)
        fr.interpolate()
        fr.center()
        fr.raw -= trans.raw
        fr.raw += comp.raw
        fr.write_to_csv(file)


if __name__ == '__main__':
    main()
