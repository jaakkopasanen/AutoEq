# -*- coding: utf-8 -*-

import os
import PyPDF2
from ghostscript import Ghostscript
import argparse
from glob import glob


def pdf_to_image(input_file_path, output_dir_path):
    input_file_path = os.path.abspath(input_file_path)
    output_dir_path = os.path.abspath(output_dir_path)

    # Read headphone model from the PDF
    f = open(input_file_path, 'rb')
    pdf = PyPDF2.PdfFileReader(f)
    page = pdf.getPage(0)
    try:
        t = page.extractText()
        start_ind = t.index('All rights reserved.') + len('All rights reserved.')
        end_ind = t.index('%THD+noise')
        name = t[start_ind:end_ind]
        print('Read "{name}" in "{fp}"'.format(name=name, fp=input_file_path))
    except:
        print('Fail to read "{}"'.format(input_file_path))
        return

    # Convert to image with ghostscript
    output_file_path = '{}.png'.format(os.path.join(output_dir_path, name))
    Ghostscript(
        b'pdf2png',
        b'-dNOPAUSE',
        b'-sDEVICE=png16m',
        b'-dBATCH',
        b'-r600',
        b'-dUseCropBox',
        '-sOutputFile={}'.format(output_file_path).encode('utf-8'),
        input_file_path.encode('utf-8')
    )
    print('\nSaved image to "{}"\n'.format(output_file_path))
    f.close()


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir_path', type=str, default=os.path.join('innerfidelity', 'pdf'),
                            help='Path to pdf directory.')
    arg_parser.add_argument('--output_dir_path', type=str, default=os.path.join('innerfidelity', 'images'),
                            help='Path to data directory.')
    cli_args = arg_parser.parse_args()

    for file_path in glob(os.path.join(os.path.abspath(cli_args.input_dir_path), '*.pdf')):
        pdf_to_image(file_path, cli_args.output_dir_path)


if __name__ == '__main__':
    main()

