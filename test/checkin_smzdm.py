#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urllib
import time
import os
import logging

logging.basicConfig(filename = os.path.join(os.getcwd(), 'checkin.log'), level = logging.DEBUG)


def login():
	#zhiyou.smzdm.com checkin
	url = 'https://zhiyou.smzdm.com/user/login/ajax_check'
	headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh,zh-CN;q=0.8,zh-TW;q=0.6,en;q=0.4"}
	headers['Connection']="keep-alive"
	headers['Cache-Control']="no-cache"
	headers['Content-Type']="application/x-www-form-urlencoded; charset=UTF-8"
	headers['Cookie']="smzdm_user_source=488065D7A054F81C7023054C2D821B51; __jsluid=a9651ad14be45599402c953f8a9cc4a1; web_ab=A1; web_fx_ab=fx18; smzdm_user_view=AEE63379641CBA318298E08914CBAF00; wt3_eid=%3B999768690672041%7C2145336635000030705%232147641261800805520; smzdm_collection_youhui=6504162; s_his=%E7%AD%BE%E5%88%B0%2C%E7%9B%B4%2C%E7%BA%B8%2CGoPro%20HERO4; comment_rating=%5B%5B74823071%2C1%5D%5D; wiki_support=%5B%22m5r643%22%5D; PHPSESSID=lfbkp3odrhrlounec0ke470gu4; _gat_UA-27058866-1=1; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1474850120,1474852704,1475888324,1476665615; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1476667645; _ga=GA1.2.2078567401.1453366340"
	headers['Host']="zhiyou.smzdm.com" 
	headers['Origin']="https://zhiyou.smzdm.com" 
	headers['Referer']="https://zhiyou.smzdm.com/user/login/window/" 
	headers['Pragma']="no-cache" 		
	headers['User-Agent']="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36"
	headers['X-Forwarded-For']="8.8.4.4"
	headers['X-Requested-With']="XMLHttpRequest" 

	requests.packages.urllib3.disable_warnings()  
	r = requests.post(url,headers=headers, data={'username':'13725569993','password':'1987611','rememberme':'1'},verify=False)
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
		if resO["error_code"]== 0:
			logging.debug("登录成功了")			
			cookiesO = r.headers['Set-Cookie']
			
			return r.cookies['sess']
		else :
			logging.debug("登录失败了")
			 


def checkin():
	logging.debug("开始checkin szzdm 。。。")
	loginCookies = login();
	
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
	
	