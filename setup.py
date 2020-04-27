#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='academico',
    description='A web api to consume QAcademico data',
    long_description=readme,
    version='0.1.0',
    url='https://github.com/giancarlopro/academico',
    license='MIT',
    author='Giancarlo Rocha',
    author_email='giancarloiff@gmail.com',
    install_requires=[
        'requests>=2.9.1'
    ],
    python_requires='>=3.5',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True
)
