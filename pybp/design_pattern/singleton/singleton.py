"""
单例装饰器

# Author: donyzhang
# Date: 2022-03-10
"""


def singleton(cls):
    """
    单例装饰器，支持多线程环境并允许传递参数。
    """
    instances = {}
    import threading
    lock = threading.Lock()

    def _singleton(*args, **kwargs):
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
