# -*- coding: utf-8 -*-

import os
import re
import numpy as np
from frequency_response import FrequencyResponse


def main():
    with open('results/README.md', 'r') as f:
        lines = f.read().split('\n')[1:]

    models = []
    rmses = []

    for line in lines:
        # Parse file path
        model = re.search('\[.+\]', line)[0][1:-1]
        url = re.search('\]\(.+\)', line)[0][2:-1]
        path = os.path.abspath(url[52:].replace('%20', ' '))
        specific_model = os.path.split(path)[-1]
        path = os.path.join(path, specific_model + '.csv')
        # Record model and RMSE of frequency response
        fr = FrequencyResponse.read_from_csv(path)
        models.append(model)
        rmses.append(np.sqrt(np.mean(np.square(fr.error))))

    # Sort models by RMSE
    models = np.array(models)
    rmses = np.array(rmses)
    sorted_inds = np.argsort(rmses)
    rmses = rmses[sorted_inds]
    models = models[sorted_inds]

    data = np.transpose(np.vstack((models, rmses)))
    print(data.shape)
    s = '# Hall of Fame\nHeadphones with smallest deviation (RMSE) from ideal frequency target.\n'
    for row in data:
        s += '- {model}: {rmse:.2f}dB\n'.format(model=row[0], rmse=float(row[1]))
    with open('Hall of Fame.md', 'w') as f:
        f.write(s)


if __name__ == '__main__':
    main()
