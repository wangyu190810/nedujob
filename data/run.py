# -*-coding:utf-8-*-
__author__ = 'Administrator'


from data.view.views import V2ex


if __name__ == "__main__":
    v2ex = V2ex("https://www.v2ex.com/api/topics/latest.json")
   # print v2ex.get_content(v2ex.request_site(),)
    v2ex.get_content(v2ex.request_site())

