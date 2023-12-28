#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 15:58
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 07_Python中的运算符.py
# @Software: PyCharm

"""
演示Python中的各类运算符
"""

# 算数运算符
print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("3 * 3 = ", 3 * 3)
print("4 / 2 = ", 4 / 2)
print("11 / 2 = ", 11 // 2) # 求整数
print("9 % 2 = ", 9 % 2)
print("2 ** 2 = ", 2 ** 2) # 求平方

# 赋值运算符
num = 1 + 2 * 3

# 复合赋值运算符
# +=
num = 1
num += 1 # num = num + 1
print("num += 1: ", num)
num -= 1
print("num -= 1: ", num)
num *=4
print("num *= 4: ", num)
num /= 2
print("num /=2:", num)
num = 3
num %= 2
print("num %% 2: ", num)

num **= 2
print("num ** 2: ", num)

num = 9
num //= 2
print("num // 2: ", num)

