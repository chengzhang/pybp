"""format time to string"""

# coding = utf8

import time
from enum import Enum


class TimeScale(Enum):
    year = 0
    month = 1
    day = 2
    hour = 3
    minute = 4
    second = 5
    ms = 6
    us = 7


def compact_format(from_scale=TimeScale.year.name, to_scale=TimeScale.second.name, separator=''):
    # TODO: perfect implement
    format_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return format_time
