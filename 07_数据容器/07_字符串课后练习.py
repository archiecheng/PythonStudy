#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 12:44
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 07_字符串课后练习.py
# @Software: PyCharm
my_str = "itheima itcast boxuegu"

count = my_str.count("it")
print(count)
replace_my_str = my_str.replace(" ", "|")
print(replace_my_str)
new_my_str = replace_my_str.split("|")
print(new_my_str)