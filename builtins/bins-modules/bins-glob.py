#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob

# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表

l = glob.glob('*.py')
print(l)        # ['bins-glob.py', 'bins-shutil.py']
