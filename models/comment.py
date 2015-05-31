# -*-coding:utf-8-*-
__author__ = 'Administrator'

import time

from sqlalchemy import Column, String, Integer, Unicode, Float, func,Text
from sqlalchemy.dialects.postgresql import JSONB

from models.base import Base
from models.user import User


class Comment(Base):
    u"""用户留言"""

    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, doc=u"留言的用户id")
    user_comment = Column(Text, doc=u"留言的内容")
    status = Column(Integer, doc=u"留言可见度,可见为1，不可见为2")
    create_time = Column(Float, default=lambda: time.time(), doc=u"创建时间")

    @classmethod
    def add_comment(cls, connection, user_id, user_comment):
        u"""用户的留言创建"""
        comment = Comment(user_id=user_id, user_comment=user_comment,status=1)
        connection.add(comment)
        connection.commit()

    @classmethod
    def get_all_comment(cls, connection, status=None):
        u"""获取所有的留言"""
        if status is None:
            return connection.query(Comment).order_by(Comment.id.desc())
        return connection.query(Comment,User).join(User,User.id==Comment.user_id).filter(Comment.status == status).order_by(Comment.id.desc())

    @classmethod
    def set_comment_status(cls, connection, comment_id, status):
        u"""设置留言的可见度"""
        connection.query(Comment).filter(Comment.id == comment_id).update(
            {
                Comment.status: status
            }
        )
        connection.commit()




