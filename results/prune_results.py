# -*- coding: utf-8 -*-

import os
import sys
import shutil
import argparse
from pathlib import Path
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))

DIR_PATH = Path(__file__).parent
ROOT_PATH = DIR_PATH.parent


def prune_results(dry_run=False, databases=None):
    for db in databases:
        measurements = list(ROOT_PATH.joinpath('measurements', db, 'data').glob('**/*.png'))
        # TODO: Unique measurement (name, form, rig), not just name
        result_files = list(DIR_PATH.joinpath(db).glob('**/*.png'))
        for path in result_files:
            item = measurement_index.find_one(true_name=path.name.replace('.png', ''))
            if not item:
                if not dry_run:
                    shutil.rmtree(path.parent)
                print(f'Removed "{path}"')


def _cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', dest='dry_run',
                        help='Check which results would be removed without removing.')
    parser.add_argument('--databases', type=str, required=True,
                        help='Comma separated list of measurement database names to modify. Use "all" to include '
                             'all of them.')
    args = parser.parse_args()
    if args.databases.lower() != 'all':
        args.databases = args.databases.split(',')
    return vars(args)


if __name__ == '__main__':
    prune_results(**_cli())
