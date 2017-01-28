# -*- coding: utf-8 -*-
from logging import getLogger, FileHandler
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
logger = getLogger(__name__)
handler = FileHandler('Suiterans.log', mode = 'w')
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
