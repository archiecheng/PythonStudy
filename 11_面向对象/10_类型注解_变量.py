#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:35
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 10_类型注解_变量.py
# @Software: PyCharm
import json
import random

# 基础数据类型注解

var_1: int = 10
var_2: str = "itheima"
var_3: bool = True

# 类对象类型注解
class Student:
    pass

stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"itheima": 666}

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "itheima", True)
my_dict: dict[str,int] = {"itheima": 666}

# 在注释中进行类型注解
var_1 = random.randint(1, 10) # type: int
var_2 = json.loads('{"name": "zhangsan"}') # type: dict[str, str]
def func():
    return 10

var_3 = func() # type: int

# 类型注释的限制
