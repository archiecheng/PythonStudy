#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 12:47
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 02_while循环的基础案例-猜数字.py
# @Software: PyCharm

# 获取范围在 1~100 的随机数字
import random
num = random.randint(1,100)
# 定义一个变量, 记录总共猜测了多少次
count = 0
# 通过一个布尔类型的变量, 做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字:"))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
        # 设置为False就是终止循环的条件
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")

print(f"你总共猜测了{count}次")