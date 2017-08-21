#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import time
import os

r'''
App.UserLic.Extended=0
App.UserLic.FirstUseOn=1492271965
App.UserLic.LaunchNum=1
App.UserLic.NagNum=0
App.UserLic.SecsUsed=462
'''

filename = "./files/myBase.ini"
print("location: %s" % os.path.abspath(filename))

print("read file: %s" % os.path.basename(filename))
with open(filename, 'r') as f:
    lines = f.readlines()
    length = len(lines)
    for i in range(0, length):
        if re.match(r'App\.UserLic\.FirstUseOn=', lines[i]):
            # 因为lines[i]保存的字符串中含有\n，故print设置不输出换行\n
            print("before: %s" % lines[i], end='')
            lines[i] = "App.UserLic.FirstUseOn=" + ('%d' % time.time()) + "\n"
            print("after: %s" % lines[i], end='')
            break

print("write file: %s" % os.path.basename(filename))
with open(filename, 'w') as f:
    f.writelines(lines)

print("successfully...")
