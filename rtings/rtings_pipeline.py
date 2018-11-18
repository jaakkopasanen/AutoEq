# -*- coding: utf-8 -*-

import os
import argparse
from glob import glob
from PIL import Image, ImageDraw
import numpy as np
import warnings

from image_graph_parser import ImageGraphParser
from frequency_response import FrequencyResponse


def parse_image(im, model, channel):
    """Parses graph image downloaded from innerfidelity.com"""
    # Find graph edges
    v_lines = ImageGraphParser.find_lines(im, 'vertical', line_color=(204, 204, 204))
    h_lines = ImageGraphParser.find_lines(im, 'horizontal', line_color=(204, 204, 204))
    h_lines = np.array(h_lines)

    # Crop by left and right edges
    box = (v_lines[0], h_lines[0], v_lines[-1], im.size[1])
    im = im.crop(box)
    h_lines -= h_lines[0]  # Cropped to first line, subtract distance from all lines

    # Add missing horizontal lines 115 - 55
    deltas = []
    for i in range(1, len(h_lines)):
        deltas.append(h_lines[i] - h_lines[i - 1])
    delta = max(deltas, key=deltas.count)
    _h_lines = list(h_lines[:1])
    for _ in range(12):  # First line + 12 additional lines
        # Estimate where the line should be
        estimate = _h_lines[-1] + delta
        # Get original lines which are at most 1 pixel away from the estimate
        originals = h_lines[np.abs(np.array(h_lines) - estimate) <= 1]
        if len(originals):
            # Original line found, use it
            estimate = originals[0]
        # Add new line
        _h_lines.append(estimate)
    h_lines = _h_lines

    px_a_max = 0
    px_a_min = h_lines[-1]
    #im.show()

    # X axis
    f_min = 20
    f_max = 20000
    f_step = (f_max / f_min) ** (1 / im.size[0])
    f = [f_min]
    for _ in range(1, im.size[0]):
        f.append(f[-1] * f_step)

    # Y axis
    a_max = 115
    a_min = 55
    a_res = (a_max - a_min) / (px_a_min - px_a_max)

    # Colors
    color_left = (79, 129, 189)
    color_right = (119, 119, 119)

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
            r, g, b = rgba[:3]
            # Graph pixels are colored
            if (channel == 'left' and (r, g, b) == color_left) or (channel == 'right' and (r, g, b) == color_right):
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
    y_0 = px_a_max + 10 / a_res
    y_1 = px_a_min - 10 / a_res
    draw.rectangle(((x0, y_0), (x1, y_1)), outline='magenta')
    draw.rectangle(((x0 + 1, y_0 + 1), (x1 - 1, y_1 - 1)), outline='magenta')

    # Create frequency response
    fr = FrequencyResponse(model, f, amplitude)
    fr.interpolate()
    fr.center()

    return fr, _im


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_dir', type=str, default='images', help='Path to images directory.')
    arg_parser.add_argument('--inspection_dir', type=str, default='inspection', help='Path to inspection directory.')
    arg_parser.add_argument('--output_dir', type=str, default='data', help='Path to data directory.')
    arg_parser.add_argument('--compensation', type=str, default='resources/rtings_compensation_w_bass.csv',
                            help='Path to compensation file.')
    cli_args = arg_parser.parse_args()

    input_dir = os.path.abspath(cli_args.input_dir)
    inspection_dir = os.path.abspath(cli_args.inspection_dir)
    output_dir = os.path.abspath(cli_args.output_dir)
    compensation_path = os.path.abspath(cli_args.compensation)

    if not os.path.isdir(inspection_dir):
        os.makedirs(inspection_dir)
    if not os.path.isdir(os.path.join(inspection_dir, 'left')):
        os.makedirs(os.path.join(inspection_dir, 'left'))
    if not os.path.isdir(os.path.join(inspection_dir, 'right')):
        os.makedirs(os.path.join(inspection_dir, 'right'))
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Compensation
    comp = FrequencyResponse.read_from_csv(compensation_path)

    for file_path in glob(os.path.join(input_dir, '*.png')):
        print(file_path)
        name = os.path.split(file_path)[-1].replace('.png', '')

        # Read and parse image
        im = Image.open(file_path)
        fr_left, inspection_left = parse_image(im, name, 'left')
        fr_right, inspection_right = parse_image(im, name, 'right')

        # Save inspection images
        inspection_left.save(os.path.join(inspection_dir, 'left', name + '.png'))
        inspection_right.save(os.path.join(inspection_dir, 'right', name + '.png'))

        # Create directory
        dir_path = os.path.join(output_dir, name)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

        # Average channels
        if not np.array_equal(fr_left.frequency, fr_right.frequency):
            warnings.warn('Left and right channel frequency data of "{}" don\'t match!'.format(name))
            continue
        raw = np.mean(np.vstack((fr_left.raw, fr_right.raw)), axis=0) + comp.raw
        fr = FrequencyResponse(name=name, frequency=fr_left.frequency, raw=raw)

        # Write to CSV
        fr.write_to_csv(os.path.join(output_dir, name, name + '.csv'))


if __name__ == '__main__':
    main()
