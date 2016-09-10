#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入SQLite数据库驱动
import sqlite3
import os


# 判断是否已经存在同路径下的文件，若存在则直接删除
db_file = os.path.join(os.path.dirname(__file__), 'sqlite3_test.db')
if os.path.isfile(db_file):
    os.remove(db_file)


def init_db():
    # 连接到SQLite数据库
    # 数据库文件为sqlite3_test.db
    # 若文件不存在，会自动在当前目录创建
    global db_file
    conn = sqlite3.connect(db_file)

    # 创建一个游标Cursor对象，用于执行SQL操作
    cursor = conn.cursor()

    # 使用Cursor对象的execute()方法来执行创建user表的SQL操作
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20), score int)')

    # 执行一条SQL语句，插入一条记录
    # cursor.execute(r"insert into user (id, name, score) values ('A-001', 'Adam', 95)")
    # cursor.execute(r"insert into user (id, name, score) values ('A-002', 'Bart', 62)")
    # cursor.execute(r"insert into user (id, name, score) values ('A-003', 'Lisa', 78)")

    # 同时插入多行记录
    users = [('A-001', 'Adam', 95),
             ('A-002', 'Bart', 62),
             ('A-003', 'Lisa', 78)]
    cursor.executemany('insert into user values (?,?,?)', users)

    # 执行查询语句
    # cursor.execute('select * from user where id=?', ('A-001',))

    # values = cursor.fetchall()        # 获取查询结果集

    # 打印查询结果，结果集是一个list，每个元素都是一个tuple，对应一行记录。
    # print(values)           # [('1', 'Michael')]

    # print(cursor.rowcount)    # 通过rowcount获得插入的行数

    cursor.close()          # 关闭游标Cursor
    conn.commit()           # 提交事务，在执行插入等操作时需要进行提交
    conn.close()            # 关闭连接Connection


def get_score_in(low, high):
    """ 返回指定分数区间的名字，按分数从低到高排序 """
    global db_file
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(r"select * from user")
    values = cursor.fetchall()                               # 1. 获取所有原始排列的数据
    cursor.close()
    conn.close()
    values = [t for t in values if low <= t[2] <= high]     # 2. 筛选出所需要的区间的数据
    values = sorted(values, key=lambda t: t[2])             # 3. 按分数从低到高排序出路
    values = [t[1] for t in values]                         # 4. 将排序后的数据中的名字重新组成一个新的列表数据
    return values                                           # 5. 返回排序的名字列表


def get_score_in2(low, high):
    """ 返回指定分数区间的名字，按分数从低到高排序 """
    global db_file
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        cursor.execute(r"select name from user where score >= ? and score <= ? order by score", (low, high))
        values = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return [t[0] for t in values]


# 测试:
init_db()

assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

assert get_score_in2(80, 95) == ['Adam'], get_score_in2(80, 95)
assert get_score_in2(60, 80) == ['Bart', 'Lisa'], get_score_in2(60, 80)
assert get_score_in2(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in2(60, 100)

print('Pass')
















