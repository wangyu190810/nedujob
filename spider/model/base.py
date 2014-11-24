#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: base.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-05
#Description: 

from sqlalchemy.schema import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative


metadata = MetaData()
from config import Config



@as_declarative(metadata=metadata)
class Base(object):
    pass


engine = create_engine(Config.db,echo=True)

def conn():
    connection = engine.connect()
    return connection

"""数据库的一些抽象"""

