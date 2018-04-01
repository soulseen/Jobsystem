# -*- coding: utf-8 -*-

from .base import Base
from sqlalchemy import Column, String, Integer


class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, autoincrement=True, primary_key=True)
    jobname = Column(String(255), nullable=False)
    money = Column(String(255))
    url = Column(String(255),nullable=False)
    origin = Column(String(255),nullable=False)
    natural = Column(String(255))
    exp = Column(String(255))
    education = Column(String(255))
    time = Column(String(255))