# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：test_api.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/6/4 17:44 
"""
import pytest

from Utils.LogUtil import logger


def test_login():
    logger.info("正在登陆")
    print("login...")


def test_login_out():
    logger.info("正在退出")
    print("login out...")


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_api.py", "--html=../reports/report.html"])
