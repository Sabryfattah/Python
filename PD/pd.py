""" PANDAS :
1- Read csv file into dataframe and print it in formatted table.
2- Write dataframe to csv file.
3- Adjust dataframe view by selected columns and rows.
4- Read Jason file into dataframe and print it as table.
5- Read sqlite3 database as dataframe and prin it.
6- Read table from url or html page into df and write to csv file.
7- Add a column to csv file.
8- Delete a column from csv.
9- Rename column titles in csv file.
10- Add row to end of table and save to csv file.
11- Delete row from csv file.
12- Update value of a particular table cell in csv file.
13- Search pattern in a column and display rows containing it.
14- Display selected rows matching a pattern in given column.
15- Display table with selected columns.
16- Replace text anywhere in table, not headers or index.
17- Display sum and statistics of given column.
18- Fill a whole column with same value.
19- Apply a function to columns (create a new column at right).
20- Merge two dataframes or two csv files.
21- Get correlation between numerical columns in dataframe.
22- Sort dataframe by a column.
23- Change Datatype of a column in dataframe.
24- Delete NaN null values in a dataframe.
25- Fill all Nan values with zero.
26- Split frame along group of similar values in any column
"""
import re
import requests
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import argparse
import seaborn as sns
import numpy as np
from tabulate import tabulate
from bs4 import BeautifulSoup
import urllib.request
from functools import reduce
#####################################################################
class PANDA():
	__all__ = ['read_csv', 'write2csv']

	def __init__(self, file=None):
		self.file = None
	
	def argparser(self):
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="pd <options> [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='csv file')
		self.parser.add_argument('-r',"--csv", action='store_true', help='read csv file into dataframe and print it')
		self.parser.add_argument('-v',"--view", action='store_true', help='adjust df view by columns and rows')
		self.parser.add_argument('-ac',"--addcol", action='store_true', help='add column to right of table')
		self.parser.add_argument('-ar',"--addrow",action='store_true',help='add row to bottom of table')
		self.parser.add_argument('-co',"--cor", action='store_true', help='calculate correlation between numerical columns')
		self.parser.add_argument('-dc',"--delcol", action='store_true', help='delete column')
		self.parser.add_argument('-dn',"--delnan", action='store_true', help='delete rows with empty columns NaN')
		self.parser.add_argument('-dr',"--delrow", action='store_true', help='delelte row')
		self.parser.add_argument('-fn',"--fillna", action='store_true', help='fill Nan with zeros')
		self.parser.add_argument('-hd',"--headers", action='store_true', help='get table headers')
		self.parser.add_argument('-fc',"--fillcol", action='store_true', help='fill column with one value')
		self.parser.add_argument('-mg',"--merge", action='store_true', help='merge 2 DataFrames sharing a key column')
		self.parser.add_argument('-rc',"--rencol", action='store_true', help='rename columns')
		self.parser.add_argument('-rh',"--readhtml", action='store_true', help='read html tables and save to csv file')
		self.parser.add_argument('-rp',"--replace", action='store_true', help='replace text anywhere in DataFrame')
		self.parser.add_argument('-sc',"--scols", action='store_true', help='select specific columns from table')
		self.parser.add_argument('-so',"--sort", action='store_true', help='sort rows by given column')
		self.parser.add_argument('-sr',"--srows", action='store_true', help='select specific rows')
		self.parser.add_argument('-st',"--stats", action='store_true', help='do stats on column')
		self.parser.add_argument('-g',"--groupby", action='store_true', help='group by column values')
		self.parser.add_argument('-m',"--modify", action='store_true', help='modify a column by applying a function to it')
		self.parser.add_argument('-p',"--plot", action='store_true', help='plot a pie')
		self.parser.add_argument('-q',"--sql", action='store_true', help='read sql database table')
		self.parser.add_argument('-s',"--search", action='store_true', help='search column for matching rows')
		self.parser.add_argument('-t',"--dtype", action='store_true', help='change column dtype')
		self.parser.add_argument('-u',"--update", action='store_true', help='update field')
		self.parser.add_argument('-j2d',"--jsn2df", action='store_true', help='convert jason file to dataframe')
		self.args = self.parser.parse_args()
		self.file = self.args.file
		return self.file

	def print_table(self,df):
		print(tabulate(df, headers = 'keys', tablefmt='fancy_grid', showindex=True, numalign="left", colalign=("left",)))
		total = df.sum(numeric_only=True)
		print(total)
		return total

	def read_csv(self, path, file):
		"Read CSV file into DataFrame and print it"
		pd.set_option('display.max_colwidth', 500)
		pd.set_option('display.expand_frame_repr', False)
		pd.set_option('display.max_columns', 500)
		df = pd.read_csv(path + file + ".csv", sep=',', encoding='iso-8859-1')
		self.print_table(df)
		total = df.sum(numeric_only=True)
		#print(round(total, 2))
		return df

	def write2csv(self, df, path):
		"write DataFrame into csv file "
		res = input("Save Result to Text, CSV or Exit ? (t = text,c = csv,x = exit) ...>>\n")
		if res == "t":
			filename = input("Filename to save section to :>>\n")
			open(filename+".txt", 'w').write(tabulate(df , headers='keys', tablefmt='psql', showindex=True, numalign="left"))
		if res == "c":
			filename = input("Name of New CSV File..>>\n")
			df.to_csv(filename+".csv", index=False)
		else:
			exit

	def headers(self, path, file):
		"Column titles or csv headers"
		df = self.read_csv(path, file)
		[print(i,e, sep=":", end="|") for i,e in enumerate(df.columns)]
		print()

	def view(self, path, file):
		"adjust df view by columns and rows"
		df = pd.read_csv(self.path + self.file + ".csv", encoding='iso-8859-1')
		self.headers(path, file)
		col = input("Give column numbers ?..>>")
		c = [int(e) for e in col.split(",")]
		#s =  input("starting row index?.\n>>")
		#r = input("last row index?..\n>>")
		df1 = df.iloc[0:, c] #int(s):int(r),c]
		self.print_table(df1) #self.write2csv(df1)

	def read_jsn(self):
		"Read Jason file into DataFrame"
		pd.set_option('display.max_colwidth', 500)
		pd.set_option('display.expand_frame_repr', False)
		pd.set_option('display.max_columns', 500)
		path = "jsn/data/"
		file = path+self.file
		with open(file+'.json') as f:
			df = pd.read_json(f, orient='index')
			print(df)
			#print(tabulate(df[:100], headers = 'keys', tablefmt='fancy_grid', showindex=True, numalign="left", colalign=("left",)))
		return df

	def read_sql(self):
		"Read sqlite db into DataFrame"
		table = input("SQL Table name ..?>>\n")
		path = "sql/db/"+self.file+".db"
		conn = sqlite3.connect(path)
		query = "SELECT * FROM {t} ".format(t=table)
		df = pd.read_sql_query(query,conn)
		print(df)
		filename = input("Filename to save section to :>>\n")
		df.to_csv(self.path+filename+".csv", index=False)
		return df

	def read_html(self):
		"read table from url or html page and write to csv file "
		url = input("html url address ..>>\n")
		tables = pd.read_html(url)
		df = tables[0]
		print(df)
		self.write2csv(df)
################### DATAFRAME ####################
	def add_col(self):
		"Add a column to csv file"
		df = self.read_csv()
		cols = df.columns.values
		col_nam = input("Column Name:>>\n")
		df[col_nam] = pd.Series(['NaN']*len(df), index=df.index).values
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	def del_col(self, path, file):
		"delete a column from csv "
		df = self.read_csv(path, file)
		colnam = input("Column to delete ? ..>>\n")
		del df[colnam]
		print(df)
		df.to_csv(path+file+".csv", index=False)

	def ren_col(self):
		"Rename column titles in csv file "
		df = self.read_csv()
		col_num = input("column number ( 0,1,2,3,4,5..etc ) [not index] ?")
		old_name = df.columns[int(col_num)]
		new_name = input("Enter new name for column: ...>>\n")
		df.rename(columns ={old_name : new_name}, inplace =True)
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	def add_row(self):
		"Add row to end of table and save to csv file"
		df = self.read_csv()
		cols = df.columns.values
		new_row = input("enter new row as values separated by commas ..>>\n")
		df.loc[len(df)] = new_row.split(",")
		df.to_csv(self.path+self.file+".csv", index=False)

	def del_row(self):
		"Delete row from csv file"
		df = self.read_csv()
		rown = input("rows numbers to delete ? ..>>\n")
		df = df.drop(int(rown))
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	def update(self, path, file):
		"Update value of a particular table cell "
		pd.set_option('display.max_colwidth', 1000)
		pd.set_option('display.max_columns', None)
		df = self.read_csv(path, file)
		pat = input("string pattern to search in row? ..>>\n")
		self.headers(path, file)
		col = input("Give column number ?..>>")
		regex = re.compile(r'.*{}.*'.format(pat), flags=re.IGNORECASE)
		result = df[df[df.columns[int(col)]].str.match(regex)]
		self.print_table(result)
		colnam = df.columns[int(col)] #input("enter column name..>>\n")
		rown =  input("enter row number..>>\n")
		new_value =  input("enter new value:.. >>\n")
		df.loc[int(rown),colnam] = new_value
		self.print_table(df)#[df[df.columns[int(col)]].str.match(regex)])
		if input("Do you like to save ..? (y/n)\n") == 'y':
			df.to_csv(path+file+".csv", index=False)
		else:
			exit

	def search(self, path, file):
		"Search pattern in a column and display rows containing it"
		df = self.read_csv(path, file)
		pat = input("patern to search? ..>>\n")
		self.headers(path, file)
		col = input("Give column number ?..>>")
		regex = re.compile(r'.*{}.*'.format(pat), flags=re.IGNORECASE)
		result = df[df[df.columns[int(col)]].str.match(regex)]
		self.print_table(result) 
		total = result.sum(numeric_only=True)
		print(total)
		self.write2csv(result, total)

	def select_cols(self):
		"Display table with selected columns "
		df = self.read_csv()
		col = input("Columns selected (comma separated)..>>\n")
		c = df.loc[:,col.split(",")]
		self.print_table(c)
		filename = input("Filename to save section to :>>\n")
		c.to_csv(filename+".csv", index=False)

	def select_rows(self):
		"Display selected rows matching a pattern in given column "
		df = self.read_csv()
		col  = input("Column to search: ..>>\n")
		pat = input("value in column : ..>>\n")
		choice = input("Is the value an integer?(y/n) :  >>\n")
		if choice == 'y':
			v = input("Enter < or > or ==")
			if v == '<':
				r = df.loc[lambda df : df[col] < int(pat)]
			if v == '>':
				r = df.loc[lambda df : df[col] > int(pat)]
			if v == '==':
				r = df.loc[lambda df : df[col] == int(pat)]
		else:
			r = df.loc[lambda df : df[col].str.contains(pat)]
		out= self.print_table(r)
		res = input("Do you want to save result (y,n) ...>>\n")
		if res == "y":
			filename = input("Filename to save section to :>>\n")
			r.to_csv(filename+".csv", index=False)
			open(filename+".csv", 'a').write(out.to_string())
		else:
			exit

	def replace(self, path, file):
		"replace text anywhere in table, not headers or index "
		df = self.read_csv(path, file)
		old = input("Text to change :...>>\n")
		new = input("New Text :...>>\n")
		print("="*90)
		df = df.replace([old], [new])
		print(df)
		df.to_csv(path+file+".csv", index=False)

	def stats(self):
		"Display sum and statistics of given column "
		df = self.read_csv()
		stat = input("type of stat:\nsum,mad,median, min,max,mode,prod,std,var,\nsem,skew,kurt,quantile,cumsum,cumprod,cummin,cummax\n")
		col = input("Column to calculate its {} :...>>\n".format(stat))
		st = eval("df['{}'].{}()".format(col, stat))
		print(round(st))

	def fill_col(self):
		"Update values a cross a whole column "
		df = self.read_csv()
		coval = input("Value for whole column..>>\n")
		colnam = input("enter column name ..>>\n")
		#df[colnam].replace(to_replace=df.loc[:, colnam], value=coval, inplace=True)
		df[colnam ] = coval
		print(df)

	def modify(self):
		"Apply a function to two columns and create a new column at right"
		df = self.read_csv()
		col = input("New Column ? ..>>\n")
		col1 = input("Column1 ? ..>>\n")
		col2 = input("Column2 ? ..>>\n")
		df[col] = df.Balance* df.Rate/100
		df.append(df[col])
		self.print_table(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	def merge(self):
		"Merge two dataframes or csv files"
		names = input("names of files to merge separetd by commas ?..\n  ").split(",")
		dfs = []
		key = input("key to merge files on ..>> \n")
		for name in names:
			df = pd.read_csv(self.path+"{}.csv".format(name), encoding='iso-8859-1')
			dfs.append(df)
		df_final = reduce(lambda left,right: pd.merge(left,right,on=key,how='left'), dfs)
		print(df_final)
		filename = input("Filename to save section to :>>\n")
		df_final.to_csv(filename+".csv", index=False)

	def corre(self):
		"Get correlation between numerical columns in dataframe"
		df = self.read_csv()
		print(df.corr(method ='pearson') )

	def sort(self, path,file):
		"Sort dataframe by a column"
		df = self.read_csv(path,file)
		col = input("Column to use for sorting..>>\n")
		df = df.sort_values(by=col, ascending=True).reset_index()
		print(df)
		df.to_csv(path+file+".csv", index=False)

	def dtype(self, path, file):
		"Change Datatype of a column in dataframe"
		df = self.read_csv(path, file)
		col = input("Column to change type ?..>>\n")
		type =  input("dtype ?..>>\n")
		df = df.astype({col: type}, errors='coerce')
		df.to_csv(path+self.file+".txt", index=False)
		df.to_csv(path+self.file+".csv", index=False)

	def fillna(self):
		"fill all Nan values with zero"
		df = self.read_csv()
		df.fillna(value=0, inplace=True)
		df.to_csv(self.path+self.file+".csv", index=False)

	def del_nan(self):
		"Delete NaN null values in a dataframe"
		df = self.read_csv()
		df1= df.dropna(how='any', inplace=True)
		#df.to_csv(self.path+self.file+".csv", index=False)
		print(df1)

	def groupby(self, path):
		"Split frame along group of similar values in any column"
		"also split by group along the rows or column index"
		"apply a function to each group, or chain of functions"
		"the result can be filtered by filter(lambda) with defined criteria"
		df = self.read_csv(path, self.argparser())
		col = input("Column to group by it :..>>\n")
		func = input("function to use, e.g. sum,mean,count ..:>>\n")
		df1 = df.groupby([col]).agg(func)
		print(df1)
		return df1

#####################################################
if __name__ == "__main__" :
	path = "pd/data/"
	p = PANDA()
	p.argparser()
	if p.args.csv : p.read_csv(path, p.file)
	if p.args.sql : p.read_sql()
	if p.args.readhtml : p.read_html()
	if p.args.headers : p.headers()
	if p.args.rencol: p.ren_col()
	if p.args.modify: p.modify()
	if p.args.srows: p.select_rows()
	if p.args.scols: p.select_cols()
	if p.args.replace : p.replace()
	if p.args.stats: p.stats()
	if p.args.addrow: p.add_row()
	if p.args.addcol: p.add_col()
	if p.args.delcol: p.del_col(path)
	if p.args.delrow: p.del_row()
	if p.args.update: p.update()
	if p.args.fillcol: p.fill_col()
	if p.args.search: p.search(path)
	if p.args.merge: p.merge()
	if p.args.cor: p.corre()
	if p.args.sort: p.sort(path,p.file)
	if p.args.view: p.view()
	if p.args.dtype : p.dtype(path, p.file)
	if p.args.fillna : p.fillna()
	if p.args.groupby : p.groupby()
	if p.args.delnan : p.del_nan()
	if p.args.jsn2df : p.read_jsn()