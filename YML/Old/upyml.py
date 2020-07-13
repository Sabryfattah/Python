"""
update Yaml file by modifying text under a tag in record.
"""
#===============================================
import yaml
import sys, re
#===============================================
path = ""
filename = "t"
file = path+"/"+filename+".yaml"
#==============================================
def read_y():
	with open('{}'.format(file), 'r') as f:
		doc = yaml.load(f)
	return doc
#=======================================================
def update(title, tag, new_text):
	doc = read_y()
	doc[title][tag]['User'] = new_text