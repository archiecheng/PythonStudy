#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 21:10
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_函数作为参数传递.py
# @Software: PyCharm

# 定义一个函数, 接收另一个函数作为传入参数

def test_func(compute):
    result = compute(1,2) # 确定 compute 是函数
    print(f"compute参数的类型是:{type(compute)}")
    print(f"计算结果: {result}")

# 定义一个函数, 准备作为参数传入另一个函数
def compute(x, y):
    return x + y

# 调用, 并传入函数
test_func(compute)