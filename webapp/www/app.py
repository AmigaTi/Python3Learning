#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import logging
from aiohttp import web


logging.basicConfig(level=logging.INFO)


def index(request):
    body = '<h1>你好Awesome</h1>'.encode('utf-8')
    headers = {'Content-Type': 'text/html; charset=utf-8'}      # 指定Content-Type中编码格式为utf-8，可以显示中文
    return web.Response(body=body, headers=headers)


@asyncio.coroutine
def init(in_loop):
    app = web.Application(loop=in_loop)
    app.router.add_route('GET', '/', index)
    srv = yield from in_loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


# testing in browser
# http://localhost:9000/




