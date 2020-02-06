======
Py2Pip
======

:language: python

Master package for Py2Pip.
This helps to those who are looking for the package of the supported Py version specially the old one.
since the Python packages has started dropping Py2.7 support with the latest release.

This is the master package for Py2pip using Python3.

It has the following functions:
    1. Required to pass python version and 3rd party package name
    2. Do not log if install as part of pip


Developer notes
===============

All Python dependent packages are part of py2pip dev env.
Code is part of pip installable path.
Basically package is help to find the package that support python2 or python2.7 but it's not limited
It can capable to search the any version of python compatible package.


Setup & Run
===========

    Setup
    =====
    pip install py2pip


    Run
    ===
    As part of python3 local install package.

        ``>> import py2pip``
        ``>> py2pip.process.Py2PIPManager('Django', '2.7').run()``
        ``Django==1.11.28``


Links
=====
Package home page

  http://pypi.python.org/pypi/py2pip

Gihub
    https://github.com/krmanish/py2pip

Issues tracker

  http://jira.onelan.com:8080/secure/RapidBoard.jspa?rapidView=13&projectKey=CMS&view=detail

