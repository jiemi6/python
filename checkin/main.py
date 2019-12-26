#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import logging
import schedule
import time
import traceback
import checkin_sokindle
#import checkin_smzdm

import os
import logging

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#logging.basicConfig(filename = os.path.join(os.getcwd(), 'checkin.log'), level = logging.DEBUG)
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



logging.warn("-----开始运行了")

def job():
	logging.warn("------inf")
	logging.debug("----debug")
#  try:
#  	checkin_smzdm.checkin()
#  except BaseException,e:
#  	logging.debug("checkin_smzdm报错了："+str(e))
#  	traceback.print_exc()

	try:
		checkin_sokindle.checkin()
	except BaseException,e:
		logging.debug("checkin_sokindle报错了："+str(e))
		traceback.print_exc()

#checkin_smzdm.checkin()
checkin_sokindle.checkin()

#schedule.every(10).seconds.do(job)
#schedule.every().day.at("08:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(10000)