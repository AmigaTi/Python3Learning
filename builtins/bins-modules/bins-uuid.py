#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid


uuid_str = uuid.uuid4().hex
print('uuid4: %s' % uuid_str)
print('len: %d' % len(uuid_str))

'''
uuid4: 8b14fff8f8c54391a4653c8f9c917b06
len: 32
'''
