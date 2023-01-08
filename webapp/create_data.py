import json
from pathlib import Path
from autoeq.frequency_response import FrequencyResponse

DIR = Path().absolute()


def write_entries_and_measurements():
    source_ranking = ['oratory1990', 'crinacle', 'rtings', 'innerfidelity', 'headphonecom', 'referenceaudioanalyzer']
    entries = dict()
    measurements = dict()
    for hp_path in DIR.parent.joinpath('measurements').glob('*/data/**/*.csv'):
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
    with open(DIR.joinpath('data', 'measurements.json'), 'w', encoding='utf-8') as fh:
        json.dump(measurements, fh, ensure_ascii=False, indent=4)
    with open(DIR.joinpath('data', 'entries.json'), 'w', encoding='utf-8') as fh:
        json.dump(entries, fh, ensure_ascii=False, indent=4)


def write_compensations():
    path = Path().resolve()
    compensations = [
        {
            'name': 'diffuse_field',
            'label': 'Diffuse Field',
            'compatible': [],
            'recommended': [],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        }, {
            'name': 'free_field',
            'label': 'Free Field',
            'compatible': [],
            'recommended': [],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        },
        {
            'name': 'zero',
            'label': 'Flat',
            'compatible': [],
            'recommended': [],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 0}
        }, {
            'name': 'autoeq_in-ear',
            'label': 'AutoEq In-ear',
            'compatible': [('crinacle', 'inear', 'unknown'), ('oratory1990', 'inear', 'unknown')],
            'recommended': [('crinacle', 'inear', 'unknown'), ('oratory1990', 'inear', 'unknown')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        }, {
            'name': 'harman_in-ear_2019v2_wo_bass',
            'label': 'Harman In-ear 2019',
            'compatible': [('crinacle', 'inear', 'unknown'), ('oratory1990', 'inear', 'unknown')],
            'recommended': [],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        }, {
            'name': 'harman_over-ear_2018_wo_bass',
            'label': 'Harman Over-ear 2018',
            'compatible': [('crinacle', 'onear', 'GRAS 43AG-7'), ('oratory1990', 'onear', 'unknown')],
            'recommended': [('crinacle', 'onear', 'GRAS 43AG-7'), ('oratory1990', 'onear', 'unknown')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        }, {
            'name': 'headphonecom_harman_in-ear_2019v2_wo_bass',
            'label': 'Headphone.com (legacy) Harman In-ear 2019v2',
            'compatible': [('headphonecom', 'inear', 'unknown')],
            'recommended': [('headphonecom', 'inear', 'unknown')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        }, {
            'name': 'headphonecom_harman_over-ear_2018_wo_bass',
            'label': 'Headphone.com (legacy) Harman Over-ear 2018',
            'compatible': [('headphonecom', 'onear', 'unknown')],
            'recommended': [('headphonecom', 'onear', 'unknown')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
        {
            'name': 'innerfidelity_harman_in-ear_2019v2_wo_bass',
            'label': 'Innerfidelity Harman In-ear 2019v2',
            'compatible': [('innerfidelity', 'inear', 'unknown')],
            'recommended': [('innerfidelity', 'inear', 'unknown')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'name': 'innerfidelity_harman_over-ear_2018_wo_bass',
            'label': 'Innerfidelity Harman Over-ear 2018',
            'compatible': [('innerfidelity', 'onear', 'unknown')],
            'recommended': [('innerfidelity', 'onear', 'unknown')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
        {
            'name': 'referenceaudioanalyzer_hdm1_harman_over-ear_2018_wo_bass',
            'label': 'RAA HDM-1 Harman Over-ear 2018',
            'compatible': [('referenceaudioanalyzer', 'onear', 'HDM1')],
            'recommended': [('referenceaudioanalyzer', 'onear', 'HDM1')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
        {
            'name': 'referenceaudioanalyzer_hdm-x_harman_over-ear_2018_wo_bass',
            'label': 'RAA HDM-X Harman Over-ear 2018',
            'compatible': [('referenceaudioanalyzer', 'onear', 'HDM-X')],
            'recommended': [('referenceaudioanalyzer', 'onear', 'HDM-X')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
        {
            'name': 'referenceaudioanalyzer_siec_harman_in-ear_2019v2_wo_bass',
            'label': 'RAA SIEC Harman Over-ear 2019',
            'compatible': [('referenceaudioanalyzer', 'inear', 'SIEC')],
            'recommended': [('referenceaudioanalyzer', 'inear', 'SIEC')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'name': 'rtings_harman_in-ear_2019v2_wo_bass',
            'label': 'Rtings Harman In-ear 2019v2',
            'compatible': [('rtings', 'inear', 'unknown')],
            'recommended': [('rtings', 'inear', 'unknown')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 9.5}
        },
        {
            'name': 'rtings_harman_over-ear_2018_wo_bass',
            'label': 'Rtings Harman Over-ear 2018',
            'compatible': [('rtings', 'onear', 'unknown')],
            'recommended': [('rtings', 'onear', 'unknown')],
            'bassBoost': {'fc': 105, 'q': 0.7, 'gain': 6}
        },
    ]
    for compensation in compensations:
        fp = path.parent.joinpath('compensation', f'{compensation["name"]}.csv')
        compensation['fr'] = FrequencyResponse.read_from_csv(fp).to_dict()
    with open(DIR.joinpath('data', 'compensations.json'), 'w', encoding='utf-8') as fh:
        json.dump(compensations, fh, ensure_ascii=False, indent=4)


def main():
    write_entries_and_measurements()
    write_compensations()


if __name__ == '__main__':
    main()
