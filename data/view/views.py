
# -*-coding:utf-8-*-
__author__ = 'Administrator'

from data.base.base import Base
from data.model.base import DBSession
from data.model.models import Job
from data.model.nosql_data import JobData

import json
from bs4 import BeautifulSoup

class V2ex(Base):

    def get_content(self,site_file=None,name=None,tag=None):
        datas = json.loads(site_file)
        for data in datas:

            title = data.get("title")
            mark = 0
            job_key = JobData.get_nedu_job_main_data(DBSession,job_key="job_key")
            for row in job_key.data:
                print row
                if row in title:

                    mark = 1
                    break

            if mark == 1:
                title = data.get("title")
                url = data.get("url")
                skill = data.get("node")
                content = data.get("content")
                content_rendered = data.get("content_rendered")
                print content
                print content_rendered
                Job.add_data_from_v2ex(DBSession, title=title,
                                       info_link=url, skill=skill.get("name"),
                                       content=content,content_rendered=content_rendered)









