#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 20:36
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : file_util.py
# @Software: PyCharm
# 文件处理相关

def print_file_info(file_name):
    """
    将给定路径的文件内容输出到控制台中
    :param file_name: 即将读取的文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        content = f.read()
        print("文件的全部内容如下:")
        print(content)
    except Exception as e:
        print(f"程序出现异常了, 原因是:{e}")
    finally:
        if f: # 如果变量是None, 表示False, 如果有任何的内容, 就是True
            f.close()

def append_to_file(file_name, data):
    """
    将指定的数据追加到指定的文件中
    :param file_name: 指定的文件路径
    :param data:
    :return: 指定的数据
    """
    f = open(file_name, "a", encoding="utf-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    # print_file_info("D:/bill.txtxxxxx")
    append_to_file("D:/test_append.txt", "传智教育")