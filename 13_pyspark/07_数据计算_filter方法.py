#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 18:16
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 07_数据计算_filter方法.py
# @Software: PyCharm
from pyspark import SparkContext, SparkConf
import findspark
findspark.init()
import os
os.environ['PYSPARK_PYTHON'] = "D:/soft/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# 对 RDD 数据进行过滤
rdd2 = rdd.filter(lambda num: num % 2 == 0)

print(rdd2.collect())