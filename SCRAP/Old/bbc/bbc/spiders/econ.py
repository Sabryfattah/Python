""" Download articles from economist site using requests, lxml and BS """
#########################################################
import urllib.request, urllib.error, urllib.parse
import requests
from bs4 import BeautifulSoup as BS
from lxml import html
import argparse
import re
###########################################################
url  = "https://www.economist.com/"
def get_tree(url):
	#response = urllib.request.urlopen(url)
	response = requests.get(url)
	htm = response.text
	tree = html.fromstring(htm)
	return tree, htm

def get_pages(url):
	urls = []
	tree = get_tree(url)[0]
	tag = ".//a[contains(@href, '2019')]/@href"
	result = tree.xpath(tag)
	for item in result:
		if item != "/printedition/2019-04-27":
			urls.append(item)
	return urls

def download():
	urls = get_pages(url)
	for u in urls:
		tree, htm = get_tree("https://www.economist.com"+u)
		text = tree.xpath(".//p")
		for item in text:
			with open("econo.txt", 'a', encoding="utf-8") as f:
				f.write(item.text_content()+"\n")
				f.write("\n")
#############################################################
download()