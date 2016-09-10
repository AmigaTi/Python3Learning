#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate


# Python中的SAX解析XML
# 实现三个事件回调处理：start_element end_element char_data
# 当SAX解析器读到一个节点时：
# <a href="/">python</a>
# 会产生3个事件：
# 1. 在读取<a href="/">时，产生start_element事件
# 2. 在读取python时，产生char_data事件
# 3. 在读取</a>时，产生end_element事件


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml_data = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''


handler = DefaultSaxHandler()
parser = ParserCreate()     # 创建并返回一个新的xmlparser对象
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml_data)

'''
sax:start_element: ol, attrs: {}
sax:char_data:

sax:char_data:
sax:start_element: li, attrs: {}
sax:start_element: a, attrs: {'href': '/python'}
sax:char_data: Python
sax:end_element: a
sax:end_element: li
sax:char_data:

sax:char_data:
sax:start_element: li, attrs: {}
sax:start_element: a, attrs: {'href': '/ruby'}
sax:char_data: Ruby
sax:end_element: a
sax:end_element: li
sax:char_data:

sax:end_element: ol
'''




