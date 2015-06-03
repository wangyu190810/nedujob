# -*-coding:utf-8-*-
__author__ = 'Administrator'
from flask import g,session,render_template,request,redirect

from data.model.models import Job
from data.model.nosql_data import JobData
from models.user import User
from models.comment import Comment
from libs.lib import validate_user_login,validate_admin_login,set_password_salt



@validate_admin_login
def admin_index():
    return render_template("admin/admin.html", blogs=Job.get_all_job(g.db))


@validate_admin_login
def admin_add_data_key():
    if request.method == "GET":
        return render_template("admin/add_key.html", datas=JobData.get_nedu_job_key(g.db))
    elif request.method == "POST":
        data = request.form
        job_key = data.get("job_key")
        job_data = data.get("job_data")
        JobData.add_nedu_job_main_key(g.db,job_key=job_key,data=job_data)
        return redirect("/admin")

def admin_login():
    if request.method == "GET":
        return render_template("admin/admin_login.html")
    elif request.method == "POST":
        data = request.form
        username = data.get("username")
        password = set_password_salt(data.get("password"))
        print(username)
        print(password)
        user = User.get_admin_login(g.db,username,password)
        if user:
            session["username"] = user.username
            return redirect("/admin")
        return redirect("/admin_login")


@validate_admin_login
def add_work_message():
    if request.method == "GET":
        return render_template("admin/add_work_message.html")
    if request.method == "POST":
        data = request.form
        title = data.get("title")
        content = data.get("content")
        info_link = data.get("info_link")
        Job.add_work_message(g.db,title,content,info_link)
        return redirect("/admin")

