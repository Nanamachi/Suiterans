# -*- coding: utf-8 -*-
from logging import getLogger
from logging.handlers import RotatingFileHandler
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
import os
logger = getLogger(__name__)
handler = RotatingFileHandler('logs/suiterans.log', maxBytes = 65536, backupCount = 3)
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
