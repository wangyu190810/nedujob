# -*-coding:utf-8-*-
__author__ = 'Administrator'

import time

from views import V2ex,LaGou


if __name__ == "__main__":
    link_num = 600190
    while True:

        # if link_num % 4 == 1:
        #     v2ex = V2ex("https://www.v2ex.com/api/topics/latest.json")
        #     v2ex.get_content(v2ex.request_site())
        link = "http://www.lagou.com/jobs/"+str(link_num)+".html"
        lagou = LaGou(link)
        try:
            site_file = lagou.request_site()
            lagou.get_content(site_file,lagou.site)
        except:
            print link_num
        finally:
            time.sleep(40)
            link_num += 1
        if link_num == 682916:
            break


    # while True:
    #     link_num = 603100
    #     link = "http://www.lagou.com/jobs/"+str(link_num)+".html"
    #     lagou = LaGou(link)
    #     with lagou.request_site() as site_file:
    #         lagou.get_content(site_file,lagou.site)
    #     link_num += 1
    #     time.sleep(10)
    # print lagou.get_content(site_file, tag="title")
    # print lagou.get_content(site_file, name="job_request", tag="class")
    # print lagou.get_content(site_file, name="job_bt", tag="class")
    # print lagou.get_content(site_file, name="c_feature reset", tag="class")
    # print lagou.get_content(site_file, name="job_company", tag="class")
    # print(lagou.get_content(site_file, tag="text"))


