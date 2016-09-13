#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import functools
import inspect
import asyncio

from urllib import parse        # Parse a query string in the URL
from aiohttp import web

from webapp.www.apierror import APIError

# reference
# http://aiohttp.readthedocs.io/en/stable/web.html


# 在aiohttp上层封装的一个框架


# 路由函数实例
# @get('/api/{table}')
# async def api_model(table, page=1, request):
#     pass
# 三个参数[table, page, request]的来源：
# 1. 网页中的GET和POST方法 (获取/?page=10还有json或form的数据)
# 2. request.match_info (获取@get('/api/{table}')装饰器里面的参数)
# 3. RequestHandler.__call__(self, request) (获取request参数)


# 定义装饰函数get，被函数get装饰后的函数将拥有__method__、__route__属性
def get(path):
    """Define decorator @get('/path')."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'      #
        wrapper.__route__ = path        #
        return wrapper
    return decorator


# 定义装饰函数post，被函数post装饰后的函数将拥有__method__、__route__属性
def post(path):
    """Define decorator @post('/path')."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'     #
        wrapper.__route__ = path        #
        return wrapper
    return decorator


# a == POSITIONAL_OR_KEYWORD        # a是用位置或参数名都可赋值的
# b == VAR_POSITIONAL               # b是可变长列表
# c == KEYWORD_ONLY                 # c只能通过参数名的方式赋值
# d == VAR_KEYWORD                  # d是可变长字典
# builtins/bins-modules/bins-inspect-indeep.py

def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters   #
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY \
                and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)


def get_named_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)


def has_named_kw_args(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True


def has_var_kw_arg(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True


def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        # 如果找到request参数的话，后面还有POSITIONAL_ONLY, POSITIONAL_OR_KEYWORD)这两类参数就报错，否则是不会报错的！
        # if found and (param.kind not in (VAR_POSITIONAL, KEYWORD_ONLY, VAR_KEYWORD))
        # if found and (param.kind in (POSITIONAL_ONLY, POSITIONAL_OR_KEYWORD))
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL
                      and param.kind != inspect.Parameter.KEYWORD_ONLY
                      and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last '
                             'named parameter in function: %s%s' % (fn.__name__, str(sig)))
    return found


# RequestHandler目的就是从URL函数中分析其需要接收的参数，从request中获取必要的参数，
# URL函数不一定是一个coroutine，因此用RequestHandler()来封装一个URL处理函数。
# 调用URL函数，然后把结果转换为web.Response对象，这样就完全符合aiohttp框架的要求。

# RequestHandler的主要作用就是构成标准的app.router.add_route第三个参数，
# 还有就是获取不同的函数的对应的参数，就这两个主要作用。

# 简化程序：从老师的先检验再获取转换成先获取再统一验证

# RequestHandler是handlers.py中的handler装饰器+++
class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn             # 保存handlers.py中定义的router handler
        self._has_request_arg = has_request_arg(fn)
        self._has_var_kw_arg = has_var_kw_arg(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._required_kw_args = get_required_kw_args(fn)

    # coroutine
    # 相当于重载括号运算符，像函数一样直接调用rh = RequestHandler(app, fn), rh(request)
    async def __call__(self, request):
        kw = None
        if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
            if request.method == 'POST':
                if not request.content_type:
                    return web.HTTPBadRequest(text='Missing Content-Type.')     # ?? specify keyword
                ct = request.content_type.lower()           # Content-Type
                if ct.startswith('application/json'):
                    params = await request.json()           # A coroutine that reads request body decoded as json
                    if not isinstance(params, dict):
                        return web.HTTPBadRequest(text='JSON body must be object.')     # ??
                    kw = params                             # post json to dict object
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                    params = await request.post()           # A coroutine that reads POST parameters from request body
                    kw = dict(**params)                      #
                else:
                    return web.HTTPBadRequest(text='Unsupported Content-Type: %s' % request.content_type)   # ??
            if request.method == 'GET':
                qs = request.query_string           # The query string in the URL, e.g., id=10
                if qs:
                    kw = dict()
                    for k, v in parse.parse_qs(qs, True).items():   # parse the Request.query_string
                        kw[k] = v[0]                # 保存请求参数键值对到kw字典中
        if kw is None:
            kw = dict(**request.match_info)         # request.match_info // @get('/api/blogs/{id}')
        else:
            if not self._has_var_kw_arg and self._named_kw_args:    # 如果不是VAR_KEYWORD
                # remove all unnamed kw:
                copy = dict()                       # 只保存handler函数中声明的且又存在kw中的参数
                for name in self._named_kw_args:
                    if name in kw:
                        copy[name] = kw[name]
                kw = copy                           #
            # check named arg:
            for k, v in request.match_info.items():   # result of route resolving // @get('/api/blogs/{id}')
                if k in kw:
                    logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
                kw[k] = v                              # 保存route 解析出来的值// @get('/api/blogs/{id}')中的id
        if self._has_request_arg:                           # ??
            kw['request'] = request          # 如果handlers.py中的handler声明了request参数则将request保存到kw中
        # check required kw:
        if self._required_kw_args:
            for name in self._required_kw_args:
                if name not in kw:          #
                    return web.HTTPBadRequest(text='Missing argument: %s' % name)   # ?? specify keyword
        logging.info('call handler with args: %s' % str(kw))
        try:
            # noinspection PyArgumentList
            r = await self._func(**kw)              # 调用handlers.py中定义的handler函数，并将处理后的kw参数传入
            return r
        except APIError as e:
            return dict(error=e.error, data=e.data, message=e.message)


# static files (Images, JavaScripts, Fonts, CSS files etc.)
def add_static(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    # Adds a router and a handler for returning static files
    # Useful for serving static content like images, javascript and css files
    app.router.add_static('/static/', path)                             # app.router.add_static
    logging.info('add static %s => %s' % ('/static', path))


# 注册一个URL处理函数
def add_route(app, fn):
    method = getattr(fn, '__method__', None)        # 由装饰器get('/path')/post('/path')得到method和path两个参数
    path = getattr(fn, '__route__', None)           # 这些被统一定义在handlers.py模块下
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)                  #
    logging.info('add route %s %s => %s(%s)' %
                 (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
    # Append handler to the end of route table
    # add_route(method, path, handler, *, name=None, expect_handler=None)
    #  - path may be either constant string like '/a/b/c' or variable rule like '/a/{var}'
    #    request.match_info['name'] in handler
    #  - method: GET/POST/PUT/DELETE/PATCH/HEAD/OPTIONS/*
    app.router.add_route(method, path, RequestHandler(app, fn))         # app.router.add_route/RequestHandler


# 自动扫描并注册handlers.py模块中所有符合条件的函数
# app - aiohttp.web.Application instance
# module_name - 定义handler request模块名称
def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == (-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n+1:]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method and path:
                # noinspection PyTypeChecker
                add_route(app, fn)                                      # add_route















