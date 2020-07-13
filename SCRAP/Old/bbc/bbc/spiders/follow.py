# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
	name = "quotes"
	start_urls = [
		'http://quotes.toscrape.com/page/1/',
	]

	def parse(self, response):
		for quote in response.css('div.quote'):
			yield {
				'text': quote.css('span.text::text').get(),
				'author': quote.css('small.author::text').get(),
				'tags': quote.css('div.tags a.tag::text').getall(),
			}
		next_page = response.css('li.next a::attr(href)').get()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)
#############################################################
if __name__ == "__main__":
	process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})

	process.crawl(QuotesSpider)
	process.start() # the script will block here until the crawling is finished