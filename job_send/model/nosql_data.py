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
    def get_nedu_job_key(cls,connection,job_key):
        return connection.query(JobData).filter(JobData.job_key==job_key)

    @classmethod
    def get_nedu_job_from_tag(cls,connection,tag):
        return connection.query(JobData).filter(JobData.job_key == tag).scalar()

    @classmethod
    def add_user_job_info_tag(cls,connection,user_id,tag):
        u"""用户关注标签的工作数据存储"""
        stmt = connection.query(JobData).filter(JobData.job_key==user_id).scalar()
        if stmt:
            tags = stmt.data
            tags.append(tag)
            connection.query(JobData).filter(JobData.job_key==user_id).update(
                {
                    JobData.job_key:tags
                }
            )
        else:
            tags = list()
            tags.append(tag)
            user_tag = JobData(job_key=user_id,data=tags)
            connection.add(user_tag)
        connection.commit()

    @classmethod
    def get_tag_num(cls,connection):
        stmt = connection.query(JobData).filter(JobData.job_key == "job_key").scalar()
        if stmt:
            tags = list()
            for row in stmt.data:
                tag = list()
                tag_data = connection.query(JobData).filter(JobData.job_key == row).scalar()
                tag.append(row)

                if type(tag_data.data) is list:
                    tag.append(len(tag_data.data))
                else:
                    tag.append(0)
                tags.append(tag)
            tags = sorted(tags,key=lambda tags:tags[1],reverse=True)
            return tags
        return None

    @classmethod
    def add_have_tag_user_id(cls,connection,user_id,tag):
        stmt = connection.query(JobData).filter(JobData.job_key=="user_id").scalar()
        if stmt:
            user_id_list = stmt.data
            user_id_list.append(user_id)
            user_id_list = list(set(user_id_list))
            print(user_id_list)
            connection.query(JobData).filter(JobData.job_key=="user_id").update(
                {
                    JobData.data:user_id_list
                }
            )
        else:
            user_id_list = list()
            user_id_list.append(user_id)
            user_id_init = JobData(job_key="user_id",data=user_id_list)
            connection.add(user_id_init)
        connection.commit()
        stmt = connection.query(JobData).filter(JobData.job_key==user_id).scalar()
        jobs = connection.query(JobData).filter(JobData.job_key==tag).scalar()
        if stmt:
            user_job_ids = stmt.data
            if type(jobs.data) is list:
                user_job_ids = list(set(user_job_ids+jobs.data))
            connection.query(JobData).filter(JobData.job_key==user_id).update(
                {
                    JobData.data:user_job_ids
                }
            )
        else:
            user_job_ids = list()
            user_id_list.append(user_id)
            init_user_id = JobData(job_key=user_id,data=user_job_ids)
            connection.add(init_user_id)
        connection.commit()

    @classmethod
    def get_user_job_ids(cls,connection):
        u"""获取所有有关注行为用户的id和所关注信息的id"""
        stmt = connection.query(JobData).filter(JobData.job_key=="user_id").scalar()
        if stmt:
            user_jobs = list()
            user_ids = stmt.data
            for user_id in user_ids:
                user_id_jobs = list()
                job_ids = connection.query(JobData).filter(JobData.job_key==user_id).scalar()
                user_id_jobs.append(user_id)
                user_id_jobs.append(job_ids)
                user_jobs.append(user_id_jobs)
            return user_jobs



# 表创建语句
# Base.metadata.create_all(engine)
