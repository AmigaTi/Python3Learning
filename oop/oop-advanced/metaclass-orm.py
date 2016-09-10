#!/usr/bin/python
# -*- coding: utf-8 -*-

is_debug = True
# is_debug = False


def logd(*obj):
    if is_debug:
        print(*obj)


# ORM - Object Relational Mapping - 对象-关系映射
# 把关系数据库的一行映射为一个对象，即一个类对应一个表，
# 这样写代码更简单，不用直接操作SQL语句。

# ORM框架编写

# 2. 定义Field类，负责保存数据库表的字段名和字段类型
# super(subclass, objectB)理解：
# 首先找到subclass的父类objectA，然后把对象objectB转换为父类的对象，
# 最后调用父类的方法

class Field(object):
    def __init__(self, name, col_type):
        self.name = name
        self.col_type = col_type
        logd('call Field.__init__(%s, %s)' % (name, col_type))

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
        logd('call StringField.__init__(%s)' % name)


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
        logd('call IntegerField.__init__(%s)' % name)


# 3. 编写最复杂的ModelMetaclass
# 在ModelMetaclass中，一共做了几件事情：
# > 排除掉对Model类的修改
# > 在当前类(比如User)中查找定义的类的所有属性，如果找到一个Field属性，
#  就把其保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，
#  否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）
# > 把表名保存到__table__中，表名默认为类名

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        logd('call ModelMetaclass.__new__({0}, {1}, {2}, {3})'.format(cls.__name__, name, bases, attrs))
        if name == 'Model':                 # 若为Model类，直接调用type创建，而不进行附加操作
            logd('exit ModelMetaclass.__new__(%s, %s) quickly' % (cls.__name__, name))
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)     # User类
        mappings = dict()
        for k, v in attrs.items():         # 类属性
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)                    # 删除类属性中的Field属性
        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name           # 假设表名和类名一致
        logd('(__mappings__, __table__) = (%s, %s)' % (str(mappings), name))
        logd('exit ModelMetaclass.__new__(%s, %s)' % (cls.__name__, name))
        return type.__new__(cls, name, bases, attrs)


# 4. 编写基类Model - 继承自dict，并指定创建类的模板
# 在Model类中，定义各种操作数据库的方法：
# save()/delete()/find()/update()/..

# 实现了save()方法，把一个实例保存到数据库中。
# 因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
        logd('call Model.__init__(%s)' % str(kw))  # 打印字典参数

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):     # 当子类User的实例对象调用此方法时，self为子类实例对象，拥有self.__mappings__属性
        logd('call Model.save()')
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():      # self.__mappings__属性由元类创建
            fields.append(v.name)           # Field.name
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))       # 打印列表参数
        logd('exit Model.save()')


# 1. 编写调用接口：定义一个User类来操作对应的数据库表User
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，
# 而save()由metaclass自动完成。
# 虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。

# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中
# 查找metaclass，如果没有找到，就继续在父类Model中查找metaclass，
# 找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，
# 即metaclass可以隐式地继承到子类，但子类自己却感觉不到。

# 初始化实例对象时，若自身类没有定义__init__()方法就用父类的__init__()方法

class User(Model):
    # 定义类属性到列的映射(attrs)
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('mail')
    password = StringField('password')


# 创建一个实例
logd('start to create a User instance >>>')
u = User(id=1, name='Tom', email='tom@hello.com', password='tom@3')
logd('completely create a User instance')

# 出错原因：在使用父类的元类创建此类时，添加了附件操作，将类属性删除了
# print(User.id)          # AttributeError: type object 'User' has no attribute 'id'

# 保存到数据库
u.save()


'''
# log ORM
Found model: User
Found mapping: name ==> <StringField:username>
Found mapping: password ==> <StringField:password>
Found mapping: mail ==> <StringField:mail>
Found mapping: id ==> <IntegerField:id>
SQL: insert into User (username,mail,password,id) values (?,?,?,?)
ARGS: ['Tom', 'tom@hello.com', 'tom@3', 1]
'''
