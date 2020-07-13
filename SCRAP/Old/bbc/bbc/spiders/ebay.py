""" Use Scrapy to get list of items on ebay webpage """
""" Run Scrapy from this script not console """
##########################################################
import scrapy
from scrapy.crawler import CrawlerProcess
##########################################################
class ProductSpider(scrapy.Spider):
	name = "product_spider"
	allowed_domains = ['ebay.com']
	start_urls = []
	for n in range(1,10):
		url = 'https://www.ebay.com/sch/i.html?_nkw=python&_sacat=0&_from=R40&_pgn={}'.format(n)
		start_urls.append(url)

	def parse(self, response):
		res = response.xpath("//h3[contains(@class,'title')]/text()").extract()
		for item in res:
			print(item)
		
#############################################################
if __name__ == "__main__":
	process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})

	process.crawl(ProductSpider)
	process.start() # the script will block here until the crawling is finished
