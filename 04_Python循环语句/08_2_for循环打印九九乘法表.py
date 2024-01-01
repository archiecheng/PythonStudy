#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 14:57
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 08_2_for循环打印九九乘法表.py
# @Software: PyCharm

# 通过外层循环控制行数
for i in range(1,10):
    # 通过内层循环控制每一行的数据
    for j in range (1, i + 1):
        # 在内层循环中输出每一行的内容
        print(f"{j} * {i} = {i * j}\t", end=' ')
    # 外层循环可以通过一个print()输出一个回车符
    print()