======
Py2Pip
======

#Role
   * language: **python**
   * Version:  **3**

Master package for Py2Pip.


Motivation
==========
Python Package has started dropping [Python 2.7](https://docs.python.org/2/index.html) support.
And It's quite obvious(at least happens in my project) that those packages are used (as part of
requirements.txt) without version. And when we install those package again, we exprience the error like
    
    zipp requires Python '>=3.6' but the running Python is 2.7.13  # Zip wit latest release drops Py2 support
 
Therefore, to get the right Py2.7 supported version, we used to visit the pypi site and browse all the released version
and scan through the page to get the support version of it. This is a tedious and time consuming process.
Hence I got this idea to wirte a small script to get rid of that manuall effort.  

Purpose
======
This helps to those who are looking for the package of the supported Py version specially the old one.
since the Python packages has started dropping Py2.7 support with the latest release.

This is the master package for Py2pip using Python3.

It has the following functions:
    1. Required to pass python version and 3rd party package name
    2. Do not log if install as part of pip


Developer notes
===============
This package is an help to find the package that support python2 or python2.7 but it's not limited to.
It's capable of to search the any version of python compatible package.

All Python dependent packages are part of py2pip dev env. Code is part of pip installable path.
Package is written in Python3.7 so needs System or virtual env to have these packages installed.
1.  Python3
2.  Python3 Devel
3.  python3-setuptools
4.  systemd-devel
5.  beautifulsoup4
6.  aiohttp
7.  packaging  


Setup & Install
===========
    pip install py2pip


Usage
===
    >> import py2pip
    >> py2pip.process.Py2PIPManager('Django', '2.7').run()
        Django==1.11.28


Links
=====
Package home page

  http://pypi.python.org/pypi/py2pip

Gihub
    https://github.com/krmanish/py2pip

Issues tracker

