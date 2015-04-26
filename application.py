# -*-coding: utf-8-*-

__author__ = 'wangyu'

from datetime import timedelta

from flask import Flask, g, current_app
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from config import Config

from views.user import user_login,user_register
from views.index import index

app = Flask(__name__)
app.secret_key = Config.SUCCESS_KEY
app.permanent_session_lifetime = timedelta(minutes=60)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.db

app.sa_engine = create_engine(Config.db)
app.DBSession = scoped_session(sessionmaker(bind=app.sa_engine))

app.add_url_rule("/index" ,methods=["GET"],
                 view_func=index)
app.add_url_rule("/", methods=["GET"],
                 view_func=index)

app.add_url_rule("/register", methods=["GET", "POST"],
                 view_func=user_register)
app.add_url_rule("/login", methods=["GET", "POST"],
                 view_func=user_login)




@app.before_request
def _before_request():
    g.db = current_app.DBSession()


@app.teardown_request
def teardown_request(*args, **kwargs):
    current_app.DBSession.remove()
    g.db.close()