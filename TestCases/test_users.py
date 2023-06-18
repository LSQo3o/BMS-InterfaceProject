# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：test_users.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/6/18 16:44 
"""
import pytest

# from Utils.AssertUtil import assert_res
from Utils.ExcelUtil import get_row_values, get_test_data
from Utils.RequestUtil import RequestUtil

argnames = get_row_values("login", 1)
argvaules = get_test_data("login")


@pytest.mark.parametrize(argnames, argvaules)
def test_login(project, module, caseid, casename, description, url, method, headers, data, content_type, assertres):
    headers = eval(headers) if headers else headers
    print(headers)
    data = eval(data) if data else data
    requestUtil = RequestUtil()
    result = requestUtil.api_requests(url=url, method=method, headers=headers, data=data, content_type=content_type)
    print(result)

    # # 是否要断言
    # if assertres:
    #     assert_res(result, assertres)


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
