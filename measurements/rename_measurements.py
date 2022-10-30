# -*- coding: utf-8 -*-

import os
import sys
from argparse import ArgumentParser
from glob import glob
import shutil
import re
from autoeq.constants import DBS
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.name_index import NameIndex, NameItem
from measurements.manufacturer_index import ManufacturerIndex

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def rename_manufacturers():
    manufacturers = ManufacturerIndex()

    for db in DBS:
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
    for db in DBS:
        # Rename existing files
        existing_files = list(glob(os.path.join(DIR_PATH, db, 'data', '**', '*.csv'), recursive=True))
        for fp in existing_files:
            dir_path, name = os.path.split(fp)
            name = name.replace('.csv', '')
            norm_name = re.sub(r'[^a-z0-9]', '', name, flags=re.IGNORECASE)
            if norm_name not in groups:
                groups[norm_name] = set()
            groups[norm_name].add(name)

    groups = {norm: group for norm, group in groups.items() if len(group) > 1}

    with open(os.path.join(DIR_PATH, 'name_groups.tsv'), 'w', encoding='utf-8') as fh:
        s = '\n'.join(sorted(['\t'.join(names) for norm_name, names in groups.items()], key=lambda x: x.lower()))
        fh.write(s + '\n')


def rename_groups(databases=DBS):
    with open(os.path.join(DIR_PATH, 'name_groups.tsv'), 'r', encoding='utf-8') as fh:
        lines = fh.read().strip().split('\n')

    # First column is always the true name
    # Create dict with each false name as key and it's true name as value
    name_map = dict()
    for line in lines:
        names = line.split('\t')
        if len(names) > 1:
            for i in range(1, len(names)):
                name_map[names[i]] = names[0]

    # Read name indexes and existing files for all supported measurement databases
    dbs = []
    for db in databases:
        if os.path.isfile(os.path.join(DIR_PATH, db, 'name_index.tsv')):
            # Read name index
            name_index = NameIndex.read_tsv(os.path.join(DIR_PATH, db, 'name_index.tsv'))
        else:
            # No name index, create one anew
            name_index = NameIndex()
        # Read all the existing files for the database
        files = list(glob(os.path.join(DIR_PATH, db, 'data', '**', '*.csv'), recursive=True))
        files = [{'name': os.path.split(file)[1].replace('.csv', ''), 'path': file} for file in files]
        # Save both to dbs
        dbs.append({'name': db, 'name_index': name_index, 'files': files})

    for old_name, new_name in name_map.items():
        print(f'"{old_name}" -> "{new_name}"')
        for db in dbs:
            name_index = db['name_index']
            # Replace true names in name index with the new name
            updated_item = False
            matches = name_index.find(true_name=old_name)
            for item in matches.items:
                if new_name == 'ignore':
                    name_index.update(
                        NameItem(false_name=item.false_name, true_name=item.true_name, form='ignore'),
                        true_name=old_name
                    )
                    print(f'    Updated item: "{item.false_name}", "{new_name}", "ignore"')
                else:
                    name_index.update(
                        NameItem(false_name=item.false_name, true_name=new_name, form=item.form),
                        true_name=old_name
                    )
                    print(f'    Updated item: "{item.false_name}", "{new_name}", "{item.form}"')
                updated_item = True

            # Rename existing files
            for name, path in [(f['name'], f['path']) for f in db['files'] if f['name'].lower() == old_name.lower()]:
                if new_name == 'ignore':
                    print(f'    Removing "{os.path.split(path)[0]}"')
                    shutil.rmtree(os.path.split(path)[0])
                    if not updated_item:
                        name_index.add(NameItem(false_name=old_name, true_name=None, form='ignore'))
                        print(f'    Added item: "{old_name}", "", "ignore"')
                    continue

                new_path = re.sub(re.escape(name), new_name, path)
                print(f'    Moving "{os.path.relpath(path, DIR_PATH)}" to "{os.path.relpath(new_path, DIR_PATH)}"')
                os.makedirs(os.path.split(new_path)[0], exist_ok=True)
                shutil.move(path, new_path)
                os.rmdir(os.path.join(path, os.pardir))
                matches = name_index.find(true_name=new_name)
                if not matches:
                    d = path
                    while True:
                        d, f = os.path.split(d)
                        if f in ['onear', 'inear', 'earbud']:
                            form = f
                            break
                    name_index.add(NameItem(false_name=old_name, true_name=new_name, form=form))
                    print(f'    Added item: "{old_name}", "{new_name}", "{form}"')
        print()

    for db in dbs:
        db['name_index'].write_tsv(os.path.join(DIR_PATH, db['name'], 'name_index.tsv'))


def _cli():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--databases', type=str, required=True,
                            help='Comma separated list of measurement database names to modify. Use "all" to include '
                                 'all of them.')
    args = arg_parser.parse_args()
    if args.databases.lower() != 'all':
        return {'databases': args.databases.split(',')}
    return {}


if __name__ == '__main__':
    # rename_manufacturers()
    # group_measurements()
    rename_groups(**_cli())
