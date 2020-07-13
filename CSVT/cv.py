"""Read CSV Files in any directory using PANDAS
1- read csv file.
2- update csv.
3- Replace value in whole table.
4- delete column.
5- search csv.
6- read_yaml
7- yaml_search
8- write dataframe
"""
################################################
import pd
import yaml
import argparse
from tabulate import tabulate
import pandas as panda
from pandas.io.json import json_normalize
import glob
#############################################
class PData():
	def __init__(self, file=None):
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="pcsv <options> [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='csv file')
		self.parser.add_argument('-r',"--rcsv", action='store_true', help='read csv file')
		self.parser.add_argument('-u',"--update", action='store_true', help='update csv')
		self.parser.add_argument('-rp',"--replace", action='store_true', help='Replace value in whole table')
		self.parser.add_argument('-dc',"--delcol", action='store_true', help='delete column')
		self.parser.add_argument('-s',"--search", action='store_true', help='Search csv')
		self.args = self.parser.parse_args()
		self.file = self.args.file

	"Read csv file into table with totals "
	def csv_read(self,path, file):
		pd.PANDA().read_csv(path, file)

	"Update csv file, modify cells"
	def csv_update(self,path, file):
		pd.PANDA().update(path, file)
	
	"Replace value in whole table"
	def csv_replace(self,path, file):
		pd.PANDA().replace(path, file)

	"Delete column in a table"
	def csv_del_col(self,path, file):
		pd.PANDA().del_col(path, file)

	"Search csv file for a record"
	def csv_search(self,path,file):
		pd.PANDA().search(path,file)

	def read_yaml(self, file):
		with open('clouds.json') as f:
			df = panda.pandas.read_json(f, lines=True)
			print(tabulate(df, headers = 'keys', tablefmt='fancy_grid', showindex=True, numalign="left", colalign=("left",)))
		return df

	def write_df(self, file, path):
		df = self.read_yaml(file)
		df = df.sort_values('Index', ascending=False).drop_duplicates('Index').sort_index()
		filename = input("Name of New CSV File..>>\n")
		df.to_csv(path + filename+".csv", index=True)

	def yaml_search(self, file):
		d = yaml.safe_load(open(file))
		for key in d.keys():
			if re.match(r'.*%s.*' % string, key, re.I|re.M):
				print('='*80)
				print(key, " at ", file)
				print('-'*80)
				for x,y in zip(d['columns'], d[key]):
					print("{:<10} : {:<10}".format(str(x), str(y)))
				print('='*80)
################################################
if __name__ == "__main__" :
	ob = PData()
	csv_path = "DATA/"
	if ob.args.rcsv : ob.csv_read(csv_path,ob.file)
	if ob.args.update : ob.csv_update(csv_path,ob.file)
	if ob.args.replace : ob.csv_replace(csv_path, ob.file)
	if ob.args.delcol : ob.csv_del_col(csv_path, ob.file)
	if ob.args.search : ob.csv_search(csv_path,ob.file)