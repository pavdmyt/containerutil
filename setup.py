#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
containerutil
~~~~~~~~~~~~~

Tools for inspecting contents of docker container file system.

:copyright: (c) Pavlo Dmytrenko
:license: MIT
"""

import codecs
import os
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


def read_version(package):
    version_path = os.path.join(package, '__version__.py')
    with open(version_path, 'r') as fd:
        for line in fd:
            if line.startswith('__version__ = '):
                return line.split()[-1].strip().strip("'")


version = read_version('containerutil')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests/']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


with codecs.open('README.rst', encoding='utf-8') as fd:
    readme = fd.read()


tests_require = [
    'docker~=2.7.0',
    'pytest~=3.3.2',
]


setup(
    name='containerutil',
    version=version,
    author='Pavlo Dmytrenko',
    author_email='mail@pavdmyt.com',
    license='MIT',
    description='Tools for inspecting contents of docker container filesystem.',  # noqa
    long_description=readme,
    keywords='docker container path pathlib file type filesystem',
    url='https://github.com/pavdmyt/containerutil',
    download_url='https://github.com/pavdmyt/containerutil/archive/master.zip',
    packages=find_packages(exclude=('tests', 'docs', 'examples')),
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    platforms=['any'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
    ],
)
