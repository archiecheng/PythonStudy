#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/4 22:29
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_类和对象.py
# @Software: PyCharm

# 设计一个闹钟类

class Clock:
    id = None    # 序列化
    price = None # 价格

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"clock id: {clock1.id}, clock price: {clock1}")
clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"clock id: {clock2.id}, clock price: {clock2}")
clock2.ring()