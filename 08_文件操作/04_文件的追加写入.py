#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 15:33
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_文件的追加写入.py
# @Software: PyCharm

# 打开文件, 不存在的文件
# f = open("D:/test.txt", "a", encoding="utf-8")
# # write 写入
# f.write("黑马程序员")
# # flush 刷新
# f.flush()
# # close 关闭
# f.close()

# 打开一个存在的文件
f = open("D:/test.txt", "a", encoding="utf-8")
# write写入, flush 刷新
f.write("\n月薪过往")
# close关闭
f.close()