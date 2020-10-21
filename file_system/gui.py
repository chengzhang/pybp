"""operate filesystem via gui"""

# coding = utf8

from enum import Enum
import argparse
import os
import easygui

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


class ActEnum(Enum):
    """action choices for main()"""
    choose_file = 0
    choose_dir = 1


def choose_file():
    """choose file via gui"""
    filename = easygui.fileopenbox()
    print('file you choose: {}'.format(filename))


def choose_dir():
    """choose dir via gui"""
    path = easygui.diropenbox()
    print('path you choose: {}'.format(path))


def parse_args():
    """parse args for main()"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--act",
        type=str,
        choices=ActEnum._member_names_,  # pylint: disable=no-member, protected-access
        default=ActEnum.choose_file.name)
    main_args = parser.parse_args()
    return main_args


if __name__ == '__main__':
    args = parse_args()
    if args.act == ActEnum.choose_file.name:
        choose_file()
    elif args.act == ActEnum.choose_dir.name:
        choose_dir()
