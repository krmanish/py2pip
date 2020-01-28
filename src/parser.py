import asyncio
import re

import config
from bs4 import BeautifulSoup


class ParseHTML(object):
    FEATURE = 'html.parser'

    def __init__(self, page, log):
        self.log = log
        self.page = page
        self.all_pkg_versions = {}  # Should be {'3.2': {'url':, '', 'datetime': ''}}

    def get_versions(self):
        return self.all_pkg_versions

    def _strip(self, text):
        return text.strip()  # Removes leading trailing and leading spaces and \n

    async def get_soup(self, content):
        return BeautifulSoup(content, features=self.FEATURE)

    async def __read_versions(self, node):
        version_node = node.find(config.LookupTags.TARGET_VERSION, attrs={'class': config.LookupClass.TARGET_VERSION})

        version = self._strip(version_node.text)

        # Exlude pre-release version
        if re.search('[a-z]+', version):
            return

        url_node = node.find(config.LookupTags.TARGET_URL, attrs={'class': config.LookupClass.TARGET_URL})
        url = config.PIPServer.HOST + url_node.get('href')

        release_date_node = node.find(config.LookupTags.TARGET_TIME)
        datetime_str = release_date_node.get('datetime')

        if version in self.all_pkg_versions:
            self.log.error(f'Error: {version} already exists')
            return

        self.all_pkg_versions[version] = {
            'url': url,
            'datetime': datetime_str
        }

    async def history_page(self, content):
        tasks = []
        soup = await self.get_soup(content)

        release_node_list = soup.find(config.LookupTags.GRAND_PARENT, attrs={'class': config.LookupClass.GRAND_PARENT}).find_all(
            config.LookupTags.PARENT, attrs={'class': config.LookupClass.PARENT})

        for node in release_node_list:
            task = asyncio.ensure_future(self.__read_versions(node))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)

    async def read_py_version(self, li_node, py_version, pkg_version):
        self.log.info(f'Iterate over python verison list')
        for element in li_node.find('ul').find_all('li'):
            version_pack = element.find('a').text.strip()
            matched = re.match('Python\s*::\s*(?P<version>[0-9.]+)\s*(::)?', version_pack)
            if matched:
                remote_py_version = matched.group('version')
                print(f'Matching List try to find..... {remote_py_version} {py_version}')
                if remote_py_version == py_version:
                    self.log.info(f'Matched:  {py_version} {pkg_version}')
                    self.page.stop(pkg_version)

    async def version_page(self, content, py_version, pkg_version):
        tasks = []
        soup = await self.get_soup(content)

        version_ul_node = soup.find('div', attrs={'class': 'vertical-tabs__tabs'}).find(
            'ul', attrs={'class': 'sidebar-section__classifiers'})

        for li in version_ul_node.children:
            # Ignore empty record
            if isinstance(li, str):
                continue
            title = li.find('strong').text.strip()
            if title == 'Programming Language':
                task = asyncio.ensure_future(self.read_py_version(li, py_version, pkg_version))
                tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)

