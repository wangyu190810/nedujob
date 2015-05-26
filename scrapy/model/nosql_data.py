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


def create_table():
    Base.metadata.create_all(engine)