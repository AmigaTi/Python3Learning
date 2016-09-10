#!/usr/bin/python
# -*- coding: utf-8 -*-

from webapp.www import config_default
# from . import config_default              # OK


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


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])        # recursion to search the element out of dict
            else:
                r[k] = override[k]
        else:
            r[k] = v                                # take the default to the result if not in override
    return r


def dictext(d):
    de = DictExt()
    for k, v in d.items():
        de[k] = dictext(v) if isinstance(v, dict) else v
        # de[k] = [v, dictext(v)][isinstance(v, dict)]      # dictext(v) if True
    return de


configs = config_default.configs

try:
    from webapp.www import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    from webapp.www import config_override

configs = dictext(configs)












