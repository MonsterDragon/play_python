#!/usr/bin/python
# -*- coding:UTF-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")

"""
为什么只输出WARNING:root:This is a warning log.
这是因为logging模块提供的日志记录函数所使用的日志器设置的日志级别是WARNING，因此只有WARNING级别的日志记录以及大于它的ERROR和CRITICAL级别的日志记录被输出了，而小于它的DEBUG和INFO级别的日志记录被丢弃了。

输出的含义：
日志级别:日志器名称:日志内容
"""


logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
