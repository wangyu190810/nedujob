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

def send_new_jobs_to_user(message,email):
    set_email_base(message, u"ccc", email)


def set_email_content(config_address,job_id,content):
    link = "<p>"+config_address+str(job_id)+"<p>"
    return link+"<p>"+content+"</p>"

def set_email_body(content):
    title = u"""<!DOCTYPE html>
        <html>
        <head lang="en">
            <meta charset="UTF-8">
            <title>订阅邮件</title>
        </head>
        """
    content = title+"<body>"+content+"</body></html>"
    return content