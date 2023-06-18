"""
读取文件目录
"""
import os

# 获取文件的绝对路径
abs_path = os.path.abspath(__file__)  # /Users/qiutiao/BMS-Interface/Conf/VarConfig.py

# 获取文件所在目录的上一级目录 也就是根目录
BASE_DIR = os.path.dirname(os.path.dirname(abs_path))  # /Users/qiutiao/BMS-Interface

# 测试数据目录
DataPath = BASE_DIR + "/Data"  # /Users/qiutiao/BMS-Interface/Data
# DataPath = BASE_DIR + os.sep + "Data" # /Users/qiutiao/BMS-Interface/Data 另一种方法

# 测试报告目录
ReportsPath = BASE_DIR + "/reports"

# 测试日志目录
LogPath = BASE_DIR + "/Log"
# print(LogPath)
