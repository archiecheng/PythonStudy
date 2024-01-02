#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/1 22:20
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 01_list列表.py
# @Software: PyCharm

# 定义一个列表 list
my_list = ["itheima", "itcast", "python"]
print(my_list)
print(type(my_list))

my_list = ["itheima", 666, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套列表
my_list = [[1, 2, 3], 4, 5, 6]
print(my_list)
print(type(my_list))
# 通过下表索引取出对应位置的数据
my_list = ["Tom", "Lily", "Rose"]
# 列表[下标索引], 从前向后从0开始, 每次 + 1, 从后向前从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 错误示范, 通过下标索引取数据, 一定不要超过范围
# print(my_list[3]) # out of range


# 通过下标索引取出数据(倒序取出)
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])


# 取出嵌套列表的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])