# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午2:13
@Software: PyCharm
@File    : word_tongxin.py
'''

from .base import Base
from sqlalchemy import Column, String, Integer

class TongxinWord(Base):
    __tablename__="tongxin_word"

    id = Column(Integer, autoincrement=True, primary_key=True)
    word = Column(String(255),nullable=False)
    count = Column(Integer)