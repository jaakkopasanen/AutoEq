# -*- coding: utf-8 -*-

import os


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
