# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import urllib
import re
import json
from collections import OrderedDict
import numpy as np
from zipfile import ZipFile
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse
from measurements.manufacturer_index import ManufacturerIndex

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


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
        if re.search(r' \(?(sample |sn)[a-zA-Z0-9]+\)?$', model, flags=re.IGNORECASE):
            # Skip measurements with sample or serial number, those have averaged results
            normalized = re.sub(r' \(?(sample |sn)[a-zA-Z0-9]+\)?$', '', model, flags=re.IGNORECASE)
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
    urls = dict()
    # Get links to Reference Audio Analyzer results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'referenceaudioanalyzer', 'zero', '*')))))
    # Get links to Headphone.com results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'headphonecom', 'sbaf-serious', '*')))))
    # Get links to Rtings results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'rtings', 'avg', '*')))))
    # Get links to Innerfidelity results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'innerfidelity', 'sbaf-serious', '*')))))
    # Get links to Crinacle results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'crinacle_over-ear', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'harman_in-ear_2019v2', '*')))))
    # Get links to oratory1990 results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'harman_over-ear_2018', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'harman_in-ear_2019v2', '*')))))
    # Get links to custom results
    urls.update(get_urls(glob(os.path.abspath(os.path.join(DIR_PATH, 'custom', '*')))))

    with open(os.path.join(DIR_PATH, 'README.md'), 'w', encoding='utf-8') as f:
        keys = sorted(urls.keys(), key=lambda s: s.lower())
        s = '''# Recommended Results
        This is a list of recommended results. Results for other measurements and target curves are available for many
        headphones, these can be found in the
        [full index](https://github.com/jaakkopasanen/AutoEq/blob/master/results/INDEX.md).

        Recommendation priority is: oratory1990 > Crinacle > Innerfidelity > Rtings > Headphone.com > Reference Audio Analyzer.
        This means if there are measurements from multiple sources for the same headphone model only the highest
        priority result will be shown in this list.

        This list has {} headphone models covered but if your headphone is missing you can create settings for it
        yourself by following this guide: [Equalizing Headphones the Easy Way](https://medium.com/@jaakkopasanen/make-your-headphones-sound-supreme-1cbd567832a9)

        '''.format(len(urls))
        s += '\n'.join([urls[key] for key in keys])
        f.write(re.sub('\n[ \t]+', '\n', s).strip())


def get_lines(dirs, source):
    lines = []
    for path in dirs:
        rel_path = os.path.relpath(path, DIR_PATH)
        model = os.path.split(rel_path)[-1]
        if model == 'README.md':
            continue
        lines.append('- [{model}]({url}) by {source}'.format(model=model, source=source, url=form_url(rel_path)))
    return lines


def write_full_index():
    lines = []
    # Get links to Reference Audio Analyzer results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'referenceaudioanalyzer', 'zero', '*'))),
        'Reference Audio Analyzer'
    ))
    # Get links to Headphone.com results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'headphonecom', 'sbaf-serious', '*'))),
        'Headphone.com'
    ))
    # Get links to Rtings results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'rtings', 'avg', '*'))),
        'Rtings'
    ))
    # Get links to Innerfidelity results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'innerfidelity', 'sbaf-serious', '*'))),
        'Innerfidelity'
    ))
    # Get links to Crinacle results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'crinacle_over-ear', '*'))),
        'Crinacle'
    ))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'crinacle', 'harman_in-ear_2019v2', '*'))),
        'Crinacle'
    ))
    # Get links to oratory1990 results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'harman_over-ear_2018', '*'))),
        'oratory1990'
    ))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'harman_in-ear_2019v2', '*'))),
        'oratory1990'
    ))

    with open(os.path.join(DIR_PATH, 'INDEX.md'), 'w', encoding='utf-8') as f:
        lines = sorted(lines, key=lambda s: s.lower())
        s = '''# Index
        This is a list of all equalization profiles. Target is in parentheses if there are results with multiple targets
        from the same source.

        '''
        s += '\n'.join(lines)
        f.write(re.sub('\n[ \t]+', '\n', s).strip())


def write_hesuvi_index():
    os.makedirs(os.path.join(DIR_PATH, 'hesuvi'), exist_ok=True)
    manufacturers = ManufacturerIndex()
    zip_object = ZipFile(os.path.join(DIR_PATH, 'hesuvi.zip'), 'w')
    dir_paths = [
        os.path.join(DIR_PATH, 'oratory1990'),
        os.path.join(DIR_PATH, 'crinacle', 'harman_in-ear_2019v2'),
        os.path.join(DIR_PATH, 'crinacle', 'crinacl_over-ear'),
        os.path.join(DIR_PATH, 'innerfidelity'),
        os.path.join(DIR_PATH, 'rtings'),
        os.path.join(DIR_PATH, 'headphonecom'),
    ]
    zip_files = set()
    for dir_path in dir_paths:
        for fp in glob(os.path.join(dir_path, '**', '* GraphicEQ.txt'), recursive=True):
            _, name = os.path.split(fp)
            name = name.replace(' GraphicEQ.txt', '')
            if re.search(r' \(?(sample |sn)[a-zA-Z0-9]+\)?$', name, flags=re.IGNORECASE):
                # Skip samples, there are averaged results available
                continue
            manufacturer, _ = manufacturers.find(name)
            name = manufacturers.model(name)
            arcname = f'eq/{manufacturer}/{name}.txt'
            if arcname in zip_files:
                # Skip duplicates
                continue
            with open(fp, 'r', encoding='utf-8') as fh:
                s = fh.read()
                data = np.array([x.split() for x in s.split(': ')[1].split('; ')], dtype='float')
                sl = np.logical_and(data[:, 0] > 100, data[:, 0] < 10000)
                data[:, 1] -= np.mean(data[sl, 1])
                s = 'GraphicEQ: '
                s += '; '.join([f'{x[0]:.0f} {x[1]:.1f}' for x in data])
                zip_object.writestr(arcname, s)
                zip_files.add(arcname)

    zip_object.close()


def main():
    write_recommendations()
    write_full_index()
    write_hesuvi_index()


if __name__ == '__main__':
    main()