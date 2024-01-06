#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:34
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 05_其它内置方法.py
# @Software: PyCharm

class Student:
    def __init__(self, name, age):
        self.name = name # 学生姓名
        self.age = age # 学生年龄

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象, name:{self.name}, age:{self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__ 魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__ 魔术方法
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("周杰伦",31)
stu2 = Student("周杰伦",36)
print(stu1 <= stu2)
print(stu1 >= stu2)

