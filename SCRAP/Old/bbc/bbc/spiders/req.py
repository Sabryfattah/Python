""" Scrape using: Requests, lxml 
Using XPATH Selectors with html lxml tree"""
#########################################################
import requests
from lxml import html
#######################################################
url = "https://www.amazon.com/b/ref=bhp_brws_awrd?ie=UTF8&node=6960520011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=XZ54QJJE8ZRDQ2DW2C5Z&pf_rd_r=XZ54QJJE8ZRDQ2DW2C5Z&pf_rd_t=101&pf_rd_p=2f0fb499-ec44-47a6-bdfc-74b34c598dbe&pf_rd_p=2f0fb499-ec44-47a6-bdfc-74b34c598dbe&pf_rd_i=283155"
tag = ".//*/ol/li/a"
########################################################
response = requests.get(url)
htm = response.text
tree = html.fromstring(htm)
result = tree.xpath(tag)
for item in result:
	print(item.text)