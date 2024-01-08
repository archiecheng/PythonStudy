#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/8 11:48
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 05_多线程编程.py
# @Software: PyCharm
import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # 唱歌的线程
    sing_thread = threading.Thread(target=sing, args=('我要唱歌, 哈哈哈',))
    # 跳舞的线程
    dance_thread = threading.Thread(target=dance, kwargs={"msg":"我在跳舞哦"})

    # 让线程执行
    sing_thread.start()
    dance_thread.start()