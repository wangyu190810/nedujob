
# -*-coding:utf-8-*-
__author__ = 'Administrator'

from data.model.base import connection
from data.base.base import Base
from data.model.base import DBSession
from data.model.models import Job
import json
from bs4 import BeautifulSoup

class V2ex(Base):

    def get_content(self,site_file=None,name=None,tag=None):
        datas = json.loads(site_file)
        for data in datas:

            title = data.get("title")
            if "[" in title or u"招聘" in title:
                print title
                url = data.get("url")
                skill = data.get("node")
                company = data.get("company")
                Job.add_data_from_v2ex(DBSession, company=company,
                                       info_link=url, skill=skill.get("name"))









