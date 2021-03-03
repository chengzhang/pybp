"""利用pickle 存储和读取文件"""

# coding = utf8

import pickle

def dump_pickle_file(filename, data):
    """
    :param data: list, dict ...
    """
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_pickle_file(filename):
    """load data from filename"""
    with open(filename, 'rb') as file:
        data = pickle.load(file)
        return data
