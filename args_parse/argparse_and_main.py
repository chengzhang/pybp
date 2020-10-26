"""parse args"""

# coding = utf8

import argparse
from enum import Enum


class ActionEnum(Enum):
    """action enum"""
    info = 1
    build = 2
    remove = 3


def parse_args():
    """parse args for main"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=80, type=int)
    parser.add_argument('--action',
                        type=str,
                        default=ActionEnum.info.name,
                        choices=ActionEnum._member_names_)  # pylint: disable=no-member, protected-access
    main_args = parser.parse_args()
    return main_args


if __name__ == '__main__':
    args = parse_args()
