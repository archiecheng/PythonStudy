#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 18:15
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 04_数据计算_flatMap方法.py
# @Software: PyCharm
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/soft/python/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["itheima itcast 666", "itheima itheima itcast", "python itheima"])

# 需求, 将RDD数据里面的一个个单词提取出来
rdd2 = rdd.flatmap(lambda x: x.split(" "))
print(rdd2.collect())