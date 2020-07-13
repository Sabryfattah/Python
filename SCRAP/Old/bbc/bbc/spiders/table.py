""" Web Scraping using requests and xpath.
"""
from lxml import html
import requests
import argparse
import sys
import re
import textwrap
import numpy
##################################################################
site = { 'bbc' : "https://www.bbc.co.uk/sport/football/premier-league/table",
'panet' : "http://panet.co.il/series/home/30007/1/496839",
'bin' : "https://pastebin.com/search?q=rotana",
'wik' : "https://en.wikipedia.org/wiki/Green_Book_(film)"}
#############################################################
tags = {
			'link' : ".//a/@href", #get all links https://www.
			'img' : ".//img/@src",  #get all images
			'hd3' : ".//a",  #headings of page in h3
			'th' : ".//div/div/div/div/div/div/div/div/div/table/thead/tr/th/abbr/@title",
			'td' : ".//div/div/div/div/div/div/div/div/div/table/tbody/tr/td/a/abbr/@title",
			'tr' : ".//div/div/div/div/div/div/div/div/div/table/tbody/tr/td",
			'par' :  ".//p" #all paragrpahs
			}
########################################################
def get_headings():
	response = requests.get(site['bbc'])
	tree = html.fromstring(response.text)
	items =  tree.xpath(tags['hd3'])
	for item in items:
		print(item.text)
	return tree
##########################################################
def get_table(tree):
	hds = []
	rows = []
	cols = []
	th = ".//div/div/div/div/div/div/div/div/div/table/thead/tr/th/abbr/@title"
	td = ".//div/div/div/div/div/div/div/div/div/table/tbody/tr/td/a/abbr/@title"
	tr = ".//div/div/div/div/div/div/div/div/div/table/tbody/tr/td"
	for item in tree.xpath(th):
		hds.append(item)
	for item in tree.xpath(tr):
		rows.append(item)
	rows =numpy.array([e.text for e in rows])
	rows = numpy.split(rows, 20)
	for item in tree.xpath(td):
		cols.append(item)
	with open("test.csv", 'w') as f:
		f.write("Club,"+ "Number,"+",".join(hds)+" \n") 
		for i in range(20):
			f.write(cols[i]+","+",".join([x for x in rows[i] if x is not None])+"\n")
#######################################################################
if __name__ == "__main__":
	tree = get_headings()
	get_table(tree)