#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import os
import logging

logging.basicConfig(filename = os.path.join(os.getcwd(), 'checkin.log'), level = logging.DEBUG)


def checkin():
	logging.debug('---------www.so-kindle.com checkin start... ')
	# www.so-kindle.com checkin
	url = 'https://www.so-kindle.com/loginform'
	r = requests.post(url, data={'account':'minkey','password':'1987611'})
	logging.debug(r.status_code)
	#logging.debug((r.headers)
	logging.debug(r.reason)
	logging.debug(r.json())
	#成功的  {'message': 'SUCCESS!', 'status': 1, 'data': 'https://www.so-kindle.com/'}
	#失败的  {'message: "用户名或者密码错误！", status: -1, data: null}
	resO = r.json();
	if resO['status'] == 1 :
		logging.debug('www.so-kindle.com checkin success ')
	else :
		logging.debug('www.so-kindle.com checkin faild. Msg'+resO['message']);
