# -*-coding:utf-8-*-
__author__ = 'Administrator'

from data.model.models import Job

from data.model.base import Base,engine

Base.metadata.create_all(engine)

