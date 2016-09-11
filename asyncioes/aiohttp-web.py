#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
from aiohttp import web

# reference
# http://aiohttp.readthedocs.io/en/stable/web.html

# 注意aiohttp的初始化函数init()也是一个coroutine，
# loop.create_server()则利用asyncio创建TCP服务

# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。


# 编写一个HTTP服务器，分别处理以下URL：
# /             -   首页返回b'<h1>Index</h1>'
# /hello/{name} -   根据URL参数返回文本hello, %s!


# aiohttp使用步骤
# 1. 编写一个用@asyncio.coroutine/async装饰的函数
# 2. 传入的参数从request获取
# 3. 构造Response对象并返回


# Variable Resources
# Resource may have variable path also. For instance, a resource with
# the path '/a/{name}/c' would match all incoming requests with paths
# such as '/a/b/c', '/a/1/c', and '/a/etc/c'.

# A variable part is specified in the form {identifier}, where the identifier
#  can be used later in a request handler to access the matched value
# for that part. This is done by looking up the identifier in the Request.match_info mapping


# Static file handling
# The best way to handle static files (images, JavaScripts, CSS files etc.)
# is using Reverse Proxy like nginx or CDN services.

# But for development it’s very convenient to handle static files by aiohttp server itself.

# To do it just register a new static route by UrlDispatcher.add_static() call:
# app.router.add_static('/prefix', path_to_static_folder)


# Implement a web server

# First
# create a request handler
# A request handler is a coroutine or regular function that
# accepts a Request instance as its only parameter and returns a Response instance
#
# def handler(request):
#     return web.Response()
#
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Hello world and hello me!</h1>')


async def greeting(request):
    await asyncio.sleep(0.5)
    name = request.match_info.get('name', 'Anonymous')      # request.match_info['name']
    text = '<h1>hello, <i style=\'color: rgba(0, 0, 255, 0.8);\'>{}!</i></h1>'.format(name)
    return web.Response(body=text.encode('utf-8'))


async def init_web_server(in_loop):
    # Next, create an Application instance and register the request handler with
    # the application's router on a particular HTTP method and path
    app = web.Application(loop=in_loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/greet/{name}', greeting)
    # coroutine
    # Create a TCP server (socket type SOCK_STREAM) bound to host and port
    server = await in_loop.create_server(app.make_handler(), '127.0.0.1', 9898)
    print('Server started at http://127.0.0.1:9898...')
    return server


loop = asyncio.get_event_loop()                 #
loop.run_until_complete(init_web_server(loop))  # Run until the Future is done
loop.run_forever()                              # Run until stop() is called


# testing in browser
# http://localhost:9898/
# http://localhost:9898/hello/firstme

'''
Server started at http://127.0.0.1:9898...
'''


# issue 20160909
'''
500 Internal Server Error

Server got itself in trouble
'''