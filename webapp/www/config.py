#!/usr/bin/python
# -*- coding: utf-8 -*-


# customized config for user
config_override = {
    'db': {
        'host': '127.0.0.1'
    }
}


# default config for server
# WARNING: DON'T TRY TO MODIFY IT.
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

