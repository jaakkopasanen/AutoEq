# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import shutil
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.name_index import NameIndex

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main():
    for db in ['crinacle', 'oratory1990', 'rtings']:
        name_index = NameIndex.read_tsv(os.path.join(DIR_PATH, db, 'name_index.tsv'))
        for fp in glob(os.path.join(DIR_PATH, db, 'data', '*', '*')):
            d, name = os.path.split(fp)
            _, form = os.path.split(d)
            if not name_index.find(true_name=name, form=form):
                print(f'Removing: "{fp}"')
                shutil.rmtree(fp)


if __name__ == '__main__':
    main()
