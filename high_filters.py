# -*- coding: utf-8 -*-

import os
from glob import glob


def main():
    for file in glob('results/*/*/*/* ParametricEQ.txt'):
        with open(file, 'r') as f:
            s = f.read()
        filts = []
        for line in s.split('\n'):
            if line == '':
                continue
            fc = line[line.index('Fc') + 3:line.index('Gain') - 1]
            gain = line[line.index('Gain') + 5:line.index('Q') - 1]
            q = line[line.index('Q') + 2:]
            if float(fc[:-3]) > 20000:
                filts.append([fc, q, gain])
        if len(filts):
            print(' '.join(os.path.split(file)[-1].split()[:-1]), filts)


if __name__ == '__main__':
    main()
