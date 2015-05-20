# -*-coding:utf-8-*-
__author__ = 'Administrator'


from data.view.views import V2ex,LaGou


if __name__ == "__main__":
    #v2ex = V2ex("https://www.v2ex.com/api/topics/latest.json")
   # print v2ex.get_content(v2ex.request_site(),)
    #v2ex.get_content(v2ex.request_site())
    lagou = LaGou("http://www.lagou.com/jobs/603100.html")
    site_file = lagou.request_site()
    lagou.get_content(site_file,lagou.site)
    # print lagou.get_content(site_file, tag="title")
    # print lagou.get_content(site_file, name="job_request", tag="class")
    # print lagou.get_content(site_file, name="job_bt", tag="class")
    # print lagou.get_content(site_file, name="c_feature reset", tag="class")
    # print lagou.get_content(site_file, name="job_company", tag="class")
    # print(lagou.get_content(site_file, tag="text"))


