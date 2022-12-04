import json
from pathlib import Path

from autoeq.frequency_response import FrequencyResponse


def main():
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

    compensations = dict()
    for fp in path.parent.joinpath('compensation').glob('*.csv'):
        name = fp.name.replace('.csv', '')
        compensations[name] = FrequencyResponse.read_from_csv(fp).to_dict()
    with open('compensations.json', 'w', encoding='utf-8') as fh:
        json.dump(compensations, fh, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
