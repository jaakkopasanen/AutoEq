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

    def read_json(self, file_path, old_file_path=None):
        """Reads JSON file containing headphone models and image urls."""
        # Read old links
        if old_file_path is not None:
            old_file_path = os.path.abspath(old_file_path)
            with open(old_file_path, 'r', encoding='utf-8') as f:
                old_image_urls = json.loads(f.read())
        else:
            old_image_urls = None

        # Read new links
        file_path = os.path.abspath(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            image_urls = json.loads(f.read())

        # Remove old links from the new links
        if old_image_urls is not None:
            keys = list(image_urls.keys())
            for key in keys:
                if key in old_image_urls.keys():
                    del image_urls[key]
        self.image_urls = image_urls

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
        arg_parser.add_argument('--old_json_path', type=str, required=False, default='',
                                help='Path to JSON file containing links already downloaded.')
        arg_parser.add_argument('--output_dir', type=str, required=True, help='Path to output directory.')
        cli_args = arg_parser.parse_args()

        json_path = os.path.abspath(cli_args.json_path)
        if cli_args.old_json_path:
            old_json_path = os.path.abspath(cli_args.old_json_path)
        else:
            old_json_path = None
        output_dir = os.path.abspath(cli_args.output_dir)

        downloader = Downloader()
        downloader.read_json(json_path, old_file_path=old_json_path)
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        downloader.download_images(output_dir)


if __name__ == '__main__':
    Downloader.main()
