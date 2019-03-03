# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import re
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main():
    with open(os.path.join(DIR_PATH, os.pardir, 'results', 'README.md'), 'r') as f:
        lines = f.read().split('\n')

    non_alphanumeric = re.compile(r'\W+')
    md_start = re.compile(r'^-( |)\[.*$')

    others = []
    others_norm = [9]
    for line in lines:
        if re.match(md_start, line):
            name = line[3:line.index(']')]
            others.append(name)
            name = re.sub(non_alphanumeric, '', name).lower()
            others_norm.append(name)

    raa = []
    raa_norm = []
    for file in glob(os.path.join(DIR_PATH, 'images', '*')):
        name = os.path.split(file)[-1][:-4]
        raa.append(name)
        name = re.sub(non_alphanumeric, '', name).lower()
        raa_norm.append(name)

    for i, x in enumerate(raa):
        if x in others:
            continue
        partial_matches = []
        for j, y in enumerate(others):
            if x in y or y in x:
                partial_matches.append(others[j])
        if len(partial_matches):
            print(raa[i] + ': ' + ' , '.join(partial_matches))


if __name__ == '__main__':
    main()