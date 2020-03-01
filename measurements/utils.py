# -*- coding: utf-8 -*-

import os


def prompt_type():
    types = ['onear', 'inear', 'earbud']
    print(f'What is it\'s type?\n' + '\n'.join(f'[{i}] {t}' for i, t in enumerate(types)))
    while True:
        form = input('> ')
        try:
            return types[int(form)]
        except:
            print('That didn\'t work, try again.')


def split_path(path):
    components = []
    while True:
        path, file = os.path.split(path)
        if file:
            components.append(file)
        elif path:
            components.append(path)
            break
        else:
            break
    return components[::-1]
