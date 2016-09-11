#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import aiomysql


logging.basicConfig(level=logging.INFO)

__pool = None


def log(sql, args=None):
    logging.info('SQL: [%s] args: %s' % (sql, args or []))


# ========================================================================
# 数据库操作工具集


# 创建全局连接池__pool，缺省情况下将编码设置为utf8，自动提交事务
# 每个HTTP请求都可以从连接池中直接获取数据库连接，而不必频繁地打开和关闭数据库连接
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    # 创建一个MySQL数据库连接池 (coroutine)
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],                    # 初始化时必须指定，因为没有提供默认值
        password=kw['password'],            # 初始化时必须指定，因为没有提供默认值
        db=kw['db'],                        # 初始化时必须指定，因为没有提供默认值
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


# Select
# SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。
# 注意要始终坚持使用带参数的SQL，而非拼接SQL字符串，以防止SQL注入攻击。
# await将调用一个子协程(即在一个协程中调用另一个协程)并直接获得子协程的返回结果。
# 若传入size参数，就通过fetchmany()获取最多指定数量的记录，否则通过fetchall()获取所有记录。
async def select(sql, args, size=None):
    log(sql, args)
    # 异步等待连接池对象返回可以连接线程，with语句则封装了清理（关闭conn）和处理异常的工作
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args)     # 将sql中的'?'替换为'%s'，因为mysql语句中的占位符为%s
            if size:
                results = await cur.fetchmany(size)             # 从数据库获取指定的行数
            else:
                results = await cur.fetchall()                  # 返回所有的结果集
        logging.info('rows returned: %s' % len(results))
        return results


# 用于SQL的Insert/Update/Delete语句，只返回影响的操作行数
async def execute(sql, args, autocommit=True):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        if not autocommit:              # 若数据库的事务为非自动提交的,则调用协程启动连接
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:    # 打开DictCursor,不同于普通游标,以dict形式返回结果
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount  # 返回受影响的行数
            if not autocommit:          # 同上, 事务非自动提交型的,手动调用协程提交增删改事务
                await conn.commit()
        except BaseException as e:
            if not autocommit:          # 出错, 回滚事务到增删改之前
                await conn.rollback()
            raise e
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


# DDL - Data Definition Language - 数据定义语言
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

# 这是一个元类,它定义了如何来构造一个类,任何定义了__metaclass__属性或指定了metaclass的都会通过元类定义的构造方法构造类
# 任何继承自Model的类,都会自动通过ModelMetaclass扫描映射关系,并存储到自身的类属性
class ModelMetaclass(type):
    # cls: 当前准备创建的类对象,相当于self
    # name: 类名,比如User继承自Model,当使用该元类创建User类时,name=User
    # bases: 父类的元组
    # attrs: 属性(方法)的字典,比如User有__table__,id,等,就作为attrs的keys
    # 排除Model类本身,因为Model类主要就是用来被继承的,其不存在与数据库表的映射
    def __new__(mcs, name, bases, attrs):
        if name == 'Model':     # 排除Mode类本身
            return type.__new__(mcs, name, bases, attrs)
        # 找到表名，若没有定义__table__属性,将类名作为表名
        table = attrs.get('__table__', name)
        logging.info('found model: %s (table: %s)' % (name, table))
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
        # 使用反引号是为了防止关键字冲突：
        # select * from `select`;
        sql_select = 'select `%s`, %s from `%s`' % \
                     (primary_key, ', '.join(escaped_fields), table)
        sql_insert = 'insert into `%s` (%s, `%s`) values (%s)' % \
                     (table, ', '.join(escaped_fields), primary_key, create_args_string(len(escaped_fields) + 1))
        sql_update = 'update `%s` set %s where `%s`=?' % \
                     (table, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primary_key)
        sql_delete = 'delete from `%s` where `%s`=?' % \
                     (table, primary_key)
        attrs['__mappings__'] = mappings            # 保存属性和列的映射关系
        attrs['__table__'] = table                  # 表名
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
    # 初始化函数,调用其父类(dict)的方法
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    # 增加__getattr__方法，使获取属性更加简单,即可通过"a.b"的形式
    # __getattr__ 当调用不存在的属性时，python解释器会试图调用__getattr__(self,'attr')来尝试获得属性
    # 例如b属性不存在，当调用a.b时python会试图调用__getattr__(self,'b')来获得属性，在这里返回的是dict a[b]对应的值
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    # 增加__setattr__方法,使设置属性更方便,可通过"a.b=c"的形式
    def __setattr__(self, key, value):
        self[key] = value

    def getvalue(self, key):
        return getattr(self, key, None)

    # 通过键取值,若值不存在,则取默认值
    def getvalueordefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                # 如果field.default可被调用，则返回field.default()，否则返回field.default
                value = field.default() if callable(field.default) else field.default   # ??
                logging.debug('using default value for %s: %s' % (key, str(value)))
                # 通过default取到值之后再将其作为当前值
                setattr(self, key, value)
        return value

    # classmethod装饰器将方法定义为类方法
    # 对于查询相关的操作,我们都定义为类方法,就可以方便查询,而不必先创建实例再查询
    # 查找所有合乎条件的信息
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

    # 根据列名和条件查看数据库有多少条信息
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

    # 根据主键查找一个实例的信息
    @classmethod
    async def find(cls, pk):
        """find object by primary key"""
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])
        # return cls(**rs[0]) if rs else None

    # 把一个实例保存到数据库
    async def save(self):
        args = list(map(self.getvalueordefault, self.__fields__))
        args.append(self.getvalueordefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warning('failed to insert record: affected rows: %s' % rows)    # logging.warn已过时

    # 更改一个实例在数据库的信息
    async def update(self):
        args = list(map(self.getvalue, self.__fields__))
        args.append(self.getvalue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warning('failed to update by primary key: affected rows: %s' % rows)

    # 把一个实例从数据库中删除
    async def remove(self):
        args = [self.getvalue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warning('failed to remove by primary key: affected rows: %s' % rows)


















