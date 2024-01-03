#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 15:32
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 02_文件读取的课后练习.py
# @Software: PyCharm

# 打开文件, 以读取的模式打开
f = open("D:/word.txt", "r", encoding="UTF-8")
# 方式1: 读取全部内容, 通过字符串count方法统计itheima单词数量
# content = f.read()
# count = content.count("itheima")
# print(f"itheima在文件中出现了:{count}次")
# 方式2: 读取内容, 一行一行读取
count = 0 # 使用 count 变量来累计itheima出现的次数
for line in f:
    line = line.strip() # 去除开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1
    # 判断单词出现的次数并统计
print(f"itheima在文件中出现了:{count}次")
# 关闭文件
f.close()