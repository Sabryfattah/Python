""" PANDAS :
1-Read and write csv files (flat files and text files with extra lines).
2-Read and write sql files
3-Read and write Excel files.
4-Read and write tables from url and html files.
5-Explore dataframes shape,columns,rows,head,tail,describe,stat summary.
6-Select rows and columns from dataframe.(and save them to file)
7-Change row and column labels, rename them.
8-Change data in whole column or row, or specific cell or all cells in df.
9-Add and remove columns or rows.
10-redistribute table by transpose, groupby and pivot.
11-sort columns, fill empty cells or remove rows with empty cells.
12-Apply one or many functions(applymap, agg) by column or whole df.
13-combine dataframes by rows(append) or columns(concat) or join with col.
14-Merge two dataframes by key column shared between them.
15-Filter dataframe by matching data in column or row or both.
16- Search DF for matching pattern.
17-Run Statistical functions on DF or coulmns.
18-Plot graphs for data columns in DF.
19-Change data types.
20-replace value in all cells or specific column or row.
"""
import re
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import argparse
import seaborn as sns
import numpy as np
from tabulate import tabulate
from bs4 import BeautifulSoup
import urllib.request
#####################################################################
class PD_CSV():
	def __init__(self, path=None, file=None):
		self.path = "c:/py/pd/data/"
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="pd <options> [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='csv file')
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
		self.parser.add_argument('-p',"--plot", action='store_true', help='plot a graph')
		self.parser.add_argument('-q',"--sql", action='store_true', help='read sql database table')
		self.parser.add_argument('-r',"--csv", action='store_true', help='read csv file')
		self.parser.add_argument('-s',"--search", action='store_true', help='search column for matching rows')
		self.parser.add_argument('-t',"--dtype", action='store_true', help='change column dtype')
		self.parser.add_argument('-u',"--update", action='store_true', help='update field')
		self.parser.add_argument('-v',"--view", action='store_true', help='adjust view by columns and rows')
		self.args = self.parser.parse_args()
		self.file = self.args.file

	##################################################################
	"Read CSV file into DataFrame"
	def read_csv(self):
		pd.set_option('display.max_colwidth', 20)
		df = pd.read_csv(self.path + self.file + ".csv", sep=";", encoding='iso-8859-1')
		self.print_table(df)
		return df

	def view(self):
		df = pd.read_csv(self.path + self.file + ".csv", sep=";", encoding='iso-8859-1')
		self.headers(df)
		col = input("Give column numbers ?..>>")
		c = [int(e) for e in col.split(",")]
		s =  input("starting row index?.\n>>")
		r = input("last row index?..\n>>")
		df1 = df.iloc[int(s):int(r),c]
		self.print_table(df1)
		self.write2csv(df1)
				
	"write DataFrame into csv file "
	def write2csv(self, df):
		res = input("Save Result to Text, CSV or Exit ? (text,csv,x) ...>>\n")
		if res == "text":
			filename = input("Filename to save section to :>>\n")
			open(filename+".txt", 'w').write(tabulate(df , headers='keys', tablefmt='psql', showindex=True, numalign="left"))
		if res == "csv":
			filename = input("Name of New CSV File..>>\n")
			df.to_csv(self.path + filename+".csv", index=False)
		else:
			exit
		
		

	"Read sqlite db into DataFrame"
	def read_sql(self):
		table = input("SQL Table name ..?>>\n")
		path = "c:/py/sql/db/"+self.file+".db"
		conn = sqlite3.connect(path)
		query = "SELECT * FROM {t} ".format(t=table)
		df = pd.read_sql_query(query,conn)
		print(df)
		return df

	def print_table(self,df):
		print(tabulate(df, headers='keys', tablefmt='psql', showindex=True, numalign="left"))
		total = df.sum(numeric_only=True)
		print(total)
		return total

	"read table from url or html page and write to csv file "
	def read_html(self):
		url = input("html url address ..>>\n")
		#htm = urllib.request.urlretrieve(url)
		#table = BeautifulSoup(open(htm,'r').read()).find('table')
		#df = pd.read_html(table)
		tables = pd.read_html(url)
		df = tables[0]
		self.write2csv(df)
	"Column titles or csv headers"
	def headers(self,df):
		[print(i,e, sep=":", end="|") for i,e in enumerate(df.columns)]
		print()

	"Add a column to csv file"
	def add_col(self):
		df = self.read_csv()
		cols = df.columns.values
		col_nam = input("Column Name:>>\n")
		df[col_nam] = pd.Series(['NaN']*len(df), index=df.index).values
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	"delete a column "
	def del_col(self):
		df = self.read_csv()
		colnam = input("Column to delete ? ..>>\n")
		del df[colnam]
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	"Rename column titles in csv file "
	def ren_col(self):
		df = self.read_csv()
		col_num = input("column number ( 0,1,2,3,4,5..etc ) [not index] ?")
		old_name = df.columns[int(col_num)]
		new_name = input("Enter new name for column: ...>>\n")
		df.rename(columns ={old_name : new_name}, inplace =True)
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)
		

	"Add row to end of table and save to csv file"
	def add_row(self):
		df = self.read_csv()
		cols = df.columns.values
		new_row = input("enter new row as values separated by commas ..>>\n")
		df.loc[len(df)] = new_row.split(",")
		df.to_csv(self.path+self.file+".csv", index=False)

	"Delete row"
	def del_row(self):
		df = self.read_csv()
		rown = input("rows numbers to delete ? ..>>\n")
		df = df.drop(int(rown))
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	"Update value of a particular table cell "
	def update(self):
		df = self.read_csv()
		colnam = input("enter column name of  field..>>\n")
		rown =  input("enterrow number of  field..>>\n")
		new_value =  input("enter new value:.. >>\n")
		df.loc[int(rown),colnam] = new_value
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	"Plot a DataFrame from csv file "
	def plot_df(self):
		df = self.read_csv()
		x_col = input("x column :..   ")
		y_col = input("y column :..  ")
		title = input("title of the graph..:   ")
		kind = input("kind of graph (bar,barh,pie,line,scatter)...  ")
		df.plot(kind=kind, title = title, x=x_col, y=y_col)
		plt.show()

	"Display a slice of a number of rows "
	def search(self):
		df = self.read_csv()
		pat = input("patern to search? ..>>\n")
		col = input("Column to search? ..>>\n")
		regex = re.compile(r'.*{}.*'.format(pat), flags=re.IGNORECASE)
		result = df[df[col].str.match(regex)]
		self.print_table(result)
		self.write2csv(result)

	"Display table with selected columns "
	def select_cols(self):
		df = self.read_csv()
		col = input("Columns selected (comma separated)..>>\n")
		c = df.loc[:,col.split(",")]
		self.print_table(c)
		filename = input("Filename to save section to :>>\n")
		c.to_csv(filename+".csv", index=False)

	"Display selected rows matching a pattern in given column "
	def select_rows(self):
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

	"replace text anywhere in table, not headers or index "
	def replace(self):
		df = self.read_csv()
		old = input("Text to change :...>>\n")
		new = input("New Text :...>>\n")
		print("="*90)
		df = df.replace([old], [new])
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	"Display sum and statistics of given column "
	def stats(self):
		df = self.read_csv()
		stat = input("type of stat:\nsum,mad,median, min,max,mode,prod,std,var,\nsem,skew,kurt,quantile,cumsum,cumprod,cummin,cummax\n")
		col = input("Column to calculate its {} :...>>\n".format(stat))
		st = eval("df['{}'].{}()".format(col, stat))
		print(round(st))

	"Update values a cross a whole column "
	def fill_col(self):
		df = self.read_csv()
		coval = input("Value for whole column..>>\n")
		colnam = input("enter column name ..>>\n")
		#df[colnam].replace(to_replace=df.loc[:, colnam], value=coval, inplace=True)
		df[colnam ] = coval
		print(df)

	"Apply a function to two columns and create a new column at right"
	def modify(self):
		df = self.read_csv()
		col = input("New Column ? ..>>\n")
		col1 = input("Column1 ? ..>>\n")
		col2 = input("Column2 ? ..>>\n")
		df[col] = df.Balance* df.Rate/100
		df.append(df[col])
		self.print_table(df)
		df.to_csv(self.path+self.file+".csv", index=False)

	def merge(self):
		csv1 = input("first csv file ..>>")
		csv2 = input("second csv file ..>>")
		key = input("key to merge files on ..>>")
		df1 = pd.read_csv(self.path+"{}.csv".format(csv1), encoding='iso-8859-1')
		df2 = pd.read_csv(self.path+"{}.csv".format(csv2), encoding='iso-8859-1')
		df3 = pd.merge(df1,df2, on=key, how="inner")
		print(df3)
		#filename = input("Filename to save section to :>>\n")
		#df3.to_csv(filename+".csv", index=False)

	def corre(self):
		df = self.read_csv()
		print(df.corr(method ='pearson') )

	def sort(self):
		df = self.read_csv()
		col = input("Column to use for sorting..>>\n")
		df = df.sort_values(by=col, ascending=True)
		print(df)
		df.to_csv(self.path+self.file+".csv", index=False)
		
	def dtype(self):
		df = self.read_csv()
		col = input("Column to change type ?..>>\n")
		type =  input("dtype ?..>>\n")
		df = df.astype({col: type})
		df.to_csv(self.path+self.file+".txt", index=False)
		df.to_csv(self.path+self.file+".csv", index=False)
	
	def fillna(self):
		df = self.read_csv()
		df.fillna(value=0, inplace=True)
		df.to_csv(self.path+self.file+".csv", index=False)
		
	def del_nan(self):
		df = self.read_csv()
		df1= df.dropna(how='any', inplace=True)
		#df.to_csv(self.path+self.file+".csv", index=False)
		print(df1)
		
	def groupby(self):
		df = self.read_csv()
		col = input("Column to group by it :..>>\n")
		#func = input("function to use ..:>>\n")
		df1 = df.groupby([col]).sum()
		print(df1)

#####################################################
if __name__ == "__main__" :
	p = PD_CSV()
	if p.args.csv : p.read_csv()
	if p.args.sql : p.read_sql()
	if p.args.readhtml : p.read_html()
	if p.args.headers : p.headers()
	if p.args.plot : df =  p.plot_df()
	if p.args.rencol: p.ren_col()
	if p.args.modify: p.modify()
	if p.args.srows: p.select_rows()
	if p.args.scols: p.select_cols()
	if p.args.replace : p.replace()
	if p.args.stats: p.stats()
	if p.args.addrow: p.add_row()
	if p.args.addcol: p.add_col()
	if p.args.delcol: p.del_col()
	if p.args.delrow: p.del_row()
	if p.args.update: p.update()
	if p.args.fillcol: p.fill_col()
	if p.args.search: p.search()
	if p.args.merge: p.merge()
	if p.args.cor: p.corre()
	if p.args.sort: p.sort()
	if p.args.view: p.view()
	if p.args.dtype : p.dtype()
	if p.args.fillna : p.fillna()
	if p.args.groupby : p.groupby()
	if p.args.delnan : p.del_nan()