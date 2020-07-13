"""
YAML FILE PROCESSING:
======================
Yaml files are dictionaries with unique keys.
*(There are no duplicate keys with same value)*
ALL KEYS SHOULD BE UNIQUE
1- print yaml file as a table using Pandas dataframe
2- Write yaml file into csv file
3- Convert csv file to yaml file
4- Search Yaml file for records and print them
5- Update yaml file
6- Sort yaml file
7- Delete records from yaml file
8- Insert record into Yaml File
"""
#========================================================
from jsn import *
import csv
#-----------------------------------------------------------------------
import yaml
import argparse
import pandas as panda
from tabulate import tabulate
from collections import OrderedDict
#####################################################
class YML():

	def __init__(self):
		self.parser = argparse.ArgumentParser(
			description = __doc__,
			formatter_class=argparse.RawDescriptionHelpFormatter,
			usage = "yml [options] <file>")
		self.parser.add_argument("file", action = "store", help="Yaml file to open")
		self.parser.add_argument("-s", "--search", action = "store_true",  help="Search file for record containing pattern")
		self.parser.add_argument("-t",  "--table", action = "store_true", help="print all records in formatted table")
		self.parser.add_argument("-w",  "--w2csv", action = "store_true", help="write to csv file")
		self.parser.add_argument("-d",  "--delrec", action = "store_true", help="delete record from yaml file")
		self.parser.add_argument("-i",  "--insrec", action = "store_true", help="insert record to yaml file")
		self.parser.add_argument("-u",  "--update", action = "store_true", help="update text in record")
		self.parser.add_argument("-sr",  "--sort", action = "store_true", help="sort yaml file")
		self.parser.add_argument("-c2y",  "--csv2yml", action = "store_true", help="convert csv to yaml file")
		self.args = self.parser.parse_args()
		self.file = self.args.file

	"open yaml file into dict (doc)"
	def get_doc(self, file):
		with open('{}'.format(file), 'r') as f:
			doc = yaml.safe_load(f)
		return doc

	"print doc dictionary as a table using Pandas dataframe"
	def read_yml(self, file):
		doc = self.get_doc(file)
		cols =[",".join(e.keys()) for e in doc[list(doc.keys())[0]]]
		df = panda.DataFrame.from_dict(doc, orient='index', columns = cols)
		df = df.applymap(lambda x: list(x.values())[0])
		df = df.sort_index()
		total = df.sum(numeric_only=True)
		print(tabulate(df, headers = 'keys', tablefmt='fancy_grid', showindex=True, numalign="left", colalign=("left",)))
		print(total)
		return df

	"Write yaml file into csv file"
	def write2csv(self, file):
		df = self.read_yml(file)
		with open('file.csv', 'w') as outfile:
			df.to_csv(outfile, line_terminator='\n', index=True, header=True)

	"Search Yaml file for records and print them"
	def search_records(self, file):
		"get record as dictionary"
		doc = self.get_doc(file)
		keys = list(doc.keys())
		patt = input("Enter Regex pattern :\n")
		print("="*80)
		for item in keys:
			if re.match(r'.*%s.*' % patt, item, re.I):
				print(item)
				for s in doc[item]:
					print("{:<15} : {}".format(list(s.keys())[0], list(s.values())[0]))
				print("="*80)

	"Delete records from yaml file"
	def del_record(self, file):
		doc = self.get_doc(file)
		print(doc)
		records = list(doc.keys())
		selected = []
		pat = input("pattern in record name ?\n")
		for record in records:
			if re.match(r'.*'+pat+'.*', record, re.I):
				print(record)
		to_del = input("record name to delete ?\n")
		answer = input("Do you want to delete record {} ?   ".format(to_del))
		if answer in ['yes', 'y', 'Yes', 'Y']:
			del doc[to_del]
			print(doc)
			with open(file, 'w') as yaml_file:
				yaml_file.write(yaml.dump(doc, default_flow_style=False))
		else:
			print("Nothing deleted")
			exit

	"Insert record into Yaml File"
	def insert_rec(self, file):
		doc = self.get_doc(file)
		cols =[",".join(e.keys()) for e in doc[list(doc.keys())[0]]]
		new_key = input("Enter new Title :\n>")
		new_record = {}
		values = []
		for col in cols:
			val = input("value for %s : " % col)
			values.append({"{}".format(col) : "{}".format(val)})
		doc[new_key] = values
		print(doc)
		with open(file, 'w') as yaml_file:
				yaml_file.write(yaml.dump(doc, default_flow_style=False, tags = False))

	"Update records in Yaml File"
	def update_rec(self, file):
		doc = self.get_doc(file)
		records = list(doc.keys())
		rec = input("Which record to modify : \n{}\n>>".format(records))
		cols =[",".join(e.keys()) for e in doc[list(doc.keys())[0]]]
		[print(i,':',e, end='|') for i,e in enumerate(cols)]
		print()
		col = input("Select column Number to update : \n")
		to_update = doc[rec][int(col)][cols[int(col)]]
		print("Text to update :"+to_update)
		new_text = input("New text : \n")
		doc[rec][int(col)] = {cols[int(col)] : new_text}
		print(doc)
		with open(file, 'w') as yaml_file:
				yaml_file.write(yaml.dump(doc, default_flow_style=False, tags = False))

	"Convert csv file to yaml file"
	def csv2yaml(self, file):
		in_file  = open(file[:-5]+'.csv', "r", encoding='iso-8859-1')
		csv.register_dialect('myDialect', delimiter = ',', skipinitialspace=True)
		reader = csv.reader(in_file, dialect='myDialect')
		reader = list(reader)
		cols = reader[0]
		for i, row in enumerate(reader, 1):
			item = {row[0]:  [{col : row[n]} for n,col in enumerate(cols[1:], 1)]}
			with open(file, 'a', encoding='iso-8859-1') as yaml_file:
				yaml.dump(item, yaml_file, default_flow_style=False)
	
	"Sort yaml file"
	def sort_yml(self, file):
		dct = self.get_doc(file)
		od = dict(OrderedDict(sorted(dct.items())))
		with open("od.yaml", 'w', encoding='iso-8859-1') as yaml_file:
				yaml.dump(od, yaml_file, default_flow_style=False)
####################################################
if __name__ == "__main__":
	y = YML()
	path = "DATA/"
	if y.args.table: y.read_yml(path+y.file+".yaml")
	if y.args.w2csv: y.write2csv(path+y.file+".yaml")
	if y.args.search: y.search_records(path+y.file+".yaml")
	if y.args.delrec : y.del_record(path+y.file+".yaml")
	if y.args.insrec : y.insert_rec(path+y.file+".yaml")
	if y.args.update : y.update_rec(path+y.file+".yaml")
	if y.args.csv2yml : y.csv2yaml(path+y.file+".yaml")
	if y.args.sort : y.sort_yml(path+y.file+".yaml")