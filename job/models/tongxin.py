# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午11:02
@Software: PyCharm
@File    : tongxin.py
'''

from .base import Base
from sqlalchemy import Column, String, Integer,ForeignKey,Text


class Tongxin(Base):
    __tablename__ = "tongxin"

    id = Column(Integer, autoincrement=True, primary_key=True)
    jobname = Column(String(255), nullable=False)
    money = Column(String(255))
    url = Column(String(255),nullable=False)
    origin = Column(String(255),nullable=False)
    natural = Column(String(255))
    exp = Column(String(255))
    education = Column(String(255))
    time = Column(String(255))
    city = Column(String(255))
    description = Column(Text(65535))
    com_id = Column(Integer,ForeignKey('tongxin_company.id'))