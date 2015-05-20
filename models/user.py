# -*-coding:utf-8-*-
__author__ = 'Administrator'

import time

from sqlalchemy import Column, String, Integer, Unicode, Float, func
from sqlalchemy.dialects.postgresql import JSONB

from models.base import Base


class User(Base):

    u"""用户信息表"""

    __tablename__ = "job_user"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(80), doc=u"用户名")
    password = Column(String(80), doc=u"密码")
    email = Column(String(80), unique=True, doc=u"邮箱")
    status = Column(Integer,doc=u"用户状态，0表示刚刚注册，没有验证邮箱，1表示验证通过，可以登陆的用户，2表示被列入黑名单的用户",)
    phone = Column(Unicode(13), unique=True, doc=u"电话", index=True)
    checknum = Column(Integer, doc=u"验证码")
    checknum_time = Column(Integer, doc=u"验证码时间")
    pic = Column(Unicode(255), doc=u"头像")
    tag = Column(JSONB,doc=u"用户关注的技能")


    @classmethod
    def login_user(cls, connection, email=None, phone=None, password=None,):
        u"""用户登陆"""
        if phone is None:
            return connection.query(User). \
                filter(User.email == email). \
                filter(User.password == password).scalar()
        elif email is None:
            return connection.query(User).\
                filter(User.phone == phone).\
                filter(User.password == password).scalar()

    @classmethod
    def register(cls,connection,email,phone,password,pic):
        u"""用户注册"""
        user = User(email=email,phone=phone,password=password,pic=pic,status=1)
        connection.add(user)
        connection.commit()
        return True


    @classmethod
    def user_follow_tag(cls,connection,user_id,tag):
        stmt = connection.query(User).filter(User.id == user_id).scalar()
        if stmt:
            skill = stmt.tag
            if skill is None:
                skill = tag
            else:
                skill.append(tag)
            connection.query(User).filter(User.id == user_id).update(
                {
                    User.tag: skill
                }
            )
            connection.commit()
            return True
        return False
