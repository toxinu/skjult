#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import re

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
def get_version():
    VERSIONFILE = 'skjult/__init__.py'
    initfile_lines = open(VERSIONFILE, 'rt').readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))

if sys.argv[-1] == 'publish':
	os.system('python3 setup.py sdist upload')
	sys.exit()

setup(
	name='Skjult',
	version=get_version(),
	description='## Set description',
	long_description=open('README.rst').read(), 
	license=open('LICENSE').read(),
	author='Geoffrey Lehée',
	author_email='geoffrey@lehee.name',
	url='https://github.com/socketubs/skjult',
	keywords='linux encfs encrypted filesystem',
	packages=['skjult'],
	scripts=['scripts/skjult'],
	install_requires=['docopt==0.5.0'],
	# classifiers=(
	# 		'Development Status :: 5 - Production/Stable',
	# 		'Intended Audience :: Developers',
	# 		'Natural Language :: English',
	# 		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
	# 		'Programming Language :: Python',
	# 		'Programming Language :: Python :: 3',
	# 		'Programming Language :: Python :: 3.0',
	# 		'Programming Language :: Python :: 3.1',
	# 		'Programming Language :: Python :: 3.2',
	# 		'Programming Language :: Python :: 3.3',
	# ),
)
