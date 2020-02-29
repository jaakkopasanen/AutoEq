# -*- coding: utf-8 -*-

import os
import sys
from ghostscript import Ghostscript
import argparse
from glob import glob
from PIL import Image, ImageDraw
import colorsys
import numpy as np
import pandas as pd
import shutil
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir, os.pardir)))
from measurements.image_graph_parser import ImageGraphParser
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def parse_image(im, model, px_top=800, px_bottom=4400, px_left=0, px_right=2500):
    """Parses graph image downloaded from innerfidelity.com"""
    # Crop out everything but graph area (roughly)
    box = (px_left, px_top, im.size[0] - px_right, im.size[1] - px_bottom)
    im = im.crop(box)
    #im.show()

    # Find graph edges
    v_lines = ImageGraphParser.find_lines(im, 'vertical')
    h_lines = ImageGraphParser.find_lines(im, 'horizontal')

    # Crop by graph edges
    box = (v_lines[0], h_lines[0], v_lines[1], h_lines[1])
    im = im.crop(box)
    #im.show()

    # X axis
    f_min = 10
    f_max = 20000
    f_step = (f_max / f_min) ** (1 / im.size[0])
    f = [f_min]
    for _ in range(1, im.size[0]):
        f.append(f[-1] * f_step)

    # Y axis
    a_max = 30
    a_min = -20
    a_res = (a_max - a_min) / im.size[1]

    _im = im.copy()
    pix = _im.load()
    amplitude = []
    y_legend = 40 / 50 * im.size[1]
    x0_legend = np.log(70 / f_min) / np.log(f_step)
    x1_legend = np.log(1000 / f_min) / np.log(f_step)
    # Iterate each column
    for x in range(im.size[0]):
        pxs = []  # Graph pixels
        # Iterate each row (pixel in column)
        for y in range(im.size[1]):
            if y > y_legend and x0_legend < x < x1_legend:
                # Skip pixels in the legend box
                continue

            # Convert read RGB pixel values and convert to HSV
            h, s, v = colorsys.rgb_to_hsv(*[v / 255.0 for v in im.getpixel((x, y))])
            # Graph pixels are colored
            if 0.7 < s < 0.9 and 20 / 360 < h < 30 / 360:
                pxs.append(float(y))
            else:
                p = im.getpixel((x, y))
                pix[x, y] = (int(0.3 * p[0]), int(255 * 0.7 + 0.3 * p[1]), int(0.3 * p[2]))
        if not pxs:
            # No graph pixels found on this column
            amplitude.append(None)
        else:
            # Mean of recorded pixels
            v = np.mean(pxs)
            # Convert to dB value
            v = a_max - v * a_res
            amplitude.append(v)

    # Inspection image
    draw = ImageDraw.Draw(_im)
    x0 = np.log(20 / f_min) / np.log(f_step)
    x1 = np.log(10000 / f_min) / np.log(f_step)
    draw.rectangle(((x0, 10 / a_res), (x1, 40 / a_res)), outline='magenta')
    draw.rectangle(((x0 + 1, 10 / a_res + 1), (x1 - 1, 40 / a_res - 1)), outline='magenta')

    fr = FrequencyResponse(model, f, amplitude)
    fr.interpolate()
    fr.center()
    return fr, _im


def pdf_to_image(input_file, output_file):
    input_file = os.path.abspath(input_file)
    output_file = os.path.abspath(output_file)

    # Read headphone model from the PDF
    f = open(input_file, 'rb')

    # Convert to image with ghostscript
    # Using temporary paths with Ghostscript because it seems to be unable to work with non-ascii characters
    tmp_in = os.path.join(os.path.split(input_file)[0], '__tmp.pdf')
    tmp_out = os.path.join(os.path.split(output_file)[0], '__tmp.png')
    if tmp_in == input_file or tmp_out == output_file:
        return
    shutil.copy(input_file, tmp_in)
    Ghostscript(
        b'pdf2png',
        b'-dNOPAUSE',
        b'-sDEVICE=png16m',
        b'-dBATCH',
        b'-r600',
        b'-dUseCropBox',
        f'-sOutputFile={tmp_out}'.encode('utf-8'),
        tmp_in.encode('utf-8')
    )
    shutil.copy(tmp_out, output_file)
    print('\nSaved image to "{}"\n'.format(output_file))
    f.close()

    return Image.open(output_file)


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir', type=str, default=os.path.join(DIR_PATH, 'pdf'),
                            help='Path to pdf directory.')
    arg_parser.add_argument('--image_dir', type=str, default=os.path.join(DIR_PATH, 'images'),
                            help='Path to images directory.')
    arg_parser.add_argument('--inspection_dir', type=str, default=os.path.join(DIR_PATH, 'inspection'),
                            help='Path to inspection directory.')
    arg_parser.add_argument('--output_dir', type=str, default=os.path.join(DIR_PATH, 'new_data'),
                            help='Path to data directory.')
    cli_args = arg_parser.parse_args()

    input_dir = os.path.abspath(cli_args.input_dir)
    image_dir = os.path.abspath(cli_args.image_dir)
    inspection_dir = os.path.abspath(cli_args.inspection_dir)
    output_dir = os.path.abspath(cli_args.output_dir)

    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(inspection_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'onear'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'inear'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'earbud'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'unknown'), exist_ok=True)

    new_data = [os.path.split(p)[1].replace('.pdf', '') for p in glob(os.path.join(output_dir, '*', '*'))]

    name_index = pd.read_csv(
        os.path.join(DIR_PATH, 'name_index.tsv'),
        sep='\t', header=None, encoding='utf-8'
    )
    name_index.columns = ['original', 'correct', 'type']

    for file_path in glob(os.path.join(input_dir, '*.pdf')):
        print(file_path)
        hp_type = 'unknown'
        name = os.path.split(file_path)[1].replace('.pdf', '')
        item = name_index.loc[name_index['original'] == name]
        if len(item) > 0:
            name = item.iloc[0]['correct']
            hp_type = item.iloc[0]['type']
        else:
            print(f'"{name}" not found in name index!')

        if hp_type == 'ignore' or name in new_data:
            continue

        output_file = os.path.join(image_dir, name + '.png')
        im = pdf_to_image(file_path, output_file)
        if im is None:
            continue
        fr, inspection = parse_image(im, name)
        inspection.save(os.path.join(inspection_dir, name + '.png'))
        dir_path = os.path.join(output_dir, hp_type, name)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        fr.write_to_csv(os.path.join(dir_path, name + '.csv'))


if __name__ == '__main__':
    main()

