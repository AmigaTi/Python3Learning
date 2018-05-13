#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

'''
selenium - PyPi
https://pypi.org/project/selenium/

实现一个集成unittest.TestCase的类TestStringMethods，
使用unittest.main()来测试该类中所有以test开头的测试用例

简单的assert方法有如下：
self.assertEquals(100, value)
self.assertTrue(value == 0)
self.assertFalse(value > 0
self.assertRaises(TypeError, value.convert_to_decimal)

在写测试用例的时候尽量使用assertEquals而不是assertTrue、assertFalse，
当assertEquals失败的时候，会打印出比较的两方值更直观。

self.fail([msg])会无条件的导致测试失败，不推荐使用。

每次运行test方法时，先用setUp初始化程序，然后运行test方法，最后使用tearDown清理程序
'''


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print("setUp()...")

    def tearDown(self):
        print("tearDown()...")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

'''
setUp()...
tearDown()...
setUp()...
tearDown()...
setUp()...
tearDown()...
'''