#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import os
os.system('')

# 前景色/字体色
print('\033[30m打印前景色0\033[0m') # 黑色字体
print('\033[31m打印前景色1\033[0m') # 红色字体
print('\033[32m打印前景色2\033[0m') # 绿色字体
print('\033[33m打印前景色3\033[0m') # 黄色字体
print('\033[34m打印前景色4\033[0m') # 蓝色字体
print('\033[35m打印前景色5\033[0m') # 紫色字体
print('\033[36m打印前景色6\033[0m') # 青色字体
print('\033[37m打印前景色7\033[0m') # 白色字体
# 背景色
print('\033[40m打印背景色0\033[0m') # 黑色背景
print('\033[41m打印背景色1\033[0m') # 红色背景
print('\033[42m打印背景色2\033[0m') # 绿色背景
print('\033[43m打印背景色3\033[0m') # 黄色背景
print('\033[44m打印背景色4\033[0m') # 蓝色背景
print('\033[45m打印背景色5\033[0m') # 紫色背景
print('\033[46m打印背景色6\033[0m') # 青色背景
print('\033[47m打印背景色7\033[0m') # 白色背景
# 显示方式
print('\033[0m打印显示方式0\033[0m')    # 默认
print('\033[1m打印显示方式1\033[0m')    # 粗体
print('\033[4m打印显示方式4\033[0m')    # 下划线
print('\033[5m打印显示方式5\033[0m')    # 闪烁
print('\033[7m打印显示方式7\033[0m')    # 反白现实
print('\033[8m打印显示方式8\033[0m')    # 不可见

# 综合打印
print('\033[5;31;47m综合打印\033[0m')