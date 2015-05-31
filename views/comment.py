# -*-coding:utf-8-*-
__author__ = 'Administrator'


from flask import g,render_template,redirect,request,session
from paginate_sqlalchemy import SqlalchemyOrmPage

from models.comment import Comment
from libs.lib import validate_user_login,get_page_nums


def get_comment(page=None):
    if request.method == "GET":
        comments = Comment.get_all_comment(g.db,status=1)
        page_nums = get_page_nums(comments)
        return render_template("comment.html",
                               comments= SqlalchemyOrmPage(comments,page=page,items_per_page=20),
                               page_nums = page_nums)

@validate_user_login
def post_comment():
    if request.method == "POST":
        user_id = session.get("user_id")
        comment = request.form.get("comment")
        Comment.add_comment(g.db,user_id=user_id,user_comment=comment)
        return redirect("/comment")
    return redirect("/")