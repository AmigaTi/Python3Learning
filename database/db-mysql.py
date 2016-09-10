#!/usr/bin/python
# -*- coding: utf-8 -*-

# =============================
# Environment Preview
# System: Windows 7 x86
# IDE: PyCharm Community Edition 2016.2.1
# SQL: mysql-5.6.32-win32.zip   => ../bin/mysqld.exe => FIRST STEP
# Driver: mysql-connector-python-rf
# ../Python35/Scripts> pip -V       # pip 8.1.2
# ../Python35/Scripts> pip install --upgrade pip
# ../Python35/Scripts> pip install --upgrade wheel
# ../Python35/Scripts> pip install mysql-connector-python-rf
# =============================

# =============================
# modify the MySQL server root password
# ../bin> mysqladmin -u root password "root@42"

# login to MySQL server with root user
# ../bin> mysql -u root -p

# check the encoding
# mysql> show variables like '%char%';
# =============================

# 导入MySQL驱动
import mysql.connector


# 创建连接，pysql - MySQL for Python operation
conn = mysql.connector.connect(user='root', password='root@42', database='pysql')
cursor = conn.cursor()

# 创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，MySQL的占位符为%s
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
row_count = cursor.rowcount
conn.commit()       # 提交事务
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)           # [('1', 'Michael')]
cursor.close()
conn.close()




