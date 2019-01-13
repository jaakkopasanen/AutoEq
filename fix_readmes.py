# -*- coding: utf-8 -*-

from glob import glob


def main():
    for file in glob('results/*/*/*/README.md'):
        with open(file, 'r') as f:
            s = f.read()
        s = s.replace(
            '\n### EqualizerAPO',
            'See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.\n\n### EqualizerAPO'
        )
        with open(file, 'w') as f:
            f.write(s)


if __name__ == '__main__':
    main()
