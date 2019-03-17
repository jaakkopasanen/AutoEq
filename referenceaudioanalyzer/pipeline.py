# -*- coding: utf-8 -*-

import os
import sys
import argparse
from glob import glob
from PIL import Image, ImageDraw
import numpy as np
import warnings
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from image_graph_parser import ImageGraphParser
from frequency_response import FrequencyResponse

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def parse_image(im, model):
    """Parses graph image downloaded from innerfidelity.com"""
    # Crop by left and right edges
    box = (69, 31, 550, 290)
    im = im.crop(box)

    px_a_max = 0
    px_a_min = im.size[1]
    #im.show()

    # X axis
    f_min = 20
    f_max = 20000
    f_step = (f_max / f_min) ** (1 / im.size[0])
    f = [f_min]
    for _ in range(1, im.size[0]):
        f.append(f[-1] * f_step)

    # Y axis
    a_max = 150
    a_min = 66
    a_res = (a_max - a_min) / (px_a_min - px_a_max)

    # Colors
    #line_color = np.array([50, 155, 254])
    line_color = np.array([0, 135, 0])

    _im = im.copy()
    inspection = _im.load()
    amplitude = []
    # Iterate each column
    for x in range(im.size[0]):
        pxs = []  # Graph pixels
        # Iterate each row (pixel in column)
        for y in range(im.size[1]):
            # Convert read RGB pixel values and convert to HSV
            rgba = im.getpixel((x, y))
            # Graph pixels are colored
            if np.mean(np.abs(line_color - rgba[:3])) < 15:
                pxs.append(float(y))
            else:
                p = im.getpixel((x, y))
                inspection[x, y] = (int(0.3 * p[0]), int(255 * 0.7 + 0.3 * p[1]), int(0 + 0.3 * p[2]))
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
    x0 = np.log(30 / f_min) / np.log(f_step)
    x1 = np.log(10000 / f_min) / np.log(f_step)
    y_0 = px_a_max + 12 / a_res
    y_1 = px_a_min - 12 / a_res
    draw.rectangle(((x0, y_0), (x1, y_1)), outline='magenta')
    draw.rectangle(((x0 + 1, y_0 + 1), (x1 - 1, y_1 - 1)), outline='magenta')

    # Create frequency response
    fr = FrequencyResponse(model, f, amplitude)
    fr.interpolate()
    fr.center()

    return fr, _im


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir', type=str, default=os.path.join(DIR_PATH, 'images'),
                            help='Path to images directory.')
    arg_parser.add_argument('--inspection_dir', type=str, default=os.path.join(DIR_PATH, 'inspection'),
                            help='Path to inspection directory.')
    arg_parser.add_argument('--output_dir', type=str, default=os.path.join(DIR_PATH, 'new_data'),
                            help='Path to data directory.')
    cli_args = arg_parser.parse_args()

    input_dir = os.path.abspath(cli_args.input_dir)
    inspection_dir = os.path.abspath(cli_args.inspection_dir)
    output_dir = os.path.abspath(cli_args.output_dir)

    if not os.path.isdir(inspection_dir):
        os.makedirs(inspection_dir)
    if not os.path.isdir(os.path.join(inspection_dir, 'parse')):
        os.makedirs(os.path.join(inspection_dir, 'parse'))
    if not os.path.isdir(os.path.join(inspection_dir, 'fr')):
        os.makedirs(os.path.join(inspection_dir, 'fr'))
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for file_path in glob(os.path.join(input_dir, '*.png')):
        print(file_path)
        name = os.path.split(file_path)[-1].replace('.png', '')

        # Read and parse image
        im = Image.open(file_path)
        try:
            fr, inspection = parse_image(im, name)
        except Exception as err:
            warnings.warn('Failed to parse "{}"'.format(file_path))
            continue

        # Save inspection images
        inspection.save(os.path.join(inspection_dir, 'parse', name + '.png'))

        # Create directory
        dir_path = os.path.join(output_dir, name)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

        # Plot
        fr.plot_graph(show=False, file_path=os.path.join(inspection_dir, 'fr', name + '.png'))

        # Write to CSV
        fr.write_to_csv(os.path.join(output_dir, name, name + '.csv'))


if __name__ == '__main__':
    main()
