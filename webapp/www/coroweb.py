#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import types
import logging
import functools
import inspect
import asyncio

from urllib import parse        # Parse a query string in the URL
from aiohttp import web

from webapp.www.apierror import APIError

"""
coroweb -> coroutine web
"""

logging.basicConfig(level=logging.INFO)


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


# 定义routes.py中的handler的装饰器函数，返回标准的异步handler(request)函数
def handler_factory(func):
    async def route_handler(request):
        # 获取函数的参数表
        required_args = inspect.signature(func).parameters
        logging.info('required args: %s' % [name for name, param in required_args.items()])

        # 获取从GET或POST传进来的参数值，如果函数参数表有这参数名就加入
        kw = {arg: value for arg, value in request.__data__.items() if arg in required_args}

        # 获取match_info的参数值，例如@get('/blog/{id}')之类的参数值
        kw.update(dict(**request.match_info))

        # 如果有request参数的话也加入
        if 'request' in required_args:
            kw['request'] = request

        # 检查参数表中有没参数缺失
        for key, arg in required_args.items():
            # request参数不能为可变长参数
            if key == 'request' and arg.kind in (arg.VAR_POSITIONAL, arg.VAR_KEYWORD):
                return web.HTTPBadRequest(text='request parameter cannot be the var argument.')
            # 如果参数类型不是变长列表和变长字典，变长参数是可缺省的
            if arg.kind not in (arg.VAR_POSITIONAL, arg.VAR_KEYWORD):
                # 如果还是没有默认值，而且还没有传值的话就报错
                if arg.default == arg.empty and arg.name not in kw:
                    return web.HTTPBadRequest(text='Missing argument: %s' % arg.name)

        logging.info('call with args: %s' % kw)
        try:
            return await func(**kw)
        except APIError as e:
            return dict(error=e.error, data=e.data, message=e.message)
    return route_handler


# POSITIONAL_ONLY              #
# POSITIONAL_OR_KEYWORD        # 位置参数，默认参数
# VAR_POSITIONAL               # 可变参数tuple - *args
# VAR_KEYWORD                  # 关键字参数dict - **kw
# KEYWORD_ONLY                 # 命名关键字参数 - *, arg


# 获取必须的参数，即没有默认值的参数
def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters   #
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY \
                and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)


# 获取命名关键字参数
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


# 是否有request参数
def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True        # 标记找到request参数名
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

# RequestHandler是routes.py中的handler装饰器+++
class RequestHandler(object):
    def __init__(self, fn):
        self._func = fn             # 保存handlers.py中定义的router handler
        self._has_request_arg = has_request_arg(fn)
        self._has_var_kw_arg = has_var_kw_arg(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._required_kw_args = get_required_kw_args(fn)

    # rh = RequestHandler(fn), rh(request)
    # 即任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
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
                    kw = params                             # post中的请求参数
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                    params = await request.post()           # A coroutine that reads POST parameters from request body
                    kw = dict(**params)                      #
                else:
                    return web.HTTPBadRequest(text='Unsupported Content-Type: %s' % request.content_type)   # ??
            if request.method == 'GET':
                qs = request.query_string           # The query string in the URL, e.g., /app/blog?id=10中的id=10
                if qs:
                    kw = dict()
                    for k, v in parse.parse_qs(qs, True).items():   # parse the Request.query_string
                        kw[k] = v[0]                # 保存请求参数键值对到kw字典中

        if kw is None:      # 如果post或get中没有携带参数则直接在url路径中获取参数
            kw = dict(**request.match_info)         # request.match_info // @get('/api/blogs/{id}')
        else:               # kw from post/get
            if not self._has_var_kw_arg and self._named_kw_args:    # 如果不是VAR_KEYWORD
                # remove all unnamed kw:
                copy = dict()
                for name in self._named_kw_args:
                    if name in kw:
                        copy[name] = kw[name]       # 只保存handler函数中的声明的命名关键字参数
                kw = copy                           #
            # check named arg:
            for k, v in request.match_info.items():   # result of route resolving // @get('/api/blogs/{id}')
                if k in kw:
                    logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
                kw[k] = v                              # 保存route 解析出来的值// @get('/api/blogs/{id}')中的id

        if self._has_request_arg:                           # ??
            kw['request'] = request          # 如果handlers.py中的handler声明了request参数则将request保存到kw中

        # check required kw:
        if self._required_kw_args:          # 获取必须的参数，即没有默认值的参数
            for name in self._required_kw_args:
                if name not in kw:          # 必要的routes.py中的handler函数参数是否在kw中已存在
                    return web.HTTPBadRequest(text='Missing argument: %s' % name)   # ?? specify keyword
        logging.info('call handler with args: %s' % str(kw))
        try:
            # noinspection PyArgumentList
            r = await self._func(**kw)              # 调用handlers.py中定义的handler函数，并将处理后的kw参数传入
            return r
        except APIError as e:
            return dict(error=e.error, data=e.data, message=e.message)


# module.name = package.module
# 自动扫描并注册routes.py模块中所有符合条件的函数
def add_routes(app, module_name):
    n = module_name.rfind('.')          # routes.py -> n = 6
    if n == (-1):       # routes
        mod = __import__(module_name, globals(), locals())      # import routes
    else:               # www.routes
        name = module_name[n+1:]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)   # from www import routes
    for attr in dir(mod):
        if attr.startswith('_') or attr in ['get', 'post']:   # 直接跳过以下划线'_'开头的模块属性或get/post装饰器函数
            continue
        func = getattr(mod, attr)         # function or module or class
        if isinstance(func, types.FunctionType):      # function
            method = getattr(func, '__method__', None)
            path = getattr(func, '__route__', None)
            if method and path:          # 排除get/post/next_id等函数
                func = asyncio.coroutine(func)  #
                args = ', '.join(inspect.signature(func).parameters.keys())
                logging.info('add route: %s %s => %s(%s)' % (method, path, func.__name__, args))
                # app.router.add_route(method, path, RequestHandler(func))      # ok
                app.router.add_route(method, path, handler_factory(func))       # ok


# static files (Images, JavaScripts, Fonts, CSS files etc.)
def add_static(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app.router.add_static('/static/', path)
    logging.info('add static: %s => %s' % ('/static/', path))

