# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：requests库.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/6/6 23:10 
"""
import requests

# 发送get请求
url = "http://httpbin.org/get"
# res = requests.get(url)  # 得到的是response对象 返回的是response code状态码
# print(res.text)  # 得到的是一些响应结果

# 带请求头 用字典表示
headers = {"Accept": "json", "token": "111"}
# res = requests.get(url=url,headers=headers)
# print(res.text)

# 带参数
params = {"id": "2", "name": "tester"}
res = requests.get(url=url, headers=headers, params=params)
print(res.text)
