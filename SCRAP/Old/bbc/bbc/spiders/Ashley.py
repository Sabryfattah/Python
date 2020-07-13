from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#############################################################

url = 'https://www.ashleyfurniture.com/c/furniture/'
def get_page(url):
	driver = webdriver.Firefox()
	driver.get(url)
	return driver

def get_names(url):
	driver = get_page(url)
	list =  driver.find_elements_by_xpath(".//div/div/div/section/div/div/ul/li/a/h3") 
	for item in list:
		print(item.text)

###########################################################
get_names(url)