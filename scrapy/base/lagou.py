#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: models.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-04
#Description: 

"""暂时定为为抓取拉钩的工作信息，方向为python"""

from base import Base

class Lagou(Base):
    def __init__(self):
        return 
    site = "http://www.lagou.com/jobs/list_python?kd=python&spc=&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city="
    base_site = Base(site)
    html = base_site.request_site()
    content = base_site.get_content(html,"clearfix",1)    
     
    def get_message(self):
        for message in self.content:
            company_url = self.base_site.get_content(str(message),"a",0)
            print company_url

