#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 18:27
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 07_None.py
# @Software: PyCharm

# 无 return 语句的函数返回值
def say_hi():
    print('hello')

result = say_hi()
print(f"无返回值函数, 返回的内容是:{result}")
print(f"无返回值函数, 返回的内容类型是:{type(result)}")

# 主动返回None的函数
def say_hi2():
    print('hello')
    return None

result2 = say_hi2()
print(f"无返回值函数, 返回的内容是:{result2}")
print(f"无返回值函数, 返回的内容类型是:{type(result2)}")

# None 用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result3 = check_age(16)
if not result3:
    # 进入 if 表明 result 是 None 值, 也就是 False
    print("未成年, 不可进入")

# None 用于声明无初始值内容的变量


