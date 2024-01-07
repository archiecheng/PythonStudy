#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 18:15
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 01_基础准备.py
# @Software: PyCharm

# 导包
from pyspark import SparkContext, SparkConf
# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)
# 打印PySpark的运行版本
print(sc.version)
# 停止SparkContext对象的运行(停止PySpark程序)
sc.stop()