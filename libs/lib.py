# -*-coding:utf-8-*-
__author__ = 'Administrator'
import hashlib
from functools import wraps
from itsdangerous import Signer
import json

from flask import session, redirect
from flask_mail import Message


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


def set_email_safe(email_address):
    s = Signer(Config.email_check)
    return s.sign(email_address)


def get_email_safe(email_address):
    s = Signer(Config.email_check)
    return s.unsign(email_address)


def get_email_link(email_address):
    content = u"""<p>亲爱的用户你好</p> 您已经注册了nudejob网站，为了验证码您邮箱的有效性，请点击链接"""
    content = content + Config.address + set_email_safe(email_address)
    return content


def user_email_check(email_address, mail):
    u"""用户邮箱验证"""
    with mail.connect() as conn:
        email = Message(
            u"用户邮箱真实性验证",
            sender=Config.email.get("MAIL_DEFAULT_SENDER"),
            recipients=["190810401@qq.com"],


        )
        email.html = get_email_link(email_address)
    conn.send(email)
    return True


def get_page(contents):
    page_list = list()
    for content in contents:
        page_list.append(content)
    if len(page_list) / 20:
        status = {"page":[pages for pages in range(len(page_list)/20)]}
        return json.dumps(status)
    return None
