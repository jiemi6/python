#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import logging
import traceback
import checkin_sokindle
import checkin_smzdm

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logging.basicConfig(filename = os.path.join(os.getcwd(), 'checkin.log'), level = logging.DEBUG)

print "开始运行了"

import schedule
import time
def job():

  logging.debug('开始执行任务')
  
  try:
  	checkin_smzdm.checkin()
  except BaseException,e:
  	logging.debug("checkin_smzdm报错了："+str(e))
  	traceback.print_exc()

  try:
  	checkin_sokindle.checkin()
  except BaseException,e:
  	logging.debug("checkin_sokindle报错了："+str(e))	
  	traceback.print_exc()

#checkin_smzdm.checkin()
 
#schedule.every(10).seconds.do(job)
schedule.every().day.at("8:30").do(job)
 
while True:
    schedule.run_pending()
    time.sleep(10000)