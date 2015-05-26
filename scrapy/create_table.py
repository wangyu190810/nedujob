# -*-coding:utf-8-*-
__author__ = 'Administrator'



from model.base import Base,engine

Base.metadata.create_all(engine)
