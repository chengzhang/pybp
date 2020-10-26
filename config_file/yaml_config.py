"""load yaml config file"""

# coding = utf8

import yaml


def load_yml_config(yml_config_file):
    """load yaml config file"""
    configs = {}
    with open(yml_config_file, encoding='utf8') as file:
        configs.update(yaml.load(file))
    return configs
