#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import logging

from aiohttp import web                         # Middleware Application Request
from webapp.www import helper
from webapp.www import ghelper


logging.basicConfig(level=logging.INFO)


# aiohttp/web.py-line_number: 86

# Middleware
# http://aiohttp.readthedocs.io/en/stable/web.html#handler
#
# async def middleware_factory(app, handler):
#     async def middleware_handler(request):
#         return await handler(request)
#     return middleware_handler
#
# Every middleware factory should accept two parameters,
# an app instance and a handler, and return a new handler.

# The handler passed in to a middleware factory is the handler
# returned by the next middleware factory. The last middleware factory
# always receives the request handler selected by the router itself (by UrlDispatcher.resolve()).


# middleware factory <- xxx_factory
# middleware是一种拦截器，一个URL在被handler处理前，可以经过一系列的middleware进行预处理
# 预处理包括：在原本的handler执行前后插入其他代码，还有对request进行属性的更改，
# 如将user绑定在request对象上，使得在到达最后真正的handler(定义在handlers.py
# 且经过coroweb.RequestHandler修饰后的handler)时，可以从request中获取到user

# 在每个响应之前打印日志
async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        return await handler(request)       #
    return logger


# 利用Middleware在处理URL之前，把cookie解析出来并将登录用户user绑定到request对象上，
# 这样后续的URL处理函数就可以直接拿到登录用户
async def auth_factory(app, handler):
    async def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None                         # 初始化一个request.__user__
        cookie_name = ghelper.get_cookie_name()
        cookie_str = request.cookies.get(cookie_name)   # 获取cookie
        if cookie_str:
            user = await helper.cookie2user(cookie_str)        # 从cookie中解析出user
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user                  # 把cookie解析出来的当前登录用户user绑定到request对象上
        # 对URL/manage/进行拦截，检查当前用户是否是管理员身份
        if request.path.startswith('/manage/') and \
                (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
        return await handler(request)
    return auth


async def data_factory(app, handler):
    async def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__ = await request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = await request.post()
                logging.info('request form: %s' % str(request.__data__))
        return await handler(request)
    return parse_data


# 把定义在handlers.py且经过coroweb.RequestHandler处理后的数据封装成浏览器可正确显示的web.Response对象，
# 以保证满足aiohttp中要求的handler(request)返回值形式
async def response_factory(app, handler):
    async def response(request):                    # handler(request)
        logging.info('Response handler...')
        r = await handler(request)                          # handle the request
        if isinstance(r, web.StreamResponse):                # -> web.StreamResponse
            return r
        if isinstance(r, bytes):                             # -> bytes
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):                               # -> str
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):                              # -> dict
            template_file = r.get('__template__')            # '__template__': 'signin.html'
            if template_file is None:                       # @get('/api/users') in handlers.py
                json_str = json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__)  # 转换成标准的JSON字符串
                resp = web.Response(body=json_str.encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:                                           # 若有指定模板文件则直接渲染模板返回
                r['__user__'] = request.__user__         # 用于渲染__base__.html中的页面 {% if __user__ %}
                template = app['__templating__'].get_template(template_file)  # 加载模板，并返回已加载的Template
                rendered = template.render(**r)      # 使用字典类型变量来渲染，并返回unicode字符串格式的渲染后的模板
                resp = web.Response(body=rendered.encode('utf-8'))            # 将unicode转成utf-8的字节码用于网络传输
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and 100 <= r < 600:            # -> int
            return web.Response(status=r)
        if isinstance(r, tuple) and len(r) == 2:             # -> tuple
            status, msg = r
            if isinstance(status, int) and 100 <= status < 600:
                return web.Response(status=status, text=str(msg))
        # default:                                            # -> default
        resp = web.Response(body=str(r).encode('utf-8'))      # 默认直接转成字符串以文本的方式返回
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response

