#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: base.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-11-04
#Description: 

import urllib2
import requests
import urllib
import re
from bs4 import BeautifulSoup

""""基础类的建设，主要是一些抓取模块的基础类"""


# 拿到网站的链接，返回html文件，等待对应的模块解析各自的文件
class Base(object):

    def __init__(self,site=None):

        if site is None:
            raise
        else:
            self.site = site

    @classmethod
    def get_site(cls):
        return

    # 解析请求数据，最后返回字符串
    def request_site(self):
        site_html = requests.get(
                    url=self.site
                )
        if site_html.status_code != 200:
            print site_html.status_code
            raise
        else:
            html = site_html.text
            return html 
    
    # 返回符合查找的信息列表
    @classmethod
    def get_content(cls,site_file=None,name=None,tag=None):
        if (site_file or tag) is None:
            raise
        else:
            soup = BeautifulSoup(site_file)
            if tag is None:
                return soup
            if tag == "class":
                content = soup.find_all(class_ = re.compile(name))
            elif tag == "html":
                content = soup.find_all(name)
            elif tag == "title":
                content = soup.title.string
            elif tag == "text":
                content = soup.body
            return content
    
    # 图片下载
    def down_img(self,img_url):
        name = img_url[40:]
        urllib.urlretrieve(img_url,name)
        


