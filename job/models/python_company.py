# -*- coding: utf-8 -*-

from .base import Base
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship

class PythonCompany(Base):
    __tablename__ = "python_company"

    id = Column(Integer, autoincrement=True, primary_key=True)
    com_name = Column(String(255),nullable=False)
    url = Column(String(255),nullable=False)
    natural = Column(String(45))
    scale = Column(String(45))
    address = Column(String(255))
    python = relationship(
        'Python',
        primaryjoin="PythonCompany.id==Python.com_id",
        backref='python_company'
    )