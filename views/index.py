# -*-coding:utf-8-*-
__author__ = 'Administrator'

import json

from flask import redirect,render_template,g,jsonify,request,session

from libs.lib import set_password_salt,email_and_phone
from config import Config
from models.user import User


def index():
    return render_template("index.html")