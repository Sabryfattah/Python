# -*- coding: utf-8 -*-
import scrapy


class BbcspiderSpider(scrapy.Spider):
    name = 'bbcSpider'
    allowed_domains = ['https://www.bbc.co.uk/news']
    start_urls = ['https://www.bbc.co.uk/news/']

    def parse(self, response):
        headlines= response.xpath("//p[contains(@class,'title')]/text()").extract()
        yield {'Headlines': headlines}

