#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 21:09
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 01_函数的多返回值.py
# @Software: PyCharm

# 演示多个变量, 接收多个返回值
def test_return():
    return 1, 2, 3

x, y, z = test_return()
print(x)
print(y)
print(z)