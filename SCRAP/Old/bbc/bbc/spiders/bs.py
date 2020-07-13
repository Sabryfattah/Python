""" Use of urllib2 to get html and beautifulsoup to extract data """
from bs4 import BeautifulSoup as BS
from lxml import html
import urllib.request, urllib.error, urllib.parse
#####################################################################
html = urllib.request.urlopen('http://quotes.toscrape.com/tag/humor/')
soup = BS(html, features="lxml")
authors = soup.findAll('small' , {'class' :'author'})
quotes = soup.findAll('span', {'class' : 'text'})
titles = soup.findAll("title", recursive=True)
for n in range(len(quotes)):
	#print(titles[n])
	print(quotes[n].get_text())
	print(authors[n].get_text())
	print("-"*80)