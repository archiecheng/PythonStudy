#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/7 22:22
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_工厂模式.py
# @Software: PyCharm
class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class PersonFactory:
    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()

pf = PersonFactory()
worker = pf.get_person("w")
stu = pf.get_person("s")
teacher = pf.get_person("t")

