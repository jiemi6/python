#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import logging

logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)


def job():
    logging.debug('qian tao')
    
 