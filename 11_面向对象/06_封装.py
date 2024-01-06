#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:35
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 06_封装.py
# @Software: PyCharm

# 定义一个类, 内含私有成员变量和私有成员方法

class Phone:
    __current_voltage = 0.5 # 当前运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def class_by_5g(self):
        if(self.__current_voltage >= 1):
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足, 无法使用5g通话, 并已设置为单核运行进行省电")


phone = Phone()
# phone.__keep_single_core()
phone.class_by_5g()