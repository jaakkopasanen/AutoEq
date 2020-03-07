# -*- coding: utf-8 -*-

import os


def prompt_name(options=None):
    options = options if options is not None else []
    if 'skip' not in options:
        options.insert(0, 'skip')
    s = 'What is it\'s true name?'
    if len(options):
        s += ' Select a number or write the name if none of the options.'
    print(s)
    if len(options):
        print(f'\n'.join(f'[{i}] {o}' for i, o in enumerate(options)))
    name = input('> ')
    try:
        name = options[int(name)]
        if name == 'skip':
            return None
    except (KeyError, ValueError):
        pass
    return name


def prompt_form():
    options = ['onear', 'inear', 'earbud']
    print('What is it\'s type?')
    print(f'\n'.join(f'[{i+1}] {o}' for i, o in enumerate(options)))
    while True:
        form = input('> ')
        try:
            return options[int(form) - 1]
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
