#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver


# Selenium WebDriver is often used as a basis for testing web application.
class ShelleverTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.shellever.com')
        self.assertIn('Shellever', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
Testing started at 00:41 ...
D:\devsoft\Python\Python36\python.exe "D:\devsoft\PyCharm Community Edition 2017.3.4\helpers\pycharm\_jb_unittest_runner.py" --path D:/workspace/PycharmProjects/Basics/thirdparty/selenium/selenium-unittest.py
Launching unittests with arguments python -m unittest D:/workspace/PycharmProjects/Basics/thirdparty/selenium/selenium-unittest.py in D:\workspace\PycharmProjects\Basics\thirdparty\selenium


Ran 1 test in 33.238s

OK
'''