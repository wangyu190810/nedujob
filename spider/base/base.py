#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: base.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-04
#Description: 

import urllib2
import requests

""""基础类的建设，主要是一些抓取模块的基础类"""


#拿到网站的链接，返回html文件，等待对应的模块解析各自的文件
class Base(object):
    def __init__(self,site=None):
        if site is None:
            raise
        else:
            self.site = site
    def request_site(self):
        site_html = requests.get(
                url = self.site
                )
        print site_html.encoding 
        html =  site_html.text
        return html 



