import os
from setuptools import setup, find_packages

NAME = 'incolumepy.utils'
NAMESPACE = NAME.split('.')[:-1]
DESCRIPTION = "package incolumepy utils"
KEYWORDS = 'python utils incolumepy'
AUTHOR = '@britodfbr'
AUTHOR_EMAIL = 'contato at incolume.com.br'
URL = 'http://www.incolume.com.br'
LICENSE = 'BSD'
CLASSIFIERS = '''
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        "Programming Language :: Python",
        'Topic :: Software Development :: Libraries :: Python Modules',
'''
VERSION = open(os.path.join(NAME.replace('.','/'), "version.txt")).read().strip()
LONG_DESCRIPTION = (
        open('README.md').read()
        + '\n'
        +'History\n'
        +'=======\n'
        + '\n' +
        open(os.path.join("docs", "HISTORY.rst")).read()
        + "\n"
        +'Contributors\n'
        +'============\n'
        + '\n' +
        open(os.path.join('docs', 'CONTRIBUTORS.rst')).read()
        + '\n'
        +'Changes\n'
        +'=======\n'
        + '\n' +
        open(os.path.join('docs', 'CHANGES.rst')).read()
        + '\n')

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,

      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          CLASSIFIERS
      ],
      keywords=KEYWORDS,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      namespace_packages=NAMESPACE,
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      test_suite='nose.collector',
      tests_require='nose',
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'pytest',
          'nose'
      ],
      entry_points={
          'console_scripts': [
              'checkinterval = incolumepy.checkinterval.Check:Check.main',
              'interval = incolumepy.checkinterval.Check:Check.interval'
          ],
          'gui_scripts': [
              'baz = my_package_gui:start_func',
          ],
      },

      # entry_points="""
      ## -*- Entry points: -*-

      # [distutils.setup_keywords]
      ##paster_plugins = setuptools.dist:assert_string_list

      # [egg_info.writers]
      ##paster_plugins.txt = setuptools.command.egg_info:write_arg
      # """,
      # paster_plugins = [''],
      )