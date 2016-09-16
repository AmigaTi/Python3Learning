#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib


# ====================================================================
# MD5
# 生成结果：固定的128 bits (16 bytes)，通常用一个32位的16进制字符串表示

# 计算一个字符串的MD5值
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())  # d26a53750bc40b38b65a520292f69306
print(md5.digest_size)  # 16 (bytes)
print(md5.block_size)   # 64 (bytes)

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())  # d26a53750bc40b38b65a520292f69306


# ====================================================================
# SHA1
# 生成结果：固定的160 bits (20 bytes)，通常用一个40位的16进制字符串表示
# 比SHA1更安全的算法是SHA256和SHA512，
# 不过越安全的算法不仅越慢，而且摘要长度更长。

# 计算一个字符串的SHA1值
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())     # 2c76b57293ce30acef38d98f6046927161b46a44
print(sha1.digest_size)     # 20 (bytes)
print('---------------------------------')

print('register-----------------------')
sha1 = hashlib.sha1()
sha1.update('hellome@163.com:hellome@7'.encode('utf-8'))
print(sha1.hexdigest() == '6496432b3fb78e671ab62ba675862a4b493ab61e')     # 6496432b3fb78e671ab62ba675862a4b493ab61e


# ====================================================================
# 1. 存储用户名和MD5加密口令的数据库登录验证实例

# 存储用户名和明文口令的数据库
db = {
    'hellome': 'hellome#74',
    'asap': 'asap#42',
    'sugar': 'sugar#53'
}


# 存储用户名和MD5加密口令的数据库
db_md5 = {
    'hellome': 'b85b50ca0982f00a95bbd68813ef1886',
    'asap': 'fc500dd6ac5d2b122f652a9d935584b6',
    'sugar': '268a9bc26fbebecb9d5eb6ec5e4d1613'
}


# 根据用户输入的口令，计算出存储在数据库中的MD5口令
def calc_md5(key_str):
    _md5 = hashlib.md5()
    _md5.update(key_str.encode('utf-8'))
    return _md5.hexdigest()


# 初始化数据库
# print(calc_md5('hellome#74'))    # b85b50ca0982f00a95bbd68813ef1886
# print(calc_md5('asap#42'))       # fc500dd6ac5d2b122f652a9d935584b6
# print(calc_md5('sugar#53'))      # 268a9bc26fbebecb9d5eb6ec5e4d1613


# 验证用户登录
# 根据用户输入的口令是否正确，返回True或False
def login(username, password):
    if username in db_md5 and calc_md5(password) == db_md5[username]:
        return True
    return False

# testing
flag = login('hellome', 'hellome#74')
if flag is True:
    print('Login successfully...')
else:
    print('Incorrect username or password')
'''
Login successfully...
'''


