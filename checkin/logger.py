#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import logging

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#logging.basicConfig(filename = os.path.join(os.getcwd(), 'checkin.log'), level = logging.DEBUG)
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)

handler = logging.FileHandler("checkin.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


logger.warn("22222222222222")