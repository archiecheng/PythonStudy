#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 21:48
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_2_猜猜心里数字练习题.py
# @Software: PyCharm

num = 5
if int(input("请输入第一次猜想的数字: ")) == num:
    print("恭喜第一次就猜对了呢")
elif int(input("猜错了, 再猜一次: ")) == num:
    print("猜对了")
elif int(input("猜错了, 再猜一次: ")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("Sorry 猜错了")
