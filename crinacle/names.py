# -*- coding: utf-8 -*-
import os
import sys
from glob import glob
import re
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))
ROOT_DIR = os.path.abspath(os.path.join(DIR_PATH, os.pardir))


def main():
    full_names = set()
    with open(os.path.join(DIR_PATH, 'names.txt')) as f:
        full_names.update(set(f.read().split('\n')))

    for file_path in glob(os.path.join(ROOT_DIR, 'headphonecom', 'data', 'inear', '*')):
        full_names.add(os.path.split(file_path)[1])
    for file_path in glob(os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'inear', '*')):
        full_names.add(os.path.split(file_path)[1])
    for file_path in glob(os.path.join(ROOT_DIR, 'oratory1990', 'data', 'inear', '*')):
        full_names.add(os.path.split(file_path)[1])
    for file_path in glob(os.path.join(ROOT_DIR, 'rtings', 'data', 'inear', '*')):
        full_names.add(os.path.split(file_path)[1])

    name_index = dict()
    unknown = []
    for file_path in glob(os.path.join(DIR_PATH, 'raw_data', '*')):
        name = os.path.split(file_path)[1]
        name = name[:-6]  # Remove ".txt" and " R" or " L" suffix
        if name in name_index:
            continue
        name_index[name] = set()
        match = False
        for full_name in full_names:
            if re.search('( |-|^){}( |$)'.format(re.escape(name)), full_name, flags=re.IGNORECASE):
                match = True
                name_index[name].add(full_name)
        if not match:
            unknown.append(name)

    print('{} unknown IEMs'.format(len(unknown)))

    s = ''
    for name, full_names in name_index.items():
        s += '{n}\t{fns}\n'.format(n=name, fns='\t'.join(full_names))

    with open(os.path.join(DIR_PATH, 'name_index.tsv'), 'w') as f:
        f.write(s)


if __name__ == '__main__':
    main()
