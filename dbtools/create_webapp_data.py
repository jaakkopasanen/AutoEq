# -*- coding: utf-8 -*-

import sys
import json
from pathlib import Path
from tqdm.auto import tqdm
from autoeq.frequency_response import FrequencyResponse
from dbtools.name_index import NameIndex

ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.constants import WEBAPP_PATH, MEASUREMENTS_PATH, TARGETS_PATH, RESULTS_PATH
from dbtools.headphonecom_crawler import HeadphonecomCrawler
from dbtools.innerfidelity_crawler import InnerfidelityCrawler

name_indexes = {
    'crinacle': NameIndex.read_tsv(MEASUREMENTS_PATH.joinpath('crinacle', 'name_index.tsv')),
    'Headphone.com Legacy': HeadphonecomCrawler().name_index,
    'Innerfidelity': InnerfidelityCrawler().name_index,
    'oratory1990': NameIndex.read_tsv(MEASUREMENTS_PATH.joinpath('oratory1990', 'name_index.tsv')),
    'Rtings': NameIndex.read_tsv(MEASUREMENTS_PATH.joinpath('Rtings', 'name_index.tsv')),
}


def measurement_rank(entry):
    order = [
        {'source': 'oratory1990', 'form': 'over-ear'},
        {'source': 'crinacle', 'form': 'over-ear', 'rig': 'GRAS 43AG-7'},
        {'source': 'Innerfidelity', 'form': 'over-ear', 'rig': 'HMS II.3'},
        {'source': 'Rtings', 'form': 'over-ear', 'rig': 'HMS II.3'},
        {'source': 'Headphone.com Legacy', 'form': 'over-ear', 'rig': 'HMS II.3'},
        {'source': 'crinacle', 'form': 'over-ear', 'rig': 'EARS + 711'},

        {'source': 'crinacle', 'form': 'in-ear', 'rig': 'Bruel & Kjaer 4620'},
        {'source': 'oratory1990', 'form': 'in-ear'},
        {'source': 'crinacle', 'form': 'in-ear', 'rig': '711'},
        {'source': 'Rtings', 'form': 'in-ear', 'rig': 'HMS II.3'},
        {'source': 'Innerfidelity', 'form': 'in-ear', 'rig': 'HMS II.3'},
        {'source': 'Headphone.com Legacy', 'form': 'in-ear', 'rig': 'HMS II.3'},

        {'source': 'oratory1990', 'form': 'earbud'},
        {'source': 'crinacle', 'form': 'earbud', 'rig': '711'},
        {'source': 'Rtings', 'form': 'earbud', 'rig': 'HMS II.3'},
        {'source': 'Innerfidelity', 'form': 'earbud', 'rig': 'HMS II.3'},
        {'source': 'Headphone.com Legacy', 'form': 'earbud', 'rig': 'HMS II.3'},
    ]
    for i, group in enumerate(order):
        if group['source'] == entry['source'] and group['form'] == entry['form'] and ('rig' not in group or group['rig'] == entry['rig']):
            return i
    raise ValueError(f'{entry} is not in list')


def write_entries_and_measurements():
    entries = dict()
    measurements = dict()
    for hp_path in tqdm(list(MEASUREMENTS_PATH.glob('*/data/**/*.csv'))):
        rel_path = hp_path.relative_to(MEASUREMENTS_PATH)
        source = rel_path.parts[0]
        name = rel_path.parts[-1].replace('.csv', '')
        item = name_indexes[source].find_one(name=name)
        if item.is_ignored:
            continue
        if name not in entries:
            entries[name] = []
        if name not in measurements:
            measurements[name] = dict()
        if source not in measurements[name]:
            measurements[name][source] = dict()
        measurements[name][source][item.rig] = FrequencyResponse.read_csv(hp_path).to_dict()
        entries[name].append({'form': item.form, 'rig': item.rig, 'source': source})
    entries = {key: entries[key] for key in sorted(list(entries.keys()), key=lambda key: key)}
    for headphone in entries.keys():
        entries[headphone] = sorted(entries[headphone], key=lambda entry: measurement_rank(entry))
    with open(WEBAPP_PATH.joinpath('data', 'measurements.json'), 'w', encoding='utf-8') as fh:
        json.dump(measurements, fh, ensure_ascii=False, indent=4)
    with open(WEBAPP_PATH.joinpath('data', 'entries.json'), 'w', encoding='utf-8') as fh:
        json.dump(entries, fh, ensure_ascii=False, indent=4)


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
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Diffuse field 5128 -1dB per octave.csv'),
            'label': 'Diffuse Field 5128 (-1 dB/oct)',
            'compatible': [{'source': 'crinacle', 'form': 'in-ear', 'rig': 'Bruel & Kjaer 4620'}],
            'recommended': [{'source': 'crinacle', 'form': 'in-ear', 'rig': 'Bruel & Kjaer 4620'}],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        },
        {
            'file': TARGETS_PATH.joinpath('Diffuse field GRAS KEMAR.csv'),
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
            'compatible': [
                {'source': 'crinacle', 'form': 'in-ear', 'rig': '711'},
                {'source': 'oratory1990', 'form': 'in-ear'},
                {'source': 'oratory1990', 'form': 'earbud'}
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Harman over-ear 2018 without bass.csv'),
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
            'file': TARGETS_PATH.joinpath('Headphone.com Legacy AutoEq in-ear.csv'),
            'compatible': [
                {'source': 'Headphone.com Legacy', 'form': 'in-ear'},
                {'source': 'Headphone.com Legacy', 'form': 'earbud'},
            ],
            'recommended': [
                {'source': 'Headphone.com Legacy', 'form': 'in-ear'},
                {'source': 'Headphone.com Legacy', 'form': 'earbud'},
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Headphone.com Legacy Harman in-ear 2019 without bass.csv'),
            'compatible': [{'source': 'Headphone.com Legacy', 'form': 'in-ear'}],
            'recommended': [],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Headphone.com Legacy Harman over-ear 2018 without bass.csv'),
            'compatible': [{'source': 'Headphone.com Legacy', 'form': 'over-ear'}],
            'recommended': [{'source': 'Headphone.com Legacy', 'form': 'over-ear'}],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
        {
            'file': TARGETS_PATH.joinpath('711 5128 delta.csv'),
            'compatible': [
                {'source': 'crinacle', 'form': 'in-ear'},
                {'source': 'oratory1990', 'form': 'in-ear'},
                {'source': 'oratory1990', 'form': 'earbud'},
            ],
            'recommended': [],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        },
        {
            'file': TARGETS_PATH.joinpath('Innerfidelity AutoEq in-ear.csv'),
            'compatible': [
                {'source': 'Innerfidelity', 'form': 'in-ear'},
                {'source': 'Innerfidelity', 'form': 'earbud'},
            ],
            'recommended': [
                {'source': 'Innerfidelity', 'form': 'in-ear'},
                {'source': 'Innerfidelity', 'form': 'earbud'},
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Innerfidelity Harman in-ear 2019 without bass.csv'),
            'compatible': [
                {'source': 'Innerfidelity', 'form': 'in-ear'},
                {'source': 'Innerfidelity', 'form': 'earbud'},
            ],
            'recommended': [],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Innerfidelity Harman over-ear 2018 without bass.csv'),
            'compatible': [{'source': 'Innerfidelity', 'form': 'over-ear'}],
            'recommended': [{'source': 'Innerfidelity', 'form': 'over-ear'}],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
        {
            'file': TARGETS_PATH.joinpath('Rtings AutoEq in-ear.csv'),
            'compatible': [
                {'source': 'Rtings', 'form': 'in-ear'},
                {'source': 'Rtings', 'form': 'earbud'},
            ],
            'recommended': [
                {'source': 'Rtings', 'form': 'in-ear'},
                {'source': 'Rtings', 'form': 'earbud'},
            ],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Rtings Harman in-ear 2019 without bass.csv'),
            'compatible': [
                {'source': 'Rtings', 'form': 'in-ear'},
                {'source': 'Rtings', 'form': 'earbud'},
            ],
            'recommended': [],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'file': TARGETS_PATH.joinpath('Rtings Harman over-ear 2018 without bass.csv'),
            'compatible': [{'source': 'Rtings', 'form': 'over-ear'}],
            'recommended': [{'source': 'Rtings', 'form': 'over-ear'}],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
    ]
    for target in targets:
        if 'label' not in target:
            target['label'] = target['file'].name.replace('.csv', '').replace(' without bass', '')
        if 'compatible' not in target:
            target['compatible'] = []
        if 'recommended' not in target:
            target['recommended'] = []
        target['fr'] = FrequencyResponse.read_csv(target['file']).to_dict()
        del target['file']
    with open(WEBAPP_PATH.joinpath('data', 'targets.json'), 'w', encoding='utf-8') as fh:
        json.dump(targets, fh, ensure_ascii=False, indent=4)


def main():
    write_entries_and_measurements()
    write_targets()


if __name__ == '__main__':
    main()
