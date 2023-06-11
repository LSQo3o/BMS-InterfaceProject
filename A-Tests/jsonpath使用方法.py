# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：jsonpath使用方法.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/6/11 14:44 
"""
from jsonpath import jsonpath

dict1 = {"username": "admin", "password": {"pwd1": "123456", "pwd2": "987987"}, "hobbies": [{"num1": 1}, {"num2": 2}]}
print(type(dict1))  # <class 'dict'>

result1 = jsonpath(dict1, "$.username")
print(result1)

result2 = jsonpath(dict1, "$.password.pwd2")
print(result2)

result3 = jsonpath(dict1, "$.hobbies[1].num2")
print(result3)
