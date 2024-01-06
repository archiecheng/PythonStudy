#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:35
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 07_封装课后练习题.py
# @Software: PyCharm

# 设计一个类, 用来描述手机

class Phone:
    # 提供私有成员变量: __is_5g_enable
    __is_5g_enable = False
    # 提供私有成员方法: __check_5g()
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭, 使用4g网络")
    # 提供公开成员方法
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()