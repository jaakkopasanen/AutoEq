# -*- coding: utf-8 -*-

import os
import sys
import shutil
from glob import glob
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from constants import DBS, ROOT_DIR


def main():
    for db in DBS:
        measurements = list(glob(
            os.path.join(ROOT_DIR, 'measurements', db, 'data', '**', '*.csv'),
            recursive=True
        ))
        measurements = [os.path.split(measurement)[1].replace('.csv', '') for measurement in measurements]
        for path in glob(os.path.join(ROOT_DIR, 'results', db, '**', '*.csv'), recursive=True):
            dir_path, file_name = os.path.split(path)
            name = file_name.replace('.csv', '')
            if name not in measurements and name != 'README.md':
                print(f'Removing "{dir_path}"')
                shutil.rmtree(dir_path)


if __name__ == '__main__':
    main()
