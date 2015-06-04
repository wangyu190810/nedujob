
# -*-coding:utf-8-*-
__author__ = 'Administrator'

from base.base import Base
from model.base import DBSession
from model.models import Job
from model.nosql_data import JobData

import json
from bs4 import BeautifulSoup

class V2ex(Base):

    def get_content(self,site_file=None,name=None,tag=None):
        datas = json.loads(site_file)
        for data in datas:
            title = data.get("title")
            mark = 0
            tag = list()
            job_key = JobData.get_nedu_job_main_data(DBSession,job_key="job_key")
            for row in job_key.data:
                #print row
                if row in title:
                    mark = 1
                    tag.append(row)
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
                                       content=content,content_rendered=content_rendered,
                                       tag=tag)


class LaGou(Base):

    def get_content(self,site_file=None,site=None):
        title = Base.get_content(site_file, tag="title")
        company = Base.get_content(site_file, name="job_company", tag="class")
        content = Base.get_content(site_file, name="job_bt", tag="class")
        skill = Base.get_content(site_file, name="job_request", tag="class")
        salary = Base.get_content(site_file,name="red",tag="class").string

        company_link = company.find_all(r"a")[1].string

        company_req = skill.find_all("span")
        publish_time = skill.find("div")
        publish_time = str(publish_time)[5:len(str(publish_time))-6]

        address = str(company_req[1])[6:len(str(company_req[1]))-7]

        skill_time = str(company_req[2])[6:len(str(company_req[2]))-7]
        skill_education = str(company_req[3])[6:len(str(company_req[3]))-7]
        skill_tag = list()
        job_key = JobData.get_nedu_job_main_data(DBSession,job_key="job_key")


        for row in job_key.data:
            if row in title or row in content.text:
                skill_tag.append(row)
        company_info = company.text

        job_info = Job.add_data_from_lagou(DBSession,
                                company=title,
                                company_link=company_link,
                                company_info=company_info,
                                title=title,
                                skill=skill_time+skill_education,
                                salary=salary,
                                info_link=site,
                                address=address,
                                content=content.text,
                                content_rendered=str(content),
                                publish_time=publish_time,
                                tag=skill_tag)
        print("asdfasdf")
        print(skill_tag)
        for row in skill_tag:

            JobData.add_tag_content(DBSession,job_kye=row,content=job_info.id)
        JobData.add_tag_content(DBSession,tag=1)










