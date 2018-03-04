# -*- coding: utf-8 -*-

import os
import requests
import argparse
import json
import shutil
import warnings


class Downloader:
    def __init__(self):
        self.image_urls = dict()

    def read_json(self, file_path):
        """Reads JSON file containing headphone models and image urls."""
        file_path = os.path.abspath(file_path)
        with open(file_path, 'r') as f:
            self.image_urls = json.loads(f.read())

    def download_images(self, dir_path):
        """Downloads images to a directory."""
        dir_path = os.path.abspath(dir_path)
        for model, url in self.image_urls.items():
            r = requests.get(url, stream=True)
            if r.status_code != 200:
                warnings.warn('Failed to download image for "{model}" at "{url}"'.format(model=model, url=url))
                continue
            with open(os.path.join(dir_path, '{}.png'.format(model)), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            del r
            print('Downloaded image for "{}"'.format(model))

    @staticmethod
    def main():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--json_path', type=str, default=os.path.join('headphonecom', 'headphonecom_40.json'),
                                help='Path to JSON file.')
        arg_parser.add_argument('--dir_path', type=str, default=os.path.join('headphonecom', 'images_40'),
                                help='Path to output directory.')
        cli_args = arg_parser.parse_args()

        downloader = Downloader()
        downloader.read_json(cli_args.json_path)
        downloader.download_images(cli_args.dir_path)


if __name__ == '__main__':
    Downloader.main()
