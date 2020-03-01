# -*- coding: utf-8 -*-

import os
import sys
import json
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from measurements.rtings.rtings_crawler import RtingsCrawler
from measurements.oratory1990.oratory1990_crawler import Oratory1990Crawler


def main():
    for cls in [RtingsCrawler, Oratory1990Crawler]:
        crawler = cls()
        crawler.process_new()
        crawler.write_name_index()


if __name__ == '__main__':
    main()
