#!/usr/bin/python
# -*- coding: utf-8 -*-

import configparser

'''
# creator.ini
[Unix]                                   # section = Unix
name = Ken Thompson & Dennis Ritchie     # option = name   => item
date = 1969                              # option = date   => item
'''

# 创建配置解析器
config = configparser.ConfigParser()
# 读取配置文件，若文件不存在则创建
config.read("creator.ini", encoding="utf-8")


# 查询操作

# 获取配置文件中的所有节点名称
sections = config.sections()
print(sections)             # ['Python', 'Linux', 'C', 'Unix']

# 获取指定节点的所有选项名称
options = config.options('Unix')
print(options)              # ['name', 'date']

# 获取指定节点的所有选项键值对
items = config.items('Unix')
print(items)                # [('name', 'Ken Thompson & Dennis Ritchie'), ('date', '1969')]

# 获取指定节点Unix的指定选项name的值
name = config.get('Unix', 'name')
print(name)                 # Ken Thompson & Dennis Ritchie

# 获取指定节点Unix的指定选项date的值
date = config.get('Unix', 'date')
print(date)                 # 1969

# 获取指定节点Unix的指定选项date的值，date选项值需要init型，否则ValueError
date = config.getint('Unix', 'date')
print(date)                 # 1969

# 检查指定节点Python是否存在，返回True或False
has_section_python = config.has_section('Python')
print('has_section_python:', has_section_python)        # has_section_python: True

# 检查指定节点Python中是否存在选项name，返回True或False
has_python_option = config.has_option('Python', 'name')
print('has_python_option:', has_python_option)          # has_python_option: True


# 增删改操作

# 添加一个新节点Lua，此时添加的节点Lua尚未写入文件
config.add_section('Lua')
# 在已存在的节点Lua中添加一个键值对，若该节点不存在则报错；
# 若key已存在，则修改value；若key不存在，则创建并赋值
config.set('Lua', 'name', 'Roberto Ierusalimschy/Waldemar Celes/Luiz Henrique de Figueiredo')
config.set('Lua', 'date', '1993')

# 将修改写入文件中进行保存
config.write(open('creator.ini', "w"))
print(config.items('Lua'))      # [('name', 'Roberto Ierusalimschy/Waldemar Celes/Luiz Henrique de Figueiredo'), ('date', '1993')]

# 删除一个节点Lua，删掉内存中的节点Lua
config.remove_section('Lua')
# 将删除节点Lua后的配置内容回写到配置文件中
config.write(open('creator.ini', "w"))
print('has_section_lua:', config.has_section('Lua'))      # has_section_lua: False
