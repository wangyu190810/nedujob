#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: lagou.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-12
#Description: 

from sqlalchemy.schema import Column,Table
from sqlalchemy.types import UnicodeText,Integer,Unicode,String,DateTime,Date
from sqlalchemy.sql import insert,select,update

from datetime import datetime

from base import metadata,conn,Base

lagou = Table("lagou",metadata,
        Column("id",Integer,primary_key=True,index=True),
        Column("company",Unicode(255),doc=u"公司"),
        Column("company_link",Unicode(255),doc=u"公司链接"),
        Column("lagou_link",Unicode(255),doc=u"拉钩链接"),
        Column("CEO",Unicode(255),doc=u"公司创始人"),
        Column("salary",Unicode(255),doc=u"公司薪水"),
        Column("skill",Unicode(255),doc=u"技能"),
        Column("timing",Date,doc=u"发布时间"),
        Column("field",Unicode(255),doc=u"公司领域"),
        Column("scale",Unicode(255),doc=u"公司规模"),
        Column("stage",Unicode(255),doc=u"公司阶段"),

        )

class Lagou(Base):

    @classmethod
    def add_company(self,company,company_link,lagou_link,CEO,salary,timing,field,scale,stage):
        lagou.insert().values()