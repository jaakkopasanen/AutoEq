# -*- coding: utf-8 -*-

import os
from glob import glob
import urllib
from frequency_response import FrequencyResponse

RESULTS_DIR = os.path.abspath(os.path.join(__file__, os.pardir))


def get_urls(files):
    urls = dict()
    for path in files:
        rel_path = os.path.relpath(path, RESULTS_DIR)
        model = os.path.split(rel_path)[-1]
        url = '/'.join(FrequencyResponse._split_path(rel_path))
        url = 'https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/{}'.format(url)
        url = urllib.parse.quote(url, safe="%/:=&?~#+!$,;'@()*[]")
        urls[model] = '[{model}]({url})'.format(model=model, url=url)
    return urls


def main():
    urls = dict()
    # Get links to Headphone.com results
    urls.update(get_urls(glob(os.path.abspath(os.path.join('headphonecom', 'sbaf-serious', '*')))))
    # Get links to Innerfidelity results and override Headphone.com results with the same name
    urls.update(get_urls(glob(os.path.abspath(os.path.join('innerfidelity', 'sbaf-serious', '*')))))

    with open('README.md', 'w') as f:
        keys = sorted(urls.keys())
        f.write('\n'.join([urls[key] for key in keys]))


if __name__ == '__main__':
    main()
