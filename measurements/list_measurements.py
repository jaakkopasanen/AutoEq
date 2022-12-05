import json
from pathlib import Path

from autoeq.frequency_response import FrequencyResponse


def write_entries_and_measurements():
    path = Path().resolve()
    source_ranking = ['oratory1990', 'crinacle', 'rtings', 'innerfidelity', 'headphonecom', 'referenceaudioanalyzer']
    entries = dict()
    measurements = dict()
    for source in ['crinacle', 'headphonecom', 'innerfidelity', 'oratory1990', 'referenceaudioanalyzer', 'rtings']:
        for hp_path in path.joinpath(source, 'data').glob('**/*.csv'):
            parts = hp_path.parts[hp_path.parts.index('data') + 1:]
            source = hp_path.parts[hp_path.parts.index('data') - 1]
            form = parts[0]
            rig = parts[1] if len(parts) == 4 else 'unknown'
            name = parts[-2]
            if name not in entries:
                entries[name] = []
            if name not in measurements:
                measurements[name] = dict()
            if source not in measurements[name]:
                measurements[name][source] = dict()
            measurements[name][source][rig] = FrequencyResponse.read_from_csv(hp_path).to_dict()
            entries[name].append({
                'form': form, 'rig': rig, 'source': source
            })
    entries = {key: entries[key] for key in sorted(list(entries.keys()), key=lambda key: key)}
    for headphone in entries.keys():
        entries[headphone] = sorted(entries[headphone], key=lambda o: source_ranking.index(o['source']))
    with open('measurements.json', 'w', encoding='utf-8') as fh:
        json.dump(measurements, fh, ensure_ascii=False, indent=4)
    with open('entries.json', 'w', encoding='utf-8') as fh:
        json.dump(entries, fh, ensure_ascii=False, indent=4)


def write_compensations():
    path = Path().resolve()
    compensations = [
        {'name': 'autoeq_in-ear', 'label': 'AutoEq In-ear', 'compatible': [
            ('crinacle', 'inear', 'unknown'), ('oratory1990', 'inear', 'unknown')
        ]},
        {'name': 'diffuse_field', 'label': 'Diffuse Field', 'compatible': []},
        {'name': 'free_field', 'label': 'Free Field', 'compatible': []},
        {'name': 'harman_in-ear_2016', 'label': 'Harman In-ear 2016', 'compatible': [
            ('crinacle', 'inear', 'unknown'), ('oratory1990', 'inear', 'unknown')
        ]},
        {'name': 'harman_in-ear_2017-1', 'label': 'Harman In-ear 2017-1', 'compatible': [
            ('crinacle', 'inear', 'unknown'), ('oratory1990', 'inear', 'unknown')
        ]},
        {'name': 'harman_in-ear_2017-2', 'label': 'Harman In-ear 2017-2', 'compatible': [
            ('crinacle', 'inear', 'unknown'), ('oratory1990', 'inear', 'unknown')
        ]},
        {'name': 'harman_in-ear_2019v2', 'label': 'Harman In-ear 2019', 'compatible': [
            ('crinacle', 'inear', 'unknown'), ('oratory1990', 'inear', 'unknown')
        ]},
        {'name': 'harman_over-ear_2013', 'label': 'Harman Over-ear 2013', 'compatible': [
            ('crinacle', 'onear', 'GRAS 43AG-7'), ('oratory1990', 'onear', 'unknown')
        ]},
        {'name': 'harman_over-ear_2015', 'label': 'Harman Over-ear 2015', 'compatible': [
            ('crinacle', 'onear', 'GRAS 43AG-7'), ('oratory1990', 'onear', 'unknown')
        ]},
        {'name': 'harman_over-ear_2018', 'label': 'Harman Over-ear 2018', 'compatible': [
            ('crinacle', 'onear', 'GRAS 43AG-7'), ('oratory1990', 'onear', 'unknown')
        ]},
    ]
    for compensation in compensations:
        fp = path.parent.joinpath('compensation', f'{compensation["name"]}.csv')
        compensation['fr'] = FrequencyResponse.read_from_csv(fp).to_dict()
    with open('compensations.json', 'w', encoding='utf-8') as fh:
        json.dump(compensations, fh, ensure_ascii=False, indent=4)


def main():
    write_entries_and_measurements()
    write_compensations()


if __name__ == '__main__':
    main()
