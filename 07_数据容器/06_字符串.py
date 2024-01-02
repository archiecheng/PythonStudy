#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 12:44
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 06_字符串.py
# @Software: PyCharm

my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素, 值是: {value}, 取下标为-16的元素, 值是: {value}")

# my_str[2] = "H"

# index 方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and, 其起始下标是: {value}")

# replace 方法
new_my_str = my_str.replace("it", "程序")
print(f"将字符串{my_str}, 进行替换后得到: {new_my_str}")

# split 方法
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到:{my_str_list}")

# strip 方法
my_str = "  itheima and itcast  "
new_my_str = my_str.strip()
print(f"字符串{my_str}被stripe后, 结果:{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12") # 12 划分为两个小子串, 满足即剔除
print(f"字符串{my_str}被strip('12')后, 结果:{new_my_str}")

# 统计字符串中某字符串的出现次数
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是: {count}")

# 统计字符串的长度,len() 函数
num = len(my_str)
print(f"字符串my_str的长度是: {num}")
