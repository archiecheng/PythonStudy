#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 16:55
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 06_包.py
# @Software: PyCharm
# 创建一个包
# 导入自定义的包中的模块, 并使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

# from my_package import my_module1
# from my_package import my_module2
# my_module1.info_print1()
# my_module2.info_print2()

# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()

# 通过 __all__ 变量, 控制 import *
from my_package import *
my_module1.info_print1()