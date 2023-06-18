# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：RequestUtil.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/5/28 18:38 
"""
import requests

from Utils.LogUtil import logger


# 定义http请求类
class RequestUtil:
    # 封装requests请求函数
    def api_requests(self, url, method, data=None, headers=None, cookies=None, content_type=None):
        # 定义变量，获取响应结果
        # 打印日志
        # logger.info("请求的URL为{},类型为{}".format(url, type(url)))
        # logger.info("请求的Method为{},类型为{}".format(method, type(method)))
        # logger.info("请求的Data为{},类型为{}".format(data, type(data)))
        # logger.info("请求的Headers为{},类型为{}".format(headers, type(headers)))
        # logger.info("请求的Cookies为{},类型为{}".format(cookies, type(cookies)))
        try:
            # 请求方法为get，关键字是data
            if method.lower() == "get":
                res = requests.get(url=url, data=data, headers=headers, cookies=cookies)
                return res.json()
            # 请求方法为post
            elif method.lower() == "post":
                # 请求数据是json格式，关键字是json
                if content_type == "application/json":
                    # if headers == {"Content-Type": "application/json"}:
                    res = requests.post(url=url, json=data, headers=headers, cookies=cookies)
                    return res.json()
                # 请求数据是表单格式，关键字是data
                elif content_type == "application/x-www-form-urlencoded":
                    res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
                    return res.json()
                else:
                    print("Http Method Not Allowed")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    url = "http://httpbin.org/post"
    data = {"username": "admin", "password": "123456"}
    method = "post"
    headers = {"Content-Type": "application/json"}
    content_type = "application/json"
    cookies = None
    print(RequestUtil().api_requests(url=url, method=method, headers=headers, cookies=cookies, data=data, content_type=content_type))
