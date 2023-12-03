# -*- coding: utf-8 -*-

import sys
import json
from pathlib import Path
from autoeq.frequency_response import FrequencyResponse
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.constants import WEBAPP_PATH, TARGETS_PATH


def write_targets():
    targets = [
        {
            'file': TARGETS_PATH.joinpath('AutoEq in-ear.csv'),
            'compatible': [
                {'source': 'crinacle', 'form': 'in-ear', 'rig': '711'},
                {'source': 'oratory1990', 'form': 'in-ear'},
                {'source': 'oratory1990', 'form': 'earbud'}
            ],
            'recommended': [
                {'source': 'crinacle', 'form': 'in-ear', 'rig': '711'},
                {'source': 'oratory1990', 'form': 'in-ear'},
                {'source': 'oratory1990', 'form': 'earbud'}
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 8}
        },
        {
            'file': TARGETS_PATH.joinpath('Diffuse field 5128 -1dB per octave.csv'),
            'label': 'Diffuse Field 5128 (-1 dB/oct)',
            'compatible': [{'source': 'crinacle', 'form': 'in-ear', 'rig': 'Bruel & Kjaer 4620'}],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        },
        {
            'file': TARGETS_PATH.joinpath('JM-1 without bass.csv'),
            'label': 'JM-1',
            'compatible': [{'source': 'crinacle', 'form': 'in-ear', 'rig': 'Bruel & Kjaer 4620'}],
            'recommended': [{'source': 'crinacle', 'form': 'in-ear', 'rig': 'Bruel & Kjaer 4620'}],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6.5}
        },
        {
            'file': TARGETS_PATH.joinpath('711 5128 delta.csv'),
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        },
        {
            'file': TARGETS_PATH.joinpath('Diffuse field GRAS KEMAR.csv'),
            'compatible': [
                {'source': 'crinacle', 'form': 'in-ear'},
                {'source': 'oratory1990', 'form': 'in-ear'},
                {'source': 'oratory1990', 'form': 'earbud'},
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        },
        {
            'file': TARGETS_PATH.joinpath('Diffuse field ISO 11904-1.csv'),
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        },
        {
            'file': TARGETS_PATH.joinpath('zero.csv'),
            'label': 'Flat',
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        },
        {
            'file': TARGETS_PATH.joinpath('Harman in-ear 2019 without bass.csv'),
            'label': 'Harman in-ear 2019',
            'compatible': [
                {'source': 'crinacle', 'form': 'in-ear', 'rig': '711'},
                {'source': 'oratory1990', 'form': 'in-ear'},
                {'source': 'oratory1990', 'form': 'earbud'}
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Harman over-ear 2018 without bass.csv'),
            'label': 'Harman over-ear 2018',
            'compatible': [
                {'source': 'crinacle', 'form': 'over-ear', 'rig': 'GRAS 43AG-7'},
                {'source': 'oratory1990', 'form': 'over-ear'}
            ],
            'recommended': [
                {'source': 'crinacle', 'form': 'over-ear', 'rig': 'GRAS 43AG-7'},
                {'source': 'oratory1990', 'form': 'over-ear'}
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
        {
            'file': TARGETS_PATH.joinpath('HMS II.3 AutoEq in-ear.csv'),
            'compatible': [
                {'source': 'Headphone.com Legacy', 'form': 'in-ear'},
                {'source': 'Headphone.com Legacy', 'form': 'earbud'},
                {'source': 'Innerfidelity', 'form': 'in-ear'},
                {'source': 'Innerfidelity', 'form': 'earbud'},
                {'source': 'Rtings', 'form': 'in-ear'},
                {'source': 'Rtings', 'form': 'earbud'},
            ],
            'recommended': [
                {'source': 'Headphone.com Legacy', 'form': 'in-ear'},
                {'source': 'Headphone.com Legacy', 'form': 'earbud'},
                {'source': 'Innerfidelity', 'form': 'in-ear'},
                {'source': 'Innerfidelity', 'form': 'earbud'},
                {'source': 'Rtings', 'form': 'in-ear'},
                {'source': 'Rtings', 'form': 'earbud'},
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 8}
        },
        {
            'file': TARGETS_PATH.joinpath('HMS II.3 Harman in-ear 2019 without bass.csv'),
            'label': 'HMS II.3 Harman in-ear 2019',
            'compatible': [
                {'source': 'Headphone.com Legacy', 'form': 'in-ear'},
                {'source': 'Headphone.com Legacy', 'form': 'earbud'},
                {'source': 'Innerfidelity', 'form': 'in-ear'},
                {'source': 'Innerfidelity', 'form': 'earbud'},
                {'source': 'Rtings', 'form': 'in-ear'},
                {'source': 'Rtings', 'form': 'earbud'},
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('HMS II.3 Harman over-ear 2018 without bass.csv'),
            'label': 'HMS II.3 Harman over-ear 2018',
            'compatible': [
                {'source': 'Headphone.com Legacy', 'form': 'over-ear'},
                {'source': 'Innerfidelity', 'form': 'over-ear'},
                {'source': 'Rtings', 'form': 'over-ear'},
            ],
            'recommended': [
                {'source': 'Headphone.com Legacy', 'form': 'over-ear'},
                {'source': 'Innerfidelity', 'form': 'over-ear'},
                {'source': 'Rtings', 'form': 'over-ear'},
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
    ]
    for target in targets:
        if 'label' not in target:
            target['label'] = target['file'].name.replace('.csv', '')
        if 'compatible' not in target:
            target['compatible'] = []
        if 'recommended' not in target:
            target['recommended'] = []
        target['fr'] = FrequencyResponse.read_csv(target['file']).to_dict()
        del target['file']
    with open(WEBAPP_PATH.joinpath('data', 'targets.json'), 'w', encoding='utf-8') as fh:
        json.dump(targets, fh, ensure_ascii=False, indent=4)


def main():
    write_targets()


if __name__ == '__main__':
    main()
