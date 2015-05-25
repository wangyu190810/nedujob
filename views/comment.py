# -*-coding:utf-8-*-
__author__ = 'Administrator'


from flask import g,render_template,redirect,request,session

from models.comment import Comment
from libs.lib import validate_user_login


def get_comment():
    if request.method == "GET":
        page = request.form.get("page")

        return render_template("comment.html",comments=Comment.get_all_comment(g.db,status=1))

@validate_user_login
def post_comment():
    if request.method == "POST":
        user_id = session.get("user_id")
        comment = request.form.get("comment")
        Comment.add_comment(g.db,user_id=user_id,user_comment=comment)
        return redirect("/user/comment")
    return redirect("/")