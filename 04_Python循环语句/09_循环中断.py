#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 15:06
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 09_循环中断.py
# @Software: PyCharm
# 演示循环中断语句, continue
# for i in range(1, 6):
#     print("语句1")
#     continue
#     print("语句2")

# 演示continue的嵌套应用
# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")

# 演示循环中断 break 语句
# for i in range(1, 101):
#     print("语句1")
#     break
#     print("语句2")
#
# print("语句3")

# 演示 break 的嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        break
        print("语句3")
    print("语句4")