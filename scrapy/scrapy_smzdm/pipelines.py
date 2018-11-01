# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import settings

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
		    # ͨ��cursorִ����ɾ���
		    self.cursor = self.connect.cursor();


		def process_item(self, item, spider):
				try:
						# ��������
						self.cursor.execute(
						    """REPLACE INTO `zhi_items` (`id`, `title`,`price`,`link`,`zhide`,`buzhi`,`collectNum`,`commentNum`,`publishTime`,`store`,`timesort`) 
						    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
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
						     item['timesort']))

						# �ύsql���
						self.connect.commit()

				except Exception as error:
						# ���ִ���ʱ��ӡ������־
						print error
				return item
        