# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

NAME = "incolumepy.utils"
PACKAGE = NAME
DESCRIPTION = "package incolumepy utils"
AUTHOR = "Ricardo Brito"
AUTHOR_EMAIL = "contato at incolume.com.br"
URL = "http://www.incolume.com.br"
LICENSE = "BSD"
LONG_DESCRIPTION = (
        open('README.rst').read()
        + '\n'
          'Contributors\n'
          '============\n'
        + '\n' +
        open('CONTRIBUTORS.rst').read()
        + '\n'
          'Changes\n'
          '=======\n'
        + '\n' +
        open('CHANGES.rst').read()
        + '\n')
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(exclude=["tests.*", "tests", 'ez_setup']),
    install_requires=[
        'setuptools',
    ],
    # Você pode ver uma lista com todos os classificadores aqui:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
