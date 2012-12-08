#!/usr/bin/env python3
# coding: utf-8
import os

from skjult.logger import stream_logger
from skjult.conf import get_conf
from skjult.helpers import which
from skjult.exceptions import *

# Checks
if not which('encfs'):
	raise CoreException('Need encfs command')
if not which('sudo'):
	raise CoreException('Need sudo command')


conf = get_conf()

from skjult.manager import Manager

manager = Manager()
