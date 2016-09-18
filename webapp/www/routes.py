#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import hashlib
import logging

from aiohttp import web

from webapp.www.coroweb import get
from webapp.www.coroweb import post
from webapp.www.models import User
from webapp.www.models import Blog
from webapp.www.models import Comment
from webapp.www.helper import Page
from webapp.www import helper
from webapp.www import ghelper
from webapp.www.apierror import APIError
from webapp.www.apierror import APIValueError
from webapp.www.apierror import APIResourceNotFoundError
from webapp.www import markdown2


logging.basicConfig(level=logging.INFO)


# REST API
# URL                                       http://localhost:9000
#
# router                           POST     handler


# 启动MySQL后台服务程序：../bin/mysqld.exe
# 启动Web 服务器： python app.py
# 浏览器访问：http://localhost:9000/test
@get('/test')
async def test():
    users = await User.findall()
    return {
        '__template__': 'html_editor.html',        # test.html
        'users': users
    }


@get('/')
async def index(*, page='1'):
    num = await Blog.findnum('count(id)')
    page = Page(num, page)
    if num == 0:
        blogs = []
    else:
        blogs = await Blog.findall(orderBy='created_at desc', limit=(page.offset, page.limit))
    return {
        '__template__': 'blogs.html',
        'page': page,
        'blogs': blogs
    }


@get('/blog/{id}')
async def get_blog(id):
    blog = await Blog.find(id)
    comments = await Comment.findall('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:                                          # 将全部的评论从文本转成html格式
        c.html_content = helper.text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)        # 支持Markdown格式文本编辑
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments
    }


@get('/api/users')
async def api_get_users(*, page='1'):
    num = await User.findnum('count(id)')
    p = Page(num, page)
    if num == 0:
        return dict(page=p, users=())
    users = await User.findall(orderBy='created_at desc', limit=(p.offset, p.limit))
    for u in users:
        u.passwd = '******'
    return dict(page=p, users=users)


# cookie
# 用户登录比用户注册复杂。由于HTTP协议是一种无状态协议，而服务器要跟踪用户状态，就只能通过cookie实现。
# 大多数Web框架提供了Session功能来封装保存用户状态的cookie。

# 采用直接读取cookie的方式来验证用户登录，每次用户访问任意URL，都会对cookie进行验证，
# 这种方式的好处是保证服务器处理任意的URL都是无状态的，可以扩展到多台服务器。

# 由于登录成功后是由服务器生成一个cookie发送给浏览器，所以要保证这个cookie不会被客户端伪造出来。
# 实现防伪造cookie的关键是通过一个单向算法(如SHA1)：
#
# 当用户输入了正确的密码登录成功后，服务器可以从数据库取到用户的id，并按照如下方式计算出一个字符串：
# "用户id" + "过期时间" + SHA1("用户id" + "用户密码" + "过期时间" + "SecretKey")
# 当浏览器发送cookie到服务器端后，服务器可以拿到的信息包括：
# 用户id//过期时间//SHA1值
# 如果未到过期时间，服务器就根据用户id查找用户密码，并计算：
# SHA1("用户id" + "用户密码" + "过期时间" + "SecretKey")
# 并与浏览器cookie中的SHA1值进行比较，如果相等则说明用户已登录，否则cookie就是伪造的。

# 对于每个URL处理函数，如果都去写解析cookie的代码，那会导致代码重复很多次。
# 利用Middleware在处理URL之前，把cookie解析出来，并将登录用户绑定到request对象上，
# 这样后续的URL处理函数就可以直接拿到登录用户。


# 用户登录界面
# signin.html中的js代码会将登录信息封装成JSON，然后当点击按钮时自动提交POST请求/api/authenticate
@get('/signin')
def signin():
    return {
        '__template__': 'signin.html'
    }


# 用户登录验证
# 在signin.html登录界面中，点击登录按钮时浏览器提交此POST请求
# 返回新生成的cookie
@post('/api/authenticate')
async def authenticate(*, email, passwd):
    helper.check_email_password(email, passwd)
    users = await User.findall('email=?', [email])              # 检查登录用户是否存在，使用邮箱来查找
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')        # 登录时没有验证邮箱地址的格式是否正确
    user = users[0]
    if user.passwd != helper.make_passwd_sha1(user.id, passwd):        # 检查登录密码
        raise APIValueError('passwd', 'Invalid password.')
    # authenticate ok, set cookie:
    r = web.Response()
    cookie_name = ghelper.get_cookie_name()
    r.set_cookie(cookie_name, helper.user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    cookie_name = ghelper.get_cookie_name()
    r.set_cookie(cookie_name, '-deleted-', max_age=0, httponly=True)
    logging.info('user signed out.')
    return r


# Server -> Client
# 用户注册界面 - 由服务器端Server返回给浏览器客户端Client
# 当点击注册按钮时，自动提交POST请求/api/users
@get('/register')
def register():
    return {
        '__template__': 'register.html'
    }


# Client -> Server
# 用户注册信息提交 - 由浏览器客户端Client通过POST请求提交数据到服务器端Server
# 用户密码是客户端传递的经过SHA1计算后的40位Hash字符串，所以服务器端并不知道用户的原始密码
# 创建一个注册页面，让用户填写注册表单，然后提交数据到注册用户的API
@post('/api/users')
async def api_register_user(*, email, name, passwd):
    helper.check_string(name=name)
    helper.check_email_password(email, passwd)
    users = await User.findall('email=?', [email])
    if len(users) > 0:
        raise APIError('register: failed', 'email', 'Email is already in use.')
    uid = ghelper.get_unique_id()                    # helper.get_unique_id
    passwd_sha1 = helper.make_passwd_sha1(uid, passwd)
    email_md5 = hashlib.md5(email.encode('utf-8')).hexdigest()
    image_str = 'http://www.gravatar.com/avatar/%s?d=mm&s=120' % email_md5
    user = User(id=uid, name=name.strip(), email=email, passwd=passwd_sha1, image=image_str)
    await user.save()           # 保存注册用户的信息
    # make session cookie:
    r = web.Response()
    cookie_name = ghelper.get_cookie_name()
    r.set_cookie(cookie_name, helper.user2cookie(user, 86400), max_age=86400, httponly=True)   # 86400s = 24h = a day
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


@get('/manage/')
def manage():
    return 'redirect:/manage/comments'


@get('/manage/comments')
def manage_comments(*, page='1'):
    return {
        '__template__': 'manage_comments.html',
        'page_index': Page.get_page_index(page)
    }


@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': Page.get_page_index(page)
    }


# 使用简单易用的MVVM框架Vue.js来实现创建Blog的页面manage_blog_edit.html
@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs'
    }


@get('/manage/blogs/edit')
def manage_edit_blog(*, id):
    return {
        '__template__': 'manage_blog_edit.html',
        'id': id,
        'action': '/api/blogs/%s' % id
    }


@get('/manage/users')
def manage_users(*, page='1'):
    return {
        '__template__': 'manage_users.html',
        'page_index': Page.get_page_index(page)
    }


@get('/api/blogs')
async def api_blogs(*, page='1'):
    num = await Blog.findnum('count(id)')
    p = Page(num, page)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = await Blog.findall(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)


@get('/api/blogs/{id}')
async def api_get_blog(*, id):
    return await Blog.find(id)


@post('/api/blogs')
async def api_create_blog(request, *, name, summary, content):
    helper.check_user(request.__user__)     # request.__user__是从拦截器auth_factory中绑定后传递到此handler
    helper.check_string(name=name, summary=summary, content=content)
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


@post('/api/blogs/{id}')
async def api_update_blog(id, request, *, name, summary, content):
    helper.check_user(request.__user__)
    helper.check_string(name=name, summary=summary, content=content)
    blog = await Blog.find(id)
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.strip()
    await blog.update()
    return blog


@post('/api/blogs/{id}/delete')
async def api_delete_blog(request, *, id):
    helper.check_user(request.__user__)
    blog = await Blog.find(id)
    await blog.remove()
    return dict(id=id)


@post('/api/blogs/{id}/comments')
async def api_create_comment(id, request, *, content):
    helper.check_user(request.__user__, adminonly=False)
    helper.check_string(content=content)
    blog = await Blog.find(id)
    if blog is None:
        raise APIResourceNotFoundError('Blog')
    comment = Comment(
        blog_id=blog.id,
        user_id=request.__user__.id,
        user_name=request.__user__.name,
        user_image=request.__user__.image,
        content=content.strip()
    )
    await comment.save()
    return comment


@get('/api/comments')
async def api_comments(*, page='1'):
    num = await Comment.findnum('count(id)')
    p = Page(num, page)
    if num == 0:
        return dict(page=p, comments=())
    comments = await Comment.findall(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, comments=comments)


@post('/api/comments/{id}/delete')
async def api_delete_comments(id, request):
    helper.check_user(request.__user__)
    c = await Comment.find(id)
    if c is None:
        raise APIResourceNotFoundError('Comment')
    await c.remove()
    return dict(id=id)

