# coding: utf-8
import sys

from skjult.core import stream_logger
from skjult.core import manager
from skjult.helpers import confirm
from skjult.exceptions import *

class Cli(object):
	def __init__(self, *args, **kwargs):
		self.args = kwargs
		stream_logger.disabled = False

	def start(self):
		if self.args.get('create', False):
			_name = self.args.get('<name>')
			manager.add_secret(_name)
			sys.exit(0)
		elif self.args.get('mount', False):
			_name = self.args.get('<name>')
			manager.mount_secret(_name)
			sys.exit(0)
		elif self.args.get('umount', False):
			_name = self.args.get('<name>')
			manager.umount_secret(_name)
			sys.exit(0)
		elif self.args.get('list', False):
			_secrets = manager.list_secrets()
			if _secrets:
				stream_logger.info('==> All secrets')
				for _secret in _secrets:
					stream_logger.info(_secret)
			else:
				stream_logger.info('==> No secrets')
			sys.exit(0)
		elif self.args.get('delete', False):
			_secret = self.args.get('<name>')
			stream_logger.info('==> Delete %s secret' % _secret)
			if confirm():
				try:
					manager.delete_secret(_secret)
					stream_logger.info('==> Done')
				except DatabaseException as err:
					stream_logger.info('Error: %s' % err)
					sys.exit(1)
			else:
				stream_logger.info('Abort.')
				sys.exit(1)
			sys.exit(0)
