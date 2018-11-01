# -*- coding: utf-8 -*-
import scrapy
from scrapy_smzdm.items import SmzdmItem


class DmozSpider(scrapy.Spider):
		name = "smzdm"
		allowed_domains = ["www.smzdm.com"]
		start_urls = ["https://www.smzdm.com/p" + str(x) for x in range(1, 20, 1) ]

	
		def parse(self, response):
				for sel in response.css('li.feed-row-wide'):
						toupiaozu = sel.xpath('.//span[@class="unvoted-wrap"]/span/text()').extract()
						articleid = sel.xpath('@articleid').extract()[0]
						#print articleid
						#3打头的才是值不值
						if articleid[0:1] != '3' :
							continue

						zhide = toupiaozu[0]
						buzhi = toupiaozu[1]

						smzdmItem = SmzdmItem()
						# 下划线之后的才是真的id
						smzdmItem['articleid'] = articleid[2:]
						smzdmItem['zhide'] = zhide
						smzdmItem['buzhi'] = buzhi
						smzdmItem['collectNum'] = sel.xpath('.//a[@data-type="fav"]/span/text()').extract()[0].rstrip()
						smzdmItem['commentNum'] = sel.xpath('.//i[@class="z-icon-comment"]/../text()').extract()[1].rstrip()
						smzdmItem['link'] = sel.xpath('h5/a/@href').extract()[0]
						smzdmItem['title'] = sel.xpath('h5/a/text()').extract()[0]
						smzdmItem['price'] = sel.xpath('h5/a/span/text()').extract()[0]
						smzdmItem['publishTime'] = sel.xpath('.//span[@class="feed-block-extras"]/text()').extract()[0].rstrip()
						smzdmItem['store'] =  sel.xpath('.//span[@class="feed-block-extras"]/a/text()').extract()[0]
						smzdmItem['timesort'] = sel.xpath('@timesort').extract()[0]
						
						yield smzdmItem

#mkv99 网站地址抓取，网站为了放抓取，吧url写在js中，需要保存html到本地再抓
class MoviveSpider(scrapy.Spider):
		name = "movies"
		allowed_domains = ["www.mkv99.net"]
		start_urls = ["http://localhost/1.html"]

	
		def parse(self, response):
				for sel in response.xpath('.//input[@name="CopyAddr2"]') :
						print sel.xpath('@value').extract()[0]
						