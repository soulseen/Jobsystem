#_*_coding:utf-8_*_

from .base import Base
from sqlalchemy import String,Column

class Url(Base):
    __tablename__="url"

    