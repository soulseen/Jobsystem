# -*- coding: utf-8 -*-

import scrapy
import re
from job.items import JobItem


class test(scrapy.Spider):
    name = 'test'
    # start_urls = ['https://www.liaoxuefeng.com/']


    def start_requests(self):
        yield scrapy.Request(
            url='https://www.liaoxuefeng.com/',
            callback=self.parse
        )

    def parse(self, response):
        item = JobItem()
        pattern = re.compile(r'<title>(.*?)</title>')
        name = pattern.search(response.body.decode('utf-8'))

        item["name"] = str(name.groups(0))
        # item['name'] = "爱上".encode('utf-8')

        print(item)
        yield item
