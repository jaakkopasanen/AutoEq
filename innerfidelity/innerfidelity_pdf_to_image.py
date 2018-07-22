# -*- coding: utf-8 -*-

import os
import PyPDF2
from ghostscript import Ghostscript
import argparse
from glob import glob
import warnings


def pdf_to_image(input_file, output_dir):
    input_file = os.path.abspath(input_file)
    output_dir = os.path.abspath(output_dir)

    # Read headphone model from the PDF
    f = open(input_file, 'rb')
    pdf = PyPDF2.PdfFileReader(f)
    page = pdf.getPage(0)
    try:
        t = page.extractText()
        start_ind = t.index('All rights reserved.') + len('All rights reserved.')
        end_ind = t.index('%THD+noise')
        name = t[start_ind:end_ind]
        print('Read "{name}" in "{fp}"'.format(name=name, fp=input_file))
    except:
        print('Fail to read "{}"'.format(input_file))
        return

    # Convert to image with ghostscript
    output_file_path = '{}.png'.format(os.path.join(output_dir, name))
    Ghostscript(
        b'pdf2png',
        b'-dNOPAUSE',
        b'-sDEVICE=png16m',
        b'-dBATCH',
        b'-r600',
        b'-dUseCropBox',
        '-sOutputFile={}'.format(output_file_path).encode('utf-8'),
        input_file.encode('utf-8')
    )
    print('\nSaved image to "{}"\n'.format(output_file_path))
    f.close()


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir', type=str, required=True, help='Path to pdf directory.')
    arg_parser.add_argument('--output_dir', type=str, required=True, help='Path to data directory.')
    cli_args = arg_parser.parse_args()

    input_dir = os.path.abspath(cli_args.input_dir)
    output_dir = os.path.abspath(cli_args.output_dir)

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    for file_path in glob(os.path.join(input_dir, '*.pdf')):
        print(file_path)
        try:
            pdf_to_image(file_path, output_dir)
        except Exception as err:
            warnings.warn('Failed to transform PDF into PNG for "{}"'.format(file_path))
            warnings.warn(str(err))


if __name__ == '__main__':
    main()

