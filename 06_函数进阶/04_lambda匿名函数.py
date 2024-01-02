#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 21:10
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_lambda匿名函数.py
# @Software: PyCharm

# 定义一个函数, 接受其他函数输入
def test_func(compute):
    result = compute(1, 2)
    print(f"结果是:{result}")

test_func(lambda x, y: x + y)