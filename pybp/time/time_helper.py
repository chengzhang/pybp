"""
时间处理函数
Author: donyzhang
Date: 2023-06-11
"""

# coding = utf8

import datetime
import time
from typing import List


def ms_timestamp_strf(ms_timestamp):
    # assuming timestamp is in milliseconds
    # timestamp = 1629878400000
    # convert to datetime object
    dt_object = datetime.datetime.fromtimestamp(ms_timestamp / 1000)
    # extract milliseconds from timestamp
    milliseconds = ms_timestamp % 1000
    # add milliseconds back to datetime object
    dt_object = dt_object + datetime.timedelta(milliseconds=milliseconds)
    # format datetime object as string with millisecond precision
    time_str = dt_object.strftime('%Y-%m-%d %H:%M:%S.%f')
    return time_str


def get_ms_timestamp():
    now = int(round(time.time() * 1000))
    return now


def get_timestamp():
    now = int(time.time())
    return now


class Timer(object):
    """
    计时器。
    简单的用法：
    ``` python
    timer = Timer()
    # some logic
    print(timer.count().diff())  # some logic 的处理时间
    # some logic 2
    print(timer.count().duration())  # some logic 和 some logic 2 的总共用时
    ```
    """

    unit_factors = {
        'hour': 3600,
        'min': 60,
        'sec': 1,
        'ms': 1 / 1000,
        'us': 1 / 1000000,
    }

    def __init__(self, unit: str = 'sec', precision: int = 2) -> None:
        if unit not in self.unit_factors:
            unit = 'sec'
        self.unit = unit  # 时间的展示单位
        self.precision = precision  # 时间的展示格式，小数点后展示几位
        self.factor = self.unit_factors[self.unit]
        self.begin_time: float = time.time()
        self.end_times: List[float] = []

    def count(self) -> 'Timer':
        """ 计次 """
        now = time.time()
        self.end_times.append(now)
        return self

    def diff(self) -> float:
        """ 计算倒数第一次计次，和倒数第二次计次，的时间差 """
        if len(self.end_times) == 0:
            delta = 0
        elif len(self.end_times) == 1:
            delta = self.end_times[0] - self.begin_time
        else:
            delta = self.end_times[-1] - self.end_times[-2]
        delta /= self.factor
        return delta

    def diff_str(self) -> str:
        """ 计算倒数第一次计次，和倒数第二次计次，的时间差，返回字符串 """
        return self.format_time(self.diff())

    def duration(self) -> float:
        """ 计算最后一次计次，与开始时间，的时间差 """
        if len(self.end_times) == 0:
            return 0
        return self.end_times[-1] - self.begin_time

    def duration_str(self) -> str:
        """ 计算最后一次计次，与开始时间，的时间差，返回字符串 """
        return self.format_time(self.duration())

    def format_time(self, t: float) -> str:
        """ 将 t 格式化，小数点后保留 self.precision 位，并附带时间单位 self.unit """
        formatted_diff = format(t, f".{self.precision}f") + f' {self.unit}'
        return formatted_diff
