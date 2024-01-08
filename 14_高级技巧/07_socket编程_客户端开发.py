#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/8 11:48
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 07_socket编程_客户端开发.py
# @Software: PyCharm
import socket
# 创建socket对象
socket_client = socket.socket()
# 连接到服务器
socket_client.connect(("localhost", 8888))
while True:
    # 发送消息
    send_msg = input("请输入要发送的消息")
    if send_msg == 'exit':
        break
    socket_client.send(send_msg.encode("UTF-8"))
    # 接收返回消息
    recv_data = socket_client.recv(1024)    # 1024 是缓冲区的大小, 一般1024即可, 同样RECV方法是阻塞的
    print(f"服务端回复的消息是:{recv_data.decode('UTF-8')}")
# 关闭链接
socket_client.close()