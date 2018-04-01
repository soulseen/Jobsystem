#-*- coding: utf-8 -*-

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'test','-o','./export/items.json'])

