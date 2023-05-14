# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import urllib
import re
import numpy as np
from zipfile import ZipFile
from tabulate import tabulate
from autoeq.constants import MOD_REGEX
from autoeq.frequency_response import FrequencyResponse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.manufacturer_index import ManufacturerIndex

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))
ROOT_DIR = os.path.join(DIR_PATH, os.pardir,)


def form_url(rel_path):
    url = '/'.join(FrequencyResponse._split_path(rel_path))
    url = './{}'.format(url)
    url = urllib.parse.quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    return url


def get_urls(files):
    urls = dict()
    skipped = dict()
    for path in files:
        rel_path = os.path.relpath(path, DIR_PATH)
        model = os.path.split(rel_path)[-1]
        if model == 'README.md' or 'fake' in model.lower():
            continue
        if re.search(MOD_REGEX, model, flags=re.IGNORECASE):
            # Skip measurements with sample or serial number, those have averaged results
            normalized = re.sub(MOD_REGEX, '', model, flags=re.IGNORECASE)
            try:
                skipped[normalized].append(rel_path)
            except KeyError as err:
                skipped[normalized] = [rel_path]
            continue
        urls[model.lower()] = '- [{model}]({url})'.format(model=model, url=form_url(rel_path))

    for model, rel_paths in skipped.items():
        # Add skipped models with only one item, these have no averaged results
        if len(rel_paths) == 1:
            urls[model.lower()] = '- [{model}]({url})'.format(model=model, url=form_url(rel_paths[0]))
    return urls


def write_recommendations():
    """Writes a single recommended result for each headphone to results/README.md."""
    urls = dict()
    # In-ear results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'Headphone.com Legacy', 'in-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'Rtings', 'in-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'Innerfidelity', 'in-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', '711 in-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'in-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'Bruel & Kjaer 4620 in-ear', '*')))))

    # Over-ear results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'EARS + 711 over-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'Headphone.com Legacy', 'over-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'Rtings', 'over-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'Innerfidelity', 'over-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'GRAS 43AG-7 over-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'over-ear', '*')))))

    with open(os.path.join(DIR_PATH, 'README.md'), 'w', encoding='utf-8') as f:
        keys = sorted(urls.keys(), key=lambda s: s.lower())
        unique = len(set(re.sub(r'\(.+\)$', '', x) for x in urls.keys()))
        s = f'''# Recommended Results
        This is a list of recommended results. Results for other measurements and target curves are available for many
        headphones, these can be found in the
        [full index](./INDEX.md).

        Where there are measurements from multiple sources for the same headphone, only the one with highest accuracy
        appears on this list.

        This list has {unique} headphone models covered but if your headphone is missing you can create settings for
        it yourself by following this guide:
        [Equalizing Headphones the Easy Way](https://medium.com/@jaakkopasanen/make-your-headphones-sound-supreme-1cbd567832a9)

        Headphone ranking based on Harman listener preference scores can be found in the
        [Headphone Ranking](./RANKING.md).

        '''
        s += '\n'.join([urls[key] for key in keys])
        f.write(re.sub('\n[ \t]+', '\n', s).strip())


def get_lines(dirs, note=None, path_root=DIR_PATH):
    lines = []
    for path in dirs:
        rel_path = os.path.relpath(path, path_root)
        model = os.path.split(rel_path)[-1]
        if model == 'README.md':
            continue
        s = f'- [{model}]({form_url(rel_path)})'
        if note is not None:
            s += f' {note}'
        lines.append(s)
    return lines


def write_full_index():
    """Writes all results in a single list."""
    lines = []
    # Get links to Headphone.com results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Headphone.com Legacy', 'over-ear', '*'))),
        note='by Headphone.com (Legacy)'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Headphone.com Legacy', 'in-ear', '*'))),
        note='by Headphone.com (Legacy)'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Headphone.com Legacy', 'earbud', '*'))),
        note='by Headphone.com (Legacy)'))
    # Get links to Rtings results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Rtings', 'over-ear', '*'))),
        note='by Rtings'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Rtings', 'in-ear', '*'))),
        note='by Rtings'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Rtings', 'earbud', '*'))),
        note='by Rtings'))
    # Get links to Innerfidelity results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Innerfidelity', 'over-ear', '*'))),
        note='by Innerfidelity'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Innerfidelity', 'in-ear', '*'))),
        note='by Innerfidelity'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'Innerfidelity', 'earbud', '*'))),
        note='by Innerfidelity'))
    # Get links to Crinacle results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'EARS + 711 over-ear', '*'))),
        note='by Crinacle, EARS + 711'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'GRAS 43AG-7 over-ear', '*'))),
        note='by Crinacle, GRAS 43AG-7'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', '711 in-ear', '*'))),
        note='by Crinacle, 711'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'Bruel & Kjaer 4620 in-ear', '*'))),
        note='by Crinacle, Bruel & Kjaer 4620'))
    # Get links to oratory1990 results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'over-ear', '*'))),
        note='by oratory1990'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'in-ear', '*'))),
        note='by oratory1990'))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'earbud', '*'))),
        note='by oratory1990'))
    lines = sorted(lines, key=lambda s: s.lower())

    with open(os.path.join(DIR_PATH, 'INDEX.md'), 'w', encoding='utf-8') as f:
        s = '''# Index
        This is a list of all equalization profiles. Target is in parentheses if there are results with multiple targets
        from the same source.

        '''
        s += '\n'.join(lines)
        f.write(re.sub('\n[ \t]+', '\n', s).strip() + '\n')


def write_headphonecom_index():
    # Get links to Headphone.com results
    base_dir = os.path.abspath(os.path.join(DIR_PATH, 'Headphone.com Legacy'))
    lines = get_lines(glob(os.path.join(base_dir, '*', '*')), path_root=base_dir)
    lines = sorted(lines, key=lambda s: s.lower())
    with open(os.path.join(DIR_PATH, 'Headphone.com Legacy', 'README.md'), 'w', encoding='utf-8') as f:
        f.write('# Headphone.com Legacy Results\n\n' + '\n'.join(lines) + '\n')


def write_rtings_index():
    # Get links to Rtings results
    base_dir = os.path.abspath(os.path.join(DIR_PATH, 'Rtings'))
    lines = get_lines(glob(os.path.join(base_dir, '*', '*')), path_root=base_dir)
    lines = sorted(lines, key=lambda s: s.lower())
    with open(os.path.join(DIR_PATH, 'Rtings', 'README.md'), 'w', encoding='utf-8') as f:
        f.write('# Rtings Results\n\n' + '\n'.join(lines) + '\n')


def write_innerfidelity_index():
    # Get links to Innerfidelity results
    base_dir = os.path.abspath(os.path.join(DIR_PATH, 'Innerfidelity'))
    lines = get_lines(glob(os.path.join(base_dir, '*', '*')), path_root=base_dir)
    lines = sorted(lines, key=lambda s: s.lower())
    with open(os.path.join(DIR_PATH, 'Innerfidelity', 'README.md'), 'w', encoding='utf-8') as f:
        f.write('# Innerfidelity Results\n\n' + '\n'.join(lines) + '\n')


def write_crinacle_index():
    base_dir = os.path.abspath(os.path.join(DIR_PATH, 'crinacle'))
    lines = get_lines(glob(os.path.join(base_dir, 'EARS + 711 over-ear', '*')), path_root=base_dir, note='on EARS + 711')
    lines.extend(get_lines(glob(os.path.join(base_dir, 'GRAS 43AG-7 over-ear', '*')), path_root=base_dir, note='on GRAS 43AG-7'))
    lines.extend(get_lines(glob(os.path.join(base_dir, '711 in-ear', '*')), path_root=base_dir, note='on 711'))
    lines.extend(get_lines(glob(os.path.join(base_dir, 'Bruel & Kjaer 4620 in-ear', '*')), path_root=base_dir, note='on Bruel & Kjaer 4620'))
    lines = sorted(lines, key=lambda s: s.lower())
    with open(os.path.join(DIR_PATH, 'crinacle', 'README.md'), 'w', encoding='utf-8') as f:
        f.write('# crinacle Results\n\n' + '\n'.join(lines) + '\n')


def write_oratory1990_index():
    # Get links to oratory1990 results
    base_dir = os.path.abspath(os.path.join(DIR_PATH, 'oratory1990'))
    lines = get_lines(glob(os.path.join(base_dir, '*', '*')), path_root=base_dir)
    lines = sorted(lines, key=lambda s: s.lower())
    with open(os.path.join(DIR_PATH, 'oratory1990', 'README.md'), 'w', encoding='utf-8') as f:
        f.write('# oratory1990 Results\n\n' + '\n'.join(lines) + '\n')


def write_hesuvi_zip():
    manufacturers = ManufacturerIndex()
    zip_object = ZipFile(os.path.join(DIR_PATH, 'hesuvi.zip'), 'w')

    dir_paths = [
        os.path.join(DIR_PATH, db) for db in ['oratory1990', 'crinacle', 'innerfidelity', 'rtings', 'headphonecom']
    ]

    dir_paths = [
        os.path.join(DIR_PATH, 'Headphone.com Legacy', 'in-ear'),
        os.path.join(DIR_PATH, 'Rtings', 'in-ear'),
        os.path.join(DIR_PATH, 'Innerfidelity', 'in-ear'),
        os.path.join(DIR_PATH, 'crinacle', '711 in-ear'),
        os.path.join(DIR_PATH, 'oratory1990', 'in-ear'),
        os.path.join(DIR_PATH, 'crinacle', 'Bruel & Kjaer 4620 in-ear'),
        os.path.join(DIR_PATH, 'crinacle', 'EARS + 711 over-ear'),
        os.path.join(DIR_PATH, 'Headphone.com Legacy', 'over-ear'),
        os.path.join(DIR_PATH, 'Rtings', 'over-ear'),
        os.path.join(DIR_PATH, 'Innerfidelity', 'over-ear'),
        os.path.join(DIR_PATH, 'crinacle', 'GRAS 43AG-7 over-ear'),
        os.path.join(DIR_PATH, 'oratory1990', 'over-ear')
    ][::-1]

    zip_files = set()
    included_paths = []
    for dir_path in dir_paths:
        for fp in glob(os.path.join(dir_path, '**', '* GraphicEQ.txt'), recursive=True):
            _, name = os.path.split(fp)
            name = name.replace(' GraphicEQ.txt', '')
            if re.search(MOD_REGEX, name, flags=re.IGNORECASE):
                # Skip samples, there are averaged results available
                continue
            manufacturer, _ = manufacturers.find(name)
            if manufacturer is None:
                print(f'Manufacturer could not be found for {name}. Will skip in hesuvi.zip.')
                continue
            name = manufacturers.model(name)
            archive_path = f'eq/{manufacturer}/{name}.txt'
            if archive_path in zip_files:
                # Skip duplicates
                continue
            with open(fp, 'r', encoding='utf-8') as fh:
                s = fh.read()
                data = np.array([x.split() for x in s.split(': ')[1].split('; ')], dtype='float')
                # Normalizing about mean level in range 100 Hz and 10 kHz
                sl = np.logical_and(data[:, 0] > 100, data[:, 0] < 10000)
                data[:, 1] -= np.mean(data[sl, 1])
                s = 'GraphicEQ: '
                s += '; '.join([f'{x[0]:.0f} {x[1]:.1f}' for x in data])
                zip_object.writestr(archive_path, s)
                zip_files.add(archive_path)
                included_paths.append(fp)
    zip_object.close()


def ranking_row(file_path, target, form='over-ear'):
    dir_path = os.path.abspath(os.path.join(file_path, os.pardir))
    rel_path = os.path.relpath(dir_path, os.path.join(ROOT_DIR, 'results'))
    url = form_url(rel_path)
    fr = FrequencyResponse.read_from_csv(file_path)
    if re.search(MOD_REGEX, fr.name):
        return None
    fr.interpolate()
    fr.compensate(target, bass_boost_gain=0.0)  # Pre-computed results are with Harman target without bass
    if form == 'over-ear':
        score, std, slope = fr.harman_overear_preference_score()
        return [f'[{fr.name}]({url})', f'{score:.0f}', f'{std:.2f}', f'{slope:.2f}']
    elif form == 'in-ear':
        score, std, slope, mean = fr.harman_inear_preference_score()
        return [f'[{fr.name}]({url})', f'{score:.0f}', f'{std:.2f}', f'{slope:.2f}', f'{mean:.2f}']


def write_ranking_table():
    harman_inear = os.path.join(ROOT_DIR, 'compensation', 'harman_in-ear_2019v2.csv')
    harman_inear = FrequencyResponse.read_from_csv(harman_inear)
    harman_overear = os.path.join(ROOT_DIR, 'compensation', 'harman_over-ear_2018.csv')
    harman_overear = FrequencyResponse.read_from_csv(harman_overear)

    overear_rows = []
    # Over-ear
    files = dict()
    for fp in glob(os.path.join(ROOT_DIR, 'results', 'crinacle', 'GRAS 43AG-7 over-ear', '*', '*.csv')):
        files[os.path.split(fp)[1]] = fp
    for fp in glob(os.path.join(ROOT_DIR, 'results', 'oratory1990', 'over-ear', '*', '*.csv')):
        files[os.path.split(fp)[1]] = fp
    for fp in files.values():
        row = ranking_row(fp, harman_overear, 'over-ear')
        if row:
            overear_rows.append(row)
    overear_rows = sorted(overear_rows, key=lambda row: float(row[1]), reverse=True)
    overear_str = tabulate(overear_rows, headers=['Name', 'Score', 'STD (dB)', 'Slope'], tablefmt='github')

    inear_rows = []
    # In-ear
    files = dict()
    for fp in glob(os.path.join(ROOT_DIR, 'results', 'crinacle', '711 in-ear', '*', '*.csv')):
        files[os.path.split(fp)[1]] = fp
    for fp in glob(os.path.join(ROOT_DIR, 'results', 'oratory1990', 'in-ear', '*', '*.csv')):
        files[os.path.split(fp)[1]] = fp
    for fp in files.values():
        row = ranking_row(fp, harman_inear, 'in-ear')
        if row:
            inear_rows.append(row)
    inear_str = sorted(inear_rows, key=lambda row: float(row[1]), reverse=True)
    inear_str = tabulate(inear_str, headers=['Name', 'Score', 'STD (dB)', 'Slope', 'Average (dB)'], tablefmt='github')

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
    with open(os.path.join(ROOT_DIR, 'results', 'RANKING.md'), 'w', encoding='utf-8') as fh:
        fh.write(re.sub('\n[ \t]+', '\n', s).strip())


def main():
    write_recommendations()
    write_full_index()
    write_headphonecom_index()
    write_rtings_index()
    write_innerfidelity_index()
    write_crinacle_index()
    write_oratory1990_index()
    write_hesuvi_zip()
    write_ranking_table()


if __name__ == '__main__':
    main()
