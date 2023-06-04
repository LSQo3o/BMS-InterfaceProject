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
class RequestSend:
    # 封装requests请求函数
    def api_run(self, url, method, data=None, headers=None, cookies=None):
        # 定义变量，获取响应结果
        res = None
        # 打印日志
        logger.info("请求的URL为{},类型为{}".format(url, type(url)))
        logger.info("请求的Method为{},类型为{}".format(method, type(method)))
        logger.info("请求的Data为{},类型为{}".format(data, type(data)))
        logger.info("请求的Headers为{},类型为{}".format(headers, type(headers)))
        logger.info("请求的Cookies为{},类型为{}".format(cookies, type(cookies)))

        # 请求方法是get
        if method.lower() == "get":
            res = requests.get(url, data=data, headers=headers, cookies=cookies)
        # 请求方法是post
        elif method.lower() == "post":
            # 请求数据是json格式
            if headers == {"Content-Type": "application/json"}:
                res = requests.post(url, json=data, headers=headers, cookies=cookies)
            # 请求数据是表单格式
            elif headers == {"Content-Type": "application/x-www-form-urlencoded"}:
                res = requests.post(url, data=data, headers=headers, cookies=cookies)
        # 获取请求响应的状态码
        code = res.status_code
        # 获取请求响应的cookie
        cookies = res.cookies.get_dict()
        dict1 = dict()
        try:
            # 获取响应结果json格式
            body = res.json()
        except:
            # 获取响应结果text格式
            body = res.text

        dict1["code"] = code
        dict1["body"] = body
        dict1["cookies"] = cookies
        # print(dict1)
        return dict1

    # 对外调用方法，**kwarg传入的参数是dict类型
    def send(self, url, method, **kwargs):
        return self.api_run(url=url, method=method, **kwargs)


if __name__ == '__main__':
    url = "http://test.albcoininworld.com:9100/"
    data = {"username": "admin", "password": "123456"}
    method = "post"
    headers = {"Content-Type": "application/json"}
    print(RequestSend().send(url=url, method=method, headers=headers, data=data))
