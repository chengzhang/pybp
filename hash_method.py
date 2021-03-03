"""some hash method"""

# coding = utf8

import hashlib


def string2numeric_hash(text):
    """return a 4 bytes int"""
    return int(hashlib.md5(text).hexdigest()[:8], 16)
