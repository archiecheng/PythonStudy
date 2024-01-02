#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 12:24
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 05_tuple元组.py
# @Software: PyCharm

# 定义元组
t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是:{type(t1)}, 内容是: {t1}")
print(f"t2的类型是:{type(t2)}, 内容是: {t2}")
print(f"t3的类型是:{type(t3)}, 内容是: {t3}")

# 定义单个元素的元组
t4 = ("hello")
print(f"t4的类型是: {type(t4)}, 内容是: {t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是: {type(t5)}, 内容是:{t5}")

# 通过下标索引取取出内容
print(f"从嵌套元组中取出的数据是:{t5[1][2]}")

# 元组的操作: index查找方法
t6 = ("传智教育", "黑马程序员", "Python")
index = t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序员, 下标是: {index}")

# 元组的操作: count 统计方法
t7 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
num = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有: {num}个")

# 元组的操作: len函数统计元组元素数量
t8 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
num = len(t8)
print(f"t8元组中的元素有{num}个")

# 元组的遍历: while
index = 0
while index < len(t8):
    print(t8[index])
    index += 1

# 元组的遍历: for
for element in t8:
    print(element)

# 定义一个元组
t9 = (1, 2, ["itheima", "itcast"])
print(f"t9的内容是:{t9}")

t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
print(f"t9的内容是:{t9}")