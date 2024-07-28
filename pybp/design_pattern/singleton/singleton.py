"""
单例装饰器

# Author: donyzhang
# Date: 2022-03-10
"""


def singleton(cls, *args, **kwargs):
    """
    单例装饰器
    """
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
