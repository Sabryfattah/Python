""" PANDAS PLOT :
1- plot bar.
2- plot comparison bar.
3- plot a pie.
4- plot a histogram.
5- plot a line.
6- plot a scatter graph.
7- plot a multiple graphs.
8- plot by seaborn graph.
"""
from pd import *
import re
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import argparse
import seaborn as sns; sns.set()
import numpy as np
from tabulate import tabulate
from bs4 import BeautifulSoup
import urllib.request
from pylab import *
#####################################################################
class PLOT():
	def __init__(self, path=None, file=None):
		self.path = "pd/data/"
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="plot <options> [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='csv file')
		self.parser.add_argument('-b',"--bar", action='store_true', help='plot bar')
		self.parser.add_argument('-cb',"--combar", action='store_true', help='plot comparison bar')
		self.parser.add_argument('-p',"--pie", action='store_true', help='plot a pie')
		self.parser.add_argument('-hs',"--hist", action='store_true', help='plot a histogram')
		self.parser.add_argument('-l',"--line", action='store_true', help='plot a line')
		self.parser.add_argument('-s',"--scatter", action='store_true', help='plot a scatter graph')
		self.parser.add_argument('-sp',"--subplot", action='store_true', help='plot a multiple graphs')
		self.parser.add_argument('-sb',"--seaborn", action='store_true', help='plot by seaborn')
		self.args = self.parser.parse_args()
		self.file = self.args.file
	
	"Plot a DataFrame from csv file "
	def pie(self):
		df = pd.read_csv(self.path+self.file+".csv")
		x_col = input("x column :..   ")
		y_col = input("y column :..  ")
		title = input("title of the graph..:   ")
		ax = df.plot(kind='pie', labels=df[x_col], y=y_col,autopct='%1.1f%%')
		ax.xlabel = df[x_col]
		ax.set_title(title, fontname='Times New Roman', fontsize=18)
		ax.legend(labels=df[x_col],bbox_to_anchor=(0.05, 0.5),loc='center left')
		plt.axis('equal')
		plt.tight_layout()
		plt.show()
		

	def bar(self):
		df = pd.read_csv(self.path+self.file+".csv")
		x_col = input("x column :..   ")
		title = input("title of the graph..:   ")
		ax = df.plot.bar(title=title)
		ax.set_xticklabels(df[x_col])
		plt.ylabel("Amount in Pounds")
		plt.show()
		
	def combar(self):
		df = pd.read_csv(self.path+self.file+".csv")
		x_col = input("x column :..   ")
		ncol1 = input("First numerical column :..  ")
		ncol2 = input("Second numerical column :..  ")
		title = input("title of the graph..:   ")
		plt.subplots()
		index = np.arange(len(df[x_col]))
		opacity = 0.8
		bar_width = 0.35
		plt.bar(index, df[ncol1],bar_width,alpha=opacity,color='b',label=ncol1)
		plt.bar(index+bar_width,df[ncol2],bar_width,alpha=opacity,color='r',label=ncol2)
		plt.xlabel(x_col)
		plt.ylabel(ncol1+" vs. "+ncol2)
		plt.title(title)
		plt.xticks(index + bar_width, (df[x_col]))
		plt.legend()
		plt.tight_layout()
		plt.show()

	def hist(self):
		df = pd.read_csv(self.path+self.file+".csv")
		x_col = input("x column :..  \n")
		y_col = input("y column :..  \n")
		title = input("title of the graph..:   \n")
		x = df[y_col]
		num_bins = 20
		plt.hist(x, num_bins)
		plt.xlabel(x_col)
		plt.ylabel(y_col)
		plt.title(title)
		plt.show()
		
	
	def line(self):
		df = pd.read_csv(self.path+self.file+".csv")
		res = input("Plot values of single column?...(y/n)>>\n")
		if res == "y":
			x_col = input("name of categories column :..   ")
			y_col = input("name of values column :..   ")
		else:
			x_col = input("name of first column :..   ")
			y_col = input("name of second column :..   ")
		df.plot(kind='line',x=x_col, y=y_col, grid=True)
		show()
		
	def scatter(self):
		df = pd.read_csv(self.path+self.file+".csv")
		x_col = input("x column :..   ")
		ncol1 = input("First numerical column :.. \n ")
		ncol2 = input("Second numerical column :..\n  ")
		title = input("title of the graph..?:..\n   ")
		df.plot(kind='scatter',x=ncol1,y=ncol2, s=20)
		plt.title(title)
		plt.xlabel(ncol1)
		plt.ylabel(ncol2)
		plt.show()
		
	def subplot(self):
		df = pd.read_csv(self.path+self.file+".csv")
		x_col = input("x column :..   ")
		ncol1 = input("First numerical column :..  ")
		ncol2 = input("Second numerical column :..  ")
		type = input("type of graph:..  ")
		df.plot(kind=type, x=ncol1, y=ncol2, subplots=True)
		show()
		
	def seaborn(self):
		df = pd.read_csv(self.path+self.file+".csv")
		x_col = input("x column :..   ")
		y_col = input("x column :..   ")
		sns.barplot(x_col, y_col, data=df)
		plt.show()
#####################################################
if __name__ == "__main__" :
	p = PLOT()
	if p.args.bar: p.bar()
	if p.args.combar: p.combar()
	if p.args.pie: p.pie()
	if p.args.hist: p.hist()
	if p.args.line: p.line()
	if p.args.scatter: p.scatter()
	if p.args.subplot: p.subplot()
	if p.args.seaborn: p.seaborn()