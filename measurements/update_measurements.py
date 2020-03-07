# -*- coding: utf-8 -*-

import os
import sys
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.rtings.rtings_crawler import RtingsCrawler
from measurements.oratory1990.oratory1990_crawler import Oratory1990Crawler


def main():
    opts = Options()
    opts.add_argument('--headless')
    driver = webdriver.Chrome(options=opts)

    for cls in [RtingsCrawler, Oratory1990Crawler]:
        print(f'Running {cls.__name__}')
        crawler = cls(driver)
        crawler.process_new(prompt=True)
        crawler.write_name_index()

    driver.close()


if __name__ == '__main__':
    main()
