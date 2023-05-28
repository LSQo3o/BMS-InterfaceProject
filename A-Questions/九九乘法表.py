# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface
@File    ：九九乘法表.py
@IDE     ：PyCharm
@Author  ：四七
@Date    ：2023/5/28 15:27
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, "*", j, "=", i * j, end=" ", )
    print()
