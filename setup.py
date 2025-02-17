#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

from ppadb import __version__

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Testing',
]

setup(
    name='pure-python-adb',
    version=__version__,
    description='Pure python implementation of the adb client',
    long_description=readme + '\n\n' + history,
    author='Swind Ou',
    author_email='swind@cloudmosa.com',
    maintainer='Nicholas Chen',
    maintainer_email='nic562@gmail.com',
    url="https://github.com/nic562/pure-python-adb",
    license='MIT license',
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    install_requires=[],
    extras_require={"async": ["aiofiles>=0.4.0"]},
    keywords="adb",
    classifiers=classifiers,
)
