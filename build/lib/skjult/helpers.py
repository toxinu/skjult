# coding: utf-8
import os

from skjult.logger import stream_logger

def which(file):
    for path in os.environ["PATH"].split(":"):
        if file in os.listdir(path):
            return "%s/%s" % (path, file)
    return False

def confirm(prompt=None, resp=False):
    try:
        if prompt is None:
            prompt = 'Confirm'

        if resp:
            prompt = '%s [%s|%s]: ' % (prompt, 'n', 'Y')
        else:
            prompt = '%s [%s|%s]: ' % (prompt, 'y', 'N')

        while True:
            ans = input(prompt)
            if not ans:
                return resp
            if ans == 'y' or ans == 'Y':
                return True
            if ans == 'n' or ans == 'N':
                return False
            else:
                return False
    except KeyboardInterrupt:
        stream_logger.info('\nAbort.')
        sys.exit(1)
