#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 15:53
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_函数的参数.py
# @Software: PyCharm

# 定义2数相加的函数, 头通过参数接收被计算的2个数字
def add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")

# 调用函数, 传入被计算的2个数字
add(2, 3)