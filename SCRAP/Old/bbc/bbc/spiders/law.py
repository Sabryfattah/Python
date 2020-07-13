"""
Scrapy example: How to follow next pages.
create a list of urls for all pages 
(if they have only the 'number' changed each time a next is clicked.)
then use scrapy to go through the list of urls.
"""
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
	name = "MySpider"
	allowed_domains = ['freshfields.com']
	urls = []
	for n in range(30):
		urls.append("https://www.freshfields.com/en-gb/contacts/find-a-lawyer/?Name=&Service=&Role=&Location=&Office=&Industry=&Page={}".format(n))
	start_urls = urls

	def parse(self, response):
		names = response.xpath(".//div/div/div/div/div/div/a/p/text()").extract()
		#imgs = response.xpath(".//img").extract()
		with open("output.txt", 'a', encoding='utf-8') as f:
			for n in range(len(names)):
				f.write(names[n].strip()+"\n")
##############################################################		
if __name__ == "__main__":
	process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})

	process.crawl(MySpider)
	process.start() # the script will block here until the crawling is finished
