# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    with open("README.md", "r") as fh:
        long_description = fh.read()
else:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name='neutrino_api',
    version='3.4.5',
    description='The general-purpose API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Neutrino API',
    author_email='tech@neutrinoapi.com',
    url='https://www.neutrinoapi.com/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ]
)