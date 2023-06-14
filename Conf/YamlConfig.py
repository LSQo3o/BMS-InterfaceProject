# -*- coding: UTF-8 -*-
"""
@Project ：BMS-Interface 
@File    ：YamlConfig.py
@IDE     ：PyCharm 
@Author  ：四七
@Date    ：2023/6/11 16:42 
"""
import os

import yaml
from dotenv import load_dotenv, find_dotenv


# 解析yaml文件 yaml文件用于切换环境env
def get_config():
    load_env = load_dotenv(find_dotenv(), override=True)  # 固定用法
    if load_env:
        current_env = os.getenv("ENV")  # 获取当前环境
        # print(current_env)
        # 读取yaml文件
        file_path = os.path.join(os.path.dirname(__file__), current_env + ".yaml")
        with open(file_path, "r", encoding="utf-8") as f:
            # 固定用法 返回 url:"http://test.albcoininworld.com:9100/"
            return yaml.safe_load(f)
    else:
        raise ModuleNotFoundError(".env 环境配置文件没找到")


config_items = get_config()
print(config_items)
print(config_items["url"])
