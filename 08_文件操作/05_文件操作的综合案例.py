#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 15:33
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 05_文件操作的综合案例.py
# @Software: PyCharm
# 打开文件得到文件对象, 准备读取
fr = open("D:/bill.txt", "r", encoding="UTF-8")
# 打开文件得到文件对象, 准备写入
fw = open("D:/bill.txt.bak", "w", encoding="UTF-8")
# for 循环读取文件
for line in fr:
    line = line.strip("\n")
    # 判断内容, 将满足的内容写出
    if line.split(",")[4] == "测试":
        continue # continue 进入下一次循环, 这一次后面的内容跳过
    # 内容写出去
    fw.write(line)
    # 由于前面对内容进行了strip()操作, 所以要手冻的写出换行符
    fw.write("\n")

# close
fr.close()
fw.close() # 调用 close 会自动flush
