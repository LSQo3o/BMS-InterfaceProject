import logging
import os.path
import time

from Conf.VarConfig import LogPath

"""
指定日志的输出格式format，这个参数可以输出很多有用的信息，如下:
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息

在工作中给的常用格式如下:
format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
这个格式可以输出日志的打印时间，是哪个模块输出的，输出的日志级别是什么，以及输入的日志内容
"""


class LogUtil:
    def __init__(self):
        # 第一步 创建一个logger（默认为root）
        self.logger = logging.getLogger("logger")
        # 设置日志级别 log等级总开关（默认为WARNING）
        self.logger.setLevel(logging.DEBUG)
        # if not self.logger.handlers:
        # 日志名称
        self.log_name = "{}.log".format(time.strftime("%Y_%m_%d", time.localtime()))
        # 日志路径
        self.log_path_file = LogPath + "/" + self.log_name

        # 第二步 创建一个handler，用于写入日志文件
        file_handler = logging.FileHandler(self.log_path_file, encoding="utf-8", mode="w")  # open的打开模式这里可以进行参考
        # 输出到file的log等级的开关
        file_handler.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # 输出到console的log等级的开关

        # 第三步 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        # 设置打印格式
        file_handler.setFormatter(formatter)

        # 第四步 将logger添加到handler里面
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log(self):
        # 返回定义好的logger对象，对外可直接调用log函数
        return self.logger


logger = LogUtil().log()

if __name__ == '__main__':
    logger.debug("这是一条测试日志")
