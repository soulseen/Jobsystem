# -*- coding: utf-8 -*-

from .base import Base
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship

class SuanfaCompany(Base):
    __tablename__ = "suanfa_company"

    id = Column(Integer, autoincrement=True, primary_key=True)
    com_name = Column(String(255),nullable=False)
    url = Column(String(255),nullable=False)
    natural = Column(String(45))
    scale = Column(String(45))
    address = Column(String(255))
    python = relationship(
        'Suanfa',
        primaryjoin="SuanfaCompany.id==Suanfa.com_id",
        backref='suanfa_company'
    )