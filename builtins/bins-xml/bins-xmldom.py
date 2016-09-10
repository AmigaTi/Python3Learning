#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom


# 使用minidom解析器打开XML文档
DOMTree = xml.dom.minidom.parse('./xmlfile/movies.xml')
collection = DOMTree.documentElement
if collection.hasAttribute('shelf'):
    print('Root element: %s' % collection.getAttribute('shelf'))

# 在集合中获取所有电影
movies = collection.getElementsByTagName('movie')

# 打印每部电影的详细信息
for movie in movies:
    print('*****Movie*****')
    if movie.hasAttribute('title'):
        print('Title: %s' % movie.getAttribute('title'))

    tag_type = movie.getElementsByTagName('type')[0]
    print('Type: %s' % tag_type.childNodes[0].data)
    tag_format = movie.getElementsByTagName('format')[0]
    print('Format: %s' % tag_format.childNodes[0].data)
    tag_rating = movie.getElementsByTagName('rating')[0]
    print('Rating: %s' % tag_rating.childNodes[0].data)
    tag_description = movie.getElementsByTagName('description')[0]
    print('Description: %s' % tag_description.childNodes[0].data)

'''
Root element: New Arrivals
*****Movie*****
Type: War, Thriller
Format: DVD
Rating: PG
Description: Talk about a US-Japan war
*****Movie*****
Type: Anime, Science Fiction
Format: DVD
Rating: R
Description: A schientific fiction
*****Movie*****
Type: Anime, Action
Format: DVD
Rating: PG
Description: Vash the Stampede!
*****Movie*****
Type: Comedy
Format: VHS
Rating: PG
Description: Viewable boredom
'''
