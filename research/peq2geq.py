import sys
import unittest
from pathlib import Path
from argparse import ArgumentParser, SUPPRESS
import re
import numpy as np
from autoeq.frequency_response import FrequencyResponse
from autoeq.constants import DEFAULT_FS
from autoeq.peq import PEQ, Peaking, LowShelf, HighShelf

classes = {'PK': Peaking, 'LS': LowShelf, 'HS': HighShelf}


def peq2geq(fcs, qs, gains, types, normalize=False):
    if not (len(fcs) == len(qs) == len(gains) == len(types)):
        raise ValueError('Different number of Fc, Q, gain and filter types')
    fr = FrequencyResponse(name='peq2geq')
    peq = PEQ(fr.frequency, DEFAULT_FS)
    for fc, q, gain, filter_type in zip(fcs, qs, gains, types):
        peq.add_filter(classes[filter_type](fr.frequency, DEFAULT_FS, fc=fc, q=q, gain=gain))
    fr.equalization = peq.fr
    return fr.eqapo_graphic_eq(normalize=normalize)


def read_eqapo(file_path):
    with open(file_path) as fh:
        lines = fh.read().strip().split('\n')
    fcs = []
    qs = []
    gains = []
    types = []
    for line in lines:
        if line[0] == '#':  # Comment line
            continue
        tokens = line.split()
        if tokens[0] == 'Filter':
            fcs.append(float(tokens[tokens.index('Fc') + 1]))
            qs.append(float(tokens[tokens.index('Q') + 1]))
            gains.append(float(tokens[tokens.index('Gain') + 1]))
            types.append(re.search(r'(PK|LS|HS)', line)[0])
        else:
            print(f'Unsupported EqualizerAPO control type "{line}"')
    return fcs, qs, gains, types


def main():
    parser = ArgumentParser('Turns parametric equalizer into EqualizerAPO\'s GraphicEQ.\nCan read filter parameters'
                            'from fc, q, gain and type arguments and/or from EqualizerAPO configuration file.\n\n'
                            'EqualizerAPO file has to contain lines such as\n'
                            '    "Filter: ON PK Fc 15500 Hz Gain -18 dB Q 2"\n')
    parser.add_argument('--fc', type=float, nargs='+',
                        help='Center frequencies in Hz, separated by spaces')
    parser.add_argument('--q', type=float, nargs='+',
                        help='Qualities, separated by spaces')
    parser.add_argument('--gain', type=float, nargs='+',
                        help='Gains, separated by spaces')
    parser.add_argument('--type', nargs='+',
                        help='Filter types. PK for peaking, LS for low-shelf and HS for high-shelf')
    parser.add_argument('--file', type=str, default=SUPPRESS,
                        help='Path to EqualizerAPO config file. Supports filters only.')
    parser.add_argument('--normalize', action='store_true', help='Normalize gain?')
    args = parser.parse_args()
    if 'file' in args and args.file:
        fcs, qs, gains, types = read_eqapo(args.file)
    else:
        fcs, qs, gains, types = [], [], [], []
    if args.fc:
        fcs += args.fc
    if args.q:
        qs += args.q
    if args.gain:
        gains += args.gain
    if args.type:
        types += args.type
    print(peq2geq(fcs, qs, gains, types, normalize=args.normalize))


if __name__ == '__main__':
    main()


class TestPeq2Geq(unittest.TestCase):
    def test_peq2geq(self):
        f = FrequencyResponse.generate_frequencies()
        peq = PEQ(f, DEFAULT_FS, filters=[
            Peaking(f, DEFAULT_FS, fc=500, q=1.41, gain=2),
            HighShelf(f, DEFAULT_FS, fc=2000, q=0.7, gain=-3)
        ])
        geq = peq2geq(
            [filt.fc for filt in peq.filters],
            [filt.q for filt in peq.filters],
            [filt.gain for filt in peq.filters],
            ['PK', 'HS']
        )
        s = geq.split('GraphicEQ: ')[1]
        pairs = [(float(p.split()[0]), float(p.split()[1])) for p in s.split('; ')]
        fr_geq = FrequencyResponse(name='geq', frequency=[_f for _f, _g in pairs], raw=[_g for _f, _g in pairs])
        fr_geq.interpolate()
        fr_geq.raw -= np.mean(peq.fr - fr_geq.raw)
        self.assertLess(np.mean(np.abs(peq.fr - fr_geq.raw)), 0.1)

    def test_read_eqapo(self):
        s = 'Filter 1: ON LS Fc 105 Hz Gain -0.5 dB Q 0.70\n' \
            'Filter 3: ON PK Fc 1773 Hz Gain 3.3 dB Q 1.83\n' \
            'Filter 10: ON HS Fc 10000 Hz Gain -1.7 dB Q 0.70\n'
        fp = Path('test_read_eqapo.txt')
        with open(fp, 'w', encoding='utf-8') as fh:
            fh.write(s)
        fcs, qs, gains, types = read_eqapo(fp)
        fp.unlink(missing_ok=True)
        self.assertEqual(fcs, [105, 1773, 10000])
        self.assertEqual(qs, [0.7, 1.83, 0.7])
        self.assertEqual(gains, [-0.5, 3.3, -1.7])
        self.assertEqual(types, ['LS', 'PK', 'HS'])


