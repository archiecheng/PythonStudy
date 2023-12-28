#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 21:31
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_if_elif_else语句的使用.py
# @Software: PyCharm

# print("欢迎来到黑马动物园")
# height = int(input("请输入你的身高(cm): "))
# vip_level = int(input("请输入您的VIP登记(1-5):"))
# day = int(input("请告诉我今天几号:"))
# if height < 120:
#     print("您的身高未超出120cm, 可以免费游玩")
# elif vip_level > 3:
#     print("vip 级别大于3, 可以免费")
# elif day == 1:
#     print("今天是1号免费日, 可以免费")
# else:
#     print("不好意思, 条件都不满足, 游玩需要购票10元")




print("欢迎来到黑马动物园")
if int(input("请输入你的身高(cm): ")) < 120:
    print("您的身高未超出120cm, 可以免费游玩")
elif int(input("请输入您的VIP登记(1-5):")) > 3:
    print("vip 级别大于3, 可以免费")
elif int(input("请输入您的VIP登记(1-5):")) == 1:
    print("今天是1号免费日, 可以免费")
else:
    print("不好意思, 条件都不满足, 游玩需要购票10元")