#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 16:55
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_模块的导入.py
# @Software: PyCharm

# 使用 import 导入 time 模块使用 sleep 功能(函数)
# import time # 导入 Python 内置的 time 模块 (time.py这个代码文件)
# print("你好")
# time.sleep(5) # 通过, 就可以使用模块内部的全部功能(类、函数、变量)
# print("我好")

# 使用 from 导入 time 的 sleep 功能(函数)
# from time import sleep
# print("你好")
# sleep(5)
# print("我好")

# 使用 * 导入 time 模块的全部功能
# from time import * # * 表示全部的意思
# print("你好")
# sleep(5)
# print("我好")

# 使用 as 给特定功能加上别名
# import time as t
# print("你好")
# t.sleep(5)
# print("我好")

from time import sleep as sl
print("你好")
sl(5)
print("我好")