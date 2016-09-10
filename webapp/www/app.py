#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import json
import asyncio
import logging

from aiohttp import web         # Middleware
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from webapp.www import orm
from webapp.www.coroweb import add_routes, add_static


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


def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape=kw.get('autoescape', True),
        block_start_string=kw.get('block_start_string', '{%'),
        block_end_string=kw.get('block_end_string', '%}'),
        variable_start_string=kw.get('variable_start_string', '{{'),
        variable_end_string=kw.get('variable_end_string', '}}'),
        auto_reload=kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 templates path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

# middleware factory <- xxx_factory
# 在每个响应之前打印日志
async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        # await asyncio.sleep(0.3)
        return await handler(request)       #
    return logger


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


# 把任何返回值封装成浏览器可正确显示的Response对象
async def response_factory(app, handler):
    async def response(request):                # handler(request)
        logging.info('Response handler...')
        r = await handler(request)          #
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and 100 <= r < 600:
            return web.Response(status=r)
        if isinstance(r, tuple) and len(r) == 2:
            status, msg = r
            if isinstance(status, int) and 100 <= status < 600:
                return web.Response(status=status, text=str(msg))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response


def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)


async def init(in_loop):
    await orm.create_pool(loop=in_loop, host='127.0.0.1', port=3306, user='www', password='www', db='awesome')
    app = web.Application(
        loop=in_loop,
        middlewares=[logger_factory, response_factory]
    )
    init_jinja2(app, filters=dict(datetime=datetime_filter))
    add_routes(app, 'handlers')         # ./handlers.py
    add_static(app)
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


# testing in browser
# http://localhost:9000/




