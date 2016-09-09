#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import aiomysql
from webapp.www.logd import logd


__pool = None


# ========================================================================
# 数据库操作工具集

# 创建全局连接池__pool，缺省情况下将编码设置为utf8，自动提交事务
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],                        # mysql
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


# Select
# SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。
# 注意要始终坚持使用带参数的SQL，而非拼接SQL字符串，以防止SQL注入攻击。
# yield from将调用一个子协程(即在一个协程中调用另一个协程)并直接获得子协程的返回结果。
# 若传入size参数，就通过fetchmany()获取最多指定数量的记录，否则通过fetchall()获取所有记录。
async def select(sql, args, size=None):
    logging.info('SQL: %s' % sql)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs


# Insert/Update/Delete
# 这3种SQL的执行都需要相同的参数，以及返回一个整数表示影响的行数
async def execute(sql, args, autocommit=True):
    logging.info('SQL: %s' % sql)
    global __pool
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException:
            if not autocommit:
                await conn.rollback()
            raise
        return affected


# ========================================================================
# ORM
# 设计ORM需要从上层调用者角度来设计。

def create_args_string(num):
    lst = []
    for n in range(num):
        lst.append('?')
    return ', '.join(lst)


class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)


# 创建基类Model的元类
# 任何继承自Model的类(如User)，会自动通过ModelMetaclass扫描映射关系，
# 并存储到自身的类属性如__table__和__mappings__中。
class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        if name == 'Model':     # 排除Mode类本身
            return type.__new__(mcs, name, bases, attrs)
        table_name = attrs.get('__table__', None) or name   # 获取table名称
        logging.info('found model: %s (table: %s)' % (name, table_name))
        # 获取所有的Field和主键名
        mappings = dict()
        fields = []
        primary_key = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v         # 保存映射关系
                if v.primary_key:
                    if primary_key:    # 当第二次查找到主键时抛出Error
                        raise RuntimeError('Duplicate primary key for field: %s' % k)
                    primary_key = k     # 保存第一次找到的主键
                else:
                    fields.append(k)    # 将非主键的字段保存到fields中
        if not primary_key:
            raise RuntimeError('Primary key not found.')        # StandardError在Python3中被移除
        for k in mappings.keys():       # 移除类属性
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))

        # 构造默认的select/insert/update/delete语句
        sql_select = 'select `%s`, %s from `%s`' % \
                     (primary_key, ', '.join(escaped_fields), table_name)
        sql_insert = 'insert into `%s` (%s, `%s`) values (%s)' % \
                     (table_name, ', '.join(escaped_fields), primary_key, create_args_string(len(escaped_fields) + 1))
        sql_update = 'update `%s` set %s where `%s`=?' % \
                     (table_name, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primary_key)
        sql_delete = 'delete from `%s` where `%s`=?' % \
                     (table_name, primary_key)
        attrs['__mappings__'] = mappings            # 保存属性和列的映射关系
        attrs['__table__'] = table_name             # 表名
        attrs['__primary_key__'] = primary_key      # 主键属性名
        attrs['__fields__'] = fields                # 除主键外的属性名
        attrs['__select__'] = sql_select
        attrs['__insert__'] = sql_insert
        attrs['__update__'] = sql_update
        attrs['__delete__'] = sql_delete
        return type.__new__(mcs, name, bases, attrs)


# 定义所有ORM映射的基类Model
# 继承自dict的Model具备所有dict的功能，同时又实现__getattr__()和__setattr__()方法，
# 可以使用print(user.id)的方法直接引用属性
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getvalue(self, key):
        return getattr(self, key, None)

    def getvalueordefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default   # ??
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod
    async def findall(cls, where=None, args=None, **kw):
        """find objects by where clause"""
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        order_by = kw.get('orderBy', None)
        if order_by:
            sql.append('order by')
            sql.append(order_by)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit values: %s' % str(limit))
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findnum(cls, select_field, where=None, args=None):
        """find number by select_field and where"""
        sql = ['select %s _num_ from `%s`' % (select_field, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        """find object by primary key"""
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getvalueordefault, self.__fields__))
        args.append(self.getvalueordefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warning('failed to insert record: affected rows: %s' % rows)    # logging.warn已过时

    async def update(self):
        args = list(map(self.getvalue, self.__fields__))
        args.append(self.getvalue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warning('failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getvalue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warning('failed to remove by primary key: affected rows: %s' % rows)


















