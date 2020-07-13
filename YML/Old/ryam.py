"""Read and edit YAML FILE :
1- search for tag text
2- delete records
3- update record data
"""
#===============================================
import yaml
import sys, re
#===============================================
path = ""
filename = sys.argv[1]
file = path+"/"+filename+".yaml"
#===============================================
""" get doc dictionary """
def read_y():
	with open('{}'.format(file), 'r') as f:
		doc = yaml.load(f)
	return doc
#==================================================
""" get records in sequence each as a list of dictionaries """
def records():
	doc = read_y()
	records = list(doc.values())
	return records
#===================================================
""" find text of tag in record with given title """
def find(title,tag):
	doc = read_y()
	titles = list(doc.keys())
	records = list(doc.values())
	print(("{:<15}{:<10}{:<10}".format("title","Tag", "Data")))
	for i, title in enumerate(titles):
		for x, record in enumerate(records):
			if title in titles and tag in record[-1][1]:
				print(("="*50))
				print(("{:<15}{:<10}{:<10}".format(title, tag, records[i][x][tag])))

#====================================================
find(sys.argv[2], sys.argv[3])