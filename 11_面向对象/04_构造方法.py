#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:34
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_构造方法.py
# @Software: PyCharm


# 演示使用构造方法对成员变量进行赋值

# 构造方法的名称: __init__

class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

stu = Student("周杰伦", 31, "18500006666")
print(stu.name)
print(stu.age)
print(stu.tel)
