#!/usr/bin/python
# -*- coding: utf-8 -*-

from webapp.www.coroweb import get
from webapp.www.models import User

"""
URL Handlers
"""


# 测试
@get('/test')
async def test():
    return {
        '__template__': 'test.html'
    }


# 通过Web框架的@get和ORM框架的Model支持，可以很容易地编写一个处理首页URL的函数
# '__template__'指定的模板文件是test.html，其他参数是传递给模板的数据
# 启动MySQL后台服务程序：../bin/mysqld.exe
# 启动Web 服务器： python app.py
# 浏览器访问：http://localhost:9000/
@get('/')
async def index(request):
    users = await User.findall()
    return {
        '__template__': 'test.html',
        'users': users
    }
