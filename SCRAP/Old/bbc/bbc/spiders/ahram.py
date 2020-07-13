"""Selenium is very slow. Download the rendered web page 
then use regex to extract relevant parts. Extract links of all pages 
on first page then download these pages or extract text from them.
This is much faster"""
#############################################################
from selenium import webdriver
import re
from lxml import html
import requests
import time
#############################################################
url= "http://ahram.org.eg/"
file_name = "ahram"
#--------------------------------------------------------------------------------------
#get source page by selenium and write it to text file
def get_source(url):
	driver = webdriver.Firefox()
	driver.get(url)
	elem = driver.find_element_by_xpath("//*")
	source_code = elem.get_attribute("outerHTML")
	f = open(file_name+'.txt', 'w', encoding= "utf-8")
	f.write(source_code)
	f.close()
#-------------------------------------------------------------------
#get links to other pages from source_code
def get_link_list(file_name):
	file = open(file_name+".txt", "r", encoding="utf-8").read()
	pattern = r'(http://www.ahram.org.eg/News/.*aspx)"'
	links = re.findall(pattern, file, re.IGNORECASE)
	link_list = []
	print(links)
	for link in links:
		link_list.append(link)
	return link_list
#----------------------------------------------------------------
#extract text from each page  from the link_list
def extract_elms(link_list):
	elms = []
	titles = []
	for link in link_list:
		page = requests.get(url+link)
		tree = html.fromstring(page.content.decode('UTF-8'))
		elm = tree.xpath(".//p/text()")
		title = link.split("/")[-1]
		title = title.replace('.aspx', '').replace("-", " ")
		elms.append(elm)
		titles.append(title)
	#and write each page to a file
	print(titles)
	file_name = "page_"
	n = 1
	for elm in elms:
		f = open(file_name+str(n)+'.txt', 'a', encoding="utf-8")
		f.write(titles[n-1])
		f.write("\n\n")
		f.write("\n".join(elm))
		f.write("\n\n")
		n += 1
		f.close()
#######################################################
def write_pages(file_name):
	link_list = get_link_list(file_name)
	extract_elms(link_list)
##########################################################
#get_source(url)
write_pages(file_name)
###########################################################
