# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import settings
import time
import datetime

class ScrapySmzdmPipeline(object):
    def process_item(self, item, spider):
        return item




class DBPipeline(object):
		def __init__(self):
		    self.connect = pymysql.connect(
						host=settings.MYSQL_HOST,
						port=settings.MYSQL_PORT,
		        db=settings.MYSQL_DBNAME,
		        user=settings.MYSQL_USER,
		        passwd=settings.MYSQL_PASSWD,
		        charset='utf8',
		        use_unicode=True)
		    # 通过cursor执行增删查改
		    self.cursor = self.connect.cursor();


		def process_item(self, item, spider):
				try:
						s1= item['timesort']
						s_str = s1.encode('unicode-escape').decode('string_escape')

						unixtime = int(s_str)//100
						#print unixtime

						dateArray = time.localtime(unixtime)
						unixtimeStr = time.strftime("%Y-%m-%d %H:%M:%S",dateArray)
							
						#print dateArray
						#print unixtimeStr
						# 插入数据
						self.cursor.execute(
						    """REPLACE INTO `zhi_items` (`id`, `title`,`price`,`link`,`zhide`,`buzhi`,`collectNum`,`commentNum`,`publishTime`,`store`,`timesort`,`timeStr`)
						    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""",
						    (item['articleid'],
						     item['title'],
						     item['price'],
						     item['link'],
						     item['zhide'],
						     item['buzhi'],
						     item['collectNum'],
						     item['commentNum'],
						     item['publishTime'],
						     item['store'],
						     item['timesort'],
						     unixtimeStr))

						# 提交sql语句
						self.connect.commit()

				except Exception as error:
						# 出现错误时打印错误日志
						print error
				return item
