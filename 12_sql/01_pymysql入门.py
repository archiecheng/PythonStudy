#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 22:05
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 01_pymysql入门.py
# @Software: PyCharm

from pymysql import Connection

# 构建到MySQL数据库的链接
connection = Connection(
    host="localhost", # 主机名IP
    port=3306,        # 端口
    user="root",      # 账户
    password="123456" # 密码
)

# print(connection.get_server_info())

# 执行非查询性质SQL
# 获取游标对象
cursor = connection.cursor()    # 获取游标对象
# 选择数据库
connection.select_db("world")
# 执行sql
# cursor.execute("create table test_pymsql2(id int)")
cursor.execute("select * from student")

results = cursor.fetchall()
for r in results:
    print(r)
# 执行查询性质SQL

# 关闭连接
connection.close()