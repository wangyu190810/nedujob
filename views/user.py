# -*-coding:utf-8-*-
__author__ = 'Administrator'

import json

from flask import redirect, render_template, g, request, session

from libs.lib import set_password_salt, email_and_phone
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
            session["user_id"] = str(user.id)
            user_info = {"user": user.phone,
                         "status": True}
            return json.dumps(user_info)
    return render_template("login.html")


def user_register():
    u"""用户注册"""
    if request.method == "POST":
        data = request.form
        email, phone = email_and_phone(data.get("user"))
        password = set_password_salt(data.get("password"))
        if User.register(g.db, email, phone, password, Config.pic):
            return redirect("/login")
    return render_template("register.html")


def user_logout():
    u"""用户注销"""
    session.pop("user_id")
    return redirect("/")