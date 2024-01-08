#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/8 11:48
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 06_socket编程_服务端开发.py
# @Software: PyCharm

import socket
# 创建 Socket对象
socket_server = socket.socket()
# 绑定 ip 地址和端口
socket_server.bind(("localhost", 8888))
# 监听端口
socket_server.listen(1)
# listen方法内接收一个整数传参数, 表示接收的链接数量
# 等待客户端链接
# result = socket_server.accept()
# conn = result[0]    # 客户端和服务端的链接对象
# address = result[1] # 客户端的地址信息
conn, address = socket_server.accept()
# accept方法返回的是二元元组(链接对象, 客户端地址信息)
# 可以通过 变量1, 变量2 = socket.server.accept()的形式, 直接接受二元元组内的两个元素
# accept()方法, 即阻塞的方法, 等待客户端的链接， 如果没有链接，就卡在这一行，不向下执行了
print(f"接收到了客户端的链接, 客户端的信息是:{address}")
while True:
    # 接受客户端消息, 要使用客户端和服务端的本次链接对象, 而非socket_server对象
    data: str = conn.recv(1024).decode("UTF-8")
    # recv 接收的参数是缓冲区大小, 一般给1024即可
    # recv的返回值是一个字节数组也就是bytes对象，不是字符串， 可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象
    print(f"客户端发来的消息是:{data}")
    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息:").encode("UTF-8") # encode可以将字符串编码为字节数组对象
    if msg == "exit":
        break
    conn.send(msg)
# 关闭链接
conn.close()
socket_server.close()
