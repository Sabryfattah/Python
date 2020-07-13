#Using Scrapy to scape Linked search page for jobs

import scrapy
from scrapy.crawler import CrawlerProcess
import csv
from itertools import islice
##############################################################
class LinkedPySpider(scrapy.Spider):
	name = 'LinkedPy'
	allowed_domains = ['linkedin.com']
	login_page = 'https://www.linkedin.com/uas/login'
	start_urls = ["https://www.linkedin.com/jobs/search/?keywords=Psychiatry"]

	def parse(self, response):
		title = response.xpath(".//main/section/ul/li/div/h3/text()").extract()
		subtitle = response.xpath(".//main/section/ul/li/div/h4/a/text()").extract()
		location = response.xpath(".//main/section/ul/li/div/div/span/text()").extract()
		#yield {'title' : title, 'subtitle' : subtitle, 'location' : location}
		dict1 = {}
		for n in range(len(title)):
			dict1[str(n)] = {'title' : title[n], 'subtitle' : subtitle[n], 'location' : location[n]}
		cdict = dict(dict1)
		writer = csv.writer(open('linked.csv','w', encoding= "utf-8"))
		headers = ["title", "subtitle", "location"]
		writer.writerow(headers)
		for key, value in cdict.items():
			ln = []
			for ik, iv in value.items():
				ln.append(iv.strip())
			writer.writerow(ln)

###########################################################
if __name__ == "__main__":
	process = CrawlerProcess(
	{'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
	})

	process.crawl(LinkedPySpider)
	process.start()