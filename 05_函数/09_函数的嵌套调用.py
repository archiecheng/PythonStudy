#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 18:45
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 09_函数的嵌套调用.py
# @Software: PyCharm

# 定义函数 func_b
def func_b():
    print("---2---")

# 定义函数 func_a, 并在函数内部调用fuc_b
def func_a():
    print("---1---")
    func_b()
    print("---3---")

func_a()