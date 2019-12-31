#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import logger
logging = logger.logger

def checkin():
	logging.debug('---------skebooks.com checkin start... ')
	# www.so-kindle.com checkin
	url = 'https://skebooks.com/loginform'
	r = requests.post(url, data={'account':'minkey','password':'1987611'})
	logging.debug(r.status_code)
	#logging.debug((r.headers)
	logging.debug(r.reason)
	logging.debug(r.json())
	#成功的  {'message': 'SUCCESS!', 'status': 1, 'data': 'https://www.so-kindle.com/'}
	#失败的  {'message: "用户名或者密码错误！", status: -1, data: null}
	resO = r.json();
	if resO['status'] == 1 :
		logging.debug('skebooks.com checkin success ')
	else :
		logging.debug('skebooks.com checkin faild. Msg'+resO['message']);
