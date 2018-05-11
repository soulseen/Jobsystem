# -*- coding: utf-8 -*-

from .base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship


class Python(Base):
    __tablename__ = "python"

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
    com_id = Column(Integer, ForeignKey('python_company.id'))


class PythonCompany(Base):
    __tablename__ = "python_company"

    id = Column(Integer, autoincrement=True, primary_key=True)
    com_name = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    natural = Column(String(45))
    scale = Column(String(45))
    address = Column(String(255))
    python = relationship(
        'Python',
        primaryjoin="PythonCompany.id==Python.com_id",
        backref='python_company'
    )


class PythonWord(Base):
    __tablename__ = "python_word"

    id = Column(Integer, autoincrement=True, primary_key=True)
    word = Column(String(255), nullable=False)
    count = Column(Integer)
