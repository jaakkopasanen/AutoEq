# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.name_index import NameIndex, NameItem

DIR_PATH = Path(__file__).parent


def rename_measurements(renames, dry_run=False):
    dbs = {}
    for db_name in ['crinacle', 'headphonecom', 'innerfidelity', 'oratory1990', 'rtings']:
        name_index = NameIndex.read_tsv(os.path.join(DIR_PATH, db_name, 'name_index.tsv'))
        files = DIR_PATH.joinpath(db_name, 'data').glob('**/*.csv')  # Read all the existing files in the database
        dbs[db_name] = {'name': db_name, 'name_index': name_index, 'measurements': files}

    # TODO: Check that all DBs exist
    # TODO: Check that all old names exist in specified DBs
    # TODO: Check that all manufacturers exist for new names
    # TODO: Remove results?

    for rename in renames:
        if not rename['old_name']:
            raise ValueError(f'Missing old_name for {rename}')
        if not rename['new_name']:
            raise ValueError(f'Missing new_name for {rename}')
        for db_name in rename['dbs']:
            db = dbs[db_name]
            for old_path in db['measurements']:
                if old_path.name.replace('.csv', '') == rename['old_name']:
                    new_path = old_path.parent.joinpath(f'{rename["new_name"]}.csv')
                    # Removing old file and writing contents to a new one to work around Windows' case insensitive paths
                    with open(old_path) as fh:
                        contents = fh.read()
                    try:
                        if not dry_run:
                            old_path.unlink()
                            with open(new_path, 'w') as fh:
                                fh.write(contents)
                        print(f'Renamed "{old_path.relative_to(DIR_PATH)}" as "{new_path.relative_to(DIR_PATH)}"')
                    except Exception as err:
                        print(f'Failed to rename "{rename["old_name"]}". Restoring old file.')
                        if not dry_run:
                            with open(old_path, 'w') as fh:
                                fh.write(contents)

                    name_item = db['name_index'].find_one(true_name=rename['old_name'])
                    if name_item is None:
                        print(f'Name index item "{rename["old_name"]}" doesn\'t exist!')
                        continue
                    if not dry_run:
                        db['name_index'].update(
                            NameItem(
                                false_name=name_item.false_name,
                                true_name=rename['new_name'],
                                form=name_item.form
                            ),
                            true_name=name_item.true_name
                        )
                        db['name_index'].write_tsv(DIR_PATH.joinpath(db['name'], 'name_index.tsv'))
