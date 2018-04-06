# -*- coding: utf-8 -*-

from job.items import JobItem #CompanyItem
from job.dbtools import DatabaseAgent
from job.models.company import Company
import scrapy
import re


class test(scrapy.Spider):
    name = 'zhilian_python'
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
        for page in range(1, pages):
            yield scrapy.Request(
                url=self.zhilian.format(**self.data, page=page),
                headers=self.header,
                callback=self.get_url
            )

    def get_url(self, response):
        job_urls = response.xpath('//a[@par]/@href').extract()
        for job_url in job_urls:
            yield scrapy.Request(
                url=job_url,
                headers=self.header,
                callback=self.parse
            )

    def parse(self, response):
        db_agent = DatabaseAgent()
        jobitem = JobItem()
        #companyItem = CompanyItem()
        jobitem["url"] = response.url
        jobitem["origin"] = 'zhilian'
        jobitem["jobname"] = response.xpath('//div[@class="inner-left fl"]/h1/text()').extract()[0]
        job_information = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/text()').extract()
        jobitem["money"] = job_information[0]
        jobitem["natural"] = job_information[1]
        jobitem["exp"] = job_information[2]
        jobitem["education"] = job_information[3]
        jobitem["time"] = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/span/text()').extract()[0]

        # CompanyItem["url"] = response.xpath('//div[@class="inner-left fl"]/h2/a/@href').extract()
        # CompanyItem["com_name"] = response.xpath('//div[@class="inner-left fl"]/h2/a/text()').extract()[0]
        # company_information = response.xpath('//ul[@class="terminal-ul clearfix terminal-company mt20"]/li/strong/text()').extract()
        # for x in company_information:
        #     print(x)
        jobitem["com_name"] = 'a'
        jobitem["com_url"] = "b"
        jobitem["com_natural"] = "c"
        jobitem["scale"] = "d"
        jobitem["address"] = "e"
        # com = db_agent.add(
        #     orm_model=Company,
        #     kwargs=dict(companyItem)
        # )
        # jobitem["com_id"] = com.id

        yield jobitem
