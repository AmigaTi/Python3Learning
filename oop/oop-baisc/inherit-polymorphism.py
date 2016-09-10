#!/usr/bin/python
# -*- coding: utf-8 -*-


# 父类
class Animal(object):
    def run(self):
        print('Animal is running...')


# 子类Dog直接从Animal继承
class Dog(Animal):
    def run(self):
        print('Dog is running...')


# 子类Cat直接从Animal继承
class Cat(Animal):
    def run(self):
        print('Cat is running...')


animal = Animal()
animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(animal, object))
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
print(isinstance(dog, Dog))
print(isinstance(cat, Cat))
print(isinstance(animal, Dog))
print(isinstance(animal, Cat))


# 通用工具类
class Runner(object):
    def __init__(self, _animal):
        self.__animal = _animal

    def run(self):
        self.__animal.run()

runner = Runner(Animal())
runner.run()
runner = Runner(Dog())
runner.run()
runner = Runner(Cat())
runner.run()


# 子类Tortoise直接从Animal继承
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

runner = Runner(Tortoise())
runner.run()

'''
Animal is running...
Dog is running...
Cat is running...
True
True
True
True
True
False
False
Animal is running...
Dog is running...
Cat is running...
Tortoise is running slowly...
'''
