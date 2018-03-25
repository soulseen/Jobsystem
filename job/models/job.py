# -*- coding: utf-8 -*-

from .base import Base
from sqlalchemy import Column, String, Integer


class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=True)
