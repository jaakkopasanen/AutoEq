# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import shutil
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.name_index import NameIndex, NameItem
from measurements.manufacturer_index import ManufacturerIndex

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main():
    manufacturers = ManufacturerIndex()

    for db in ['crinacle', 'headphonecom', 'innerfidelity', 'oratory1990', 'rtings']:
        if os.path.isfile(os.path.join(DIR_PATH, db, 'name_index.tsv')):
            name_index = NameIndex.read_tsv(os.path.join(DIR_PATH, db, 'name_index.tsv'))
        else:
            name_index = NameIndex()

        for item in name_index.items:
            if item.form == 'ignore' or not item.true_name:
                continue
            true_name = manufacturers.replace(item.true_name)
            if true_name is None:
                print(f'"{name}" not found in manufacturers')
                continue
            if true_name == item.true_name:
                continue

            print(f'Renamed "{item.true_name}" with "{true_name}"')
            name_index.update(
                NameItem(item.false_name, true_name, item.form),
                item.false_name, item.true_name, item.form
            )

        if name_index:
            name_index.write_tsv(os.path.join(DIR_PATH, db, 'name_index.tsv'))

        existing = list(glob(os.path.join(DIR_PATH, db, 'data', '**', '*.csv'), recursive=True))
        for fp in existing:
            dir_path, name = os.path.split(fp)
            name = name.replace('.csv', '')
            true_name = manufacturers.replace(name)
            if true_name is None:
                print(f'"{name}" not found in manufacturers')
                continue
            dir_path = os.path.abspath(os.path.join(dir_path, os.pardir, true_name))
            new_path = os.path.join(dir_path, f'{true_name}.csv')
            if new_path != fp:
                print(f'Moved "{os.path.relpath(fp, DIR_PATH)}" to "{os.path.relpath(new_path, DIR_PATH)}"')
                shutil.move(fp, new_path)


if __name__ == '__main__':
    main()
