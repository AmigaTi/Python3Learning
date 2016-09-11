#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import time
import json
import hashlib
import logging

from aiohttp import web

from webapp.www.coroweb import get
from webapp.www.coroweb import post
from webapp.www.models import next_id
from webapp.www.models import User
from webapp.www.models import Blog
from webapp.www.page import Page
from webapp.www.apierror import APIError
from webapp.www.apierror import APIValueError
from webapp.www.apierror import APIPermissionError
from webapp.www.config import configs


"""
URL Handlers
# router handlers
"""


COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret        # config_default.py


# 测试
# 通过Web框架的@get和ORM框架的Model支持，可以很容易地编写一个处理首页URL的函数
# '__template__'指定的模板文件是test.html，其他参数是传递给模板的数据
# 启动MySQL后台服务程序：../bin/mysqld.exe
# 启动Web 服务器： python app.py
# 浏览器访问：http://localhost:9000/test
@get('/test')
async def test():
    users = await User.findall()
    return {
        '__template__': 'test.html',
        'users': users
    }


# 浏览器访问：http://localhost:9000/
@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, ' \
              'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


# 浏览器访问：http://localhost:9000/api/users
# 返回JSON数据
@get('/api/users')
async def api_get_users():
    users = await User.findall(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'             # 使用星号*来屏蔽显示用户密码
    return dict(users=users)


# # 计算加密cookie
def user2cookie(user, max_age):
    """
    Generate cookie str by user.
    """
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)


# 解密cookie
async def cookie2user(cookie_str):
    """
    Parse cookie and load user if cookie is valid.
    """
    if not cookie_str:
        return None
    try:
        cookie_list = cookie_str.split('-')
        if len(cookie_list) != 3:
            return None
        uid, expires, sha1 = cookie_list
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None


# 用户登录界面
# signin.html中的js代码会将登录信息封装成JSON，然后当点击按钮时自动提交POST请求/api/authenticate
@get('/signin')
def signin():
    return {
        '__template__': 'signin.html'
    }


# 用户登录验证
# 在signin.html登录界面中，点击登录按钮时浏览器提交此POST请求
@post('/api/authenticate')
async def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not passwd:
        raise APIValueError('passwd', 'Invalid password.')
    users = await User.findall('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')        # 登录时没有验证邮箱地址的格式是否正确
    user = users[0]
    # check passwd:
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest():
        raise APIValueError('passwd', 'Invalid password.')
    # authenticate ok, set cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True)
    logging.info('user signed out.')
    return r


# Server -> Client
# 用户注册界面 - 由服务器端Server返回给浏览器客户端Client
# 浏览器访问：http://localhost:9000/register
# 当点击注册按钮时，自动提交POST请求/api/users
@get('/register')
def register():
    return {
        '__template__': 'register.html'
    }


_RE_EMAIL = re.compile(r'^[a-z0-9.\-_]+@[a-z0-9\-_]+(\.[a-z0-9\-_]+){1,4}$')   # Redundant character escape
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


# Client -> Server
# 用户注册信息提交 - 由浏览器客户端Client通过POST请求提交数据到服务器端Server
# 用户密码是客户端传递的经过SHA1计算后的40位Hash字符串，所以服务器端并不知道用户的原始密码
# 创建一个注册页面，让用户填写注册表单，然后提交数据到注册用户的API
@post('/api/users')
async def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd):
        raise APIValueError('passwd')
    users = await User.findall('email=?', [email])
    if len(users) > 0:
        raise APIError('register: failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    passwd_sha1 = hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()
    email_md5 = hashlib.md5(email.encode('utf-8')).hexdigest()
    image_str = 'http://www.gravatar.com/avatar/%s?d=mm&s=120' % email_md5
    user = User(id=uid, name=name.strip(), email=email, passwd=passwd_sha1, image=image_str)
    await user.save()
    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


# 浏览器访问：http://localhost:9000/manage/blogs
@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }


# 浏览器访问：http://localhost:9000/manage/blogs/create
@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs'
    }


def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError:
        pass
    if p < 1:
        p = 1
    return p


@get('/api/blogs')
async def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = await Blog.findnum('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = await Blog.findall(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)


@get('/api/blogs/{id}')
async def api_get_blog(*, id):
    blog = await Blog.find(id)
    return blog


# 数据库改表，有个列是0或1表示管理员
def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:  # not request.__user__.admin
        raise APIPermissionError()


# 编写一个REST API，用于创建一个Blog
@post('/api/blogs')
async def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')

    # request.__user__是从拦截器auth_factory中绑定后传递到此handler
    blog = Blog(
        user_id=request.__user__.id,
        user_name=request.__user__.name,
        user_image=request.__user__.image,
        name=name.strip(),
        summary=summary.strip(),
        content=content.strip()
    )
    await blog.save()
    return blog


'''
HTTP: 500
服务器内部错误
'''

'''
    if request.__user__ is None or not request.__user__.admin:
AttributeError: 'Request' object has no attribute '__user__'
'''