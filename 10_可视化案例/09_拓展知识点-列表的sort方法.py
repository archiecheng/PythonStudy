#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/4 21:12
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 09_拓展知识点-列表的sort方法.py
# @Software: PyCharm

# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]

# 排序, 基于带名函数
def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key, reverse=True)

# 排序, 基于lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)

print(my_list)
