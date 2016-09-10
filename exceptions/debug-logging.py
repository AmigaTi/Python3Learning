#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

# logging

# 指定记录信息级别
# level = DEBUG/INFO/WARNING/ERROR
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


