#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import logging

from aiohttp import web

from webapp.www import orm
from webapp.www.coroweb import add_routes, add_static
from webapp.www.middlewares import logger_factory
from webapp.www.middlewares import auth_factory
from webapp.www.middlewares import response_factory
from webapp.www.renderengine import init_jinja2
from webapp.www.renderengine import datetime_filter


logging.basicConfig(level=logging.INFO)


async def init(in_loop):
    await orm.create_pool(loop=in_loop, host='127.0.0.1', port=3306, user='www-data', password='www-data', db='awesome')
    # 1. Create an Application instance, Application is a dict-like object
    app = web.Application(
        loop=in_loop,
        middlewares=[logger_factory, auth_factory, response_factory]        # Register Middleware factory
    )
    # 2. Initialize render templates config
    init_jinja2(app, filters=dict(datetime=datetime_filter))
    # 3. Register the request handler with the application’s router on a particular HTTP method and path
    # handler -> RequestHandler decorator -> app.router.add_route
    add_routes(app, 'handlers')         # ./handlers.py
    # 4. # Adds a router and a handler for returning static files (Images, JavaScripts, Fonts, CSS files etc.)
    add_static(app)
    # 5. Create a TCP server (socket type SOCK_STREAM) bound to host and port
    # web.Application.make_handler - Creates HTTP protocol factory for handling requests
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return server


loop = asyncio.get_event_loop()         #
loop.run_until_complete(init(loop))     #
loop.run_forever()                      #

