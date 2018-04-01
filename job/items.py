# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    com_name = scrapy.Field()
    url = scrapy.Field()
    origin = scrapy.Field()
    money = scrapy.Field()
    naturl = scrapy.Field()
    exp = scrapy.Field()
    education = scrapy.Field()
    time = scrapy.Field()
