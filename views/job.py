# -*-coding:utf-8-*-
__author__ = 'Administrator'

from data.model.models import Job
from data.model.nosql_data import JobData
from libs.lib import get_page_nums,validate_user_login
from models.user import User
import time
import json

import paginate_sqlalchemy


from flask import redirect,render_template,request,g,session,flash


def job_info(job_id):
    if request.method == "GET":
        return render_template("job_info.html",
                               jobs=Job.get_job_info(g.db, job_id))


def job_info_site(site):
    if request.method == "GET":
        return render_template("index.html", jobs=Job.get_job_info(g.db, 100,site))

#@validate_user_login
def add_job_tag():
    u"""用户关注tag"""
    if request.method == "POST":
        user_id = session.get("user_id")
        tag = request.form.get("tag")
        print(tag)
        User.user_follow_tag(g.db, user_id, tag=tag)
        JobData.add_have_tag_user_id(g.db, user_id, tag=tag)
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
            page = request.args.get("page")
            return render_template("filter.html",
                                   jobs = paginate_sqlalchemy.SqlalchemyOrmPage(jobs,page=page,items_per_page=20),
                                   date=date,
                                   page_nums=get_page_nums(jobs))
        return render_template("filter.html",
                               tags=JobData.get_nedu_job_main_data(g.db,"job_key").data,
                               address=Job.get_all_address(g.db))


def search_tag(tag):
    if request.method == "GET":
        jobs = Job.get_job_from_tag(g.db,tag)
        if jobs:
            return render_template("filter.html",
                                jobs = paginate_sqlalchemy.SqlalchemyOrmPage(jobs,page=1,items_per_page=20),
                                page_nums=get_page_nums(jobs))
        flash(u"没有找到，请重新选择")
        return redirect("/filter")


def get_work_message():
    if request.method == "GET":
        return render_template("work_message.html",jobs = Job.get_work_message(g.db))


def search_addr(addr):
    if request.method == "GET":
        jobs = Job.get_job_from_address(connection=g.db,address=addr)
        return render_template("filter.html",
                               jobs =paginate_sqlalchemy.SqlalchemyOrmPage(jobs,page=1,items_per_page=20), )

def get_count():
    return render_template("count.html",
                           address=Job.get_count_addr_num(g.db),
                           tags=JobData.get_tag_num(g.db))





