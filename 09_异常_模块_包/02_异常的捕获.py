#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 16:55
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 02_异常的捕获.py
# @Software: PyCharm

# 基本捕获语法
# try:
#     f = open("D:/abc.txt", "r", encoding="utf-8")
# except:
#     print("出现异常了, 因为文件不存在, 我将open的模式改为w模式去打开")
#     f = open("D:/abc.txt", "w", encoding="utf-8")

# 捕获指定的异常
# try:
#     print(name)
#     # print(1 / 0)
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)

# 捕获多个异常
# try:
#     # 1 / 0
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量未定义或者除以0的异常错误")

# 未正确设置捕获异常类型, 将无法捕获异常


# 捕获所有异常
try:
    # 1 / 0
    # print(name)
    f = open("D:/123.text", "r", encoding="utf-8")
    # print("Hello")
except Exception as e:
    print("出现异常了")
    f = open("D:/123.text", "w", encoding="utf-8")
else:
    print("好高兴, 没有异常")
finally:
    print("我是finally, 有没有异常我都要执行")
    f.close()

