#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 18:51
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 10_变量的作用域.py
# @Software: PyCharm

# 演示局部变量
# def test_a():
#     num = 100
#     print(num)
#
# test_a()
# 出了函数体, 局部变量就无法使用了
# print(num)


# 演示全局变量
# num = 200
# def test_a():
#     print(f"test_a:{num}")
#
# def test_b():
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)


# 在函数内修改全局变量
# num = 200
# def test_a():
#     print(f"test_a:{num}")
#
# def test_b():
#     num = 500 # 定义的 num 变量是局部变量
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)

# global 关键字, 在函数内部声明变量为全局变量
num = 200
def test_a():
    print(f"test_a:{num}")

def test_b():
    global num # 使用 global 使其变为全局变量
    num = 500
    print(f"test_b:{num}")

test_a()
test_b()
print(num)