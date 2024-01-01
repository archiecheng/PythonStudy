#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 13:38
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 05_2_for循环练习题-数一数有几个a.py
# @Software: PyCharm

str = "itheima is a brand of itcast"
count = 0
for c in str:
    if c == 'a':
        count += 1

print(f"字符串中a的个数是:{count}")