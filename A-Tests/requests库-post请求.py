# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：requests库-post请求.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/6/7 22:44 
"""
import requests

# 发送post请求
url = "http://httpbin.org/post"
# res = requests.post(url=url)
# print(res.text)

# 带请求头
headers = {"token": "123456"}
# res = requests.post(url=url, headers=headers)
# print(res.text)

# 带参数 表单形式 "Content-Type": "application/x-www-form-urlencoded",关键字是data
data = {"username": "admin", "password": "123456"}
# res = requests.post(url=url, headers=headers,data=data)
# print(res.text)

# 带参数 json形式 "Content-Type": "application/json",关键字是json
# res = requests.post(url=url, headers=headers, json=data)
# print(res.text)

# 带参数 quert_string XXX.com/1/2，没有"Content-Type"，关键字是params，参数在args里面
# res = requests.post(url=url, headers=headers, params=data)
# print(res.text)

# 上传文件 "Content-Type": "multipart/form-data; boundary=2f1b6d05d6ee0c427b977ad18728c29e",是一种特殊的格式，关键字是files
file = {"file1": open("2023_05_28.log", "rb")}
# res = requests.get(url=url, headers=headers, params=params, files=file)
# print(res.text)

# encoding
res = requests.post(url=url, headers=headers, data=data)
# print(res.encoding)  # 获取响应结果编码格式 utf-8
# res.encoding = "ISO-8859-1"  # 更改编码格式
# print(res.encoding)  # ISO-8859-1

# print(res.text)
# print(type(res.text))  # 为字符串类型

print(res.json())
print(type(res.json()))  # 为字典类型 是可以转换成json的

# print(res.status_code)  # 获取响应状态码

print(res.headers)  # 获取响应头
print(type(res.headers))
print(res.headers["Content-Type"])  # 字典方法取值
