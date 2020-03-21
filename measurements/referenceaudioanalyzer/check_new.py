# -*- coding: utf-8 -*-

import os
import sys
import json
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    with open(os.path.join(DIR_PATH, 'names.txt'), 'r', encoding='utf-8') as f:
        old = f.read().split('\n')

    with open(os.path.join(DIR_PATH, 'links.json'), 'r', encoding='utf-8') as f:
        new = json.loads(f.read())

    for name in list(new.keys()):
        if name in old:
            del new[name]

    with open(os.path.join(DIR_PATH, 'links_new.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(new, ensure_ascii=False, intend=2))

    with open(os.path.join(DIR_PATH, 'names.txt'), 'w+', encoding='utf-8') as f:
        f.write('\n'.join(new.keys()))


if __name__ == '__main__':
    main()
