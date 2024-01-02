#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 21:09
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 02_函数参数的多种使用形式.py
# @Software: PyCharm

def user_info(name, age, gender):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")
# 位置参数 - 使用默认形式
user_info("小明",20,"男")

# 关键字参数
user_info(name="小王", age=11, gender="女孩")
user_info(age=11, name="笑笑", gender="女孩") # 可以不按照参数的定义顺序传参
user_info("甜甜", gender="女孩", age=45)

# 缺省参数
def user_info(name, age, gender='男'): # 默认值只能设置到最后，不能是第一个
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")

user_info("小天",13)
user_info("小天",13, gender='女')


# 不定长 - 位置不定长, * 号
# 不定长定义的形式参数会作为元组存在, 接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是: {type(args)}, 内容是: {args}")

user_info(1,2,3,4,"小明","男孩")

# 不定长 - 关键字不定长, ** 号

def user_info(**kwargs):
    print(f"args参数的类型是: {type(kwargs)}, 内容是: {kwargs}")

user_info(name="小王", age = 11, gender="男孩", addr = "北京")