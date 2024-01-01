#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 14:51
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 08_for循环的嵌套使用.py
# @Software: PyCharm

# 坚持表白100天，每天都送10朵花
# range

for i in range(1,101):
    print(f"今天是向小美表白的第{i}天")
    # 写内层循环了
    for j in range(1,11):
        print(f"给小美送的第{j}朵玫瑰花")

    print("小美我喜欢你")

print(f"第{i}天, 表白成功")