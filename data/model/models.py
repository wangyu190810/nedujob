#! /usr/bin/python
# -*- coding:utf-8 -*-
# Filename: models.py
# Author: wangyu190810
# E-mail: wo190810401@gmail.com
# Date: 2014-11-12
# Description:
from datetime import datetime
from time import time

from sqlalchemy.schema import Column,Table
from sqlalchemy.types import UnicodeText,Integer,Unicode,String,DateTime,Date
from sqlalchemy import func
from base import Base


class Job(Base):

    u"""用户信息表"""
    __tablename__= "job"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    company = Column("company",Unicode(255),doc=u"公司")
    company_link = Column("company_link",Unicode(255),doc=u"公司链接")
    address = Column("address",Unicode(255),doc=u"公司地址")
    info_link = Column("info_link",Unicode(255),doc=u"信息链接")
    CEO = Column("CEO",Unicode(255),doc=u"公司创始人")
    salary = Column("salary",Unicode(255),doc=u"公司薪水")
    skill = Column("skill",Unicode(255),doc=u"技能")
    create_time = Column("create_time",Integer,default=lambda: time(), doc=u"发布时间")
    company_info = Column("company_info",Unicode(1000),doc=u"公司简介")
    field = Column("field",Unicode(255),doc=u"公司领域")
    scale = Column("scale",Unicode(255),doc=u"公司规模")
    stage = Column("stage",Unicode(255),doc=u"公司阶段")
    source = Column("source",Unicode(255),doc=u"信息来源")

    @classmethod
    def add_data_from_lagou(cls,connection, company, company_link,
                            skill, company_info, salary,
                            info_link=None,field=None,scale=None,
                            CEO=None,stage=None,adderss=None):
        u"""lagou来的数据"""
        job = Job(company=company, company_link=company_link,
                  skill=skill, info_link=info_link,
                  company_info=company_info,field=field,
                  stage=stage,CEO=CEO,
                  salary=salary,scale=scale,
                  adderss=adderss,source=u"lagou"
                )
        connection.add(job)
        connection.commit()

    @classmethod
    def add_data_from_v2ex(cls,connection,company,info_link,skill):
        u"""v2ex来源的数据"""
        job = Job(company=company,info_link=info_link,
                  skill=skill, source=u"v2ex")
        connection.add(job)
        connection.commit()
        return True


    @classmethod
    def get_job_info_index(cls,connection,limit_num,source=None):
        u"""取出数据"""
        if source:
            return connection.query(Job).filter(Job.source == source).\
                order_by(Job.id).limit(limit_num)
        return connection.query(Job).order_by(Job.id).limit(limit_num)


    @classmethod
    def get_job_info(cls,connection,job_id):
        return connection.query(Job).filter(Job.id == job_id)


