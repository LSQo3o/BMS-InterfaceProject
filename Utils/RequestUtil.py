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


class RequestSend:
    def api(self, url, method, data=None, headers=None, cookies=None):
        res = None
        logger.info("请求的URL为{},类型为{}".format(url, type(url)))
        logger.info("请求的Method为{},类型为{}".format(method, type(method)))
        logger.info("请求的Data为{},类型为{}".format(data, type(data)))
        logger.info("请求的Headers为{},类型为{}".format(headers, type(headers)))
        logger.info("请求的Cookies为{},类型为{}".format(cookies, type(cookies)))
        if method.lower() == "get":
            res = requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method.lower() == "post":
            # 请求数据是json格式
            if headers == {"Content-Type": "application/json"}:
                res = requests.post(url, json=data, headers=headers, cookies=cookies)
            # 请求数据是表单格式
            elif headers == {"Content-Type": "application/x-www-form-urlencoded"}:
                res = requests.post(url, data=data, headers=headers, cookies=cookies)
        # 获取请求相应的状态码
        code = res.status_code

        cookies = res.cookies.get_dict()
        dict1 = dict()
        try:
            body = res.json()
        except:
            body = res.text

        dict1["code"] = code
        dict1["body"] = body
        dict1["cookies"] = cookies

        return dict1

    def ReSend(self, url, method, **kwargs):
        return self.api(self, url, method=method, **kwargs)


if __name__ == '__main__':
    pass
