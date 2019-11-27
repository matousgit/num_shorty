#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('pandoc --from=markdown --to=rst -o README.rst README.md')
    os.system('python setup.py sdist upload')
    sys.exit()

README = open('README.rst').read()

setup(
    name='num_shorty',
    version='1.0.1',
    description="Converts an integer to a hexdigest like string - except not 16 length but provided alphabet length",
    long_description=README,
    author='Matouš Höschl',
    packages=[
        'num_shorty',
    ],
    package_dir={'num_shorty': 'num_shorty'},
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    entry_points={
    },
    download_url='https://github.com/matousgit/num_shorty/archive/1.0.1.tar.gz',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
)
