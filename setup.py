"""
安装脚本

Author: donyzhang
Date: 2024-07-10
Update: 2024-07-10
"""

# coding = utf8

import os

from setuptools import find_packages, setup

current_dir = os.path.dirname(os.path.realpath(__file__))


def requirements():
    packages = []
    with open(os.path.join(current_dir, 'requirements.txt')) as ins:
        for line in ins:
            line = line.strip()
            if line and not line.startswith('#'):
                packages.append(line)
    return packages


def readme():
    with open(os.path.join(current_dir, 'README.md')) as ins:
        description = ins.read()
        return description


setup(
    name='pybp',
    version='0.0.1',
    description='my commonly used skills',
    long_description=readme(),
    keywords='bp, bestpractise, utils, common, wheel',
    project_urls={
        'Documentation': 'https://github.com/chengzhang/pybp/README.md',
        'Source': 'https://github.com/chengzhang/pybp',
        'Tracker': 'https://github.com/chengzhang/pybp/issue',
    },
    entry_points={
        'console_scripts': [
            'pybp = bin.command:cli'
        ]
    },
    packages=find_packages(),
    package_data={'pybp': ['config/settings.json']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Natural Language :: Chinese',
    ],
    url='https://github.com/chengzhang/pybp',
    author='Zhang Cheng',
    author_email='zhangwpc@gmail.com',
    tests_require=['pytest'],
    install_requires=requirements(),
    python_requires='>=3.8, <4',
    zip_safe=False
)
