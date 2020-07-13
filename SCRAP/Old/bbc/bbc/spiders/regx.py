""" Use requests and lxml 
using regular expressions to extract data.
[Extract urls for internet classic radio stations] """
##############################################################
from lxml import html
import requests
import re
#===========================================================
class REGX():
	url2 = "https://www.radionomy.com/en/style/classic/baroque"
	def get_page_content(self) :
		url = "https://www.radionomy.com/en/style/classic/classic"
		page = requests.get(url)
		page_content = page.text
		return  page_content

	def regx_extract(self):
		#enter regex pattern to extract from text of web page
		pattern = r'(http.*?);&quot'
		text = self.get_page_content()
		data_list = re.findall(pattern, text, re.M)
		return data_list

	def print_result(self):
		data_list = self.regx_extract()
		for item in data_list:
			print(item)

	def save2file(self):
		data_list = self.regx_extract()
		filename = input("Filename :  ")
		with open(filename+".txt", 'a') as f:
			for i in data_list:
				f.write(i+"\n")
#####################################################################
if __name__ == "__main__":
	d = REGX()
	d.print_result()