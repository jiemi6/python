#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urllib
import time
import os
import logging

logging.basicConfig(filename = os.path.join(os.getcwd(), 'lbs.log'), level = logging.DEBUG)


def login():
	#url = 'https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=40&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=18&city=110000&geoobj=116.336582%7C39.89077%7C116.377782%7C39.941394&classify_data=query_type%3DTQUERY%2Breserved_keywords%3Dtrue%3Bcategory%3D160119&user_loc=116.343449%2C39.915428&keywords=%E5%8C%97%E4%BA%AC%E9%93%B6%E8%A1%8C'
	url='https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=2&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=13&city=350200&geoobj=118.061267%7C24.427264%7C118.214045%7C24.547397&keywords=%E5%8E%A6%E9%97%A8%E9%93%B6%E8%A1%8C'
	requests.packages.urllib3.disable_warnings()  
	r = requests.get(url)
	logging.debug(r.status_code)
	#logging.debug(r.headers)
	logging.debug(r.reason)
	# 成功的 {"error_code":0,"error_msg":"","is_use_captcha":false,"data":[],"redirect_to":""}
	#失败的 返回xml 
	
	try:
		resO=r.json();
	except BaseException:
		logging.debug("转成json报错了，应该是失败了")
		logging.debug("返回信息为："+r.text)
	else:
		array=resO["data"]["poi_list"]
		logging.debug("获取成功"+str(len(array)))			
		for item in array:
			logging.debug(item['disp_name']+':'+item['tel']+':'+item['address']+':'+item['longitude']+','+item['latitude'])
		
		
			 
login()