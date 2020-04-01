#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import logging, sys, os
from logging.handlers import RotatingFileHandler # 导入rotatingfilehandler负责将日志消息发送到磁盘文件，并支持日志文件按大小切割

logger = logging.getLogger(__name__) #获取logger对象作为整个日志器的入口，实例化Logger类
logger.setLevel(logging.INFO) #设置logger的等级为INFO
#获取日志器的格式器，对handler输出的日志进行格式化
log_formatter = logging.Formatter("[%(levelname)s:%(asctime)s %(process)s %(filename)s:%(lineno)d]: %(message)s", "%Y-%m-%d %H:%M:%S")

file_handler = RotatingFileHandler(os.path.dirname(os.path.abspath(__file__)) + "/test_logger.log", "a", 1024 * 1024 * 20, 5)
file_handler.setFormatter(log_formatter)

console_handler = logging.StreamHandler(sys.stdout) # 将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象
console_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

if __name__ == "__main__":
    logger.info('info message')
