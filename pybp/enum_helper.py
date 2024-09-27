"""
Enum 类型的便利基类
Author: donyzhang
Date: 2023-06-01
"""

# coding = utf8

from enum import Enum
from functools import lru_cache


class EnumHelper(Enum):

    @classmethod
    @lru_cache
    def names(cls):
        return set(cls._member_names_)

    @classmethod
    @lru_cache
    def values(cls):
        return set(cls._value2member_map_.keys())

    @classmethod
    @lru_cache
    def name_to_value_dic(cls):
        return {k: v.value for k, v in cls._member_map_.items()}

    @classmethod
    @lru_cache
    def value_to_name_dic(cls):
        return {v.value: v.name for k, v in cls._member_map_.items()}

    @classmethod
    def convert_name_to_value(cls, name):
        dic = cls.name_to_value_dic()
        return dic.get(name)

    @classmethod
    def convert_value_to_name(cls, value):
        dic = cls.value_to_name_dic()
        return dic.get(value)

    @classmethod
    @lru_cache
    def name_to_enum_dic(cls):
        return {v.nmae: cls[v.name] for k, v in cls._member_map_.items()}

    @classmethod
    @lru_cache
    def value_to_enum_dic(cls):
        return {v.value: cls[v.name] for k, v in cls._member_map_.items()}

    @classmethod
    def from_name(cls, name):
        n2e_dic = cls.name_to_enum_dic()
        return n2e_dic.get(name)

    @classmethod
    def from_value(cls, value):
        v2e_dic = cls.value_to_enum_dic()
        return v2e_dic.get(value)
