#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 16:56
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 07_综合案例练习.py
# @Software: PyCharm

import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("itheima", 0, 4))

# file_util.print_file_info("D:/test_append.txt")
file_util.append_to_file("D:/test_append.txt", "itheima")