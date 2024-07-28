"""
命令行入口

Author: donyzhang
Date: 2024.07.10
"""

# coding = utf8

import click
import os
from typing import Optional
from sgame_nlp_data.utils.logger import get_logger
from sgame_nlp_data.utils.file_util import load_text_line_file, dump_text_line_file
from sgame_nlp_data.cleaner.cleaner import Cleaner

logger = get_logger()


@click.group()
def cli():
    pass


@cli.command()
@click.argument("text", type=str, help='要打印的句子')
@click.option("--uppercase", is_flag=False, help='是否要打印大写')
@click.option("--n", type=int, default=1, help='打印几遍')
def filter_entity(
        text: str,
        uppercase: Optional,
        n: Optional,
):
    if uppercase:
        text = text.upper()
    for i in range(n):
        print(text)


if __name__ == '__main__':
    cli()
