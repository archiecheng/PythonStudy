#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/8 11:49
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 10_递归.py
# @Software: PyCharm
import os

def test_os():
    print(os.listdir("D:/test"))     # 列出路径下的内容
    # print(os.path.isdir("D:/test/a"))# 判断指定路径是不是文件夹
    # print(os.path.exists("D:/test")) # 判断指定路径是不是存在

def get_files_recursion_from_dir(path):
    """
    从指定的文件中使用递归的方式, 获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list, 包含全部的文件, 如果目录不存在或者无文件夹就返回一个空list
    """
    file_list = []
    if os.path.isdir(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                # 进入到这里, 表明这个目录是文件夹而不是文件
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}, 不存在")
        return []

    return file_list

if __name__ == '__main__':
    print(get_files_recursion_from_dir("D:/test"))