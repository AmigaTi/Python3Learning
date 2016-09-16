#!/usr/bin/python
# -*- coding: utf-8 -*-


# user customized config
config_override = {
    'db': {
        'host': '127.0.0.1'
    }
}


# server default config
config_default = {
    'server': {
        'host': '127.0.0.1',
        'port': 9000
    },
    'database': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'db': 'awesome'
    },
    'cookie': {
        'name': 'AweSession',
        'key': 'Awesome'
    }
}


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


configs = dictext(merge(config_default, config_override))   # default <-- override

