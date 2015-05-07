# -*-coding:utf-8-*-
__author__ = 'Administrator'

from data.model.models import Job


from flask import redirect,render_template,request,g


def job_info(job_id):
    if request.method == "GET":
        return render_template("job_info.html", jobs=Job.get_job_info(g.db, job_id))


def job_info_site(site):
    if request.method == "GET":
        return render_template("index.html", jobs=Job.get_job_info(g.db, 100,site))
