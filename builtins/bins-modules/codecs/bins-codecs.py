#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

file = open('test.txt', 'a')
# text_line1 = "我爱祖国"
# file.write(text_line1)

text_line2 = u'我爱祖国'
# text_line2 --decode--> unicode --encode--> utf-8
file.write(text_line2)      # 直接保存会导致乱码

fc = codecs.open('test_cs.txt', 'a', 'utf-8')
fc.write(text_line2)        # 直接保存就可以
