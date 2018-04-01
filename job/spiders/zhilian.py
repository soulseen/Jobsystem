# -*- coding: utf-8 -*-

from job.items import JobItem
from job.dbtools import DatabaseAgent
import scrapy
import re


class test(scrapy.Spider):
    name = 'test'
    zhilian = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl={city}&kw={name}&sm=0&sg=897d9246117644c0b19afbf08e729ca7&p={page}"
    header = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWe'
                            'bKit/537.36(KHTML, like Gecko) Chrome/6'
                            '3.0.3239.132 Safari/537.36'}
    data = {
        "city": "上海",
        "name": "python工程师"
    }

    def start_requests(self):
        yield scrapy.Request(
            url=self.zhilian.format(**self.data, page=""),
            headers=self.header,
            callback=self.get_page
        )

    def get_page(self, response):
        pattern = re.compile(r'共<em>(\d+)</em>个职位满足条件')
        name = pattern.search(response.body.decode('utf-8'))
        pages = int(int(name.group(1)) / 60) + 2
        for page in range(1,pages):
            yield scrapy.Request(
                url=self.zhilian.format(**self.data,page=page),
                headers=self.header,
                callback=self.get_url
            )

    def get_url(self,response):
        job_urls = response.xpath('//a[@par]/@href').extract()
        for job_url in job_urls:
            yield scrapy.Request(
                url=job_url,
                headers=self.header,
                callback=self.parse
            )

    def parse(self,response):
        jobitem = JobItem()
        db_agent = DatabaseAgent()
        url = {"url":response.url}
        db_agent.add(

        )
        jobitem["job_name"] = response.xpath('//div[@class="inner-left fl"]/h1/text()').extract()[0]
        jobitem["com_name"] = response.xpath('//div[@class="inner-left fl"]/h2/a/text()').extract()[0]
        information = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/text()').extract()
        jobitem["money"] = information[0]
        jobitem["all_day"] = information[1]
        jobitem["exp"] = information[2]
        jobitem["education"] = information[3]



        #return jobitem