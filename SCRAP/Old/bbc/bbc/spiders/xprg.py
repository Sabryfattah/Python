""" Simple Scraper to get links from a web site 
Use urllib2 to open url and get response
read response and convert it to doc using lxml.html to get tree
Search tree using regexp or xpath to get all the links
"""
#=============================================================================
# REQUIRED MODULES
from lxml import html
import requests
import argparse
import sys
import re
import textwrap
import urllib.request, urllib.error, urllib.parse
#==============================================================
url = "https://www.bbc.co.uk"
def get_tree(url):
	response = urllib.request.urlopen(url)
	page = response.read()
	tree = html.fromstring(page)
	return tree, page

def regexp(url):
	page = get_tree(url)[1]
	result = re.findall(r'href="(.*?)"', page.decode(), re.DOTALL)
	for item in result:   #filter : return only links ending in digits
		if item[-1].isdigit():
			print(item)

def expath(tree):
	xp = ".//a/@href"
	elements = tree.xpath(xp)
	links =  [e for e in elements] #remove unicode characters
	for e in links: 
		print(e)
		print("="*80)
###########################################################################
if __name__ == "__main__":
	tree, page = get_tree(url)
	#expath(tree)
	regexp(url)