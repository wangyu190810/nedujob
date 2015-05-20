#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: config.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-04
#Description: 

class Config(object):
    db = "postgresql://postgres:2015@localhost/nedujob"
    SUCCESS_KEY = u"adsfsdf"
    salt = u"asdfa"
    pic = ""
    email_check = "email"
    address = "http://127.0.0.1:8888/check_email"
    def lziy(self):
        pass

    email = {


        # mail settings
        "MAIL_SERVER": 'smtp.163.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,

        # 163 authentication
        "MAIL_USERNAME": "wo190810401@163.com",
        "MAIL_PASSWORD": "wangyu190810",

        # mail accounts
        "MAIL_DEFAULT_SENDER": 'wo190810401@163.com'
    }
