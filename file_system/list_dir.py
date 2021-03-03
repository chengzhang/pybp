"""find file/subdir ..."""

# coding = utf8

import os
import shutil


def list_1st_file(dir):
    files = os.listdir(dir)
    if len(files) == 0:
        return None
    return os.path.join(dir, files[0])

def clean_dir(dir):
    for path in os.listdir(dir):
        path = os.path.join(dir, path)
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.islink(path):
            os.unlink(path)

def list_dir_files(dir):
    subs = os.listdir(dir)
    files = [path for path in subs if os.path.isfile(path)]
    return files
