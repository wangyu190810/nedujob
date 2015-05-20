# -*-coding:utf-8-*-
__author__ = 'Administrator'

from data.model.models import Job
from models.user import User

import json

from flask import redirect,render_template,request,g,session


def job_info(job_id):
    if request.method == "GET":
        return render_template("job_info.html", jobs=Job.get_job_info(g.db, job_id))


def job_info_site(site):
    if request.method == "GET":
        return render_template("index.html", jobs=Job.get_job_info(g.db, 100,site))


def add_job_tag():
    if request.method == "POST":
        user_id = session.get("user_id")
        tag = request.form.get("tag")
        User.user_follow_tag(g.db, user_id, tag=tag)
        result = {"status": "success", "tag": tag}
        return json.dumps(result)
    result = {"status": "success"}
    return json.dumps(result)
