# -*- coding: utf-8 -*-

import os
import sys
import re
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


class ManufacturerIndex:
    def __init__(self):
        with open(os.path.join(DIR_PATH, 'manufacturers.tsv'), encoding='utf-8') as fh:
            manufacturers = fh.read().strip().split('\n')
        self.manufacturers = [m.strip().split('\t') for m in manufacturers]

    def find(self, name):
        matches = []
        for manufacturer in self.manufacturers:
            for variant in manufacturer:
                if re.search(f'^{variant}', name, flags=re.IGNORECASE):
                    # Case insensitive match with manufacturer, add true manufacturer and the matching variant
                    matches.append((manufacturer[0], variant))
                    break

        if not matches:
            return None

        # Select longest match
        true_manufacturer, match = sorted(matches, key=lambda x: len(x[1]), reverse=True)[0]
        return true_manufacturer, match

    def replace(self, name):
        manufacturer, match = self.find(name)
        # Replace manufacturer with the match
        true_name = re.sub(f'^{match}', manufacturer, name, flags=re.IGNORECASE)
        return true_name
