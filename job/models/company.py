# -*- coding: utf-8 -*-

from .base import Base
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, autoincrement=True, primary_key=True)
    com_name = Column(String(255),nullable=False)
    url = Column(String(255),nullable=False)
    natural = Column(String(45))
    scale = Column(String(45))
    address = Column(String(255))
    python = relationship(
        'Python',
        #primaryjoin="Company.id==Python.com_id",
        backref='company'
    )