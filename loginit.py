# -*- coding: utf-8 -*-
from logging import getLogger, Formatter
from logging.handlers import RotatingFileHandler
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
import os

class SuiteransLoggerManager():
    def __init__(self, name = None, func = None, *args):
        self._logger = getLogger(name + '.' + func.__name__)
        self._func = func
        self._args = args
    def __call__(self, *args):
        try:
            return self._func(*self._args, *args)

        except Exception as e:
            logger.critical(
                "Unexpected error occured. Program Stop...\n"\
                + "{}: {}"
                .format(type(e), e.args)
            )
            logger.exception(e)
            raise

class SuiteransFormatter(Formatter):
    def format(self, record):
        s = super().format(record)
        s = s.replace('\n', '\n' + ' '*8 + '| ')
        return s

SLM = SuiteransLoggerManager
logger = getLogger()
formatter = SuiteransFormatter(
    '{levelname:<8}| {message}', style = '{'
)
handler = RotatingFileHandler('logs/suiterans.log', maxBytes = 65536, backupCount = 3)
handler.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(handler)
