#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 18:15
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_数据计算_map方法.py
# @Software: PyCharm
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/soft/python/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# 通过 map 方法将全部数据都乘以10
def func(data):
    return data * 10

rdd2 = rdd.map(lambda x: x * 10)
print(rdd2.collect())
# (T) -> U
# (T) -> T 表示传入类型, 返回就是什么类型

# 链式调用
rdd3 = rdd2.map(lambda x: x + 5)


