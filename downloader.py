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
        with open(file_path, 'r', encoding='utf-8') as f:
            self.image_urls = json.loads(f.read())

    def download_images(self, output_dir):
        """Downloads images to a directory."""
        output_dir = os.path.abspath(output_dir)
        for model, url in self.image_urls.items():
            r = requests.get(url, stream=True)
            if r.status_code != 200:
                warnings.warn('Failed to download image for "{model}" at "{url}"'.format(model=model, url=url))
                continue
            try:
                file_path = os.path.join(output_dir, '{}.png'.format(model))
                with open(file_path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            except OSError:
                print('Failed to save', model)
                continue
            del r
            print('Downloaded image to "{}"'.format(file_path))

    @staticmethod
    def main():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--json_path', type=str, required=True, help='Path to JSON file containing links.')
        arg_parser.add_argument('--output_dir', type=str, required=True, help='Path to output directory.')
        cli_args = arg_parser.parse_args()

        json_path = os.path.abspath(cli_args.json_path)
        output_dir = os.path.abspath(cli_args.output_dir)

        downloader = Downloader()
        downloader.read_json(json_path)
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        downloader.download_images(output_dir)


if __name__ == '__main__':
    Downloader.main()
