#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 18:15
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 02_数据输入.py
# @Software: PyCharm

from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 通过parallelize方法将Python对象加载到Spark内, 成为RDD对象
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize("abcdefg")
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
# # 如果要查看RDD里又什么内容, 需要用 collect() 方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())


# 通过 textFile 方法, 读取文件数据加载到Spark内, 成为 RDD 对象

rdd = sc.textFile("D:/hello.txt")
print(rdd.collect())


sc.stop()
