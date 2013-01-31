# -*- coding: utf-8 -*-
import codecs
import os
import isit

from skjult.logger import stream_logger
if isit.py2:
    from ConfigParser import SafeConfigParser
else:
    from configparser import SafeConfigParser

default_conf = """[settings]
mount_path  = /media
secrets_path = %s/.skjult/secrets
""" % os.getenv('HOME')

def get_conf():
    # Create paths
    user_home = os.getenv('HOME')
    skjult_path = os.path.join(user_home, '.skjult')
    skjult_conf = os.path.join(skjult_path, 'skjult.conf')

    if not os.path.exists(skjult_path):
        stream_logger.info('Create skjult conf folder')
        os.makedirs(skjult_path)
        with codecs.open(skjult_conf, mode='w', encoding='utf-8') as f:
            f.write(default_conf)

    parser = SafeConfigParser()
    parser.read(skjult_conf)

    # Defaults
    if not parser.has_section('settings'):
        parser.add_section('settings')
    if not parser.has_option('settings', 'mount_path'):
        parser.set('settings', 'mount_path', '/media')
    if not parser.has_option('settings', 'secrets_path'):
        parser.set('settings', 'secrets_path', os.path.join(skjult_path, 'secrets'))

    parser.add_section('paths')
    parser.set('paths', 'home', user_home)
    parser.set('paths', 'skjult', skjult_path)
    parser.set('paths', 'conf', skjult_conf)
    parser.set('paths', 'secrets', parser.get('settings', 'secrets_path'))
    parser.set('paths', 'mount', parser.get('settings', 'mount_path'))

    secrets_path = parser.get('paths', 'secrets')

    return parser
