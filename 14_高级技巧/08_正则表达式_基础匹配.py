#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/8 11:48
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 08_正则表达式_基础匹配.py
# @Software: PyCharm
import re

s = "1python itheima python python"
# match 从头匹配
result = re.match("python", s)
print(result)
# print(result.span())
# print(result.group())
# search 搜索匹配
result = re.search("python", s)
print(result)
# findall 搜索全部匹配
result = re.findall("pthon", s)
print(result)