#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 18:17
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 11_数据输出_输出为Python对象.py
# @Software: PyCharm
"""
演示将RDD输出为Python对象
"""

from pyspark import SparkConf, SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = "D:/soft/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# collect算子，输出RDD为list对象
rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))
# reduce算子，对RDD进行两两聚合
num = rdd.reduce(lambda a, b: a + b)
print(num)
# take算子，取出RDD前N个元素，组成list返回
take_list = rdd.take(3)
print(take_list)
# count，统计rdd内有多少条数据，返回值为数字
num_count = rdd.count()
print(f"rdd内有{num_count}个元素")

sc.stop()
