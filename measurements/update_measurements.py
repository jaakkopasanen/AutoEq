# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.rtings.rtings_crawler import RtingsCrawler
from measurements.oratory1990.oratory1990_crawler import Oratory1990Crawler
from measurements.crinacle.crinacle_crawler import CrinacleCrawler
from measurements.average import average_measurements

DIR_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


def main():
    opts = Options()
    opts.add_argument('--headless')
    driver = webdriver.Chrome(options=opts)

    for cls in [RtingsCrawler, Oratory1990Crawler, CrinacleCrawler]:
        print(f'Running {cls.__name__}')
        crawler = cls(driver=driver)
        crawler.process_new(prompt=True)
        crawler.write_name_index()

    for dir_path in glob(os.path.join(DIR_PATH, '*', 'data', '*')):
        average_measurements(input_dir=dir_path, output_dir=dir_path)

    driver.close()


if __name__ == '__main__':
    main()
