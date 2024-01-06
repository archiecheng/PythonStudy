#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 10:36
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 12_类型注解_Union联合类型.py
# @Software: PyCharm

# 使用 Union 类型, 必须先导包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]

def func(data: Union[int, str]) -> Union[int, str]:
    pass

func()






