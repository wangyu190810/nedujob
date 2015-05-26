#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: base.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-05
#Description: 

from sqlalchemy.schema import MetaData
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative


from config import Config

from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
Base = declarative_base()

engine = create_engine(Config.db,echo=True)

DBSession = scoped_session(sessionmaker(bind=engine))


def connection():
    connection = engine.connect()
    return connection

"""数据库的一些抽象"""

