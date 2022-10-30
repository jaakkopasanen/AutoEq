# -*- coding: utf-8 -*-

import os
import argparse
import numpy as np
from glob import glob
from PIL import Image, ImageDraw
import colorsys
from operator import itemgetter
from itertools import groupby
import warnings
from autoeq.frequency_response import FrequencyResponse


class ImageGraphParser:
    def __init__(self):
        self.images = dict()
        self.frequency_responses = dict()

    def read_images(self, dir_path):
        """Reads images from file.

        Args:
            dir_path: Path to a directory full of images. Mutually exclusive to `file_path`

        Returns:
            - **data:** Graph data for parsed images
        """
        file_paths = [os.path.abspath(file_path) for file_path in glob(os.path.join(dir_path, '*.png'))]

        for file_path in file_paths:
            try:
                with open(file_path, 'rb') as f:
                    model = os.path.split(file_path)[-1].split('.')[0]
                    self.images[model] = Image.open(file_path)
            except:
                warnings.warn('Failed to read image in path "{}"'.format(file_path))

    def parse_images(self, source, models=None, inspection_dir=None):
        """Parses all read images."""
        if models is not None:
            images = {model: self.images[model] for model in models}
        else:
            images = self.images

        if inspection_dir is not None:
            inspection_dir = os.path.abspath(inspection_dir)
            os.makedirs(inspection_dir, exist_ok=True)

        for model, image in images.items():
            try:
                if source == 'headphonecom':
                    self.frequency_responses[model] = self.parse_headphonecom(image, model=model)
                elif source == 'innerfidelity':
                    self.frequency_responses[model], inspection = self.parse_innerfidelity(image, model=model)
                    if inspection_dir is not None:
                        inspection.save(os.path.join(inspection_dir, model+'.png'))
            except Exception as err:
                warnings.warn('Image for "{model}" parsing failed: "{err}"'.format(model=model, err=err))
                continue
            print('Parsed image for "{}"'.format(model))

    @staticmethod
    def parse_headphonecom(im, model, scale=40):
        """Parses graph image downloaded from headphone.com"""
        # Crop out everything but graph area
        px_top = 24  # Pixels from top to +30dB
        px_bottom = 125  # Pixels from bottom to -30dB
        px_left = 51  # Pixels from left to 10Hz
        px_right = 50  # Pixels from right edge
        box = (px_left, px_top, im.size[0]-px_right, im.size[1]-px_bottom)
        im = im.crop(box)

        # X axis
        f_min = 10
        f_max = 20000
        px_f_max = 71
        f_step = (f_max / f_min)**(1/(im.size[0]-(px_f_max-px_right)))
        f = [f_min]
        for _ in range(1, im.size[0]):
            f.append(f[-1] * f_step)

        # Y axis
        a_max = scale
        a_min = -scale
        a_res = (a_max - a_min) / im.size[1]  # dB / px

        amplitude = []
        # Iterate each column
        for x in range(im.size[0]):
            pxs = []  # Graph pixels
            # Iterate each row (pixel in column)
            for y in range(im.size[1]):
                # Convert read RGB pixel values and convert to HSV
                h, l, s = colorsys.rgb_to_hls(*[v/255.0 for v in im.getpixel((x, y))])
                # Scale hue to 0-255
                h *= 255
                # Graph pixels are blue
                if s > 0.5 and 140 < h < 160:
                    pxs.append(float(y))
            if not pxs:
                # No graph pixels found on this column
                amplitude.append(None)
            else:
                # Mean of recorded pixels
                v = sum(pxs) / len(pxs)
                # Convert to dB value
                v = a_max - v * a_res
                amplitude.append(v)

        fr = FrequencyResponse(model, f, amplitude)
        return fr

    @staticmethod
    def find_lines(im, orientation, line_color=None):
        if orientation == 'vertical':
            ori1 = 0
            ori2 = 1
        elif orientation == 'horizontal':
            ori1 = 1
            ori2 = 0
        else:
            raise ValueError('\'orientation\' must be "vertical" or "horizontal"!')

        lines = []
        for i in range(1, im.size[ori1]):
            # Count number of black pixels
            count = 0
            for j in range(im.size[ori2]):
                if orientation == 'vertical':
                    rgba = im.getpixel((i, j))
                else:
                    rgba = im.getpixel((j, i))
                r, g, b = rgba[:3]
                if line_color is not None:
                    if (r, g, b) == line_color:
                        count += 1
                else:
                    if r + g + b < 450 and r == g == b:
                        count += 1
            if count > im.size[ori2] / 2:
                # More than half of pixels are black -> this is a line
                lines.append(i)

        means = []
        for k, g in groupby(enumerate(lines), lambda x:x[0]-x[1]):
            group = map(itemgetter(1), g)
            means.append(int(np.round(np.mean(list(group)))))

        return means

    @staticmethod
    def parse_innerfidelity(im, model, px_top=800, px_bottom=4600, px_left=500, px_right=2500):
        """Parses graph image downloaded from innerfidelity.com"""
        # Crop out everything but graph area (roughly)
        box = (px_left, px_top, im.size[0]-px_right, im.size[1]-px_bottom)
        im = im.crop(box)

        # Find graph edges (thick lines)
        v_lines = ImageGraphParser.find_lines(im, 'vertical')
        h_lines = ImageGraphParser.find_lines(im, 'horizontal')

        px_top = h_lines[0]
        px_bottom = h_lines[-1]
        px_left = v_lines[0]
        px_right = v_lines[-1]
        im = im.crop((px_left, px_top, px_right, px_bottom))
        # Crop right edge to 30kHz
        lines = ImageGraphParser.find_lines(im, 'vertical')
        px_30khz = lines[-8]
        im = im.crop((0, 0, px_30khz, im.size[1]))

        # X axis
        f_min = 10
        f_max = 30000
        f_step = (f_max / f_min)**(1/im.size[0])
        f = [f_min]
        for _ in range(1, im.size[0]):
            f.append(f[-1] * f_step)

        # Y axis
        a_max = 20
        a_min = -50
        a_res = (a_max - a_min) / im.size[1]  # dB / px

        # Check crop
        _im = im.crop((20, 20, im.size[0] - 20, im.size[1] - 20))
        # im.show()
        n_h = len(ImageGraphParser.find_lines(_im, 'horizontal'))
        n_v = len(ImageGraphParser.find_lines(_im, 'vertical'))
        if n_v != 28:
            print(n_v)
            raise ValueError('Innerfidelity image parsing for "{}" failed because X-axis is not correct!'.format(model))
        if n_h != 13:
            print(n_h)
            raise ValueError('Innerfidelity image parsing for "{}" failed because Y-axis is not correct!'.format(model))

        _im = im.copy()
        pix = _im.load()
        amplitude = []
        # Iterate each column
        for x in range(im.size[0]):
            pxs = []  # Graph pixels
            # Iterate each row (pixel in column)
            for y in range(im.size[1]):
                # Convert read RGB pixel values and convert to HSV
                h, s, v = colorsys.rgb_to_hsv(*[v/255.0 for v in im.getpixel((x, y))])
                # Graph pixels are colored
                if s > 0.8:
                    pxs.append(float(y))
                else:
                    p = im.getpixel((x, y))
                    pix[x, y] = (int(0.9*p[0]), int(255*0.1+0.9*p[1]), int(0+0.9*p[2]))
            if not pxs:
                # No graph pixels found on this column
                amplitude.append(None)
            else:
                # Mean of recorded pixels
                v = np.mean(pxs)
                # Convert to dB value
                v = a_max - v * a_res
                amplitude.append(v)

        draw = ImageDraw.Draw(_im)
        x0 = np.log(20/f_min) / np.log(f_step)
        x1 = np.log(20000/f_min) / np.log(f_step)
        draw.rectangle(((x0, 10/a_res), (x1, 60/a_res)), outline='magenta')

        fr = FrequencyResponse(model, f, amplitude)
        return fr, _im

    @staticmethod
    def parse_cropped(im, name='fr', f_min=20, f_max=20000, a_min=-20, a_max=20):
        """Parses an image which has been cropped tightly to given boundaries. Image left boundary must be cropped
        to f_min, right boundary to f_max, bottom boundary to a_min and top boundary to a_max. Only colored pixels will
        be scanned.

        Args:
            im: Image
            name: Name of the image / produced FrequencyResponse
            f_min: Frequency at left boundary of the image
            f_max: Frequency at right boundary of the image
            a_min: Amplitude at bottom boundary of the image
            a_max: Amplitude at top boundary of the image

        Returns:
            FrequencyResponse created from colored pixels in the image
        """
        # X axis (frequencies)
        f_step = (f_max / f_min) ** (1 / im.size[0])
        f = [f_min]
        for _ in range(1, im.size[0]):
            f.append(f[-1] * f_step)

        # Y axis (amplitude)
        a_res = (a_max - a_min) / im.size[1]  # dB / px

        _im = im.copy()
        pix = _im.load()
        amplitude = []
        for x in range(im.size[0]):
            pxs = []  # Graph pixels
            # Iterate each row (pixel in column)
            for y in range(im.size[1]):
                # Convert read RGB pixel values and convert to HSV
                h, s, v = colorsys.rgb_to_hsv(*[v/255.0 for v in im.getpixel((x, y))])
                # Graph pixels are colored
                if s > 0.8:
                    pxs.append(float(y))
                else:
                    p = im.getpixel((x, y))
                    pix[x, y] = (int(0.9*p[0]), int(255*0.1+0.9*p[1]), int(0+0.9*p[2]))
            if not pxs:
                # No graph pixels found on this column
                amplitude.append(None)
            else:
                # Mean of recorded pixels
                v = np.mean(pxs)
                # Convert to dB value
                v = a_max - v * a_res
                amplitude.append(v)
        return FrequencyResponse(name=name, frequency=f, raw=amplitude)

    @staticmethod
    def main():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--input_dir', type=str, required=True, help='Path to directory containing images.')
        arg_parser.add_argument('--output_dir', type=str, required=True, help='Path to output directory.')
        arg_parser.add_argument('--inspection_dir', type=str, required=True, help='Path to inspection directory.')
        arg_parser.add_argument('--source', type=str, default='headphonecom', help='Where did the image come from?')
        cli_args = arg_parser.parse_args()

        input_dir = os.path.abspath(cli_args.input_dir)
        output_dir = os.path.abspath(cli_args.output_dir)
        inspection_dir = os.path.abspath(cli_args.inspection_dir)

        if os.path.isdir(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        if os.path.isdir(inspection_dir):
            os.makedirs(inspection_dir, exist_ok=True)

        parser = ImageGraphParser()
        parser.read_images(input_dir)
        parser.parse_images(cli_args.source, inspection_dir=inspection_dir)
        for fr in parser.frequency_responses.values():
            dir_path = os.path.join(os.path.abspath(output_dir), fr.name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            fr.write_to_csv(os.path.join(dir_path, fr.name+'.csv'))
            # fr.plot_graph(show=True)


if __name__ == '__main__':
    ImageGraphParser.main()
