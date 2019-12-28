# -*- coding: utf-8 -*-

import os
import sys
import shutil
from glob import glob
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    for path in glob(os.path.join(ROOT_DIR, 'results', '*', '*', '*')):
        _path, name = os.path.split(path)
        _path, target = os.path.split(_path)
        _path, source = os.path.split(_path)
        if source == 'referenceaudioanalyzer':
            # Reference Audio Analyzer measurements are not organized by type
            measurements = list(glob(os.path.join(ROOT_DIR, source, 'data', '*')))
        else:
            measurements = list(glob(os.path.join(ROOT_DIR, source, 'data', '*', '*')))
        measurements = [os.path.split(measurement)[1].lower() for measurement in measurements]
        if name.lower() not in measurements and name != 'README.md':
            print(f'Removing "{path}" ...')
            shutil.rmtree(path)


if __name__ == '__main__':
    main()
