# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午11:02
@Software: PyCharm
@File    : tongxin_company.py
'''


from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class TongxinCompany(Base):
    __tablename__ = "tongxin_company"

    id = Column(Integer, autoincrement=True, primary_key=True)
    com_name = Column(String(255),nullable=False)
    url = Column(String(255),nullable=False)
    natural = Column(String(45))
    scale = Column(String(45))
    address = Column(String(255))
    python = relationship(
        'Tongxin',
        primaryjoin="TongxinCompany.id==Tongxin.com_id",
        backref='tongxin_company'
    )