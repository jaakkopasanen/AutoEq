# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
from constants import ROOT_DIR
from frequency_response import FrequencyResponse


def main():
    paths = list(glob(os.path.join(ROOT_DIR, 'measurements', '**', '*.csv'), recursive=True))
    paths += list(glob(os.path.join(ROOT_DIR, 'compensation', '*.csv'), recursive=True))
    for file_path in paths:
        fr = FrequencyResponse.read_from_csv(file_path)
        fr.interpolate()
        fr.write_to_csv(file_path)


if __name__ == '__main__':
    main()
