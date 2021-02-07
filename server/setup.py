#!/usr/bin/python
# coding=UTF-8
#
# Auto EQ Server
#
# Copyright © 2021 Carl Wilson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Setup details for the Auto EQ Flask server."""
from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'setuptools',
    'flask>=0.12.3',
]
PYTHON_REQUIRES = '>=3.6, <4'

TEST_DEPS = [
    'pre-commit',
    'pytest',
    'pylint',
    'pytest-coverage'
]
EXTRAS = {
    'testing': TEST_DEPS,
}

README = open('README.md', 'r')
README_TEXT = README.read()
README.close()

setup(
    name='autoeq-server',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_DEPS,
    extras_require=EXTRAS,
    python_requires=PYTHON_REQUIRES,
    platforms=['POSIX'],
    description='Convenient web server for AutoEQ settings.',
    long_description=README_TEXT,
    long_description_content_type='text/markdown',
    author='Carl Wilson',
    author_email='',
    maintainer='Carl Wilson',
    maintainer_email='',
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
