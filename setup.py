# -*- coding: utf-8 -*-
# flake8: noqa
# isort:skip_file

# isbnlib-dnb-sru -- an isbnlib plugin that pulls metadata from the
# Deutsche Nationalbibliothek (DNB; German national library) using the
# SRU protocol (see https://www.dnb.de/DE/Professionell/Metadatendienste/Datenbezug/SRU/sru_node.html).
# Copyright (C) 2026  Heiner Walter
#
# This plugin is based on the plugin isbnlib-porbase by:
# Copyright (C) 2018-2019  Alexandre Lima Conde

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from pathlib import Path
import re


ROOT = Path(__file__).parent

def read_version():
    init_file = ROOT / "isbnlib_dnb_sru" / "__init__.py"
    text = init_file.read_text(encoding="utf-8")
    match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]+)[\'"]', text, re.MULTILINE)
    if not match:
        raise RuntimeError("Unable to find __version__ in isbnlib_dnb_sru/__init__.py")
    return match.group(1)


setup(
    name='isbnlib-dnb-sru',
    version=read_version(),
    author='Heiner Walter',
    author_email='',
    url='https://github.com/heinerwalter/isbnlib-dnb-sru',
    download_url='https://github.com/heinerwalter/isbnlib-dnb-sru/archive/v' + read_version() + '.zip',
    packages=['isbnlib_dnb_sru/'],
    entry_points={'isbnlib.metadata': ['dnb-sru=isbnlib_dnb_sru:query']},
    install_requires=[
        "isbnlib>=3.11",  # formerly "isbnlib>=3.10.9,<3.11.0"
    ],
    license='LGPL v3',
    description='A plugin for isbnlib that pulls metadata from the Deutsche Nationalbibliothek (DNB; German national library) using the SRU protocol.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='ISBN isbnlib dnb german bibliographic-references',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
