#!/usr/bin/env python3

import argparse
import logging
import time
import sys

from logging.handlers import RotatingFileHandler

import config
from process import Py2PIPManager


MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MiB
MAX_BACKUP_FILE = 5


def get_logger():
    """
    Creates a rotating log
    """
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger("Py2pip handler")
    logger.setLevel(logging.DEBUG if config.DEBUG else logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(str(config.PATH_LOG_FILE), maxBytes=MAX_FILE_SIZE, backupCount=MAX_BACKUP_FILE, encoding='UTF-8')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

log = get_logger()

def options():
    parser = argparse.ArgumentParser('Verify-And-Install-Package')
    parser.add_argument('-i', '--install', action='store_true',
            help="Pass if you want to install package of supported Python version")
    parser.add_argument('-v', '--version', dest='support', type=str, required=True,
            help="Find Support Python Version i.e 2.7, 2.6, 3.1, 3.5 etc.")
    parser.add_argument('-p', '--package', type=str, help="Python Package Name registered to PIP", required=True)
    
    args = parser.parse_args()
    return args


def main():
    try:
        option = options()
        if not option.support:
            return
        py2pip_manager = Py2PIPManager(log, option.package, option.support, option.install)
        
        stime = time.time()
        result = py2pip_manager.run()
        etime = time.time()
        print(f'Support Version: {result}\nExecution time: {etime - stime}')

    except ValueError as e:
        log.exception(f'Error: {str(e)}')

if __name__ == '__main__':
    sys.exit(main())
