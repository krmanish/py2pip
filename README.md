The py2pip module provides an api to get the latest package of the supported version.

Master repo: https://github.com/krmanish/py2pip



Motivation
==========
Python Package has started dropping [Python 2.7](https://docs.python.org/2/index.html) support.
And It's quite obvious(at least happens in one of my project) that those packages are used (as part of
requirements.txt) without version. And when we install those package again, we experience the error like

    zipp requires Python '>=3.6' but the running Python is 2.7.13  # Zip with latest release drops Py2 support

Therefore, to get the right Py2.7 supported version, we used to visit the pypi site and browse all the released version
and scan through the page to get the support version of it. This is a tedious and time consuming process.
Hence I got this idea to write a small script to get rid of that manual effort.


Purpose
=======
This helps to those who are looking for the package of the supported Py version specially the old one.
since the Python packages has started dropping Py2.7 support with the latest release.

This is the master package for Py2pip using Python3.

It has the following functions:
    1. Required to pass python version and 3rd party package name
    2. Log will work only if executed as a standalone script.
    3. Log path dir: ~/.local/py2pip/


Installation
============
To install py2pip, type::

    pip install py2pip


Development
===========
This package is an help to find the package that support python2 or python2.7 but it's not limited to.
It's capable of to search any versions of python.

All Python dependent packages are part of py2pip dev env. Code is part of pip installable path.
Package is written in Python3.7 so needs System or virtual env to have these packages installed.
1.  Python3
2.  Python3 Devel
3.  python3-setuptools
4.  systemd-devel
5.  beautifulsoup4
6.  aiohttp
7.  packaging

Usage
=====

```
>> import py2pip
>> py2pip.process.Py2PIPManager('Django', '2.7').run()

    Django==1.11.28
```

**Using CLI:**

```
>> python3 -m py2pip --py-version 2.7 -p mock

    Execution time: 2.062346935272217
    Supported Version: mock==3.0.5

```


Links
=====
Package home page::

  http://pypi.python.org/pypi/py2pip
