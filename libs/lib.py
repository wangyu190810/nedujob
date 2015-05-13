# -*-coding:utf-8-*-
__author__ = 'Administrator'
import hashlib
from functools import wraps

from flask import session, redirect

from config import Config


def set_password_salt(password):
    u"""密码加密"""
    m = hashlib.sha224(password+Config.salt).hexdigest()
    return m


def email_and_phone(user_info):
    u"""用户email还是电话"""
    if "@" in user_info:
        email = user_info
        phone = None
    else:
        email = None
        phone = user_info
    return email, phone


def get_user_pic():
    return Config.pic


def validate_user_login(func):
    @wraps(func)
    def _validate_user_login(*args, **kwargs):
        if "user_id" in session:
            return func(*args, **kwargs)
        return redirect("/login")
    return _validate_user_login

from datetime import time, tzinfo,timedelta

