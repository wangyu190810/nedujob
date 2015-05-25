# -*-coding:utf-8-*-
__author__ = 'Administrator'

import json

from flask import redirect,render_template,g,jsonify,request,session

from libs.lib import set_password_salt,email_and_phone
from config import Config
from models.user import User

from data.model.models import Job



def index_job_info():
    if request.method == "GET":
        return render_template("index.html", jobs=Job.get_job_info_index(g.db, 100),
                               tags=Job.get_all_tag(g.db))


def index_job_info_site(site):
    if request.method == "GET":
        return render_template("index.html", jobs=Job.get_job_info_index(g.db, 100, site))
