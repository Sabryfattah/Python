""" Scrape BBC Site using xpath """
import urllib.request, urllib.error, urllib.parse
from lxml import html
#---------------------------------------------------------------------------------------------
URL = 'https://www.bbc.co.uk/news/'
xp = ".//h3"
#----------------------------------------------------------------------------------------
response = urllib.request.urlopen(URL)
htm = response.read()
tree = html.fromstring(htm)
def show_result(xp):
	result = tree.xpath(xp)
	for i,item in enumerate(result):
		print(i, " : ", item.text)
############################################################
show_result(xp)