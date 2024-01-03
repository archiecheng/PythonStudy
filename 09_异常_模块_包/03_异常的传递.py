#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 16:55
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_异常的传递.py
# @Software: PyCharm

# 定义一个出现异常的方法
def func1():
    print('func1 开始执行')
    num = 1 / 0
    print("func1 结束执行")


# 定义一个无异常的方法
def func2():
    print('func2 开始执行')
    func1()
    print('func2 结束执行')

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了, 异常的信息是:{e}")

main()