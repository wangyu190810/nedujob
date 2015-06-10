# -*-coding:utf-8-*-
__author__ = 'Administrator'

from model.base import DBSession

from model.nosql_data import JobData
from model.models import Job
from model.user import User
from config import Config
from lib import send_new_jobs_to_user,set_email_body,set_email_content

users_job_ids = JobData.get_user_job_ids(DBSession)
for user_id,job_ids in users_job_ids:
    content = ""
    print(job_ids.data)
    for job_id in job_ids.data:
        print(job_id)
        job = Job.get_job_info_by_id(DBSession,job_id=job_id)
        content =content + set_email_content(Config.send_job_address,job.id,job.content_rendered)
    email_body = set_email_body(content)
    send_new_jobs_to_user(email_body,User.get_user(DBSession,user_id).email)


