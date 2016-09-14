#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


t = time.time()                     # Return the time in seconds since the epoch as a floating point number
t1000 = int(t * 1000)

print('t: %d' % t)                  # t: 1473827255
print('t1000: %015d' % t1000)       # t1000: 001473827255865

t = time.gmtime(time.time())        #
s = time.strftime('%Y-%m-%d %H:%M:%S', t)
print(s)                            # 2016-09-14 04:27:35
