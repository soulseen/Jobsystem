# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午11:02
@Software: PyCharm
@File    : tongxin.py
'''

from .base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship


class Tongxin(Base):
    __tablename__ = "tongxin"

    id = Column(Integer, autoincrement=True, primary_key=True)
    jobname = Column(String(255), nullable=False)
    money = Column(String(255))
    url = Column(String(255), nullable=False)
    origin = Column(String(255), nullable=False)
    natural = Column(String(255))
    exp = Column(String(255))
    education = Column(String(255))
    time = Column(String(255))
    city = Column(String(255))
    description = Column(Text(65535))
    com_id = Column(Integer, ForeignKey('tongxin_company.id'))


class TongxinCompany(Base):
    __tablename__ = "tongxin_company"

    id = Column(Integer, autoincrement=True, primary_key=True)
    com_name = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    natural = Column(String(45))
    scale = Column(String(45))
    address = Column(String(255))
    python = relationship(
        'Tongxin',
        primaryjoin="TongxinCompany.id==Tongxin.com_id",
        backref='tongxin_company'
    )


class TongxinWord(Base):
    __tablename__ = "tongxin_word"

    id = Column(Integer, autoincrement=True, primary_key=True)
    word = Column(String(255), nullable=False)
    count = Column(Integer)
