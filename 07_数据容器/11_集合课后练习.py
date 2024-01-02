#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 12:47
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 11_集合课后练习.py
# @Software: PyCharm

my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客','itheima', 'itcast', 'itheima', 'itcast', 'best']

# 定义一个空集合
my_set = set()

# 通过 for 循环遍历而来

for element in my_list:
    my_set.add(element)

print(my_list)
print(my_set)