#!/usr/bin/python
# -*- coding: utf-8 -*-


# MixIn: 多重继承
# 目的：给一个类增加多个功能

class Animal(object):
    pass


class Mammal(object):
    pass


class RunnableMixIn(object):
    pass


class CarnivorousMinIn(object):
    pass


class Dog(Mammal, RunnableMixIn, CarnivorousMinIn):
    pass

