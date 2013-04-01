# coding: utf-8
import os
import shutil

from skjult.core import conf
from skjult.core import user
from skjult.logger import stream_logger
from skjult.exceptions import *

class Manager(object):
	def __init__(self):
		self.mount_path = os.path.join(conf.get('paths', 'mount'), user)
		self.secrets_path = conf.get('paths', 'secrets')
		self.home = conf.get('paths', 'home')

		if not os.path.exists(self.secrets_path):
			os.makedirs(self.secrets_path)

	def _is_secret(self, name):
		base_path = os.path.join(self.secrets_path, name)
		secret_mount_path = os.path.join(self.mount_path, name)

		if os.path.exists(os.path.join(base_path, '.encfs6.xml')) or os.path.exists(os.path.join(secret_mount_path, '.skjult')):
			return True
		return False

	def add_secret(self, name):
		base_path = os.path.join(self.secrets_path, name)
		secret_mount_path = os.path.join(self.mount_path, name)

		if os.path.exists(base_path) and self._is_secret(name):
			raise DatabaseException('This secret already exists')
		elif os.path.exists(base_path) and os.listdir(base_path):
			raise DatabaseException('Something is wrong in secrets dir')
		elif os.path.exists(base_path) and not os.listdir(base_path):
			shutil.rmtree(base_path)

		stream_logger.info('==> Create new secret')
		os.makedirs(base_path)
		self.mount_secret(name)
		try:
			open(os.path.join(secret_mount_path, '.skjult'), 'w').close()
		except:
			raise DatabaseException('Problem during new secret creation (.skjult not created)')

		if not self._is_secret(name):
			raise DatabaseException('Problem during new secret creation')

	def delete_secret(self, name):
		secret_mount_path = os.path.join(self.mount_path, name)

		if not name in self.list_secrets():
			raise DatabaseException('This secret dit not exists')
		shutil.rmtree(os.path.join(self.secrets_path, name))
		os.system('sudo umount %s' % secret_mount_path)
		if os.path.exists(secret_mount_path):
			if not os.listdir(secret_mount_path):
				os.system('sudo rm -r %s' % secret_mount_path)

	def mount_secret(self, name):
		base_path = os.path.join(self.secrets_path, name)
		secret_mount_path = os.path.join(self.mount_path, name)

		if not name in self.list_secrets():
			raise DatabaseException('This secret dit not exists')

		if not os.path.exists(secret_mount_path):
			os.system('sudo mkdir %s' % secret_mount_path)
			os.system('sudo chown %s %s' % (user, secret_mount_path))
			rt = os.system('encfs %s %s' % (base_path, secret_mount_path))
			if rt > 0:
				os.system('sudo rm -r %s' % secret_mount_path)
		else:
			raise DatabaseException('Secret or something else already mounted')

	def umount_secret(self, name):
		base_path = os.path.join(self.secrets_path, name)
		secret_mount_path = os.path.join(self.mount_path, name)

		if not name in self.list_secrets():
			raise DatabaseException('This secret dit not exists')

		if not os.path.exists(secret_mount_path):
			raise DatabaseException('This secret is not mounted')

		if not os.path.exists(os.path.join(secret_mount_path, '.skjult')):
			raise DatabaseException('This secret is not mounted')

		os.system('sudo umount %s' % secret_mount_path)
		if not os.listdir(secret_mount_path):
			os.system('sudo rm -r %s' % secret_mount_path)
		else:
			raise DatabaseException('Secret not cleanly umounted')

	def list_secrets(self):
		return os.listdir(self.secrets_path)
