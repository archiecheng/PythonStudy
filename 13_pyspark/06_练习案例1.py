#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 18:16
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 06_练习案例1.py
# @Software: PyCharm
# 1. 构建执行环境入口对象
from pyspark import SparkContext, SparkConf
import findspark
findspark.init()
import os
os.environ['PYSPARK_PYTHON'] = "D:/soft/python/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 2. 读取数据文件
rdd = sc.textFile("D:/hello.txt")
# 3. 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 4. 将所有单词都转换成二元元组，单词为Key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 5. 分组求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
# 6. 打印输出结果
print(result_rdd.collect())