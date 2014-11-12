#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: base.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-05
#Description: 

from sqlalchemy.shema import metaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
metadata = metaData()

@as_declarative(metadata=metadata)
class Base(object):
    pass


engine = create_engine("mysql://root:1234@localhost/nedujob?charset=utf8",echo=True)
conn = engine.connect()


"""数据库的一些抽象"""

