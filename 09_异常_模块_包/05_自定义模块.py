#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 16:55
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 05_自定义模块.py
# @Software: PyCharm

# 导入自定义模块使用
# import my_module1
# my_module1.test(1, 2)
# from my_module1 import test
# test(1, 2)

# 导入不同模块的同名功能
# from my_module1 import test
# from my_module2 import test
# test(1, 2)

# __main__ 变量
# from my_module1 import test

# __all__ 变量
from my_module1 import *
test_a(1, 2)
test_b(1, 2)