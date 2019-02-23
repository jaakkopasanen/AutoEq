# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import urllib
import re
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def form_url(rel_path):
    url = '/'.join(FrequencyResponse._split_path(rel_path))
    url = 'https://github.com/jaakkopasanen/AutoEq/tree/master/results/{}'.format(url)
    url = urllib.parse.quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    return url


def get_lines(dirs, source):
    lines = []
    for path in dirs:
        rel_path = os.path.relpath(path, DIR_PATH)
        model = os.path.split(rel_path)[-1]
        if model == 'README.md':
            continue
        lines.append('- [{model}]({url}) by {source}'.format(model=model, source=source, url=form_url(rel_path)))
    return lines


def main():
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
    # Get links to oratory1990 results
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'harman_over-ear_2018', '*'))),
        'oratory1990'
    ))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join(DIR_PATH, 'oratory1990', 'harman_in-ear_2017-1', '*'))),
        'oratory1990 (Harman in-ear 2017-1'
    ))
    lines.extend(get_lines(
        glob(os.path.abspath(os.path.join('oratory1990', 'usound', '*'))),
        'oratory1990 (Usound)'
    ))
    # Get links to custom results
    lines.extend(get_lines(glob(os.path.abspath(os.path.join('custom', '*'))), 'AutoEQ'))

    with open(os.path.join(DIR_PATH, 'INDEX.md'), 'w') as f:
        lines = sorted(lines)
        s = '''# Index
        This is a list of all equalization profiles. Target is in parentheses if there are results with multiple targets
        from the same source.
        
        '''
        s += '\n'.join(lines)
        f.write(re.sub('\n[ \t]+', '\n', s).strip())


if __name__ == '__main__':
    main()
