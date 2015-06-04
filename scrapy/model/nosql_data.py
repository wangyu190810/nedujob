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
from sqlalchemy.dialects.postgresql import JSONB
from base import Base,engine


class JobData(Base):
    u"""网站NoSql数据"""
    __tablename__= "job_data"
    job_key = Column(Unicode(255),primary_key=True)
    data = Column(JSONB)


    @classmethod
    def add_nedu_job_main_key(cls,connection,job_key,data):
        stmt = connection.query(JobData).filter(JobData.job_key == job_key).scalar()
        if stmt:
            abc = stmt.data
            print abc
            abc.append(data)
            connection.query(JobData).filter(JobData.job_key == job_key).update(
                {
                    JobData.data: abc
                }
            )
        else:
            jobdata = JobData(job_key=job_key,data=data)
            connection.add(jobdata)
        connection.commit()
        return True

    @classmethod
    def get_nedu_job_main_data(cls,connection,job_key):
        return connection.query(JobData).filter(JobData.job_key == job_key).scalar()

    @classmethod
    def get_nedu_job_key(cls,connection):
        return connection.query(JobData)

    @classmethod
    def add_tag_content(cls,connection,job_kye=None,content=None,tag=None):
        u"""将标签放到数据数据库中"""
        print job_kye,content
        if (job_kye or content) is None:
            return 0
        if tag == 1:
            connection.commit()
        stmt = connection.query(JobData).filter(JobData.job_key == job_kye).scalar()
        if stmt:
            keys = stmt.data
            print(type(keys))
            if type(keys) is int:
                keys = list()
                keys.append(stmt.data)
            keys.append(content)
            print(keys)
            ccc = set(keys)
            keys = list(ccc)
            print(keys)
            connection.query(JobData).filter(JobData.job_key == job_kye).update(
                {
                    JobData.data: keys
                }
            )
        else:
            stmt = JobData(job_key=job_kye,data=content)
            connection.add(stmt)




def create_table():
    Base.metadata.create_all(engine)