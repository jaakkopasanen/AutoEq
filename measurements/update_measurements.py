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
from measurements.average import average_measurements

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main(crinacle=False, oratory1990=False, rtings=False):
    classes = []
    if crinacle or (not oratory1990 and not rtings):
        classes.append(CrinacleCrawler)
    if oratory1990 or (not crinacle and not rtings):
        classes.append(Oratory1990Crawler)
    if rtings or (not oratory1990 and not crinacle):
        classes.append(RtingsCrawler)

    if Oratory1990Crawler in classes:
        opts = Options()
        opts.add_argument('--headless')
        driver = webdriver.Chrome(options=opts)
    else:
        driver = None

    for cls in classes:
        print(f'Running {cls.__name__}')
        crawler = cls(driver=driver)
        crawler.process_new(prompt=True)
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
    return vars(parser.parse_args())


if __name__ == '__main__':
    main(**create_cli())
