# -*- coding: utf-8 -*-

from glob import glob
from frequency_response import FrequencyResponse


def main():
    for file in glob('oratory1990/data/*/*/*.csv'):
        fr = FrequencyResponse.read_from_csv(file)
        fr.interpolate()
        fr.center()
        fr.write_to_csv(file)
        print(fr.name)


if __name__ == '__main__':
    main()
