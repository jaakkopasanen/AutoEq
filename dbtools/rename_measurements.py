# -*- coding: utf-8 -*-

import sys
from pathlib import Path
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.name_index import NameIndex, NameItem
from dbtools.manufacturer_index import ManufacturerIndex, UnknownManufacturerError
from dbtools.constants import MEASUREMENTS_PATH


class UnknownDatabaseError(Exception):
    pass


def rename_measurements(renames, dry_run=False):
    dbs = {}
    for db_name in ['crinacle', 'headphonecom', 'innerfidelity', 'oratory1990', 'rtings']:
        name_index = NameIndex.read_tsv(MEASUREMENTS_PATH.joinpath(db_name, 'name_index.tsv'))
        # Read all the existing files in the database
        files = list(MEASUREMENTS_PATH.joinpath(db_name, 'data').glob('**/*.csv'))
        dbs[db_name] = {'name': db_name, 'name_index': name_index, 'measurements': files}

    manufacturers = ManufacturerIndex()
    for rename in renames:
        if not rename['old_name']:
            raise ValueError(f'Missing old_name for {rename}')
        if not rename['new_name']:
            raise ValueError(f'Missing new_name for {rename}')
        manufacturer, match = manufacturers.find(rename['new_name'])
        if manufacturer is None:
            raise UnknownManufacturerError(f'Manufacturer for "{rename["new_name"]}" is unknown')
        for db_name in rename['dbs']:
            if db_name not in dbs:
                raise UnknownDatabaseError(f'Database "{db_name}" in {rename} doesn\'t exist')
            db = dbs[db_name]
            for old_path in db['measurements']:
                if old_path.name.replace('.csv', '') == rename['old_name']:
                    if not old_path.exists():
                        raise FileNotFoundError(f'Measurement in "{old_path}" doesn\'t exist')
                    new_path = old_path.parent.joinpath(f'{rename["new_name"]}.csv')
                    # Removing old file and writing contents to a new one to work around Windows' case insensitive paths
                    with open(old_path) as fh:
                        contents = fh.read()
                    try:
                        if not dry_run:
                            old_path.unlink()
                            with open(new_path, 'w') as fh:
                                fh.write(contents)
                        print(f'Renamed "{old_path.relative_to(MEASUREMENTS_PATH)}" as "{new_path.relative_to(MEASUREMENTS_PATH)}"')
                    except Exception as err:
                        print(f'Failed to rename "{rename["old_name"]}". Restoring old file.')
                        if not dry_run:
                            with open(old_path, 'w') as fh:
                                fh.write(contents)

                    name_item = db['name_index'].find_one(name=rename['old_name'])
                    if len(db['name_index']) > 0 and name_item is None:
                        continue
                    if not dry_run:
                        db['name_index'].update(NameItem(
                            name_item.source_name, rename['new_name'], name_item.form, url=name_item.url,
                            rig=name_item.rig),
                        )
                        db['name_index'].write_tsv(MEASUREMENTS_PATH.joinpath(db['name'], 'name_index.tsv'))
