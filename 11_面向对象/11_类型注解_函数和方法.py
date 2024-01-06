#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:36
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 11_类型注解_函数和方法.py
# @Software: PyCharm

# 对形参进行类型注释
def add(x: int, y: int):
    return x + y

# 对返回值进行类型注解
def func(data: list) -> list:
    return data