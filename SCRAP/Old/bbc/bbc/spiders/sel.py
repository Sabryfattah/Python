""" Use of selenium headless to download pages from pastebin """
##############################################################
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
#############################################################
class Sel():

	def create_driver(self):
		#Create Driver
		options = FirefoxOptions()
		options.add_argument("--headless")
		driver = webdriver.Firefox(options=options)
		driver.get('https://pastebin.com/search?q=rotana')
		return driver

	def get_source(self, driver):
		#get page source in case you use BS or Regex
		html = driver.page_source
		return html
		
	def get_links(self, driver):
		#find elements matching xpath
		links = driver.find_elements_by_xpath('.//a')
		list = []
		for link in links:
			text = link.get_attribute('data-ctorig')
			if text: list.append(text)
		return list
	
	def write_pages(self, list):
		#open links and save them to files
		for link in list: 
			part = link[-8:]
			response = requests.get("https://pastebin.com/raw/"+part)
			text = response.content
			with open("{}.txt".format(part), 'wb') as f:
				f.write(text)
####################################################################
if __name__ == "__main__":
	s = Sel()
	driver = s.create_driver()
	list = s.get_links(driver)
	print(list)
	s.write_pages(list)

