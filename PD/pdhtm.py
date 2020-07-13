""" Get tables from rendered HTML pages 
using Selenium and Pandas """
from selenium import webdriver
from lxml import etree
import requests
import pandas as pd
import urllib
import argparse
##################################################################
class Get_html():
	def __init__(self, url=None):
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="ght <options> url")
		self.parser.add_argument('url',nargs="?", action='store', help='url  to open')
		self.parser.add_argument('-gs', '--getsource', action='store_true', help='get source raw')
		self.parser.add_argument('-df', '--getdfs', action='store_true', help='get dfs')
		self.parser.add_argument('-t', '--tables', action='store_true', help='save tables')
		self.parser.add_argument('-w', '--write', action='store_true', help='write to html')
		self.args = self.parser.parse_args()
		self.url = self.args.url

	def get_source(self):
		browser = webdriver.Firefox()
		page_source = browser.get(self.url)
		html_source = browser.page_source
		print(html_source)
		return html_source

	def write_html(self):
		filename = input("file name for html\n")
		html_source = self.get_source()
		with open("{}.html".format(filename), 'w', encoding="utf-8") as f:
			f.write(html_source)
			
	def html2df(self):
		html_source = self.get_source()
		df_list = pd.read_html(html_source)
		return df_list

	def save_tables(self):
		df_list = self.html2df()
		n = 0
		#Save each tables to a csv file
		for df in df_list:
			print(df)
			print("="*80)
			df.to_csv("test-{}.csv".format(n), index=False, encoding='utf-8')
			n += 1

	def get_xpath(self):
		web = urllib.urlopen('Test.html')
		s = web.read()
		html = etree.HTML(s)
		tr_nodes = html.xpath('//table[@*]/tr')
		header = [i[0].text for i in tr_nodes[0].xpath("th")]
		print(header)
		td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]
		print(td_content)

################################################################
if __name__ == "__main__" :
	GH = Get_html()
	if GH.args.getsource:GH.get_source()
	if GH.args.getdfs:GH.html2df()
	if GH.args.tables:GH.save_tables()
	if GH.args.write:GH.write_html()