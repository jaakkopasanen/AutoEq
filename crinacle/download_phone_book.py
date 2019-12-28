# -*- coding: utf-8 -*-

import os
import sys
import requests
import json
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main():
    res = requests.get('https://crinacle.com/graphing/data/phone_book.json')
    with open(os.path.join(DIR_PATH, 'phone_book.json'), 'w') as fh:
        fh.write(res.content.decode('utf-8'))


if __name__ == '__main__':
    main()
