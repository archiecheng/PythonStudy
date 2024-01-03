#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 15:32
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 01_文件的读取.py
# @Software: PyCharm
import time

# 打开文件
# f = open("D:/测试.txt", "r", encoding="UTF-8")
# print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果:{f.read(10)}")
# print(f"read方法读取全部内容的结果是:{f.read()}")
print("-------------------------------------------")
# 读取文件 - readLines()
# 读取文件的全部行, 封装到列表中
# lines = f.readlines()
# print(f"lines对象的类型:{type(lines)}")
# print(f"lines对象的内容:{lines}")

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是: {line1}")
# print(f"第一行数据是: {line2}")
# print(f"第一行数据是: {line3}")

# for 循环读取文件行
# for line in f:
#     print(f"每一行数据是: {line}")
#
# # 文件的关闭
# time.sleep(500000)
# f.close()

with open("D:/测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是:{line}")