# -*-coding:utf-8-*-
__author__ = 'Administrator'

import time

from sqlalchemy import Column, String, Integer, Unicode, Float, func
from sqlalchemy.dialects.postgresql import JSONB

from base import Base


class User(Base):

    u"""用户信息表"""

    __tablename__ = "job_user"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(80), doc=u"用户名")
    password = Column(String(80), doc=u"密码")
    email = Column(String(80), unique=True, doc=u"邮箱")
    status = Column(Integer, doc=u"用户状态，0表示刚刚注册，没有验证邮箱，1表示验证通过，可以登陆的用户，2表示被列入黑名单的用户,8表示root用户",)
    phone = Column(Unicode(13), unique=True, doc=u"电话", index=True)
    checknum = Column(Integer, doc=u"验证码")
    checknum_time = Column(Integer, doc=u"验证码时间")
    pic = Column(Unicode(255), doc=u"头像")
    tag = Column(JSONB,doc=u"用户关注的技能")
    create_time = Column(Integer,doc=u"用户注册时间", default=lambda: time.time())


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
    def register(cls,connection,email,password,pic,username):
        u"""用户注册"""
        user = User(email=email,password=password,pic=pic,status=0,username=username)
        connection.add(user)
        connection.commit()
        return True


    @classmethod
    def user_follow_tag(cls,connection,user_id,tag):
        stmt = connection.query(User).filter(User.id == user_id).scalar()
        if stmt:
            skill = stmt.tag
            if skill is None:
                skill = list()
                skill.append(tag)
            elif type(skill) is not list:
                skill = list()
                skill.append(tag)
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


    @classmethod
    def get_user(cls,connection,user_id):
        return connection.query(User).filter(User.id == user_id).scalar()

    @classmethod
    def get_admin_login(cls,connection,username,password):

        stmt = connection.query(User).\
            filter(User.email == username).\
            filter(User.password == password).\
            filter(User.status == 100).scalar()
        if stmt is None:
            return None
        return stmt

    @classmethod
    def user_status_change(cls,connection,email):
        connection.query(User).filter(User.email == email).update({
            User.status:1
        })
        connection.commit()




