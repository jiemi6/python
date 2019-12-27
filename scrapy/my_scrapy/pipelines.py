# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings
import time
import datetime

class MyScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class Smzdm_DBPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.get('MYSQL_HOST'),
            port=settings.get('MYSQL_PORT'),
            db=settings.get('MYSQL_DBNAME'),
            user=settings.get('MYSQL_USER'),
            passwd=settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            timesort = item['timesort'].encode('unicode-escape').decode('string_escape')
            dateArray = time.localtime(int(timesort))

            publishTime = item['publishTime']
            if len(publishTime) == 5:
                ymdStr = time.strftime("%Y-%m-%d", dateArray)
                publicTime = '%s %s' % (ymdStr, publishTime)
            elif len(publishTime) == 11:
                yStr = time.strftime("%Y", dateArray)
                publicTime = '%s-%s' % (yStr, publishTime)

            timesort2date = time.strftime("%Y-%m-%d %H:%M:%S", dateArray)
            print(timesort2date)
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
                 publicTime,
                 item['store'],
                 item['timesort'],
                 timesort2date))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item
