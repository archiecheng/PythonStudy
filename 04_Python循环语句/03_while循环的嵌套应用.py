#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 12:59
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_while循环的嵌套应用.py
# @Software: PyCharm

# 外层: 表白100天的控制
# 内层:每天的表白都送10只玫瑰花的控制

i = 1
while i <= 100:
    print(f"今天是第{i}天, 准备表白....")
    #内层循环控制变量
    j = 1
    while j <= 10:
        print(f"送给小妹第{j}只玫瑰花")
        j += 1

    print("小美, 我喜欢你")
    i += 1

print(f"坚持到第{i - 1}天, 表白成功")