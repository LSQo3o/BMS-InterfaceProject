# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：test_login.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/6/11 11:05 
"""
import pytest

from Utils.ExcelUtil import get_row_values, get_test_data
from Utils.RequestUtil import RequestUtil

# 数据从Excel中取
argnames = get_row_values("login", 1)
argvalues = get_test_data("login")


# argvalues = ["http://httpbin.org/post", "post", "None", "None", "None", "None"] 这种格式是错的，外面不该加[]

@pytest.mark.parametrize(argnames, argvalues)
def test_login(project, module, caseid, casename, description, url, method, headers, data, content_type, assertres):
    # requestsUtil = RequestUtil()
    try:
        print(type(headers), type(data))
        headers = eval(headers)  # TODO：研究下为什么此处不能直接用dict转换成字典呢？
        data = eval(data)
        print(type(headers), type(data))
        # headers = eval(headers) if headers else headers
        # data = eval(data) if data else data
        res = RequestUtil().api_requests(url=url, method=method, headers=headers, data=data, content_type=content_type)

        print(res, type(res))
    except Exception as e:
        print(e)


# 断言


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
