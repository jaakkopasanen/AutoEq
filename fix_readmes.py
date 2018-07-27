# -*- coding: utf-8 -*-

from glob import glob
import math


def main():
    for file_path in glob('results/*/*/*/*/*.md'):
        with open(file_path, 'r') as f:
            lines = f.read().split('\n')

        lines = [lines[i] for i in [0, 7, 8, 9, 10, 12]]
        preamp = float(lines[3][8:14][:-2])
        preamp = math.floor(preamp*10) / 10
        lines.insert(2, 'Preamp: {}dB'.format(preamp))
        del lines[4]
        lines.insert(1, 'Replace `C:\Program Files\EqualizerAPO\config\config.txt` with:')
        lines.insert(6, '**OR** if using HeSuVi replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and '
                        'omit `Preamp: {f_preamp}dB` and instead set Global volume in the UI for both channels to '
                        '**{i_preamp}**.'.format(f_preamp=preamp, i_preamp=int(preamp*10)))

        with open(file_path, 'w') as f:
            f.write('\n'.join(lines))


if __name__ == '__main__':
    main()
