# -*- coding: utf-8 -*-

"""
This script transforms innerfidelity old compensated measurements into raw microphone data.

Files will be changed in-place. Take backups if you wish to keep the old data.

Specify input path glob in a loop.
"""

import os
from glob import glob
from autoeq.frequency_response import FrequencyResponse


def main():
    compensation = FrequencyResponse.read_from_csv(os.path.join('resources', 'innerfidelity_compensation_2016.csv'))
    compensation.center()
    for file in glob(os.path.join('data', 'adhoc', '**', '*.csv'), recursive=True):
        fr = FrequencyResponse.read_from_csv(file)
        print(fr.name)
        fr.interpolate()
        fr.center()
        fr.raw += compensation.raw
        fr.write_to_csv(file)


if __name__ == '__main__':
    main()
