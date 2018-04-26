#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver

# open a new Firefox browser
browser = webdriver.Firefox()

# load the page at the given URL
browser.get("http://shellever.com")

print(browser.title)     # Shellever - make it better


elements_desc = browser.find_elements_by_class_name('description')
for element in elements_desc:
    print(element.tag_name)
    #print(element.text)

browser.quit()

'''
Traceback (most recent call last):
  File "D:\devsoft\Python\Python36\lib\site-packages\selenium\webdriver\common\service.py", line 76, in start
    stdin=PIPE)
  File "D:\devsoft\Python\Python36\lib\subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "D:\devsoft\Python\Python36\lib\subprocess.py", line 997, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] The system cannot find the file specified

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:/workspace/PycharmProjects/Basics/thirdparty/selenium/selenium-get.py", line 5, in <module>
    driver = webdriver.Firefox()
  File "D:\devsoft\Python\Python36\lib\site-packages\selenium\webdriver\firefox\webdriver.py", line 152, in __init__
    self.service.start()
  File "D:\devsoft\Python\Python36\lib\site-packages\selenium\webdriver\common\service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 
'''
