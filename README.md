nedujob
=======
##毕业设计
--------
###题目:大学生招聘信息网站设计与实现
毕业设计，使用python爬虫进行工作的信息的查找和更新，

现在暂时定为使用拉钩,周伯通,v2ex,这几个站点的工作信息进项抓取

暂时定为计算机方向的技术工作，

语言范围是:

python , php , java,

平台是:

linux，mac，Android，iPhone，

##使用开发语言为:
####python

##使用技术为：
linux  服务器

ngnix 静态文件服务器

flask 框架作为开发框架

bootstrap 作为前端的展示

postgresql 网站的数据库

sqlalchemy 网站的数据库的orm构架

nuittest 网站的测试用例框架

暂时使用这些技术，如果后期出现负载问题，可能会使用redis


需求分析



1. 用户模块

    1. 用户注册，及其注册的相关的验证
    2. root用户的生成会用sql语句，将root用户进行标记
    3. 用户登录，先验证用户的合法性，再验证用户的权限
    4. 用户登录之后进行相关信息的关注
    5. 用户给网站留言
    6. root用户，登录之后进行采集信息的一些修改（主要是把不准确的信息剔除）

2. 数据模块

    1. [v2ex](https://www.v2ex.com)数据采集，采集比较简单，v2ex提供了api，直接采集就行了
    2. [lagou](http://www.lagou.com)的数据采集,
