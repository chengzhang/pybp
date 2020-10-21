"""define a pretty logger"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format=
    '[%(levelname)-8s %(asctime)-14s.%(msecs)d %(pathname)s %(filename)s %(funcName)s %(lineno)-4d] %(message)s',
    datefmt='%m-%d,%H:%M:%S')
logger = logging.getLogger('mylogger')
