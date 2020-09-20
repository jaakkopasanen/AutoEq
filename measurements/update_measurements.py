# -*- coding: utf-8 -*-

import os
import sys
import argparse
from glob import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.rtings.rtings_crawler import RtingsCrawler
from measurements.oratory1990.oratory1990_crawler import Oratory1990Crawler
from measurements.crinacle.crinacle_crawler import CrinacleCrawler
from measurements.referenceaudioanalyzer.reference_audio_analyzer_crawler import ReferenceAudioAnalyzerCrawler
from measurements.average import average_measurements

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main(crinacle=False, oratory1990=False, rtings=False, referenceaudioanalyzer=False, prompt=False):
    classes = []
    if not (crinacle | oratory1990 | rtings | referenceaudioanalyzer):
        # None means all
        crinacle = True
        oratory1990 = True
        rtings = True
        referenceaudioanalyzer = True

    if crinacle:
        classes.append(CrinacleCrawler)
    if oratory1990:
        classes.append(Oratory1990Crawler)
    if rtings:
        classes.append(RtingsCrawler)
    if referenceaudioanalyzer:
        classes.append(ReferenceAudioAnalyzerCrawler)

    if Oratory1990Crawler in classes or ReferenceAudioAnalyzerCrawler in classes or RtingsCrawler in classes:
        # oratory1990 and Reference Audio Analyzer crawlers require Selenium Web Driver
        opts = Options()
        opts.add_argument('--headless')
        driver = webdriver.Chrome(os.path.join(DIR_PATH, 'chromedriver'), options=opts)
    else:
        driver = None

    for cls in classes:
        print(f'Running {cls.__name__}')
        crawler = cls(driver=driver)
        crawler.process_new(prompt=prompt)
        crawler.write_name_index()

    for dir_path in glob(os.path.join(DIR_PATH, '*', 'data', '*')):
        average_measurements(input_dir=dir_path, output_dir=dir_path)

    if driver is not None:
        driver.close()


def create_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--crinacle', action='store_true', help='Update Crinacle measurements?')
    parser.add_argument('--oratory1990', action='store_true', help='Update oratory1990 measurements?')
    parser.add_argument('--rtings', action='store_true', help='Update Rtings measurements?')
    parser.add_argument('--referenceaudioanalyzer', action='store_true',
                        help='Update Reference Audio Analyzer measurements?')
    parser.add_argument('--prompt', action='store_true', help='Prompt for true names and forms?')
    return vars(parser.parse_args())


if __name__ == '__main__':
    main(**create_cli())
