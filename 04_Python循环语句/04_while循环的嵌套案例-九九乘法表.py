#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 13:09
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_while循环的嵌套案例-九九乘法表.py
# @Software: PyCharm

# end 代表不换行
# print("Hello", end='')
# print("World", end='')

# print("Hello\tWorld")
# print("itheima\tbest")

i = 1
# 定义外层循环的控制变量
while i <= 9:
    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的 print 语句, 不要换行
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1
    i+= 1
    print() # print空内容, 就是输出一个换行