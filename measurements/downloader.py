# -*- coding: utf-8 -*-

import os
import requests
import argparse
import json
import shutil
import warnings


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
            if key in old_image_urls.keys() and image_urls[key] == old_image_urls[key]:
                del image_urls[key]
    self.image_urls = image_urls


def download(urls, output_dir, file_type=None):
    """Downloads images to a directory."""
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    for model, url in urls.items():
        r = requests.get(url, stream=True)
        if r.status_code != 200:
            warnings.warn(f'Failed to download "{model}" at "{url}"')
            continue
        if file_type is None:
            file_type = url.split('.')[-1]
            file_type = file_type.split('?')[0]
        file_path = os.path.join(output_dir, '{}.{}'.format(model, file_type))
        with open(file_path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        del r
        print('Downloaded to "{}"'.format(file_path))


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--json_path', type=str, required=True, help='Path to JSON file containing links.')
    arg_parser.add_argument('--old_json_path', type=str, required=False, default='',
                            help='Path to JSON file containing links already downloaded.')
    arg_parser.add_argument('--output_dir', type=str, required=True, help='Path to output directory.')
    arg_parser.add_argument('--file_type', type=str, default='png', help='File type of the downloaded files.')
    cli_args = arg_parser.parse_args()

    json_path = os.path.abspath(cli_args.json_path)
    if cli_args.old_json_path:
        old_json_path = os.path.abspath(cli_args.old_json_path)
    else:
        old_json_path = None
    output_dir = os.path.abspath(cli_args.output_dir)

    urls = read_json(json_path, old_file_path=old_json_path)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    download(urls, output_dir, file_type=cli_args.file_type)


if __name__ == '__main__':
    main()
