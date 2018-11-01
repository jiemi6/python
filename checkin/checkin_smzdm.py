#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urllib
import time
import os
import logging

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logging.basicConfig(filename = os.path.join(os.getcwd(), 'checkin.log'), level = logging.DEBUG)


def login():
	#zhiyou.smzdm.com checkin
	url = 'https://zhiyou.smzdm.com/user/login/ajax_check'
	headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate,br","Accept-Language":"zh,zh-CN;q=0.9,zh-TW;q=0.8,en;q=0.7"}
	headers['Connection']="keep-alive"
	headers['Cache-Control']="no-cache"
	headers['Content-Type']="application/x-www-form-urlencoded; charset=UTF-8"
	headers['Cookie']="__ckguid=nJb2V4fOtAyiO9GFH6UbnI4; device_id=1948179922152712611046983392cb8c8f6f94335a67e18e804366afb8; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1527126111; zdm_qd=%7B%7D; PHPSESSID=97e84405c0d805f3d9482887009a102e; __jsluid=c737f5d163cd5caa2fff81766c3227c1; _ga=GA1.2.998586185.1527126112; _gid=GA1.2.1628254823.1527126112; _gat_UA-27058866-1=1; smzdm_id=9432792065; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1527126141"
	headers['Host']="zhiyou.smzdm.com" 
	headers['Origin']="https://zhiyou.smzdm.com" 
	headers['Referer']="https://zhiyou.smzdm.com/user/login/window/" 
	headers['Pragma']="no-cache" 		
	headers['User-Agent']="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36"
	headers['Content-Length']="126"
	headers['X-Requested-With']="XMLHttpRequest" 

	requests.packages.urllib3.disable_warnings()  
	r = requests.post(url,headers=headers, data={'username':'13725569993','password':'1987611','rememberme':'1'},verify=False)
	logging.debug(r.status_code)
	#logging.debug(r.headers)
	logging.debug(r.reason)
	# 成功的 {"error_code":0,"error_msg":"","is_use_captcha":false,"data":[],"redirect_to":""}
	#失败的 返回xml 
	#logging.debug("返回信息为："+r.text)
	
	try:
		resO=r.json();
	except BaseException:
		logging.debug("转成json报错了，应该是失败了")
		logging.debug("返回信息为："+r.text)
	else:
		if resO["error_code"]== 0:
			logging.debug("登录成功了")
			cookiesO = r.headers['Set-Cookie']
			
			return r.cookies['sess']
		else :
			logging.debug("登录失败了")
			logging.debug("返回信息为："+str(resO["error_msg"]))


def checkin():
	logging.debug("-----------开始checkin szzdm 。。。")
	loginCookies = login();
	#loginCookies = "N2ZlNDZ8MTUzMTAxMzg5NXw5NDMyNzkyMDY1fGI5MmY1NDkxYzM5M2Q5NDkzY2I1MDExMzhlMWYxN2Nm"
	#now = int(time.time())
	#callBack = "jQuery1124018554895975558328_"+str(now)+"&_="+str(now+2);
	url = 'http://zhiyou.smzdm.com/user/checkin/jsonp_checkin?callback='
	headers = {"Accept":"*/*"}
	headers['Accept-Encoding']="gzip, deflate, sdch"
	headers['Accept-Language']="zh,zh-CN;q=0.8,zh-TW;q=0.6,en;q=0.4" 
	headers['Cache-Control']="no-cache"
	headers['Connection']="keep-alive"
	
	headers['Referer']="http://www.smzdm.com/" 
	headers['Pragma']="no-cache" 
	headers['Host']="zhiyou.smzdm.com" 	
	headers['User-Agent']="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36"

	cookies = {"sess": loginCookies}
	
	cookies["smzdm_user_source"]="488065D7A054F81C7023054C2D821B51"
	cookies["__jsluid"]="a9651ad14be45599402c953f8a9cc4a1"
	cookies["web_ab"]="A1"
	cookies["smzdm_wordpress_360d4e510beef4fe51293184b8908074"]="minkey%7C1476610598%7C9da7223c1f42e93184d186e115cf4513"
	cookies["user-role-smzdm"]="subscriber"
	cookies["user"]="minkey%7C9432792065"
	cookies["web_fx_ab"]="fx18"
	cookies["PHPSESSID"]="796je67dqbn6lt346d4qp29n26"
	cookies["smzdm_user_view"]="AEE63379641CBA318298E08914CBAF00"
	cookies["wt3_eid"]="%3B999768690672041%7C2145336635000030705%232147605933000838921"
	cookies["wt3_sid"]="%3B999768690672041"
	cookies["s_his"]="%E7%AD%BE%E5%88%B0"
	cookies["_gat_UA-27058866-1"]="1"
	cookies["Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58"]="1474520590,1474850120,1474852704,1475888324"
	cookies["Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58"]="1476060384"
	cookies["crtg_rta"]=""
	cookies["_ga"]="GA1.2.2078567401.1453366340"
	
	requests.packages.urllib3.disable_warnings()
	r = requests.post(url,headers=headers,cookies=cookies,verify=False)
	logging.debug(r.status_code)
	#logging.debug(r.headers)
	logging.debug(r.reason)
	
	try:
		resO=r.json();
	except BaseException:
		logging.debug("转成json报错了，checkin应该是失败了")
		logging.debug("返回信息 "+r.text)
	else:
		if resO["error_code"]== 0:
			logging.debug("www.smzdm.com 打卡成功了")			
			logging.debug("返回的信息 ："+str(resO["data"]))
		else :
			logging.debug("打卡失败了")
			logging.debug("返回信息为："+str(resO["error_msg"]))
	
	