# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface
@File    ：冒泡排序.py
@IDE     ：PyCharm
@Author  ：四七
@Date    ：2023/5/28 15:27
"""
lst = [2, 4, 7, 9, 6, 10]
for i in range(0, len(lst)):
    for j in range(0, len(lst)-1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)


