#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/4 22:29
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 02_成员方法.py
# @Software: PyCharm
# 定义一个带有成员方法的类

class Student:
    name = None # 学生姓名

    def say_hi(self):
        print(f"大家好呀, 我是{self.name}, 欢迎大家多多关照")

    def say_hi2(self,msg):
        print(f"大家好, 我是{self.name}, {msg}")

stu1 = Student()
stu1.name = "Archie"
stu1.say_hi2("Nice")

stu2 = Student()
stu2.name = "林俊杰"
stu2.say_hi2("我爱唱歌")