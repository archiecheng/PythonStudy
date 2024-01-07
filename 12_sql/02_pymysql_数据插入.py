#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 22:05
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 02_pymysql_数据插入.py
# @Software: PyCharm

from pymysql import Connection

# 构建到MySQL数据库的链接
connection = Connection(
    host="localhost", # 主机名IP
    port=3306,        # 端口
    user="root",      # 账户
    password="123456", # 密码
    autocommit=True    # 设置自动提交
)

# print(connection.get_server_info())

# 执行非查询性质SQL
# 获取游标对象
cursor = connection.cursor()    # 获取游标对象
# 选择数据库
connection.select_db("world")
# 执行sql
cursor.execute("insert into student values(10002, '林俊杰', 31, '男')")
# 通过 commit确认
# connection.commit()
# 关闭连接
connection.close()