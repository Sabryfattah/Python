""" Test View :
1- read csv, print df and view slices of it.
2- print as list of notes.
3- change data types.
4- drop NaN columns.
5- plot lines.
6- Search for pattern.
"""
import pandas as pd
import argparse
from tabulate import tabulate
import re
#########################################################
class T():
	def __init__(self, path=None, file=None):
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="pd <options> [file]")
		#self.parser.add_argument('path',nargs="?", action='store', help='file path')
		self.parser.add_argument('file',nargs="?", action='store', help='csv file')
		self.parser.add_argument("sep", nargs="?", default= ';', action='store', help='separator')
		self.parser.add_argument('-v',"--view", action='store_true', help='view')
		self.parser.add_argument('-r',"--read", action='store_true', help='read')
		self.parser.add_argument('-dc',"--dropnac", action='store_true', help='drop NaN columns')
		self.parser.add_argument('-t',"--dtype", action='store_true', help='convert dtype')
		self.parser.add_argument('-pl',"--plotline", action='store_true', help='Plot Line')
		self.parser.add_argument('-gt',"--groupdt", action='store_true', help='Group by Datetime')
		self.parser.add_argument('-l',"--list", action='store_true', help='print in notes list')
		self.parser.add_argument('-s',"--search", action='store_true', help='search for pattern')
		self.parser.add_argument('-g',"--group", action='store_true', help='group by coln')
		self.args = self.parser.parse_args()
		self.file = self.args.file
		self.path = "data/"
		self.sep =  self.args.sep

	def print_table(self,df):
		print(tabulate(df, headers='keys', tablefmt='', showindex=True, numalign="left"))
		total = df.sum(numeric_only=True)
		print(total)
		return total

	def view(self):
		pd.set_option('display.max_colwidth', 500)
		pd.set_option('display.expand_frame_repr', True)
		pd.set_option('display.max_columns', 500)
		df = pd.read_csv(self.path + self.file + ".csv", encoding='iso-8859-1')
		self.headers()
		col = input("Give column numbers ?..>>")
		c = [int(e) for e in col.split(",")]
		s =  0 # input("starting row index?.\n>>")
		r =  1000 #input("last row index?..\n>>")
		df1 = df.iloc[s:r,c]
		self.print_table(df1)
		#df1 = df.iloc[int(s):int(r),c]
		#self.write2csv(df1)
		
	"Read CSV file into DataFrame"
	def read_csv(self):
		pd.set_option('display.max_colwidth', 500)
		pd.set_option('display.expand_frame_repr', False)
		pd.set_option('display.max_columns', 500)
		df = pd.read_csv(self.path + self.file + ".csv", encoding='iso-8859-1',engine='python')
		return df

	def headers(self):
		df = self.read_csv()
		[print(i,e, sep=":", end="|") for i,e in enumerate(df.columns)]
		print()
	
	def dropnacol(self):
		df = self.read_csv()
		df1 = df.dropna(axis=1)
		print(df1)
		df1.to_csv(self.path + self.file+".csv", index=False)
		
	def group_dt(self):
		df = self.read_csv()
		df1 = df.set_index(pd.DatetimeIndex(df['Date']))
		freq =input("frequency of periods : M month, Y year, d Day>>\n")
		g = df1.groupby(pd.Grouper(freq=freq)).sum()
		print(g)
		

	def groupby(self):
		df = self.read_csv()
		col = input("Column to group by it :..>>\n")
		func = input("function to use ..:>>\n")
		df1 = df.groupby([col]).agg(func)
		print(df1)

	def list(self, df):
		for n in range(len(df)):
			print("="*80)
			print(df.iloc[n])
			print("="*80)
			
	def search(self):
		df = self.read_csv()
		pat = input("patern to search? ..>>\n")
		self.headers()
		col = input("Give column number ?..>>")
		regex = re.compile(r'.*{}.*'.format(pat), flags=re.IGNORECASE)
		result = df[df[df.columns[int(col)]].str.match(regex)]
		print("="*150)
		self.print_table(result)
		print("="*150)

##################################################
if __name__ == "__main__" :
	p = T()
	if p.args.dropnac: p.dropnacol()
	if p.args.view : p.view()
	if p.args.read: p.print_table(p.read_csv())
	if p.args.dtype: PD_CSV.dtype(p)
	if p.args.plotline: PLOT.line(p)
	if p.args.groupdt: p.group_dt()
	if p.args.list: p.list(p.read_csv())
	if p.args.search: p.search()
	if p.args.group: p.groupby()
	
"""
import re
from bs4 import BeautifulSoup
import urllib.request
from functools import reduce
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sqlite3
"""