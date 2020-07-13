"""
Scrapy example to extract titles and summary of BBC NEWS site.
"""
import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):
	name = "MySpider"
	allowed_domains = ['bbc.co.uk/news']
	start_urls = ["https://www.bbc.co.uk/news"]

	def parse(self, response):
		titles = response.xpath(".//h3[contains(@class, 'title')]/text()").extract()
		summary = response.xpath(".//p[contains(@class, 'summary')]/text()").extract()
		with open("output.txt", 'a') as f:
			for n in range(len(titles)):
				f.write(titles[n])
				f.write("\n")
				f.write(summary[n])
				f.write("\n")
				f.write("="*80)
				f.write("\n")
##############################################################		
if __name__ == "__main__":
	process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	})

	process.crawl(MySpider)
	process.start() # the script will block here until the crawling is finished
"""

	def __init__(self):
		self.driver = webdriver.Firefox()
self.driver.get(response.url)
		items = self.driver.find_element_by_xpath(".//a[@data-ctorig]")
		item= items.getAttribute("data-ctorig")
		yield item
		self.driver.close()
		"//h3[contains(@class,'title')]/text()"
from selenium import webdriver
"""
