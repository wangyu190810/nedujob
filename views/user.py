# -*-coding:utf-8-*-
__author__ = 'Administrator'

import json

from flask import redirect, render_template, g, request, session

from libs.lib import set_password_salt, email_and_phone,user_email_check
from config import Config
from models.user import User


def user_login():
    u"""用户登陆"""
    if request.method == "POST":
        data = request.form
        email, phone = email_and_phone(data.get("user"))
        password = set_password_salt(data.get("password"))
        user = User.login_user(g.db, email, phone, password)
        if user:
            if user.status == 1:
                session["user_id"] = str(user.id)
                return render_template("admin.html")
            elif user.status == 0:
                return render_template("index.html")
            else:
                return render_template("index.html")
    return render_template("login.html")


def user_register():
    u"""用户注册"""
    if request.method == "POST":
        data = request.form
        email, phone = email_and_phone(data.get("user"))
        password = set_password_salt(data.get("password"))
        if User.register(g.db, email, phone, password, Config.pic):
            from application import mail
            if user_email_check(email,mail):
                return redirect("/login")
    return render_template("register.html")


def user_logout():
    u"""用户注销"""
    session.pop("user_id")
    return redirect("/")


def check_user_email():
    return json.dumps({"status": True})

