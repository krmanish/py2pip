"""
Define all the constant and hard code value
"""

import enum


SHOW_PRINT = True


class LookupTags():
    GRAND_PARENT = 'div'
    PARENT = 'div'
    TARGET_VERSION = 'p'
    TARGET_URL = 'a'
    TARGET_TIME = 'time'


class LookupClass():
    GRAND_PARENT = 'release-timeline'
    PARENT = 'release'
    TARGET_VERSION = 'release__version'
    TARGET_URL = ['release__card', 'card']  # Precise way to check


class PIPServer():
    HOST = 'https://pypi.org/'
    PATH = 'project/{project}/#history'
