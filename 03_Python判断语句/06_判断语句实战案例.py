#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 22:21
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 06_判断语句实战案例.py
# @Software: PyCharm
import random
num = random.randint(1,10)

print(num)

guess_num = int(input("请输入您要猜测的数字: "))

if  guess_num == num:
    print("恭喜, 第一次就猜中了")
else:
    if guess_num > num:
        print("您猜测的数字大了")
    else:
        print("您猜测的数字小了")

    guess_num = int(input("请输入您要猜测的数字: "))

    if guess_num == num:
        print("第二次就猜中了")
    else:
        if guess_num > num:
            print("您猜测的数字大了")
        else:
            print("您猜测的数字小了")

        guess_num = int(input("请输入您要猜测的数字: "))

        if guess_num == num:
            print("第三次猜中了")
        else:
            if guess_num > num:
                print("您猜测的数字大了")
            else:
                print("您猜测的数字小了")

            guess_num = int(input("请输入您要猜测的数字: "))
