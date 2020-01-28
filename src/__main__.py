#!/usr/bin/env python3

import argparse
import time
import sys

from py2pip import Py2PIP


def options():
    parser = argparse.ArgumentParser('Verify-And-Install-Package')
    parser.add_argument('-i', '--install', action='store_true', help="Install package")
    parser.add_argument('-s', '--support', type=str, help="Find Support Python Version, 2.7, 2.6, 3.1, 3.5 etc.")
    parser.add_argument('-p', '--package', type=str, help="Package Name", required=True)
    
    args = parser.parse_args()
    return args


def main():
    try:
        option = options()
        if not option.support:
            return

        py2pip_manager = Py2PIP(option.package, option.support, option.install)
        
        stime = time.time()
        result = py2pip_manager.run()
        etime = time.time()
        print(f'Support Version is {result}  took time {etime - stime}')

    except ValueError as e:
        print('Error: {}'.format(str(e)))

if __name__ == '__main__':
    sys.exit(main())

