#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import logging

from aiohttp import web

from webapp.www import orm
from webapp.www import helper
from webapp.www import ghelper
from webapp.www import coroweb
from webapp.www import render
from webapp.www.middlewares import factory


logging.basicConfig(level=logging.INFO)


async def init(loop):
    host, port, user, password, db = ghelper.get_database_conf()
    await orm.create_pool(loop=loop, host=host, port=port, user=user, password=password, db=db)
    # 1. Create an Application instance, Application is a dict-like object
    app = web.Application(
        loop=loop,
        middlewares=[factory.log, factory.auth, factory.data, factory.resp]        # Register Middleware factory
    )
    # init to create a admin user when create server firstly
    await helper.init_admin_user()
    # 2. Initialize render templates config
    render.init_jinja2(app, filters=dict(datetime=render.datetime_filter))
    # 3. Register the request handler with the application’s router on a particular HTTP method and path
    # handler -> RequestHandler decorator -> app.router.add_route
    coroweb.add_routes(app, 'routes')
    # 4. # Adds a router and a handler for returning static files (Images, JavaScripts, Fonts, CSS files etc.)
    coroweb.add_static(app)
    # 5. Create a TCP server (socket type SOCK_STREAM) bound to host and port
    # web.Application.make_handler - Creates HTTP protocol factory for handling requests
    host, port = ghelper.get_server_conf()
    server = await loop.create_server(app.make_handler(), host, port)
    logging.info('server started at http://%s:%d...' % (host, port))
    return server


def run():
    loop = asyncio.get_event_loop()         #
    loop.run_until_complete(init(loop))     #
    loop.run_forever()                      #


if __name__ == '__main__':
    run()

