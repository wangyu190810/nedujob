# -*-coding: utf-8-*-

__author__ = 'wangyu'

from datetime import timedelta

from flask import Flask, g, current_app
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from flask_mail import Mail

from config import Config

from views.user import user_login,user_register,check_user_email
from views.index import index_job_info,index_job_info_site
from views.admin import admin_index,admin_add_data_key
from views.job import job_info,add_job_tag
from views.comment import get_comment,post_comment


app = Flask(__name__)
app.secret_key = Config.SUCCESS_KEY
app.permanent_session_lifetime = timedelta(minutes=60)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.db

app.sa_engine = create_engine(Config.db)
app.DBSession = scoped_session(sessionmaker(bind=app.sa_engine))

mail = Mail(app)
mail.init_mail(Config.email)

# ---index---

app.add_url_rule("/index" ,methods=["GET"],
                 view_func=index_job_info)
app.add_url_rule("/", methods=["GET"],
                 view_func=index_job_info)
app.add_url_rule("/info/<site>",methods=["GET"],
                 view_func=index_job_info_site)

# ----user----

app.add_url_rule("/register", methods=["GET", "POST"],
                 view_func=user_register)
app.add_url_rule("/login", methods=["GET", "POST"],
                 view_func=user_login)
app.add_url_rule("/check_email", methods=["GET"],
                 view_func=check_user_email)
app.add_url_rule("/user/comment", methods=["GET"],
                 view_func=get_comment)
app.add_url_rule("/user/postcomment",methods=["POST"],
                 view_func=post_comment)

# ---job---

app.add_url_rule("/job/<int:job_id>",methods=["GET"],
                 view_func=job_info)
app.add_url_rule("/add_job_tag",methods=["POST"],
                 view_func=add_job_tag)

# ---admin---

app.add_url_rule("/admin", methods=["GET"],
                 view_func=admin_index)
app.add_url_rule("/admin_add_data_key",methods=["POST","GET"],
                 view_func=admin_add_data_key)


@app.before_request
def _before_request():
    g.db = current_app.DBSession()


@app.teardown_request
def teardown_request(*args, **kwargs):
    current_app.DBSession.remove()
    g.db.close()