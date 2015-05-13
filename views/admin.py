# -*-coding:utf-8-*-
__author__ = 'Administrator'
from flask import g,session,render_template,request,redirect

from data.model.models import Job
from data.model.nosql_data import JobData
from libs.lib import validate_user_login


@validate_user_login
def admin_index():
    return render_template("admin.html", blogs=Job.get_all_job(g.db))


@validate_user_login
def admin_add_data_key():
    if request.method == "GET":
        return render_template("add_key.html", datas=JobData.get_nedu_job_key(g.db))
    elif request.method == "POST":
        data = request.form
        job_key = data.get("job_key")
        job_data = data.get("job_data")
        JobData.add_nedu_job_main_key(g.db,job_key=job_key,data=job_data)
        return redirect("/admin")
