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
from sqlalchemy.types import UnicodeText,Integer,Unicode,String,DateTime,Date,TEXT
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import func
from base import Base


class Job(Base):

    u"""工作信息表"""
    __tablename__= "job"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    company = Column(Unicode(255),doc=u"公司")
    title = Column(Unicode(255),doc=u"数据标题")
    content = Column(Unicode(2000),doc=u"数据内容原文")
    content_rendered = Column(TEXT,doc=u"数据内容html")
    company_link = Column(Unicode(255),doc=u"公司链接")
    address = Column(Unicode(255),doc=u"公司地址")
    info_link = Column(Unicode(255),doc=u"信息链接")
    CEO = Column(Unicode(255),doc=u"公司创始人")
    salary = Column(Unicode(255),doc=u"公司薪水")
    skill = Column(Unicode(255),doc=u"技能")
    create_time = Column(Integer,default=lambda: time(), doc=u"采集时间")
    publish_time = Column(Unicode(255),doc=u"发布时间")
    company_info = Column(Unicode(1000),doc=u"公司简介")
    field = Column(Unicode(255),doc=u"公司领域")
    scale = Column(Unicode(255),doc=u"公司规模")
    stage = Column(Unicode(255),doc=u"公司阶段")
    source = Column(Unicode(255),doc=u"信息来源")
    tag = Column(JSONB,doc=u"工作标签")

    @classmethod
    def add_data_from_lagou(cls,connection, company, company_link,
                            skill, company_info, salary,title,
                            info_link,content,content_rendered,
                            publish_time,field=None,scale=None,
                            CEO=None,stage=None,address=None,
                            tag=None):
        u"""lagou来的数据"""
        job = Job(company=company, company_link=company_link,
                  skill=skill, info_link=info_link,
                  company_info=company_info,field=field,
                  stage=stage,CEO=CEO,
                  salary=salary,scale=scale,
                  address=address,source=u"lagou",
                  title=title,
                  content=content,
                  content_rendered=content_rendered,
                  publish_time = publish_time,
                  tag=tag
                )
        connection.add(job)
        connection.commit()

    @classmethod
    def add_data_from_v2ex(cls, connection, title,
                           info_link, skill, content,
                           content_rendered,tag):
        u"""v2ex来源的数据"""
        job = Job(title=title, info_link=info_link,
                  skill=skill, source=u"v2ex",
                  content=content, content_rendered=content_rendered,
                  tag =tag)
        connection.add(job)
        connection.commit()
        return True


    @classmethod
    def get_job_info_index(cls,connection,limit_num=None,source=None):
        u"""取出数据"""
        if source:
            return connection.query(Job).filter(Job.source == source).\
                order_by(Job.id.desc()).limit(limit_num)
        if limit_num:
            return connection.query(Job).order_by(Job.id.desc()).limit(limit_num)
        return connection.query(Job).order_by(Job.id.desc())

    @classmethod
    def get_job_info(cls,connection,job_id):
        u"""具体工作的具体信息"""
        return connection.query(Job).filter(Job.id == job_id)


    @classmethod
    def get_all_job(cls, connection):
        u"""所有的工作"""
        return connection.query(Job).order_by(Job.id.desc())

    @classmethod
    def get_all_tag(cls, connection):
        u"""所有标签"""
        stmt = connection.query(Job.tag).all()
        return stmt

    @classmethod
    def search_job(cls, connection, search):
        u"""工作内容查找"""
        return connection.query(Job).\
            filter(Job.content_rendered.like("%"+search+"%")).\
            order_by(Job.id.desc())

    @classmethod
    def search_job_create_time(cls,connection,start_time,end_time):
        u"""根据时间查找"""
        return connection.query(Job).\
            filter(Job.create_time > start_time).\
            filter(Job.create_time < end_time).order_by(Job.id.desc())