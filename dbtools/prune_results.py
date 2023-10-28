# -*- coding: utf-8 -*-

import sys
from pathlib import Path
import shutil
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.constants import RESULTS_PATH


target_to_source = {
    'crinacle/711 in-ear': ROOT_PATH.joinpath('measurements', 'crinacle', 'data', 'in-ear', '711'),
    'crinacle/Bruel & Kjaer 4620 in-ear': ROOT_PATH.joinpath('measurements', 'crinacle', 'data', 'in-ear', 'Bruel & Kjaer 4620'),
    'crinacle/EARS + 711 over-ear': ROOT_PATH.joinpath('measurements', 'crinacle', 'data', 'over-ear', 'EARS + 711'),
    'crinacle/GRAS 43AG-7 over-ear': ROOT_PATH.joinpath('measurements', 'crinacle', 'data', 'in-ear', 'GRAS 43AG-7'),
    'oratory1990/earbud': ROOT_PATH.joinpath('measurements', 'oratory1990', 'data', 'earbud'),
    'oratory1990/in-ear': ROOT_PATH.joinpath('measurements', 'oratory1990', 'data', 'in-ear'),
    'oratory1990/over-ear': ROOT_PATH.joinpath('measurements', 'oratory1990', 'data', 'over-ear'),
    'Rtings/earbud': ROOT_PATH.joinpath('measurements', 'rtings', 'data', 'earbud'),
    'Rtings/in-ear': ROOT_PATH.joinpath('measurements', 'rtings', 'data', 'in-ear'),
    'Rtings/over-ear': ROOT_PATH.joinpath('measurements', 'rtings', 'data', 'over-ear'),
    'Headphone.com Legacy/earbud': ROOT_PATH.joinpath('measurements', 'headphonecom', 'data', 'earbud'),
    'Headphone.com Legacy/in-ear': ROOT_PATH.joinpath('measurements', 'headphonecom', 'data', 'in-ear'),
    'Headphone.com Legacy/over-ear': ROOT_PATH.joinpath('measurements', 'headphonecom', 'data', 'over-ear'),
    'Innerfidelity/earbud': ROOT_PATH.joinpath('measurements', 'innerfidelity', 'data', 'earbud'),
    'Innerfidelity/in-ear': ROOT_PATH.joinpath('measurements', 'innerfidelity', 'data', 'in-ear'),
    'Innerfidelity/over-ear': ROOT_PATH.joinpath('measurements', 'innerfidelity', 'data', 'over-ear'),
}


def prune_results(dry_run=False, databases=None):
    for db in databases:
        result_paths = list(RESULTS_PATH.joinpath(db).glob('**/*.png'))
        for result_path in result_paths:
            target_key = str(result_path.relative_to(RESULTS_PATH).parent.parent).replace('\\', '/')
            source_dir = target_to_source[target_key]
            if not source_dir.joinpath(f'{result_path.parent.name}.csv').exists():
                if not dry_run:
                    shutil.rmtree(result_path.parent)
                print(f'Removed "{result_path.parent.relative_to(RESULTS_PATH)}"')

