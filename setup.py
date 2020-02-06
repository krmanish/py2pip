# -*- coding: utf-8 -*-
"""
======
Py2pip
======

Master package for Py2pip
"""
import os
import packaging.version
import re
import sys
import subprocess

from distutils.core import Command
from distutils.command.sdist import sdist as _sdist
from distutils.command.bdist_rpm import bdist_rpm as _bdist_rpm
from setuptools import setup, find_packages


PACKAGE_NAME = 'py2pip'
version = '1.0.0'


class Sdist(_sdist):
    def run(self):
        # unless we update this, the sdist command will keep using the old
        # version
        self.distribution.metadata.version = version
        return _sdist.run(self)

class Bdist_rpm(_bdist_rpm):
    def run(self):
        # unless we update this, the bdist command will keep using the old
        # version
        self.distribution.metadata.version = version
        return _bdist_rpm.run(self)


this_directory = os.path.abspath(os.path.dirname(__file__))

def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

long_description = '\n\n'.join(
    read(*paths) for paths in (('README.rst',),('CHANGES.rst',)))

setup(name=PACKAGE_NAME,
    version=version,
    description="Master package for Py2PIP",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Development Status :: 5 - Production/Stable",
        "Environment :: No Input/Output (Daemon)",
        "Framework :: AsyncIO",
        "Framework :: Scrapy",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    keywords='Developer, Python, Version, Compatibility',
    author='Manish Kumar',
    author_email='kumarmanish890@gmail.com',
    url='http://pypi.python.org/pypi/py2pip',
    license='Other',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "packaging",
        "beautifulsoup4",
        "aiohttp",
    ],
    entry_points={
        'console_scripts': [
            'py2pip=__main__:main',
        ]
    },
    cmdclass={
        "sdist": Sdist,
        "bdist_rpm": Bdist_rpm,
    }
)
