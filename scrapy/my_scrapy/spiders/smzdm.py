# -*- coding: utf-8 -*-
import scrapy

from my_scrapy.items import SmzdmItem


class SmzdmSpider(scrapy.Spider):
    name = "smzdm"
    allowed_domains = ["www.smzdm.com"]
    start_urls = ["https://www.smzdm.com/p" + str(x) for x in range(1, 3, 1)]

    def parse(self, response):
        for sel in response.css('li.feed-row-wide'):
            toupiaozu = sel.xpath('.//span[@class="unvoted-wrap"]/span/text()').extract()
            articleid = sel.xpath('@articleid').extract()[0]
            # print articleid
            # 3打头的才是值不值
            if articleid[0:1] != '3':
                continue

            zhide = toupiaozu[0]
            buzhi = toupiaozu[1]

            smzdmItem = SmzdmItem()
            # 下划线之后的才是真的id
            smzdmItem['articleid'] = articleid[2:]
            smzdmItem['zhide'] = zhide
            smzdmItem['buzhi'] = buzhi
            smzdmItem['collectNum'] = sel.xpath('.//a[@data-type="fav"]/span/text()').extract()[0].rstrip()
            smzdmItem['commentNum'] = sel.xpath('.//i[@class="icon-comment-o-thin"]/../span/text()').extract()[0]

            smzdmItem['link'] = sel.xpath('.//h5/a/@href').extract()[0]
            smzdmItem['title'] = sel.xpath('.//h5/a/text()').extract()[0]
            # print sel.xpath('.//span[@class="feed-block-extras"]/a/span').extract()[0]
            smzdmItem['price'] = sel.xpath('.//div[@class="z-feed-content"]/div/a/text()').extract()[0]
            smzdmItem['publishTime'] = sel.xpath('.//span[@class="feed-block-extras"]/text()').extract()[0].replace(
                "\n", "").replace("\r", "").strip()
            smzdmItem['store'] = sel.xpath('.//span[@class="feed-block-extras"]/a/span/text()').extract()[0]
            smzdmItem['timesort'] = sel.xpath('@timesort').extract()[0]

            yield smzdmItem