# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from common.dbtools import DatabaseAgent
import jieba


class JobPipeline(object):
    def __init__(self):
        self.db_agent = DatabaseAgent()

    def process_item(self, item, spider, model):
        seg_list = jieba.cut(item["description"])
        for x in seg_list:
            if x==" ":
                continue
            exists = self.db_agent.get(
                filter_kwargs={
                    "word":str(x)
                },
                orm_model=model
            )
            if exists:
                self.db_agent.update(
                    filter_kwargs={
                        "word": str(x)
                    },
                    method_kwargs={
                        "count":1+exists.count
                    },
                    orm_model=model
                )
            else:
                self.db_agent.add(
                    kwargs={
                        "word": str(x),
                        "count":1
                    },
                    orm_model=model
                )


        return item
