#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib

# md52salt -> md5 2salt -> md5 @salt -> md5 add salt

# ====================================================================
# 2. 存储用户名和更安全(加盐)MD5加密口令的数据库登录验证实例

# 存储用户名和更安全(加盐)MD5加密口令的数据库
db2 = {}
salt = '@salt'


def get_md5(key_str):
    key_md5 = hashlib.md5()
    key_md5.update(key_str.encode('utf-8'))
    return key_md5.hexdigest()


def register(username, password):
    db2[username] = get_md5(password + username + salt)


def login2(username, password):
    if username in db2 and get_md5(password + username + salt) == db2[username]:
        return True
    return False


def db2_init():
    register('hellome', 'hellome#74')
    register('candy', 'candy#53')
    register('todoso', 'todoso#63')


def welcome():
    print(u"""
# ----------------------------------------
# Welcome to User login interface
# Author: linuxforshine
# Note: ONLY to login with signed username
# ----------------------------------------""")
    print('initialize database...')
    db2_init()
    print('completely...')
    while True:
        flag2 = input('start to login? (Y or N to exit): ')
        if flag2 == 'N':
            print('exited login interface.')
            break
        elif flag2 != 'Y':
            print('please enter the right choice again.')
            continue

        username = input('username: ')
        password = input('password: ')
        flag2 = login2(username, password)
        if flag2 is True:
            print('login successfully...')
            # break
        else:
            print('incorrect username or password.')


if __name__ == '__main__':
    welcome()


'''
# ----------------------------------------
# Welcome to User login interface
# Author: linuxforshine
# Note: ONLY to login with signed username
# ----------------------------------------
initialize database...
completely...
start to login? (Y or N to exit): Y
username: hellome
password: hellome#74
login successfully...
start to login? (Y or N to exit): N
exited login interface.
'''