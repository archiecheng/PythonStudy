#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 22:21
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_list列表常用操作课后练习.py
# @Software: PyCharm

# 1. 定义这个列表，并用变量接收它， 内容是：[21, 25, 21, 23, 22, 20]
mylist = [21, 25, 21, 23, 22, 20]

# 2. 追加一个数字31，到列表的尾部
mylist.append(31)
print(mylist)
# 3. 追加一个新列表[29, 33, 30]，到列表的尾部
mylist.extend([29,33,30])
print(mylist)
# 4. 取出第一个元素（应是：21）
first = mylist[0]
print(first)
# 5. 取出最后一个元素（应是：30）
last = mylist[-1]
print(last)
# 6. 查找元素31，在列表中的下标位置
index = mylist.index(31)
print(index)
print(mylist)