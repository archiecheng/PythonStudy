#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 15:32
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_文件的写入.py
# @Software: PyCharm

# 打开文件, 不存在的文件
# f = open("D:/test.txt", "w", encoding="UTF-8")
# # write 写入
# f.write("Hello World!!!")# 内容写入到内存中
# # flush 刷新
# f.flush()# 将内存中积攒的内容，写入到硬盘的文件中
# # close 关闭
# f.close()# close方法, 内置了flush功能

# 打开一个存在的文件
f = open("D:/test.txt", "w", encoding="UTF-8")
# write写入, flush 刷新
f.write("黑马程序员")
# close 关闭
f.close()# close方法, 内置了flush功能