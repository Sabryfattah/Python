""" Straightforward Simple Example of extracting all text in a site:
'Newcastle University Law School' through sitemap
Using urrlib,lxml and xpath
"""
#######################################################
import urllib.request, urllib.error, urllib.parse
from lxml import html
#---------------------------------------------------------------------------------------
url = 'https://www.ncl.ac.uk/nuls/sitemap/'
tag = ".//a/@href"
#--------------------------------------------------------------------------------------
response = urllib.request.urlopen(url)
tree = html.fromstring(response.read())
result = tree.xpath(tag)
for item in result:
	if item.startswith('/nuls'):
		page = urllib.request.urlopen("https://www.ncl.ac.uk/"+item)
		tree = html.fromstring(page.read())
		r = tree.xpath(".//p/text()")
		title = item.replace('/', ' ').split(' ')
		with open("{}.txt".format(title[2]), 'a', encoding="utf-8") as f:
			f.write(title[2])
			f.write("\n\n".join(r))