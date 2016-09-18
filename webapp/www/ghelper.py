#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import uuid

from webapp.www.config import config_default
from webapp.www.config import config_override


"""
ghelper(get function helper)
"""


# 交叉依赖导致无法整成找到ghelper的模块属性
# 获取唯一的id号
def get_unique_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)  # 15 + 32 + 3 = 50


def get_created_time():
    return time.time()


# --------------------------------------------------------------------------------------------
class DictExt(dict):
    """
    Define extended dict to support the access style as DictExt.key
    """
    def __init__(self, names=(), values=(), **kw):
        super(DictExt, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def merge(default, override):
    config = {}
    for k, v in default.items():
        if k in override:
            if isinstance(v, dict):
                config[k] = merge(v, override[k])        # recursion to search the element out of dict
            else:
                config[k] = override[k]
        else:
            config[k] = v                                # take the default to the result if not in override
    return config


def dictext(d):
    de = DictExt()
    for k, v in d.items():
        de[k] = dictext(v) if isinstance(v, dict) else v
    return de


# usage example:
configs = dictext(merge(config_default, config_override))   # default <-- override


# 获取定义在config.py中的关于数据库的配置信息
def get_database_conf():
    database = configs.database
    host = database.host
    port = database.port
    user = database.user
    password = database.password
    db = database.db
    return host, port, user, password, db       # tuple


# 获取定义在config.py中的关于服务器的配置信息
def get_server_conf():
    server = configs.server
    host = server.host
    port = server.port
    return host, port                           # tuple


def get_cookie_conf():
    cookie = configs.cookie
    name = cookie.name
    key = cookie.key
    return name, key


def get_cookie_name():
    return configs.cookie.name


def get_cookie_key():
    return configs.cookie.key

