#!/usr/bin/env python3
"""
Find supported python2 package version... Supply the package it will check and return the correct package name
"""
import aiohttp
import asyncio
import subprocess
import sys

import config
from utils import Logger
from parser import ParseHTML


class Py2PIP(object):

    def __init__(self, project_name, support_py_version, install=False):
        self.package = project_name
        self.install = install
        self.support_py_version = support_py_version
        self.log = Logger()
        self.process = ProcessHistoryPage(self)

    def run(self):
        self.process.start()

        # Return value upon completion
        return self.process.get_support_pkg_version()


class ProcessHistoryPage(object):

    def __init__(self, py2pip_manager):
        self.py2pip_manager = py2pip_manager
        self.log = py2pip_manager.log
        self.support_py_version = py2pip_manager.support_py_version
        self.support_pkg_version = None
        self.found_matched = False

        self.url = config.PIPServer.HOST + config.PIPServer.PATH.format(project=self.py2pip_manager.package)

        self.html_parser = ParseHTML(self, self.log)

    def get_support_pkg_version(self):
        if not self.support_pkg_version or not self.found_matched:
            return
        return f'{self.py2pip_manager.package}=={self.support_pkg_version}'

    def start(self):
        self.log.info(f'Start the loop and so the process')
        self.loop = asyncio.get_event_loop()
        asyncio.ensure_future(self.download_versions())
        self.loop.run_forever()  # close will have no effect if called with run_until_complete
    
    def _close_all_tasks(self):
        self.log.info(f'Close all active tasks')
        i = 1
        for task in asyncio.Task.all_tasks():
            print('Canceling tasks:  ', i)
            i = i+1
            task.cancel()

    def stop(self, pkg_version):
        """ Should be called to find the valid py version otherwise no matching version found"""
        self.log.info(f'Close IO loop started')
        if self.found_matched:
            return

        self.found_matched = True
        self.support_pkg_version = pkg_version

        if self.loop.is_running():
            self._close_all_tasks()
            self.log.info(f'Closing IO loop')
            self.loop.stop()
            self.loop.close()
        sys.exit(255)

    async def process_version_page(self, session):
        version_list = self.html_parser.get_versions()
        if not version_list:
            return

        tasks = []
        for pkg_version, pkg_data in version_list.items():
            url = pkg_data['url']
            print(f'Process Package as follow:  {pkg_version}')
            # task = asyncio.ensure_future(self.read_version_page(session, url, pkg_version))
            # tasks.append(task)
            await self.read_version_page(session, url, pkg_version)
        # await asyncio.gather(*tasks, return_exceptions=True)

    async def read_version_page(self, session, url, package_version):
        """
        Ensure consistency to share the package version as well
        """
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                await self.html_parser.version_page(content, self.support_py_version, package_version)

    async def process_page(self, session, url):
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                await self.html_parser.history_page(content)

    async def download_versions(self):
        async with aiohttp.ClientSession() as session:
            await self.process_page(session, self.url)
            await self.process_version_page(session)
