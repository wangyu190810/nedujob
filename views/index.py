# -*-coding:utf-8-*-
__author__ = 'Administrator'

import json


import paginate_sqlalchemy
from flask import redirect,render_template,g,jsonify,request,session

from libs.lib import set_password_salt,email_and_phone,get_page_nums
from config import Config
from models.user import User


from data.model.models import Job



def index_job_info(page):
    if request.method == "GET":
        if page is None:
            page = 1
        jobs = Job.get_job_info_index(g.db)
        return render_template("index.html",
                               jobs=paginate_sqlalchemy.SqlalchemyOrmPage(jobs,page=page,items_per_page=20),
                               tags=Job.get_all_tag(g.db),
                               page_nums=get_page_nums(jobs))


def index_info():
    if request.method == "GET":
        jobs = Job.get_job_info_index(g.db)
        return render_template("index.html", jobs=paginate_sqlalchemy.SqlalchemyOrmPage(jobs,page=1,items_per_page=20),
                               tags=Job.get_all_tag(g.db),
                               page_nums =get_page_nums(jobs))

