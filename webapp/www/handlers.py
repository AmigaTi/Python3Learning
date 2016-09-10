#!/usr/bin/python
# -*- coding: utf-8 -*-

from webapp.www.coroweb import get


# 测试
@get('/test')
async def test():
    return {
        '__template__': 'test.html'
    }

