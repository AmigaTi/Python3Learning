#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

# 针对日常的文件和目录管理任务，shutil模块提供了一个易于使用的高级接口
# os模块提供了对目录或者文件的新建/删除/查看文件属性，还提供了对文件以及目录的路径操作。
# shutil模块是对os模块中文件操作的补充：移动 复制  打包 压缩 解压。

# 复制文件内容到另一个文件，可以copy指定大小的内容
# copyfileobj(fsrc, fdst, length=16*1024)
# fsrc和fdst都是文件对象，都需要打开后才能进行复制操作
src_file = open('firstme.txt', 'r')
dst_file = open('copytest/copyfileobj.txt', 'w+')
shutil.copyfileobj(src_file, dst_file)      # 使用默认length

# 复制文件内容到另外一个文件，不需要手动打开文件
# copyfile(src, dst, *, follow_symlinks=True)
shutil.copyfile('firstme.txt', 'copytest/copyfile.txt')

# 仅复制权限(rwx)，不更改文件内容、所属组和用户
# copymode(src, dst, *, follow_symlinks=True)
# 目标文件必须存在，否则会包如下错误：
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'copymode.txt'
# shutil.copymode('firstme.txt', 'copymode.txt')

# 复制所有的状态信息，包括权限，组，用户，时间等
# copystat(src, dst, *, follow_symlinks=True)

# 复制文件的内容以及权限，先copyfile后copymode
# copy(src, dst, *, follow_symlinks=True)

# 复制文件的内容以及文件的所有状态信息。先copyfile后copystat
# copy2(src, dst, *, follow_symlinks=True)

# 递归的复制文件内容及状态信息
# copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)
if os.path.exists('copytree'):
    shutil.rmtree('copytree')
shutil.copytree('copytest', 'copytree')

# 递归地删除文件
# rmtree(path, ignore_errors=False, onerror=None)
# shutil.rmtree('copytree')

# 递归的移动文件
# move(src, dst, copy_function=copy2)

# 压缩打包
# make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)
# base_name - 压缩打包后的文件名或者路径名
# format    - 压缩或者打包格式 "zip", "tar", "bztar", "gztar" or "xztar"
# root_dir  - 将哪个目录或者文件打包（也就是源文件）
shutil.make_archive('copytest-archive', 'gztar', root_dir='copytest')
