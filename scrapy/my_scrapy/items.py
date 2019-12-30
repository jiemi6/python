# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SmzdmItem(scrapy.Item):
		articleid = scrapy.Field()
		zhide = scrapy.Field()
		buzhi = scrapy.Field()
		title = scrapy.Field()
		price = scrapy.Field()
		link = scrapy.Field()
		desc = scrapy.Field()
		commentNum = scrapy.Field()
		publishTime = scrapy.Field()
		collectNum = scrapy.Field()
		store = scrapy.Field()
		timesort = scrapy.Field()