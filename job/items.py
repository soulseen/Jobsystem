# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    jobname = scrapy.Field()
    url = scrapy.Field()
    origin = scrapy.Field()
    money = scrapy.Field()
    natural = scrapy.Field()
    exp = scrapy.Field()
    education = scrapy.Field()
    time = scrapy.Field()
    com_name = scrapy.Field()
    com_url = scrapy.Field()
    com_natural = scrapy.Field()
    scale = scrapy.Field()
    address = scrapy.Field()