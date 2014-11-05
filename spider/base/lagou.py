#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: lagou.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-04
#Description: 

"""暂时定为为抓取拉钩的工作信息，方向为python"""

from  base import Base

class Lagou(Base):
    site = "http://www.lagou.com/jobs/list_python?kd=python&spc=&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city="
    base_site = Base(site)
    html =  base_site.request_site()
    
    def get_html(self):
        print self.html


if __name__ == "__mian__":
    lagou_site = Lagou()
    print lagou_site.html
    lagou_site.get_html()
    #print lagou_site.html
    #print site
