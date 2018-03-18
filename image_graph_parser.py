# -*- coding: utf-8 -*-

import os
import argparse
import numpy as np
from glob import glob
from PIL import Image, ImageDraw
import colorsys
from frequency_response import FrequencyResponse
from operator import itemgetter
from itertools import groupby


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
        file_paths = [os.path.abspath(file_path) for file_path in glob(os.path.join(dir_path, '*'))]

        for file_path in file_paths:
            with open(file_path, 'rb') as f:
                model = os.path.split(file_path)[-1].split('.')[0]
                self.images[model] = Image.open(file_path)

    def parse_images(self, source, models=None):
        """Parses all read images."""
        if models is not None:
            images = {model: self.images[model] for model in models}
        else:
            images = self.images
        for model, image in images.items():
            try:
                if source == 'headphonecom':
                    self.frequency_responses[model] = self.parse_headphonecom(image, model=model)
                elif source == 'innerfidelity':
                    self.frequency_responses[model] = self.parse_innerfidelity(image, model=model)
            except Exception as err:
                # warnings.warn('Image for "{model}" parsing failed: "{err}"'.format(model=model, err=err))
                raise err
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
    def _find_lines(im, orientation):
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
                    r, g, b = im.getpixel((i, j))
                else:
                    r, g, b = im.getpixel((j, i))
                if r + g + b < 450:
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
        v_lines = ImageGraphParser._find_lines(im, 'vertical')
        h_lines = ImageGraphParser._find_lines(im, 'horizontal')

        # Find line thickness
        thickness = 1
        while thickness < len(v_lines):
            if v_lines[thickness] - 1 == v_lines[thickness - 1]:
                thickness += 1
            else:
                break

        # Tight crop
        px_top = h_lines[0] + round(thickness / 2)
        px_bottom = h_lines[-1] - round(thickness) / 2
        px_left = v_lines[0] + round(thickness / 2)
        px_right = v_lines[-1] - thickness - 1
        im = im.crop((px_left, px_top, px_right, px_bottom))
        # Crop right edge to 30kHz
        lines = ImageGraphParser._find_lines(im, 'vertical')
        px_30khz = lines[-7]
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
        _im = im.crop((10, 10, im.size[0] - 10, im.size[1] - 10))
        n_h = len(ImageGraphParser._find_lines(_im, 'horizontal'))
        n_v = len(ImageGraphParser._find_lines(_im, 'vertical'))
        if n_v != 28:
            raise ValueError('Innerfidelity image parsing for "{}" failed because X-axis is not correct!')
        if n_h != 13:
            raise ValueError('Innerfidelity image parsing for "{}" failed because Y-axis is not correct!')

        pix = im.load()
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
                # else:
                #     pix[x, y] = (0, 0, 0)
            if not pxs:
                # No graph pixels found on this column
                amplitude.append(None)
            else:
                # Mean of recorded pixels
                v = np.mean(pxs)
                # Convert to dB value
                v = a_max - v * a_res
                amplitude.append(v)

        fr = FrequencyResponse(model, f, amplitude)
        # im.show()
        return fr

    @staticmethod
    def main():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--in_dir_path', type=str, default=os.path.join('innerfidelity', 'images'),
                                help='Path to directory containing images.')
        arg_parser.add_argument('--out_dir_path', type=str, default=os.path.join('innerfidelity', 'data'),
                                help='Path to output directory.')
        arg_parser.add_argument('--source', type=str, default='innerfidelity', help='Where did the image come from?')
        cli_args = arg_parser.parse_args()

        parser = ImageGraphParser()
        parser.read_images(cli_args.in_dir_path)
        parser.parse_images(cli_args.source)
        for fr in parser.frequency_responses.values():
            dir_path = os.path.join(os.path.abspath(cli_args.out_dir_path), fr.name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            fr.write_to_csv(os.path.join(dir_path, fr.name+' ORIG.csv'))
            fr.plot_graph(show=True)


if __name__ == '__main__':
    ImageGraphParser.main()
