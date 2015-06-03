# -*-coding:utf-8-*-
__author__ = 'Administrator'
import hashlib
from functools import wraps
from itsdangerous import Signer
import json

from flask import session, redirect
from flask_mail import Message

import smtplib
from email.mime.text import MIMEText

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


def validate_admin_login(func):
    @wraps(func)
    def _validate_admin_login(*args, **kwargs):
        if "username" in session:
            return func(*args, **kwargs)
        return redirect("/admin_login")
    return _validate_admin_login


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

def set_email_base(message,subject,email):
    u"""邮件基础定义"""
    meg = MIMEText(message.encode("utf-8"))
    meg['From'] = Config.email.get("MAIL_DEFAULT_SENDER")
    meg["SUbject"] = subject
    meg["To"] = email

    try:
        s = smtplib.SMTP_SSL(Config.email.get("MAIL_SERVER"),Config.email.get("MAIL_PORT"))
        print(s)
        s.login(Config.email.get("MAIL_USERNAME"),Config.email.get("MAIL_PASSWORD"))
        print("login_email")
        s.sendmail(Config.email.get("MAIL_DEFAULT_SENDER"),email,meg.as_string())
        print("send_email")

    except IndexError:
        pass
    finally:
        s.close()

    return True


def user_email_check(email_address):
    u"""用户邮箱检测"""
    if set_email_base(get_email_link(email_address), u"用户合法性验证", email_address):
        return True
    return False


def get_page_nums(contents):
    page_list = list()
    for content in contents:
        page_list.append(content)
    page_nums = 1
    if len(page_list) / 20:
        page_nums = len(page_list)/20
    return page_nums
