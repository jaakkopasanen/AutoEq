# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
import shutil
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.constants import RESULTS_PATH, MEASUREMENTS_PATH

target_to_source = {
    'crinacle/711 in-ear': MEASUREMENTS_PATH.joinpath('crinacle', 'data', 'in-ear', '711'),
    'crinacle/Bruel & Kjaer 4620 in-ear': MEASUREMENTS_PATH.joinpath('crinacle', 'data', 'in-ear', 'Bruel & Kjaer 4620'),
    'crinacle/EARS + 711 over-ear': MEASUREMENTS_PATH.joinpath('crinacle', 'data', 'over-ear', 'EARS + 711'),
    'crinacle/GRAS 43AG-7 over-ear': MEASUREMENTS_PATH.joinpath('crinacle', 'data', 'over-ear', 'GRAS 43AG-7'),
    'oratory1990/earbud': MEASUREMENTS_PATH.joinpath('oratory1990', 'data', 'earbud'),
    'oratory1990/in-ear': MEASUREMENTS_PATH.joinpath('oratory1990', 'data', 'in-ear'),
    'oratory1990/over-ear': MEASUREMENTS_PATH.joinpath('oratory1990', 'data', 'over-ear'),
    'Rtings/earbud': MEASUREMENTS_PATH.joinpath('Rtings', 'data', 'earbud'),
    'Rtings/in-ear': MEASUREMENTS_PATH.joinpath('Rtings', 'data', 'in-ear'),
    'Rtings/over-ear': MEASUREMENTS_PATH.joinpath('Rtings', 'data', 'over-ear'),
    'Headphone.com Legacy/earbud': MEASUREMENTS_PATH.joinpath('Headphone.com Legacy', 'data', 'earbud'),
    'Headphone.com Legacy/in-ear': MEASUREMENTS_PATH.joinpath('Headphone.com Legacy', 'data', 'in-ear'),
    'Headphone.com Legacy/over-ear': MEASUREMENTS_PATH.joinpath('Headphone.com Legacy', 'data', 'over-ear'),
    'Innerfidelity/earbud': MEASUREMENTS_PATH.joinpath('Innerfidelity', 'data', 'earbud'),
    'Innerfidelity/in-ear': MEASUREMENTS_PATH.joinpath('Innerfidelity', 'data', 'in-ear'),
    'Innerfidelity/over-ear': MEASUREMENTS_PATH.joinpath('Innerfidelity', 'data', 'over-ear'),
}


def prune_results(dry_run=False, databases=None):
    for db in databases:
        result_paths = list(RESULTS_PATH.joinpath(db).glob('**/*.png'))
        for result_path in result_paths:
            source_name = result_path.relative_to(RESULTS_PATH).parent.parent.parent.name
            form = result_path.relative_to(RESULTS_PATH).parent.parent.name
            target_key = f'{source_name}/{form}'
            if target_key in target_to_source:
                source_path = target_to_source[target_key]
            else:
                source_path = MEASUREMENTS_PATH.joinpath(source_name, 'data', form)
            source_path = source_path.joinpath(f'{result_path.parent.name}.csv')
            if not source_path.exists() or result_path.name.replace('.png', '.csv') not in os.listdir(source_path.parent):
                if not dry_run:
                    shutil.rmtree(result_path.parent)
                print(f'Removed "{result_path.parent.relative_to(RESULTS_PATH)}"')

