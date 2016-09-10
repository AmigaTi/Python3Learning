#!/usr/bin/python
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, _name):
        self.name = _name

    def intro(self):
        print('hello, my name is %s. I\'m a student.' % self.name)


stu = Student('curry')
print(stu.__dict__)         # 存储成员信息


'''
{'name': 'curry'}
'''


# =====================================================================
class Person(object):
    def __init__(self, _obj):
        self.__dict__.update(_obj)

    def __str__(self):
        return str(self.__dict__)

obj = {
    'name': 'curry',
    'age': 18,
    'gender': 'female',
    'email': 'curry@curry.com',
    'country': 'us'
}

person = Person(obj)
print(person)
print('name: %s' % person.name)

'''
{'age': 18, 'name': 'curry', 'gender': 'female', 'country': 'us', 'email': 'curry@curry.com'}
name: curry
'''


















