# encoding: utf8

import time
import codecs
from logging.handlers import BaseRotatingHandler
from gunicorn.glogging import Logger as GunicornLogger


class MultiProcessSafeDailyRotatingFileHandler(BaseRotatingHandler):
    def __init__(self, filename, suffix="%Y-%m-%d", encoding=None, delay=False, utc=False, **kwargs):
        self.utc = utc
        self.suffix = suffix
        self.baseFilename = filename
        self.currentFileName = self._compute_fn()
        BaseRotatingHandler.__init__(self, filename, "a", encoding, delay)

    def shouldRollover(self, record):
        if self.currentFileName != self._compute_fn():
            return True
        return False

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        self.currentFileName = self._compute_fn()

    def _compute_fn(self):
        return self.baseFilename + "." + time.strftime(self.suffix, time.localtime())

    def _open(self):
        if self.encoding is None:
            stream = open(self.currentFileName, self.mode)
        else:
            stream = codecs.open(self.currentFileName, self.mode, self.encoding)
        return stream


class CustomGunicornLogger(GunicornLogger):

    def now(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")
