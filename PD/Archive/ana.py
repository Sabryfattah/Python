"""PANDAS DATA ANALYSIS:
1- search column for matching rows.
2- adjust view by columns and rows.
3- apply function to column or more.
4- calculate correlation between numerical columns.
5- merge 2 DataFrames sharing a key column.
6- select specific columns from table.
7- sort rows by given column.
8- select specific rows.
9- do stats on column.
10- pivot a table.
11- groupby a table.
12- Plot data from a table
"""
import re
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import seaborn as sns
import numpy as np
from tabulate import tabulate
##########################################################
class PD_ANA():
	def __init__(self, path=None, file=None):
		self.path = "c:/py/pd/data/"
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="pda <options> [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='csv file')
		self.parser.add_argument('-g',"--groupby", action='store_true', help='group by column values')
		self.parser.add_argument('-m',"--modify", action='store_true', help='modify a column by applying a function to it')
		self.parser.add_argument('-p',"--plot", action='store_true', help='plot a graph')
		self.parser.add_argument('-r',"--csv", action='store_true', help='read csv file')
		self.parser.add_argument('-s',"--search", action='store_true', help='search column for matching rows')
		self.parser.add_argument('-v',"--view", action='store_true', help='adjust view by columns and rows')
		self.parser.add_argument('-ap',"--apply", action='store_true', help='apply function to column or more ')
		self.parser.add_argument('-co',"--cor", action='store_true', help='calculate correlation between numerical columns')
		self.parser.add_argument('-mg',"--merge", action='store_true', help='merge 2 DataFrames sharing a key column')
		self.parser.add_argument('-sc',"--scols", action='store_true', help='select specific columns from table')
		self.parser.add_argument('-so',"--sort", action='store_true', help='sort rows by given column')
		self.parser.add_argument('-sr',"--srows", action='store_true', help='select specific rows')
		self.parser.add_argument('-st',"--stats", action='store_true', help='do stats on column')
		self.parser.add_argument('-pvt',"--pivot", action='store_true', help='pivot a table')
		self.args = self.parser.parse_args()
		self.file = self.args.file
#----------------------------------------------------------------------------------------------
	"Column titles or csv headers"
	def headers(self,df):
		[print(i,e, sep=":", end="|") for i,e in enumerate(df.columns)]
		print()
	
	"Read CSV file into DataFrame"
	def read_csv(self):
		pd.set_option('display.max_colwidth', 20)
		pd.set_option('display.max_columns', None)
		df = pd.read_csv(self.path + self.file + ".csv",encoding='iso-8859-1')
		self.print_table(df)
		print(df.sum(numeric_only=True))
		return df
	
	"Print in tabulate format"
	def print_table(self,df):
		print(tabulate(df, headers='keys', tablefmt='psql', showindex=True, numalign="left"))
		total = df.sum(numeric_only=True)
		print("Total:")
		print(total)
		return total
	
	"write DataFrame into csv file "
	def write2csv(self, df):
		res = input("Save Result to Text, CSV or Exit ? (text,csv,x) ...>>\n")
		if res == "text":
			filename = input("Filename to save section to :>>\n")
			open(filename+".txt", 'w').write(tabulate(df , headers='keys', tablefmt='psql', showindex=True, numalign="left"))
		if res == "csv":
			filename = input("Name of New CSV File..>>\n")
			df.to_csv(self.path + filename+".csv", index=True)
		else:
			exit
	
	"View Sections (Coulmns and Rows) of DataFrames"
	def view(self):
		df = pd.read_csv(self.path + self.file + ".csv", encoding='iso-8859-1')
		self.headers(df)
		col = input("Give column numbers ?..>>")
		c = [int(e) for e in col.split(",")]
		s =  input("starting row index?.\n>>")
		r = input("last row index?..\n>>")
		df1 = df.iloc[int(s):int(r),c]
		self.print_table(df1)
		self.write2csv(df1)
		
	"View Rows with matching pattern in  given Column "
	def search(self):
		df = self.read_csv()
		col = input("Column to search? ..>>\n")
		pat = input("patern to search? ..>>\n")
		regex = re.compile(r'.*{}.*'.format(pat), flags=re.IGNORECASE)
		result = df[df[col].str.match(regex)]
		self.print_table(result)
		self.write2csv(result)
	
	def groupby(self):
		df = self.read_csv()
		col = input("Column to group by it :..>>\n")
		#func = input("function to use ..:>>\n")
		df1 = df.groupby([col]).sum()
		print(df1)
		self.write2csv(df1)
		
	def apply(self):
		df = self.read_csv()
		col = input("Column to apply function to:..>>\n")
		f = input("function to apply : np.functions or lambda ..>\n")
		r = input("numpy function or lambda : (s,l)..>>\n")
		if r == 's':
			s= df[col].apply("{}".format(f))
			print(f, s)
		else:
			s= df[col].apply(eval(f))
			print(f, s)
	
	def pivot_table(self):
		df = self.read_csv()
		idxcol = input("index columns separated by commas : ..>>\n")
		cols = input("columns separated by commas : ..>>\n")
		colval = input("values column : ..>>\n")
		func = input("Function to use : ..>>\n")
		df2 = df.pivot_table(index=idxcol,columns=cols,values=colval, aggfunc=func)
		print(df2)
	
	def correlation(self):
		df = self.read_csv()
		print(df.corr(method ='pearson') )
		
	def stats(self):
		df = self.read_csv()
		stat = input("type of stat:\nsum,mad,median, min,max,mode,prod,std,var,\nsem,skew,kurt,quantile,cumsum,cumprod,cummin,cummax\n")
		col = input("Column to calculate its {} :...>>\n".format(stat))
		st = eval("df['{}'].{}()".format(col, stat))
		print(round(st))
	
	"Plot a DataFrame from csv file "
	def plot_df(self):
		df = self.read_csv()
		x_col = input("x column :..   ")
		y_col = input("y column :..  ")
		title = input("title of the graph..:   ")
		kind = input("kind of graph (bar,barh,pie,line,scatter)...  ")
		df.plot(kind=kind, 
		title = title,
		#labels = df[x_col],
		x=x_col,
		y=y_col)
		plt.ylabel= df[x_col]
		plt.legend(labels=df[x_col], loc="best")
		plt.show()

###############################################################
if __name__ == "__main__" :
	p = PD_ANA()
	if p.args.csv : p.read_csv()
	if p.args.view: p.view()
	if p.args.search: p.search()
	if p.args.groupby: p.groupby()
	if p.args.apply: p.apply()
	if p.args.pivot: p.pivot_table()
	if p.args.cor: p.correlation()
	if p.args.stats: p.stats()
	if p.args.plot: p.plot_df()