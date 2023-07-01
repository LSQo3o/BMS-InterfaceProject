# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface
@File    ：选择排序.py
@IDE     ：PyCharm
@Author  ：四七
@Date    ：2023/5/28 15:27
"""
"""
选择排序（Selection sort）是一种简单直观的排序算法。
工作原理是：第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，
然后放到已排序的序列的末尾。以此类推，直到全部待排序的数据元素的个数为零。
选择排序是不稳定的排序方法。
"""
lst1 = [10, 2, 4, 7, 9, 6, 1]  # 无序区
for i in range(0, len(lst1)-1):
    max_index = i
    for j in range(i + 1, len(lst1)):
        if lst1[j] > lst1[max_index]:
            max_index = j
    lst1[i], lst1[max_index] = lst1[max_index], lst1[i]

print(lst1)
