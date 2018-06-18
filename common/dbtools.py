# -*- coding: utf-8 -*-

import os
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from job.models.base import Base

MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_DBNAME = os.getenv("MYSQL_DBNAME", "jobsystem")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWD = os.getenv("MYSQL_PASSWD", "1234")
MYSQL_PORT = os.getenv("MYSQL_PORT", 3306)

DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER,
                                                       MYSQL_PASSWD,
                                                       MYSQL_HOST,
                                                       MYSQL_PORT,
                                                       MYSQL_DBNAME
                                                       )
engine = create_engine(DATABASE_URL,
                       encoding="utf8",
                       connect_args={'charset': 'utf8'})


@contextmanager
def sqlalchemy_session():
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.expunge_all()
        session.close()


def orm_session_control(orm_func):
    """控制SQLAlchemy session的动态创建"""

    def decorator(*args, **kwargs):
        with sqlalchemy_session() as session:
            kwargs["session"] = session
            return orm_func(*args, **kwargs)

    return decorator


class DatabaseAgent():
    """封装SQLAlchemy的逻辑做一些db CRUD的工作"""

    orm_model = None

    @orm_session_control
    def get(self, filter_kwargs={}, just_first=True, orm_model=None, session=None):
        query_result = session.query(orm_model).filter_by(**filter_kwargs)
        if just_first:
            return query_result.first()
        else:
            return query_result.all()

    @orm_session_control
    def add(self, kwargs, orm_model=None, session=None):
        new_orm = orm_model(**kwargs)
        session.add(new_orm)
        session.commit()
        return new_orm

    @orm_session_control
    def update(self, filter_kwargs, method_kwargs,
               need_commit=True, orm_model=None, session=None):
        orm_model = orm_model if orm_model is not None else self.orm_model
        session.query(orm_model).filter_by(**filter_kwargs).update(method_kwargs)
        if need_commit:
            session.commit()


def create_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


def drop_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
