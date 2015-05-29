# -*-coding:utf-8-*-
__author__ = 'Administrator'

from data.model.models import Job
from models.user import User
import time
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


def search_job():
    if request.method == "GET":
        search = request.args.get("search")
        print request.args
        search_data = Job.search_job(g.db, search)
        return render_template("search.html", jobs=search_data)


def search_more_requirement():
    if request.method == "GET":
        date = request.args.get("daterange")
        if date:
            start_time,end_time = date.split("-")
            end_time = end_time + " 00:00:00"
            if start_time == end_time:
                end_time = end_time[1:] + " 23:59:59"
            start_time = start_time+" 00:00:00"
            start_time = time.mktime(time.strptime(str(start_time),r"%m/%d/%Y  %H:%M:%S"))
            end_time = time.mktime(time.strptime(str(end_time),r" %m/%d/%Y %H:%M:%S"))
            jobs = Job.search_job_create_time(g.db,start_time,end_time)
            return render_template("filter.html",jobs = jobs)
        return render_template("filter.html")

def get_some_message():
    if request.method == "GET":
        return