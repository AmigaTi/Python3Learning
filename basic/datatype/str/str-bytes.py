#!/usr/bin/python           # Linux/OS X系统中Python为可执行程序，Windows中忽略
# -*- coding: utf-8 -*-     # Python解释器以utf-8编码格式读取源代码文件


# 使用单引号或双引号来创建字符串
# Python3中，字符串是以Unicode编码的

# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输时，
# 就转换为UTF-8编码。


# ==============================================
# 单个字符(英文或中文)的编码
# ord() = 获取字符的编码整数数值表示
# chr() = 将编码整数数值转换为对应的字符
print(ord('A'))         # 65
print(chr(65))          # A
print(ord('空'))        # 31354
print(chr(31354))       # 空

print('=' * 30)


# ==============================================
# 字符串的编码
# Python的字符串在内存中以Unicode表示，一个字符对应若干个字节。
# 若要在网络上传输或者保存到磁盘上，就需要把字符串变为以字节为单位的bytes类型。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示。
# x = b'ABC'
# 在bytes类型中，无法显示为ascii字符的字节，用\x##表示

# encode() = 将字符串编码为bytes类型，默认为utf-8编码
# decode() = 将bytes类型解码为字符串

# 编码 - encode() => 将xxx编码格式的字符串转变成bytes类型
# 纯英文的字符串用ascii编码为bytes类型
by = 'ABC'.encode('ascii')
print(by)               # b'ABC'
# 含有中文的字符串用utf-8编码为bytes类型
by = '空前'.encode('utf-8')
print(by)               # b'\xe7\xa9\xba\xe5\x89\x8d'
by = '空前'.encode('gbk')
print(by)               # b'\xbf\xd5\xc7\xb0'

# --------------------------------------------

# 解码 - decode() => 将bytes类型还原成原先xxx编码格式的字符串
st = b'ABC'.decode('ascii')
print(st)               # ABC
st = b'\xe7\xa9\xba\xe5\x89\x8d'.decode('utf-8')
print(st)               # 空前
st = b'\xbf\xd5\xc7\xb0'.decode('gbk')
print(st)               # 空前

print('=' * 30)

# ==============================================
# len() = 计算字符串中的字符个数，若为bytes类型，则为字节数
le = len('ABC')
print(le)               # 3
le = len(b'ABC')
print(le)               # 3
le = len('空前')
print(le)               # 2
le = len('空前'.encode('utf-8'))
print(le)               # 6

print('=' * 30)











