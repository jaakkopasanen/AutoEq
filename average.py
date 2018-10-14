# -*- coding: utf-8 -*-

import os
import re
from glob import glob
import numpy as np
from frequency_response import FrequencyResponse

DIR = 'innerfidelity/data/onear'
DIR = os.path.abspath(DIR)
OUT_DIR = os.path.join('innerfidelity/data/avg')


def main():
    models = {}
    for file_path in glob(os.path.join(DIR, '*')):
        model = os.path.split(file_path)[-1]
        if not (re.search(' sample [a-zA-Z0-9]$', model, re.IGNORECASE) or re.search(' sn[a-zA-Z0-9]+$', model, re.IGNORECASE)):
            # Skip measurements with sample or serial number, those have averaged results
            continue
        norm = re.sub(' sample [a-zA-Z0-9]$', '', model, 0, re.IGNORECASE)
        norm = re.sub(' sn[a-zA-Z0-9]+$', '', norm, 0, re.IGNORECASE)
        try:
            models[norm].append(model)
        except KeyError as err:
            models[norm] = [model]

    for norm, origs in models.items():
        if len(origs) > 1:
            print(norm, origs)
            avg = np.zeros(613)
            f = FrequencyResponse.generate_frequencies()
            for model in origs:
                fr = FrequencyResponse.read_from_csv(os.path.join(DIR, model, model + '.csv'))
                fr.interpolate()
                fr.center()
                avg += fr.raw
            avg /= len(origs)
            fr = FrequencyResponse(name=norm, frequency=f, raw=avg)
            d = os.path.join(OUT_DIR, norm)
            if not os.path.isdir(d):
                os.makedirs(d)
            fr.write_to_csv(os.path.join(d, norm + '.csv'))
            #fr.plot_graph()


if __name__ == '__main__':
    main()
