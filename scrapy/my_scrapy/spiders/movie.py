# -*- coding: utf-8 -*-
import scrapy


#mkv99 网站地址抓取，网站为了放抓取，吧url写在js中，需要保存html到本地再抓
class MoviveSpider(scrapy.Spider):
		name = "movies"
		allowed_domains = ["www.mkv99.net"]
		start_urls = ["http://localhost/1.html"]


		def parse(self, response):
				for sel in response.xpath('.//input[@name="CopyAddr2"]') :
						print(sel.xpath('@value').extract()[0])
