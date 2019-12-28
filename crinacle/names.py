# -*- coding: utf-8 -*-
import os
import sys
from glob import glob
import re
import pandas as pd
import json
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))
ROOT_DIR = os.path.abspath(os.path.join(DIR_PATH, os.pardir))


def get_book():
    with open(os.path.join(DIR_PATH, 'phone_book.json')) as fh:
        data = json.load(fh)
    book = dict()
    for manufacturer in data:
        manufacturer_name = manufacturer['name']
        if 'suffix' in manufacturer:
            manufacturer_name += f' {manufacturer["suffix"]}'
        for model in manufacturer['phones']:
            if type(model) == str:
                # Plain string
                book[model.strip()] = f'{manufacturer_name} {model}'.strip()

            else:
                # Object
                if type(model['file']) == str:
                    # Single file as string, wrap in list
                    model['file'] = [model['file']]

                if 'suffix' in model:
                    for f, suffix in zip(model['file'], model['suffix']):
                        book[f.strip()] = f'{manufacturer_name} {model["name"]} {suffix}'.strip()
                else:
                    for f in model['file']:
                        book[f.strip()] = f'{manufacturer_name} {model["name"]}'.strip()

    return book


def add_last_word(name, keys, name_proposals, d=None):
    for key in keys:
        if re.search(' {}$'.format(re.escape(name)), key, flags=re.IGNORECASE):
            name_proposals[name].add(d[key] if d is not None else key)


def add_any_word(name, keys, name_proposals, d=None):
    for key in keys:
        if re.search('( |-|^){}( |$)'.format(re.escape(name)), key, flags=re.IGNORECASE):
            name_proposals[name].add(d[key] if d is not None else key)


def add_partials(name, keys, name_proposals, d=None):
    for key in keys:
        if re.search(re.escape(name), key, flags=re.IGNORECASE):
            name_proposals[name].add(d[key] if d is not None else key)


def main():
    full_names = set()
    with open(os.path.join(DIR_PATH, 'names.txt')) as f:
        full_names.update(set(f.read().split('\n')))
    with open(os.path.join(DIR_PATH, 'names.txt'), 'w') as f:
        f.write('\n'.join(sorted(full_names, key=lambda x: x.lower())))

    for file_path in glob(os.path.join(ROOT_DIR, 'headphonecom', 'data', 'inear', '*')):
        full_names.add(os.path.split(file_path)[1])
    for file_path in glob(os.path.join(ROOT_DIR, 'innerfidelity', 'data', 'inear', '*')):
        full_names.add(os.path.split(file_path)[1])
    for file_path in glob(os.path.join(ROOT_DIR, 'oratory1990', 'data', 'inear', '*')):
        full_names.add(os.path.split(file_path)[1])
    for file_path in glob(os.path.join(ROOT_DIR, 'rtings', 'data', 'inear', '*')):
        full_names.add(os.path.split(file_path)[1])

    book = get_book()
    s = '\n'.join([f'{key}\t{book[key]}' for key in book.keys()])
    with open(os.path.join(DIR_PATH, 'book.tsv'), 'w') as fh:
        fh.write(s)
    for name in book.values():
        full_names.add(name)

    name_proposals = dict()
    unknown = []
    for file_path in glob(os.path.join(DIR_PATH, 'raw_data', '*')):
        name = os.path.split(file_path)[1]
        # Remove ".txt" and " R" or " L" suffix
        name = re.sub('\.txt$', '', name)
        name = re.sub(' (L|R)', '', name)
        if name in name_proposals:
            continue

        name_proposals[name] = set()

        # Add last words of book keys
        add_last_word(name, book.keys(), name_proposals, d=book)

        if len(name_proposals[name]) == 0:
            # No end matches, find full words anywhere in book keys
            add_any_word(name, book.keys(), name_proposals, d=book)

        if len(name_proposals[name]) == 0:
            # No full word matches, find partials in book keys
            add_partials(name, book.keys(), name_proposals, d=book)

        if len(name_proposals[name]) == 0:
            # Look for full names where current name is the last word
            add_last_word(name, full_names, name_proposals)

        if len(name_proposals[name]) == 0:
            # No end matches, find full words anywhere
            add_any_word(name, full_names, name_proposals)

        if len(name_proposals[name]) == 0:
            # No full word matches, find partials
            add_partials(name, full_names, name_proposals)

        if len(name_proposals[name]) == 0:
            unknown.append(name)

    print('{} unknown IEMs'.format(len(unknown)))

    name_index = pd.read_csv(os.path.join(DIR_PATH, 'name_index.tsv'), sep='\t', header=None)
    name_index = list(name_index[0])

    s = ''
    for name, full_names in name_proposals.items():
        if name in name_index:
            continue
        s += '{n}\t{fns}\t\n'.format(n=name, fns='\t'.join(full_names))

    with open(os.path.join(DIR_PATH, 'name_proposals.tsv'), 'w') as f:
        f.write(s)


if __name__ == '__main__':
    main()
