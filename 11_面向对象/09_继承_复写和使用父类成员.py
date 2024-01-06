#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:35
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 09_继承_复写和使用父类成员.py
# @Software: PyCharm
class Phone:
    IMEI = None     # 序列号
    producer = "ITCAST" # 厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类, 复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA" # 复写父类的成员属性

    def call_by_5g(self):
        print("开启CPU单核模式, 确保通话的时候省电")
        # 方式1
        # print(f"父类的厂商是: {Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是: {super().producer}")
        super().call_by_5g()
        # print("使用5g网络进行通话")
        print("关闭CPU单核模式, 确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

# 在子类中, 调用父类成员