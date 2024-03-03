# -*- coding: utf-8 -*-

import sys
from pathlib import Path
import json
from urllib.parse import quote
import re
import numpy as np
from zipfile import ZipFile
from tabulate import tabulate
from tqdm.auto import tqdm
from autoeq.frequency_response import FrequencyResponse
from dbtools.headphonecom_crawler import HeadphonecomCrawler
from dbtools.innerfidelity_crawler import InnerfidelityCrawler
from dbtools.name_index import NameIndex
ROOT_PATH = Path(__file__).parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from dbtools.manufacturer_index import ManufacturerIndex
from dbtools.constants import RESULTS_PATH, TARGETS_PATH, MEASUREMENTS_PATH, WEBAPP_PATH

name_indexes = {}
for fp in MEASUREMENTS_PATH.glob('*/name_index.tsv'):
    name_indexes[fp.parent.name] = NameIndex.read_tsv(fp)
name_indexes['Headphone.com Legacy'] = HeadphonecomCrawler().name_index
name_indexes['Innerfidelity'] = InnerfidelityCrawler().name_index


class ResultPath:
    priorities = [  # Higher index means higher priority
        ('Headphone.com Legacy', 'earbud'),
        ('Rtings', 'earbud'),
        ('Innerfidelity', 'earbud'),
        ('Kazi', 'earbud'),
        ('Regan Cipher', 'earbud'),
        ('kr0mka', 'earbud'),
        ('Super Review', 'earbud'),
        ('HypetheSonics', 'earbud'),
        ('oratory1990', 'earbud'),

        ('Headphone.com Legacy', 'in-ear'),  # STD 1.05 (small sample)
        ('Rtings', 'in-ear'),  # STD 2.09
        ('Innerfidelity', 'in-ear'),  # STD 1.96
        ('HypetheSonics', 'Bruel & Kjaer 5128 in-ear'),
        ('crinacle', 'Bruel & Kjaer 4620 in-ear'),
        ('Filk', 'in-ear'),  # No calibration
        ('DHRME', 'in-ear'),  # No calibration
        ('Jaytiss', 'in-ear'),  # No calibration
        ('Kazi', 'in-ear'),  # No calibration
        ('Regan Cipher', 'in-ear'),  # STD 0.69 (very small sample)
        ('Ted\'s Squig Hoard', 'in-ear'),  # STD 4.24 (unreliable, bad outliers)
        ('ToneDeafMonk', 'in-ear'),  # 0.87 (small sample)
        ('Auriculares Argentina', 'in-ear'),  # STD 1.62 (small sample)
        ('Bakkwatan', 'in-ear'),  # STD 0.83 (small sample)
        ('Hi End Portable', 'in-ear'),  # STD 1.30 (increased by few outliers)
        ('RikudouGoku', 'in-ear'),  # STD 0.80 (significant deviation in bass for mean)
        ('Fahryst', 'in-ear'),  # STD 1.18
        ('kr0mka', 'in-ear'),  # STD 1.15
        ('Harpo', 'in-ear'),  # STD 1.04
        ('freeryder05', 'in-ear'),  # STD 0.92
        ('Super Review', 'in-ear'),  # STD 0.90 (large sample)
        ('crinacle', '711 in-ear'),
        ('HypetheSonics', 'GRAS RA0045 in-ear'),
        ('oratory1990', 'in-ear'),

        ('crinacle', 'EARS + 711 over-ear'),
        ('Headphone.com Legacy', 'over-ear'),  # STD 2.77
        ('Innerfidelity', 'over-ear'),  # STD 1.92
        ('Rtings', 'over-ear'),  # STD 1.62
        ('HypetheSonics', 'over-ear'),  # Bruel & Kjaer 5128
        ('Regan Cipher', 'over-ear'),  # No calibration
        ('RikudouGoku', 'over-ear'),  # No calibration
        ('Filk', 'over-ear'),  # STD 2.04 (small sample)
        ('kr0mka', 'over-ear'),  # STD 1.20 (small sample, one outlier increases STD)
        ('Auriculares Argentina', 'over-ear'),  # STD 1.64
        ('Super Review', 'over-ear'),  # STD 1.56
        ('Kuulokenurkka', 'over-ear'),  # STD 1.26
        ('crinacle', 'GRAS 43AG-7 over-ear'),
        ('oratory1990', 'over-ear'),
    ][::-1]

    def __init__(self, path):
        self._absolute_path = Path(path).absolute()
        self._path_relative_to_root = self._absolute_path.relative_to(RESULTS_PATH)
        self._source_name = self._path_relative_to_root.parts[0]
        self._form_rig = self._path_relative_to_root.parts[1]
        self._rig = self._form_rig.replace('earbud', '').replace('in-ear', '').replace('over-ear', '').strip()
        self._form = self._form_rig.replace(self._rig, '').strip()
        self._path_relative_to_source = self._absolute_path.relative_to(RESULTS_PATH.joinpath(self._source_name))
        self._name = self._absolute_path.parts[-1]

    def __str__(self):
        return json.dumps({
            'absolute_path': str(self.absolute_path),
            'path_relative_to_root': str(self.path_relative_to_root),
            'url_relative_to_root': str(self.url_relative_to_root),
            'source_name': str(self.source_name),
            'form': str(self.form),
            'rig': str(self.rig),
            'priority': str(self.priority),
            'path_relative_to_source': str(self.path_relative_to_source),
            'url_relative_to_source': str(self.url_relative_to_source),
        }, ensure_ascii=False, indent=4)

    def __getitem__(self, key):
        if key == 'absolute_path':
            return self.absolute_path
        if key == 'path_relative_to_root':
            return self.path_relative_to_root
        if key == 'url_relative_to_root':
            return self.url_relative_to_root
        if key == 'source_name':
            return self.source_name
        if key == 'form':
            return self.form
        if key == 'rig':
            return self.rig
        if key == 'priority':
            return self.priority
        if key == 'path_relative_to_source':
            return self.path_relative_to_source
        if key == 'url_relative_to_source':
            return self.url_relative_to_source
        if key == 'name':
            return self.name

    def urlify(self, url):
        return quote(url, safe="%/:=&?~#+!$,;'@()*[]")

    @property
    def name(self):
        return self._name

    @property
    def absolute_path(self):
        return self._absolute_path

    @property
    def path_relative_to_root(self):
        return self._path_relative_to_root

    @property
    def url_relative_to_root(self):
        return self.urlify('/'.join(['.'] + list(self.path_relative_to_root.parts)))

    @property
    def source_name(self):
        return self._source_name

    @property
    def form(self):
        return self._form

    @property
    def rig(self):
        return self._rig

    @property
    def priority(self):
        return self.__class__.priorities.index((self.source_name, self._form_rig))

    @property
    def path_relative_to_source(self):
        return self._path_relative_to_source

    @property
    def url_relative_to_source(self):
        return self.urlify('/'.join(['.'] + list(self.path_relative_to_source.parts)))


def group_by(paths, prop):
    """Groups paths into groups in dict with sorted keys"""
    grouped = {}
    for path in paths:
        if path[prop] not in grouped:
            grouped[path[prop]] = []
        grouped[path[prop]].append(path)
    return {sorted_key: grouped[sorted_key] for sorted_key in sorted(list(grouped.keys()))}


def sort_by(paths, prop):
    """Sorts paths by a property"""
    return sorted(paths, key=lambda path: path[prop].lower() if type(path[prop]) == str else path[prop])


def sort_each_group_by(groups, prop):
    """Sorts paths in each group by property"""
    for group_key in groups.keys():
        groups[group_key] = sort_by(groups[group_key], prop)
    return groups


def write_recommendations(paths):
    print('Creating recommendations index...')
    grouped_by_name = group_by(paths, 'name')
    grouped_by_name = sort_each_group_by(grouped_by_name, 'priority')

    s = f'''# Recommended Results
            This is a list of recommended results. Results for other measurements and target curves are available for many
            headphones, these can be found in the
            [full index](./INDEX.md).

            Where there are measurements from multiple sources for the same headphone, only the one with the highest accuracy
            appears on this list.

            This list has {len(grouped_by_name)} headphone models covered, but if your headphone is missing, you can create settings for
            it yourself by following this guide:
            [Equalizing Headphones the Easy Way](https://medium.com/@jaakkopasanen/make-your-headphones-sound-supreme-1cbd567832a9)

            Headphone ranking based on Harman listener preference scores can be found in the
            [Headphone Ranking](./RANKING.md).
            '''
    for name in sorted(list(grouped_by_name.keys()), key=lambda key: key.lower()):
        s += f'\n- [{name}]({grouped_by_name[name][0].url_relative_to_root})'

    with open(RESULTS_PATH.joinpath('README.md'), 'w', encoding='utf-8') as f:
        f.write(re.sub('\n[ \t]+', '\n', s).strip())


def write_full_index(paths):
    print('Creating full index...')
    grouped_by_name = group_by(paths, 'name')
    grouped_by_name = sort_each_group_by(grouped_by_name, 'priority')

    s = f'''# Index
            This is a list of all equalization profiles. Target is in parentheses if there are results with multiple targets
            from the same source.
            '''

    for name in sorted(list(grouped_by_name.keys()), key=lambda key: key.lower()):
        for path in grouped_by_name[name]:
            hp_str = f'\n- [{path.name}]({path.url_relative_to_root}) by {path.source_name}'
            if path.rig:
                hp_str += f' on {path.rig}'
            s += hp_str

    with open(RESULTS_PATH.joinpath('INDEX.md'), 'w', encoding='utf-8') as f:
        f.write(re.sub('\n[ \t]+', '\n', s).strip() + '\n')


def write_source_indexes(paths):
    print('Creating source indices...')
    grouped_by_source = group_by(paths, 'source_name')
    grouped_by_source = sort_each_group_by(grouped_by_source, 'form')

    for source_name, source_paths in grouped_by_source.items():
        s = f'# {source_name} Results\n'
        grouped_by_name = group_by(source_paths, 'name')
        for name in sorted(list(grouped_by_name.keys()), key=lambda key: key.lower()):
            for path in sort_by(grouped_by_name[name], 'priority'):
                hp_str = f'\n- [{path.name}]({path.url_relative_to_source})'
                if path.rig:
                    hp_str += f' on {path.rig}'
                s += hp_str

        with open(RESULTS_PATH.joinpath(source_name, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(re.sub('\n[ \t]+', '\n', s).strip() + '\n')


def write_hesuvi_zip(paths):
    print('Creating HeSuVi ZIP archive...')
    manufacturers = ManufacturerIndex()
    zip_object = ZipFile(RESULTS_PATH.joinpath('hesuvi.zip'), 'w')
    zip_files = set()

    grouped_by_name = group_by(paths, 'name')
    grouped_by_name = sort_each_group_by(grouped_by_name, 'priority')

    for name, group_paths in tqdm(grouped_by_name.items()):
        manufacturer, _ = manufacturers.find(name)
        if manufacturer is None:
            print(f'Manufacturer could not be found for {name}. Will skip in hesuvi.zip.')
            continue
        model = manufacturers.model(name)
        archive_path = f'eq/{manufacturer}/{model}.txt'

        file_path = next(group_paths[0].absolute_path.glob('* GraphicEQ.txt'))
        with open(file_path, 'r', encoding='utf-8') as fh:
            s = fh.read()
            data = np.array([x.split() for x in s.split(': ')[1].split('; ')], dtype='float')
            # Normalizing about mean level in range 100 Hz and 10 kHz
            sl = np.logical_and(data[:, 0] > 100, data[:, 0] < 10000)
            data[:, 1] -= np.mean(data[sl, 1])
            s = 'GraphicEQ: '
            s += '; '.join([f'{x[0]:.0f} {x[1]:.1f}' for x in data])
            zip_object.writestr(archive_path, s)
            zip_files.add(archive_path)
    zip_object.close()


def write_ranking_table(paths):
    print('Creating ranking index...')
    harman_inear = FrequencyResponse.read_csv(TARGETS_PATH.joinpath('Harman in-ear 2019.csv'))
    harman_overear = FrequencyResponse.read_csv(TARGETS_PATH.joinpath('Harman over-ear 2018.csv'))

    grouped_by_name = group_by(paths, 'name')
    for name, group_paths in grouped_by_name.items():
        grouped_by_name[name] = [path for path in group_paths if (
                path.source_name == 'oratory1990' or
                (path.source_name == 'crinacle' and (
                        path.rig == 'GRAS 43AG-7' or path.rig == '711'
                )) or
                (path.source_name == 'HypetheSonics' and path.rig == 'GRAS RA0045')
        )]
    grouped_by_name = sort_each_group_by(grouped_by_name, 'priority')

    over_ears = []
    in_ears = []

    for name, group_paths in tqdm(grouped_by_name.items()):
        if not group_paths:  # No eligible measurements for this headphone
            continue
        path = group_paths[0]
        if path.form == 'over-ear':
            fr = FrequencyResponse.read_csv(path.absolute_path.joinpath(f'{path.name}.csv'))
            fr.compensate(harman_overear)
            score, std, slope = fr.harman_overear_preference_score()
            over_ears.append([
                f'[{path.name}]({path.url_relative_to_root})', f'{score:.0f}', f'{std:.2f}', f'{slope:.2f}'
            ])
        elif path.form == 'in-ear':
            fr = FrequencyResponse.read_csv(path.absolute_path.joinpath(f'{path.name}.csv'))
            fr.compensate(harman_inear)
            try:
                score, std, slope, mean = fr.harman_inear_preference_score()
                in_ears.append([
                    f'[{path.name}]({path.url_relative_to_root})',
                    f'{score:.0f}', f'{std:.2f}', f'{slope:.2f}', f'{mean:.2f}'
                ])
            except:
                print(path.absolute_path)
                print(fr.error)
    over_ears = sorted(over_ears, key=lambda row: float(row[1]), reverse=True)
    overear_str = tabulate(over_ears, headers=['Name', 'Score', 'STD (dB)', 'Slope'], tablefmt='github')
    in_ears = sorted(in_ears, key=lambda row: float(row[1]), reverse=True)
    inear_str = tabulate(in_ears, headers=['Name', 'Score', 'STD (dB)', 'Slope', 'Average (dB)'], tablefmt='github')

    s = f'''# Headphone Ranking
            Headphones ranked by Harman headphone listener preference scores.

            Tables include the preference score (Score), standard deviation of the error (STD), slope of the logarithimc
            regression fit of the error (Slope) for both over-ear and in-ear headphones and average of the absolute error (Average) for in-ears
            headphones. STD tells how much the headphone deviates from neutral and slope tells if the headphone is warm (< 0) or
            bright (> 0).

            Keep in mind that these numbers are calculated with deviations from Harman targets and you're preferences might
            differ.

            Over-ear table includes headphones measured by oratory1990 and Crinacle using GRAS systems. Measurements from
            other databases and systems are not included because they are not compatible with measurements, targets and
            preference scoring developed by Sean Olive et al.

            ## Over-ear Headphones    
            {overear_str}

            ## In-ear Headphones
            {inear_str}

            '''
    with open(RESULTS_PATH.joinpath('RANKING.md'), 'w', encoding='utf-8') as fh:
        fh.write(re.sub('\n[ \t]+', '\n', s).strip())


def write_webapp_entries_and_measurements(paths):
    print('Creating webapp data...')
    grouped_by_name = group_by(paths, 'name')
    grouped_by_name = sort_each_group_by(grouped_by_name, 'priority')

    entries = dict()
    measurements = dict()
    for name in tqdm(sorted(list(grouped_by_name.keys()), key=lambda key: key.lower())):
        entries[name] = []
        measurements[name] = {}
        for path in grouped_by_name[name]:
            rig = path.rig
            if not rig:
                try:
                    rig = name_indexes[path.source_name].find_one(name=name).rig
                except Exception as err:
                    print(f'name: {name}')
                    print(f'source_name: {path.source_name}')
                    raise err
            entries[name].append({'form': path.form, 'rig': rig, 'source': path.source_name})
            if path.source_name not in measurements[name]:
                measurements[name][path.source_name] = dict()
            csv_path = path.absolute_path.joinpath(f'{path.name}.csv')
            fr = FrequencyResponse.read_csv(csv_path)
            fr.reset(
                raw=False, smoothed=True, error=True, error_smoothed=True, equalization=True, fixed_band_eq=True,
                parametric_eq=True, equalized_raw=True, equalized_smoothed=True, target=True)
            measurements[name][path.source_name][rig] = fr.to_dict()

    with open(WEBAPP_PATH.joinpath('data', 'measurements.json'), 'w', encoding='utf-8') as fh:
        json.dump(measurements, fh, ensure_ascii=False, indent=4)
    with open(WEBAPP_PATH.joinpath('data', 'entries.json'), 'w', encoding='utf-8') as fh:
        json.dump(entries, fh, ensure_ascii=False, indent=4)


def update_all_indexes():
    paths = [ResultPath(readme_path.parent) for readme_path in Path(RESULTS_PATH).glob('*/*/**/*.md')]
    write_ranking_table(paths)
    write_recommendations(paths)
    write_full_index(paths)
    write_source_indexes(paths)
    write_hesuvi_zip(paths)
    write_webapp_entries_and_measurements(paths)


if __name__ == '__main__':
    update_all_indexes()
