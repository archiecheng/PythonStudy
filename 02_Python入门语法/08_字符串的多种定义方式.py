#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 16:13
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 08_字符串的多种定义方式.py
# @Software: PyCharm

# 单引号定义法, 使用单引号进行包围

name = '黑马程序员'
print(type(name))
# 双引号定义法

name = "黑马程序员"
print(type(name))
# 三引号定义法, 写法和多行注释是一样的

name = """
我是programmer
"""
print(type(name))

# 在字符串内 包含双引号

name = '"黑马程序员"'

# 在字符串内 包含单引号

name = "'黑马程序员'"

# 使用转义字符 \ 解除引号的效用

name = "\"黑马程序员\""

