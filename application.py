# -*-coding: utf-8-*-

__author__ = 'wangyu'

from datetime import timedelta

from flask import Flask, g, current_app,session
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from flask_mail import Mail

from config import Config

from views.user import user_login,user_register,check_user_email,get_user,\
    get_user_info,user_logout
from views.index import index_job_info,index_info
from views.admin.admin import admin_index,admin_add_data_key,admin_login,\
    add_work_message
from views.job import job_info,add_job_tag,search_job,search_more_requirement,\
    get_work_message
from views.comment import get_comment,post_comment

from models.user import User

app = Flask(__name__)
app.secret_key = Config.SUCCESS_KEY
app.permanent_session_lifetime = timedelta(minutes=60)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.db

app.sa_engine = create_engine(Config.db)
app.DBSession = scoped_session(sessionmaker(bind=app.sa_engine))

mail = Mail(app)
mail.init_mail(Config.email)

# ---index---

app.add_url_rule("/index/<int:page>" ,methods=["GET"],
                 view_func=index_job_info)
app.add_url_rule("/", methods=["GET"],
                 view_func=index_info)


# ----user----

app.add_url_rule("/register", methods=["GET", "POST"],
                 view_func=user_register)
app.add_url_rule("/login", methods=["GET", "POST"],
                 view_func=user_login)
app.add_url_rule("/logout",methods=["GET"],
                 view_func=user_logout)
app.add_url_rule("/check_email", methods=["GET"],
                 view_func=check_user_email)
app.add_url_rule("/user/<int:user_id>",methods=["GET"],
                 view_func=get_user)
app.add_url_rule("/user",methods=["GET"],
                 view_func=get_user_info)

# ---comments----

app.add_url_rule("/comment/<int:page>", methods=["GET"],
                 view_func=get_comment)
app.add_url_rule("/comment", methods=["GET"],
                 view_func=get_comment)

app.add_url_rule("/postcomment",methods=["POST"],
                 view_func=post_comment)


# ---job---

app.add_url_rule("/job/<int:job_id>",methods=["GET"],
                 view_func=job_info)
app.add_url_rule("/add_job_tag",methods=["POST"],
                 view_func=add_job_tag)
app.add_url_rule("/search",methods=["GET"],
                 view_func=search_job)
app.add_url_rule("/filter",methods=["GET"],
                 view_func=search_more_requirement)
app.add_url_rule("/work_message", methods=["GET"],
                 view_func=get_work_message)

# ---admin---

app.add_url_rule("/admin", methods=["GET"],
                 view_func=admin_index)
app.add_url_rule("/admin_add_data_key",methods=["POST","GET"],
                 view_func=admin_add_data_key)
app.add_url_rule("/admin_login",methods=["GET","POST"],
                 view_func=admin_login)
app.add_url_rule("/admin_work_message",methods=["GET","POST"],
                 view_func=add_work_message)

@app.before_request
def _before_request():
    g.db = current_app.DBSession()


@app.before_request
def load_user():
    if session.get("user_id"):
        user = g.db.query(User).filter(User.id == session["user_id"]).first()
    elif session.get("username"):
        user = g.db.query(User).filter(User.username == session["username"]).first()
    else:
        user = {"username":None}
    g.user = user


@app.teardown_request
def teardown_request(*args, **kwargs):
    current_app.DBSession.remove()
    g.db.close()