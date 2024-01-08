#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/8 11:49
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 09_正则表达式_元字符匹配.py
# @Software: PyCharm
import re

# s = "itheima1 @@python2 !!666 ##itcast3"
# result = re.findall(r'[a-zA-Z]', s) # 字符串前面带上r标记, 表示字符串中转义字符无效, 就是普通字符的意思
# print(result)

# 匹配账号, 只能由字母和数字组成, 长度限制6到10位
# r = '^[0-9a-zA-Z]{6,10}$'
# s = '1234567'
# print(re.findall(r, s))

# 匹配QQ号, 要求纯数字, 长度5-11, 第一位不为0
# r = '[1-9][0-9]{4,10}'
# s = '012345678'
# print(re.findall(r, s))

# 匹配邮箱地址, 只允许QQ、163、gmail三种邮箱地址
# {内容}.{内容}@
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
# s = 'a.b.c.e.f@qq.com.z.c.e'
s = 'a.b.c.e.f@123.com.z.c.e'
print(re.findall(r, s))