#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='simple',
    version='0.1.0',
    description='simple package tests',
    author='shellever',
    author_email='shellever@163.com',
    maintainer='shellever',
    maintainer_email='shellever@163.com',
    url='http://shellever.com',
    long_description=README,
    # long_description_content_type="text/markdown",
    license='MIT License',
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# packaging this module
# dist/simple-0.1.0.tar.gz
# python setup.py sdist

