#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


is_debug = True
use_logging_info = False


def set_logging_info(use=True):
    global use_logging_info
    use_logging_info = use


def set_debug(debug=True):
    global is_debug
    is_debug = debug


def reset_debug():
    set_debug(False)


def logd(*obj):
    if is_debug is True:
        if use_logging_info is True:
            logging.info(*obj)
        else:
            print(*obj)


def logf(*, formatted, data):
    print(formatted % tuple(data))


