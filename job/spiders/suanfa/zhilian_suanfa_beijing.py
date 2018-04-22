# -*- coding: utf-8 -*-

import re

import scrapy

from common.common import clear, parse_word
from common.dbtools import DatabaseAgent
from job.items import JobItem, CompanyItem
from job.models.suanfa import Suanfa
from job.models.suanfa_company import SuanfaCompany
from job.models.word_suanfa import SuanfaWord


class test(scrapy.Spider):
    name = 'zhilian_python_beijing'
    zhilian = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl={city}&kw={name}&sm=0&sg=897d9246117644c0b19afbf08e729ca7&p={page}"
    header = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWe'
                            'bKit/537.36(KHTML, like Gecko) Chrome/6'
                            '3.0.3239.132 Safari/537.36'}
    data = {
        "city": "北京",
        "name": "算法工程师"
    }
    com_model = SuanfaCompany
    job_model = Suanfa
    word_model = SuanfaWord
    db_agent = DatabaseAgent()

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
            job = self.db_agent.get(
                filter_kwargs={"url": job_url},
                orm_model=self.job_model
            )
            if job:
                continue
            yield scrapy.Request(
                url=job_url,
                headers=self.header,
                callback=self.parse
            )

    def parse(self, response):
        jobitem = JobItem()
        companyitem = CompanyItem()
        jobitem["city"] = self.data.get("city")
        jobitem["url"] = response.url
        jobitem["origin"] = 'zhilian'
        jobitem["jobname"] = response.xpath('//div[@class="inner-left fl"]/h1/text()').extract()[0]
        job_information = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/text()').extract()
        jobitem["money"] = job_information[0]
        if '-' in job_information[1]:
            num = 1
        else:
            num = 0
        jobitem["natural"] = job_information[num + 1]
        jobitem["exp"] = job_information[num + 2]
        jobitem["education"] = job_information[num + 3]
        try:
            jobitem["time"] = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/span/text()').extract()[0]
        except:
            jobitem["time"] = response.xpath('//div[@class="terminalpage-left"]/ul/li/strong/text()').extract()[0]
        des_lis = response.xpath(
            '//div[@class="tab-cont-box"][1]/div[@class="tab-inner-cont"]/p/text()').extract()
        description = ''
        for des in des_lis:
            description = description + des
        jobitem["description"] = clear(description)

        companyitem["url"] = response.xpath(
            '//a[@onclick="recordOutboundLink(this, \'terminalpage\', \'tocompanylink3\');"]/@href').extract()[0]
        companyitem["com_name"] = response.xpath('//div[@class="inner-left fl"]/h2/a/text()').extract()[0]
        company_information = response.xpath(
            '//ul[@class="terminal-ul clearfix terminal-company mt20"]/li/strong/text()').extract()
        companyitem["scale"] = company_information[0]
        companyitem["natural"] = company_information[1]
        companyitem["address"] = company_information[2].strip()
        com = self.db_agent.get(
            filter_kwargs=companyitem,
            orm_model=self.com_model
        )
        if not com:
            com = self.db_agent.add(
                orm_model=self.com_model,
                kwargs=dict(companyitem)
            )
        jobitem["com_id"] = com.id

        self.db_agent.add(
            kwargs=dict(jobitem),
            orm_model=self.job_model
        )
        parse_word(jobitem["description"],self.word_model)

        yield jobitem
