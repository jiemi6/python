#!/usr/bin/python
# -*- coding: UTF-8 -*-

import traceback
import checkin_sokindle
import checkin_smzdm
import schedule
import time
import logger
logging = logger.logger

logging.debug("系统开始运行了")

# checkin_sokindle.checkin()
# checkin_smzdm.checkin()

def job():
    logging.info('开始执行任务')

    try:
        checkin_smzdm.checkin()
    except BaseException as e:
        logging.debug("checkin_smzdm报错了：" + str(e))
        traceback.print_exc()

    try:
        checkin_sokindle.checkin()
    except BaseException as e:
        logging.debug("checkin_sokindle报错了：" + str(e))
        traceback.print_exc()


# schedule.every(10).seconds.do(job)
schedule.every().day.at("08:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(10000)