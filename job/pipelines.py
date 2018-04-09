# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from common.dbtools import DatabaseAgent
from .models.python import Python
from .models.job_python import PythonWord
import jieba


class JobPipeline(object):
    def __init__(self):
        self.db_agent = DatabaseAgent()

    def process_item(self, item, spider):
        seg_list = jieba.cut(item["description"])
        for x in seg_list:
            if x==" ":
                continue
            exists = self.db_agent.get(
                filter_kwargs={
                    "word":str(x)
                },
                orm_model=PythonWord
            )
            if exists:
                self.db_agent.update(
                    filter_kwargs={
                        "word": str(x)
                    },
                    method_kwargs={
                        "count":1+exists.count
                    },
                    orm_model=PythonWord
                )
            else:
                self.db_agent.add(
                    kwargs={
                        "word": str(x),
                        "count":1
                    },
                    orm_model=PythonWord
                )

        self.db_agent.add(
            kwargs=dict(item),
            orm_model=Python
        )

        return item
