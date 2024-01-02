#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 16:01
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 05_函数的参数练习案例.py
# @Software: PyCharm

# 定义函数, 接收1个形式参数, 数字类型，表示体温
def check(num):
    # 在函数体重判断体温
    print("欢迎来到黑马程序员! 请出示您的健康码以及72小时核酸证明，并配合测量体温!")
    if num <= 37.5:
        print(f"体温测量中, 您的体温是: {num}度, 体温正常请进!")
    else:
        print(f"体温测量中, 您的体温是: {num}度, 体温正常请进!")

# 调用函数, 传入实际参数
check(37.6)