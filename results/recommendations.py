# -*- coding: utf-8 -*-

import os
from glob import glob
import urllib
import re
from frequency_response import FrequencyResponse

RESULTS_DIR = os.path.abspath(os.path.join(__file__, os.pardir))


def form_url(rel_path):
    url = '/'.join(FrequencyResponse._split_path(rel_path))
    url = 'https://github.com/jaakkopasanen/AutoEq/tree/master/results/{}'.format(url)
    url = urllib.parse.quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    return url


def get_urls(files):
    urls = dict()
    skipped = dict()
    for path in files:
        rel_path = os.path.relpath(path, RESULTS_DIR)
        model = os.path.split(rel_path)[-1]
        if model == 'README.md':
            continue
        if re.search(' sample [a-zA-Z0-9]$', model, re.IGNORECASE) or re.search(' sn[a-zA-Z0-9]+$', model, re.IGNORECASE):
            # Skip measurements with sample or serial number, those have averaged results
            model = re.sub(' sample [a-zA-Z0-9]$', '', model, 0, re.IGNORECASE)
            model = re.sub(' sn[a-zA-Z0-9]+$', '', model, 0, re.IGNORECASE)
            try:
                skipped[model].append(rel_path)
            except KeyError as err:
                skipped[model] = [rel_path]
            continue
        urls[model.lower()] = '- [{model}]({url})'.format(model=model, url=form_url(rel_path))

    for model, rel_paths in skipped.items():
        # Add skipped models with only one item, these have no averaged results
        if len(rel_paths) == 1:
            urls[model.lower()] = '- [{model}]({url})'.format(model=model, url=form_url(rel_paths[0]))
    return urls


def main():
    urls = dict()
    # Get links to Headphone.com results
    urls.update(get_urls(glob(os.path.abspath(os.path.join('headphonecom', 'sbaf-serious', '*')))))
    # Get links to Rtings results
    urls.update(get_urls(glob(os.path.abspath(os.path.join('rtings', 'avg', '*')))))
    # Get links to Innerfidelity results
    urls.update(get_urls(glob(os.path.abspath(os.path.join('innerfidelity', 'sbaf-serious', '*')))))
    # Get links to oratory1990 results
    urls.update(get_urls(glob(os.path.abspath(os.path.join('oratory1990', 'harman_over-ear_2018', '*')))))
    urls.update(get_urls(glob(os.path.abspath(os.path.join('oratory1990', 'harman_in-ear_2017-1', '*')))))
    # Get links to custom results
    urls.update(get_urls(glob(os.path.abspath(os.path.join('custom', '*')))))

    with open('README.md', 'w') as f:
        keys = sorted(urls.keys())
        s = '''# Recommended Results
        This is a list of recommended results. Results for other measurements are available for many headphones, these
        can be found in the [full index](https://github.com/jaakkopasanen/AutoEq/blob/master/results/INDEX.md).
        
        Recommendation priority is: oratory1990 > Innerfidelity > Rtings > Headphone.com. This means if there are
        measurements from multiple sources for the same headphone model only the highest priority result will be shown
        in this list.
        '''
        s += '\n'.join([urls[key] for key in keys])
        f.write(re.sub('\n[ \t]+', '\n', s).strip())


if __name__ == '__main__':
    main()
