#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 18:16
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 05_数据计算_reduceByKey方法.py
# @Software: PyCharm
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/soft/python/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 99), ('女', 66)])
# 求男生和女生两个组的成绩之和
rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())