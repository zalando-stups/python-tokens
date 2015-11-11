#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def read_version(package):
    with open(os.path.join(package, '__init__.py'), 'r') as fd:
        for line in fd:
            if line.startswith('__version__ = '):
                return line.split()[-1].strip().strip("'")


__version__ = read_version('tokens')


class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None
        self.pytest_args = ['--cov', 'tokens', '--cov-report', 'term-missing']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='stups-tokens',
    packages=find_packages(),
    version=__version__,
    description='Python library to manage OAuth access tokens',
    long_description=open('README.rst').read(),
    author='Henning Jacobs',
    author_email='henning.jacobs@zalando.de',
    url='https://github.com/zalando-stups/python-tokens',
    license='Apache License Version 2.0',
    setup_requires=['flake8'],
    install_requires=['requests'],
    tests_require=['pytest-cov', 'pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
