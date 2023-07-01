# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：字典和json之间的转换.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/6/18 17:52 
"""
import json

"""
1.json.dumps() 将Python字典类型转换为 JSON 对象, json.loads()将json格式转换成python字典类型
2.json中除数据即数字外，key和value都是字符串，要用双引号引起来；空值为null；布尔值为false/true(小写);
3.字典，key,value可单引号；空值为None；布尔值为False/True
"""
dict1 = {'username': 'admin', 'password': '123456'}
json1 = json.dumps(dict1)
print(json1)  # 双引号
dict2 = json.loads(json1)
print(dict2)  # 单引号
