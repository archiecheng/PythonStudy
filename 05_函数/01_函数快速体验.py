#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 15:29
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 01_函数快速体验.py
# @Software: PyCharm

# 需求, 统计字符串的长度, 不适用内置函数len()
str1 = "itheima"
str2 = "itcast"
str3 = "python"

# 定义一个计数的变量
count = 0
for i in str1:
    count = count + 1

print(f"字符串{str1}的长度是: {count}")

count = 0
for i in str2:
    count = count + 1

print(f"字符串{str2}的长度是: {count}")

count = 0
for i in str3:
    count = count + 1

print(f"字符串{str3}的长度是: {count}")

# 可以用函数, 来优化
def my_len(data):
    count = 0
    for i in data:
        count = count + 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)