#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 21:27
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_2_我要买票吗练习题.py
# @Software: PyCharm

print("欢迎来到黑马动物园")
height = int(input("请输入你的身高(cm): "))
if height > 120:
    print("您的身高超出120cm, 游玩需要购票10元")
else:
    print("您的身高未超出120cm, 可以免费游玩")

print("祝您游玩愉快")