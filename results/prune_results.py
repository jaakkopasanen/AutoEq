# -*- coding: utf-8 -*-

import os
import sys
import shutil
from glob import glob
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    for db in ['crinacle', 'headphonecom', 'innerfidelity', 'oratory1990', 'referenceaudioanalyzer', 'rtings']:
        if db == 'referenceaudioanalyzer':
            continue
        measurements = list(glob(
            os.path.join(ROOT_DIR, 'measurements', db, 'data', '**', '*.csv'),
            recursive=True
        ))
        measurements = [os.path.split(measurement)[1].lower().replace('.csv', '') for measurement in measurements]
        for path in glob(os.path.join(ROOT_DIR, 'results', db, '*', '*')):
            _, name = os.path.split(path)
            if name.lower() not in measurements and name != 'README.md':
                print(f'Removing "{path}" ...')
                shutil.rmtree(path)


if __name__ == '__main__':
    main()
