""" Using Requests and lxml to scrape a site """
from lxml import html
import requests
##############################################################
url = 'http://quotes.toscrape.com/tag/humor/'
#############################################################
class REQX():
	# use requests to open url and use lxml to create tree from page content
	def get_tree(self):
		page = requests.get(url)
		tree = html.fromstring(page.content)
		return tree

	#use xpath to extract specific content'
	def extract_data(self):
		quote = self.get_tree().xpath(".//span[@class='text']/text()")
		author = self.get_tree().xpath(".//small[@class='author']/text()")
		return (quote,author)

	def save2file(self, data):
		file = input("Name of file to save to :   >>" )
		with open(file+".txt", 'w') as f:
			f.write(data)
			
###########################################################################
if __name__ == "__main__":
	#create an object from class REQX
	x = REQX()
	tree = x.get_tree()
	data = x.extract_data()
	for n in range(len(data[0])):
		print(data[0][n])
		print(data[1][n])
		print("="*80)