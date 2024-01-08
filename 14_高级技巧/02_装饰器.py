#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/7 22:22
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 02_装饰器.py
# @Software: PyCharm
# 装饰器的一般写法(闭包)
# def outer(func):
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
# def sleep():
#     import random
#     import time
#     print("睡眠中...")
#     time.sleep(random.randint(1, 5))
#
# fn = outer(sleep)
# fn()


# 装饰器的快捷写法(语法糖)
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中...")
    time.sleep(random.randint(1, 5))

sleep()