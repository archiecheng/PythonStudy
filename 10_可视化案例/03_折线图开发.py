#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/3 11:43
# @Author  : Laiyong(Archie) Cheng
# @Site    : 
# @File    : 03_折线图开发.py
# @Software: PyCharm

# 导包

# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
#
# # 创建一个折线图对象
# line = Line()
#
# # 给折线图对象添加x轴的数据
# line.add_xaxis(["中国","美国","英国"])
#
# # 给折线图对象添加y轴数据
# line.add_yaxis("GDP", [30, 20, 10])
#
# # 全局配置选项set_global_opts配置
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
#
# # 通过 render 方法, 将代码生成为图像
# line.render()

import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
# 处理数据
f_us = open("D:/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read() # 美国的全部内容

f_jp = open("D:/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read() # 日本的全部内容

f_in = open("D:/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read() # 美国的全部内容

# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(","")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# JSON转Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(type(us_dict))
# print(us_dict)

# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# print(type(trend_data))
# print(trend_data)

# 获取日期数据, 用于x轴, 取2020年, (到314下标结束)
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确认数据, 用于y轴
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line() # 构建折线图对象

# 添加 x 轴数据
line.add_xaxis(us_x_data) # x 轴是共用的, 所以使用一个国家的数据即可

# 添加 y 轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False)) # 添加美国的y轴数据
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False)) # 添加日本的y轴数据
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False)) # 添加印度的y轴数据

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)

# 调用render方法，生成图表
line.render()
# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()



