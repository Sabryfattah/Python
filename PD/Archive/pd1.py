"""PANDAS MASTER FILE
1- import data from csv
2- read sql table, write to sql table
3- import table from html
4-create a DataFrame(from dictionary, file)
5- manipulate a DataFrame: Select chunks from df(columns, rows,pieces)
6-print df to csv file,sqlite,excel and others.
7-change index, column names, add column, delete column,add row, delete row
8-update row,update column
9-Join tables, split tables, apply function to part of table
10-split table to parts by grouping
11-plot table ddata into graphs
12-apply statistics to table data
"""
import re
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import argparse
import seaborn as sns
import numpy as np
#####################################################################
def argpar():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description = __doc__,
		usage="pd <options> [file] [table]")
	parser.add_argument('file', nargs ="?", action='store', help='csv or sql file')
	parser.add_argument('table', nargs ="?", action='store', help='table')
	parser.add_argument('-ac', "--addcol", action='store_true', help='add new column')
	parser.add_argument('-ar', "--addrow", action='store_true', help='add new row')
	parser.add_argument('-c', "--csv", action='store_true', help='read csv file')
	parser.add_argument('-d', "--delcol", action='store_true', help='delete column')
	parser.add_argument('-dr', "--delrow", action='store_true', help='delete row')
	parser.add_argument('-gc', "--getcols", action='store_true', help='get specific columns')
	parser.add_argument('-gr', "--getrow", action='store_true', help='get specific row')
	parser.add_argument('-hd', "--headers", action='store_true', help='get headers of table')
	parser.add_argument('-k', "--chunk", action='store_true', help='get table chunk')
	parser.add_argument('-mf', "--modify", action='store_true', help='modify values in a column')
	parser.add_argument('-mu', "--mupdate", action='store_true', help='update all values in a column')
	parser.add_argument('-p', "--plot", action='store_true', help='plot a graph')
	parser.add_argument('-q', "--sql", action='store_true', help='read sql file')
	parser.add_argument('-r', "--readhtm", action='store_true', help='read html table')
	parser.add_argument('-rc', "--rencol", action='store_true', help='rename columns')
	parser.add_argument('-rp', "--replace", action='store_true', help='replace text in DataFrame')
	parser.add_argument('-sq', "--selectsql", action='store_true', help='select rows from sql table')
	parser.add_argument('-st', "--stats", action='store_true', help='do stats on column')
	parser.add_argument('-u', "--update", action='store_true', help='update field')
	parser.add_argument('-w', "--write", action='store_true', help='write2csv')
	args = parser.parse_args()
	return args
##################################################################






"Select part of sql table by matching pattern in given column "


"Change column titles in csv file "

"Display number of rows from table with all columns "

"Display Headers"


"Display Table with selected rows matching a pattern in given column "
def select_rows(file):
	df = read_csv(file)
	col = input("Column to search ..>>\n")
	pat = input("value in column : ..>>\n")
	choice = input("Value is integer?(y/n) :  >>\n")
	if choice == 'y':
		r = df.loc[lambda df : df[col] > int(pat)]
	else:
		r = df.loc[lambda df : df[col].str.contains(pat)]
	print(r)

"Display table with selected columns "
def select_cols(file):
	df = read_csv(file)
	col = input("Columns selected ..>>\n")
	c = df.loc[:,col.split(",")]
	print(c)

"replace text in table, not headers or index "
def replace(file):
	old = input("Text to change :...>>\n")
	new = input("New Text :...>>\n")
	df = read_csv(file)
	print("="*90)
	df = df.replace([old], [new])

"Display sum and statistics of given column "
def stats(file):
	df = read_csv(file)
	stat = input("type of stat:\nsum,mad,median, min,max,mode,abs,prod,std,var,sem,skew,kurt,quantile,cumsum,cumprod,cummin,cummax\n")
	col = input("Column to calculate its {} :...>>\n".format(stat))
	st = eval("df['{}'].{}()".format(col, stat))
	print(round(st))

"Add row to end of table and save to csv file"
def add_row(file):
	df = read_csv(file)
	cols = df.columns.values
	new_row = input("enter new row as values separated by commas ..>>\n")
	df.loc[len(df)] = new_row.split(",")
	df.to_csv("out.csv", index=False)

"Add a column to table"
def add_col(file):
	df = read_csv(file)
	cols = df.columns.values
	col_nam = input("Column Name:>>\n")
	df[col_nam] = pd.Series(['NaN']*len(df), index=df.index).values
	print(df)
	df.to_csv("out.csv", index=False)

"delete a column "
def del_col(file):
	df = read_csv(file)
	colnam = input("Column to delete ? ..>>\n")
	del df[colnam]
	print(df)
	df.to_csv("out.csv", index=False)

"Delete row"
def del_row(file):
	df = read_csv(file)
	rown = input("rows numbers to delete ? ..>>\n")
	df = df.drop(int(rown))
	print(df)
	df.to_csv("out.csv", index=False)



#####################################################
if __name__ == "__main__" :
	args = argpar()
	file = args.file
	table = args.table
	if args.csv : df = read_csv(args.file)
	if args.sql : df = read_sql(args.file, args.table)
	if args.plot : df =  read_csv(args.file); plot_df(df)
	if args.write: write2csv(df)
	if args.readhtm: read_htm()
	if args.rencol: ren_col(file)
	if args.selectsql: select_sql(file,table)
	if args.chunk: chunk(file)
	if args.headers: headers(file)
	if args.getrow: select_rows(file)
	if args.getcols: select_cols(file)
	if args.replace : replace(file)
	if args.stats: stats(file)
	if args.addrow: add_row(file)
	if args.addcol: add_col(file)
	if args.delcol: del_col(file)
	if args.delrow: del_row(file)
	if args.update: update(file)
	if args.mupdate: mupdate(file)
	if args.modify: modify(file)