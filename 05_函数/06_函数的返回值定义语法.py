#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 18:19
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 06_函数的返回值定义语法.py
# @Software: PyCharm

# 定义一个函数, 完成2数相加的功能
def add(a, b):
    result = a + b
    # 通过返回值, 将相加的结果返回给使用者
    return result
    # 返回结果后, 还想输出一句话
    # print("我完事了")

# 函数的返回值, 可以通过变量去接收
r = add(1,2)
print(r)