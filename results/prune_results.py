# -*- coding: utf-8 -*-

import os
import sys
import shutil
import argparse
from pathlib import Path
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))

DIR_PATH = Path(__file__).parent
ROOT_PATH = DIR_PATH.parent


target_to_source = {
    'crinacle/711 in-ear': ROOT_PATH.joinpath('measurements', 'crinacle', 'data', 'in-ear', '711'),
    'crinacle/Bruel & Kjaer 4620 in-ear': ROOT_PATH.joinpath('measurements', 'crinacle', 'data', 'in-ear', 'Bruel & Kjaer 4620'),
    'crinacle/EARS + 711 over-ear': ROOT_PATH.joinpath('measurements', 'crinacle', 'data', 'over-ear', 'EARS + 711'),
    'crinacle/GRAS 43AG-7 over-ear': ROOT_PATH.joinpath('measurements', 'crinacle', 'data', 'in-ear', 'GRAS 43AG-7'),
    'oratory1990/earbud': ROOT_PATH.joinpath('measurements', 'oratory1990', 'data', 'earbud'),
    'oratory1990/in-ear': ROOT_PATH.joinpath('measurements', 'oratory1990', 'data', 'in-ear'),
    'oratory1990/over-ear': ROOT_PATH.joinpath('measurements', 'oratory1990', 'data', 'over-ear'),
}


def prune_results(dry_run=False, databases=None):
    for db in databases:
        result_paths = list(DIR_PATH.joinpath(db).glob('**/*.png'))
        for result_path in result_paths:
            target_key = str(result_path.relative_to(DIR_PATH).parent.parent).replace('\\', '/')
            source_dir = target_to_source[target_key]
            if not source_dir.joinpath(f'{result_path.parent.name}.csv').exists():
                if not dry_run:
                    shutil.rmtree(result_path.parent)
                print(f'Removed "{result_path.parent.relative_to(DIR_PATH)}"')


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
