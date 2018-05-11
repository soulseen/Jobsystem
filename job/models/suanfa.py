# -*- coding: utf-8 -*-

from .base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship


class Suanfa(Base):
    __tablename__ = "suanfa"

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
    com_id = Column(Integer, ForeignKey('suanfa_company.id'))


class SuanfaCompany(Base):
    __tablename__ = "suanfa_company"

    id = Column(Integer, autoincrement=True, primary_key=True)
    com_name = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    natural = Column(String(45))
    scale = Column(String(45))
    address = Column(String(255))
    python = relationship(
        'Suanfa',
        primaryjoin="SuanfaCompany.id==Suanfa.com_id",
        backref='suanfa_company'
    )


class SuanfaWord(Base):
    __tablename__ = "suanfa_word"

    id = Column(Integer, autoincrement=True, primary_key=True)
    word = Column(String(255), nullable=False)
    count = Column(Integer)
