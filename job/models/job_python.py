#_*_coding:utf-8_*_

from .base import Base
from sqlalchemy import Column, String, Integer

class PythonWord(Base):
    __tablename__="python_word"

    id = Column(Integer, autoincrement=True, primary_key=True)
    word = Column(String(255),nullable=False)
    count = Column(Integer)