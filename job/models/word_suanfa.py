#_*_coding:utf-8_*_

from .base import Base
from sqlalchemy import Column, String, Integer

class SuanfaWord(Base):
    __tablename__="suanfa_word"

    id = Column(Integer, autoincrement=True, primary_key=True)
    word = Column(String(255),nullable=False)
    count = Column(Integer)