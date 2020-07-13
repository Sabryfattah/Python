"""
JASON, YAML and CSV INTERCHANGE
---------------------------------------------------
1- convert csv to jason file 
2- convert jason to dataframe
3- convert dataframe to csv
4- convert yaml to jason file
5- convert jason file to yaml
6- edit jason file and update or delete records
7- Search jason file for a pattern
"""
##################################################
import csv
import re
import json
import simplejson
import sys
import yaml
import pandas as panda
from tabulate import tabulate
import argparse
##############################################
class JSYM():
	def __init__(self, file=None):
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="JSYM <options> [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='csv file')
		self.parser.add_argument('-j2c',"--js2csv", action='store_true', help='convert jason to csv file')
		self.parser.add_argument('-c2j',"--csv2js", action='store_true', help='convert csv to jason')
		self.parser.add_argument('-y2j',"--ym2js", action='store_true', help='convert yaml to jason file')
		self.parser.add_argument('-j2y',"--js2ym", action='store_true', help='convert jason file to yaml')
		self.parser.add_argument('-j2d',"--js2df", action='store_true', help='display jason file as dataframe')
		self.parser.add_argument('-wv',"--w2csv", action='store_true', help='write dataframe of jason to csv')
		self.parser.add_argument('-ej',"--edjs", action='store_true', help='edit jason file and update records')
		self.parser.add_argument('-sj',"--srjs", action='store_true', help='Search jason file for a pattern')
		self.parser.add_argument('-dj',"--deljs", action='store_true', help='delete jason record by key')
		self.args = self.parser.parse_args()
		self.file = self.args.file

	#convert csv to jason file
	def csv2js(self, file):
		csvfile = open(self.file+'.csv', 'r')
		jsonfile = open(self.file+'.json', 'w')
		fieldnames = ('Site', 'Email', 'User', 'Password')
		reader = csv.DictReader(csvfile, fieldnames)
		for row in reader:
			json.dump(row, jsonfile)
			jsonfile.write('\n')

	#convert jason to df and print it as a table
	def jason2df(self, file):
		with open(file+'.json') as f:
			df = panda.pandas.read_json(f, orient='index')
			print(tabulate(df[:10], headers = 'keys', tablefmt='fancy_grid', showindex=True, numalign="left", colalign=("left",)))
		return df

	#write df to csv file
	def write2csv(self, file):
		df = self.jason2df(file)
		filename = input("Name of New CSV File..>>\n")
		df.to_csv(file+".csv", index=True)

	#convert yaml to jason file
	def yaml2jason(self, file):
		with open(file+".yaml", 'r') as yaml_in:
			yml_object = yaml.safe_load(yaml_in)
		with open(file+".json", "w") as json_out:
			json.dump(yml_object, json_out)
	
	#convert jason back to yaml file
	def jason2yaml(self, file):
		with open(file+'.json', 'r') as stream :
				datamap = json.load(stream)
		with open(file+'_bk.yaml', 'w') as output:
			yaml.dump(datamap, output)

	#edit jason records and update fields
	def edit_jason(self, file):
		self.jason2df(file)
		with open(file+'.json', 'r+') as f:
			data = json.load(f)
			column = list(data.keys())[0]
			record = input("Which record to modify ? \n")
			[print(n,e, end='|') for n,e in enumerate(data[column])]
			n = input("Which column number ? \n")
			v = input("New value ? \n")
			data[record][int(n)] = v # <--- add `id` value.
			f.seek(0)        # <--- should reset file position to the beginning.
			json.dump(data, f)
			f.truncate()     # remove remaining part
			
	
	#search jason for a matching regex pattern and show records
	def search_jason(self,file):
		self.jason2df(file)
		table = []
		with open(file+'.json', 'r') as f:
			data = json.load(f)
		patt = input("key to search for ? \n")
		col = list(data.keys())[0]
		table.append([col]+list(data[col]))
		for k in list(data.keys()):
			if re.match(r'(.*|\b)'+patt+'.*', k, re.I):
				table.append([k]+list(data[k]))
		print(tabulate(table, headers = 'keys', tablefmt='fancy_grid', showindex=True, numalign="left", colalign=("left",)))

	#delete a record from jason file
	def del_js_record(self, file):
		key = input("key of record ? \n")
		with open(file+'.json', 'r+') as f:
			data = json.load(f)
			del data[key]
			f.seek(0)        # <--- should reset file position to the beginning.
			json.dump(data, f)
			f.truncate()     # remove remaining part
########################################################
if __name__ == "__main__" :
	j = JSYM()
	ypath = "Data/"
	jpath = "Data/"
	if j.args.csv2js : j.csv2js(file)
	if j.args.js2df : j.jason2df(jpath+j.file)
	if j.args.w2csv : j.write2csv(ypath+j.file)
	if j.args.ym2js : j.yaml2jason(ypath+j.file)
	if j.args.js2ym : j.jason2yaml(ypath+j.file)
	if j.args.edjs : j.edit_jason(ypath+j.file)
	if j.args.srjs : j.search_jason(jpath+j.file)
	if j.args.deljs : j.del_js_record(ypath+j.file)

