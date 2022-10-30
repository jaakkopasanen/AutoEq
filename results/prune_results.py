# -*- coding: utf-8 -*-

import os
import sys
import shutil
from glob import glob
import argparse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.crinacle.crinacle_crawler import CrinacleCrawler
from measurements.oratory1990.oratory1990_crawler import Oratory1990Crawler
from measurements.referenceaudioanalyzer.reference_audio_analyzer_crawler import ReferenceAudioAnalyzerCrawler
from measurements.rtings.rtings_crawler import RtingsCrawler

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))
ROOT_DIR = os.path.join(DIR_PATH, os.pardir)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', dest='dry_run',
                        help='Check which results would be removed without removing.')
    parser.add_argument('--crinacle', action='store_true')
    parser.add_argument('--oratory1990', action='store_true')
    parser.add_argument('--referenceaudioanalyzer', action='store_true')
    parser.add_argument('--rtings', action='store_true')
    cli_args = parser.parse_args()
    dry_run = cli_args.dry_run
    dbs = []
    crawlers = []
    if cli_args.crinacle:
        dbs.append('crinacle')
        crawlers.append(CrinacleCrawler)
    if cli_args.oratory1990:
        dbs.append('oratory1990')
        crawlers.append(Oratory1990Crawler)
    if cli_args.referenceaudioanalyzer:
        dbs.append('referenceaudioanalyzer')
        crawlers.append(ReferenceAudioAnalyzerCrawler)
    if cli_args.rtings:
        dbs.append('rtings')
        crawlers.append(RtingsCrawler)
    for db, crawler in zip(dbs, crawlers):
        existing = crawler.get_existing()
        for path in glob(os.path.join(ROOT_DIR, 'results', db, '**', '*.png'), recursive=True):
            dir_path, file_name = os.path.split(path)
            name = file_name.replace('.png', '')
            item = existing.find_one(true_name=name)
            if not item:
                print(f'Removing "{dir_path}"')
                if not dry_run:
                    shutil.rmtree(dir_path)


if __name__ == '__main__':
    main()
