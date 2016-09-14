#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import logging

from datetime import datetime
from jinja2 import Environment, FileSystemLoader


logging.basicConfig(level=logging.INFO)


def init_jinja2(app, **kw):
    logging.info('init jinja2 (The Python Template Engine)...')
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
    # 创建一个 Environment 对象并指定加载器查找模板的路径，用于加载HTML模板
    env = Environment(loader=FileSystemLoader(path), **options)     # jinja2.Environment
    filters = kw.get('filters', None)       #
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f           # 注册自定义过滤器，应用于模板环境中
    # store global-like variable variables in an Application instance for data sharing
    # and get it back in the handler
    # 创建全局变量app['__templating__']来存储jinja2.Environment实例对象env，
    # 然后在拦截器Middleware的响应工厂response_factory中通过app['__templating']重新获取，
    # 用于加载及渲染HTML模板文件
    app['__templating__'] = env


# 构建前端
# 通过jinja2的filter（过滤器），把一个浮点数转换成日期字符串
# 模板文件中：<p class="uk-article-meta">发表于{{ blog.created_at|datetime }}</p>
# 将会以datetime(blog.created_at)的方式被调用
def datetime_filter(t):
    delta = int(time.time() - t)        # unit: second
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

