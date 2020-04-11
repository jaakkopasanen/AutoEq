# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import shutil
import re
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.name_index import NameIndex, NameItem
from measurements.manufacturer_index import ManufacturerIndex

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def rename_manufacturers():
    manufacturers = ManufacturerIndex()

    for db in ['crinacle', 'headphonecom', 'innerfidelity', 'oratory1990', 'referenceaudioanalyzer', 'rtings']:
        if os.path.isfile(os.path.join(DIR_PATH, db, 'name_index.tsv')):
            # Rename entries in name index if such exists
            name_index = NameIndex.read_tsv(os.path.join(DIR_PATH, db, 'name_index.tsv'))

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

                name_index.write_tsv(os.path.join(DIR_PATH, db, 'name_index.tsv'))

        # Rename existing files
        existing_files = list(glob(os.path.join(DIR_PATH, db, 'data', '**', '*.csv'), recursive=True))
        for fp in existing_files:
            dir_path, name = os.path.split(fp)
            name = name.replace('.csv', '')
            true_name = manufacturers.replace(name)
            if true_name is None:
                print(f'"{name}" not found in manufacturers')
                continue
            new_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir, true_name))
            new_file_path = os.path.join(new_dir_path, f'{true_name}.csv')
            os.makedirs(new_dir_path, exist_ok=True)
            if os.path.normcase(os.path.normpath(new_file_path)) != os.path.normcase(os.path.normpath(fp)):
                print(f'Moved "{os.path.relpath(fp, DIR_PATH)}" to "{os.path.relpath(new_file_path, DIR_PATH)}"')
                shutil.move(fp, new_file_path)
                try:
                    os.rmdir(dir_path)
                except OSError:
                    pass


def group_measurements():
    groups = dict()
    for db in ['crinacle', 'headphonecom', 'innerfidelity', 'oratory1990', 'referenceaudioanalyzer', 'rtings']:
        # Rename existing files
        existing_files = list(glob(os.path.join(DIR_PATH, db, 'data', '**', '*.csv'), recursive=True))
        for fp in existing_files:
            dir_path, name = os.path.split(fp)
            name = name.replace('.csv', '')
            norm_name = re.sub(r'[^a-z0-9]', '', name, flags=re.IGNORECASE)
            if norm_name not in groups:
                groups[norm_name] = set()
            groups[norm_name].add(name)

    with open(os.path.join(DIR_PATH, 'groups.tsv'), 'w', encoding='utf-8') as fh:
        s = '\n'.join(sorted(['\t'.join(names) for norm_name, names in groups.items()], key=lambda x: x.lower()))
        fh.write(s + '\n')


if __name__ == '__main__':
    # rename_manufacturers()
    group_measurements()
