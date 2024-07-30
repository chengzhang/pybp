"""
提供 Logger
"""

# coding=utf-8

import inspect
import logging
import os
from logging.handlers import TimedRotatingFileHandler

from pybp.design_pattern.singleton import singleton


APP_NAME = os.getenv('APP_NAME', 'UNDEFINED_APP')

PREFIX = os.path.join("log/")
if not os.path.exists(PREFIX):
    os.makedirs(PREFIX)


@singleton
class AppLogger:
    """
    Logger 类
    """
    def __init__(self):
        # file_name, 按天, interval, 保留几个
        rh = TimedRotatingFileHandler(
            "{}/{}.log.txt".format(PREFIX, APP_NAME),
            when="H",
            backupCount=24
        )
        fm = logging.Formatter(
            "[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(thread)d] %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        rh.setFormatter(fm)
        logging.addLevelName(logging.DEBUG, "debug")
        logging.addLevelName(logging.INFO, "info")
        logging.addLevelName(logging.WARN, "warning")
        logging.addLevelName(logging.ERROR, "error")
        logging.addLevelName(logging.CRITICAL, "critical")
        self.logger = logging.getLogger(APP_NAME)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(rh)
        self.logger.propagate = False

    def __get_call_info(self):
        stack = inspect.stack()
        fn = stack[2][1]
        fn = fn.split("/")[-1]
        ln = stack[2][2]
        func = stack[2][3]
        return fn, ln, func

    def debug(self, message):
        """
        debug 日志
        """
        fn, ln, func = self.__get_call_info()
        self.logger.debug("[{}:{} {}] {}".format(fn, ln, func, message))

    def info(self, message):
        """
        info 日志
        """
        fn, ln, func = self.__get_call_info()
        self.logger.info("[{}:{} {}] {}".format(fn, ln, func, message))

    def warn(self, message):
        """
        warn 日志
        """
        fn, ln, func = self.__get_call_info()
        self.logger.warning("[{}:{} {}] {}".format(fn, ln, func, message))

    def warning(self, message):
        """
        warn 日志
        """
        fn, ln, func = self.__get_call_info()
        self.logger.warning("[{}:{} {}] {}".format(fn, ln, func, message))

    def error(self, message):
        """
        error 日志
        """
        fn, ln, func = self.__get_call_info()
        self.logger.error("[{}:{} {}] {}".format(fn, ln, func, message))

    def crit(self, message):
        """
        crit 日志
        """
        fn, ln, func = self.__get_call_info()
        self.logger.critical("[{}:{} {}] {}".format(fn, ln, func, message))


def get_logger():
    """
    获取 logger
    """
    return AppLogger()
