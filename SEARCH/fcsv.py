"""
Dislays a given csv file in C:\CSV as a table with headers.
Default directory is c:\CSV, rows are displayed in columns of equal length.
To get names of files in C:\CSV use parameter -d, i.e. fcsv -d
Parameter -s searches for a givern pattern in all csv files and display records"""  
#=========================================================
import csv
import os
import re
import argparse
import operator
#=========================================================
parser = argparse.ArgumentParser(
formatter_class=argparse.RawDescriptionHelpFormatter,
description=__doc__,
usage="fcsv [optional arguments] [parameter : file to list or pattern to search]")
parser.add_argument("parameter", action='store', help='file or pattern to process')
parser.add_argument('-l', "--list", action='store_true', help='list a selected csv file')
parser.add_argument('-d', "--dir", action='store_true', help='list files in directory csv')
parser.add_argument('-w', "--write", action='store_true', help='write sorted csv file back')
parser.add_argument('-s', "--search", action='store_true', help='search all csv files for pattern')
args = parser.parse_args()
#=========================================================
FILES = []
DIRS = []
#============================================================
def get_files():
	tree = os.walk("C:\CSV")
	for d in tree:
		DIRS.append(d[0])
		for f in d[2]:
			 if f.endswith(".csv"): 
				FILES.append(d[0]+"\\"+f)
	return FILES
#=============================================================
file = "C:\CSV\\"+args.parameter+".csv"
def get_content(file):
	with open(file, 'rb') as f:
		content = [row for row in csv.reader(f.read().splitlines())]
	return sorted(content)
#===========================================================
def print_table(file):
	csvfile = open(file, 'rb')
	table = csv.reader(csvfile)
	max_len = len(max([num for elem in list(table) for num in elem], key=len))
	csvfile.seek(0)
	headers = next(table)
	for header in headers:
		print("{:<{}}".format(header, max_len), end=' ')
	fields = len(list(table)[0])
	print("\n", "="*(fields*max_len), end=' ')
	table = get_content(file)
	for row in table[1:]:
		print("\n")
		for e in row:
			print("{:<{}}".format(e, max_len), end=' ')
#===========================================================

def search_csv():
	pattern = args.parameter.split(" ")
	pattern = ".*".join(pattern)
	FILES = get_files()
	for file in FILES:
		csvfile = open(file, 'rb')
		table = csv.reader(csvfile)
		csvfile.seek(0)
		headers = next(table)
		for row in table:
			if re.search(pattern.lower(),",".join(row).lower(),  re.IGNORECASE):
				print("="*78)
				for N in range(0,len(row)):
					print("{:<10} : {:<20}".format(headers[N],  row[N]))
				print("*"*25,"found in ", file, "*"*25)
#==========================================================
def write_sorted(file):
		data = csv.reader(open(file),delimiter=',')
		data = list(data)
		header = data[0]
		sortedlist = sorted(data[1:], key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
		#now write the sorte result into new CSV file
		with open(file, "wb") as f:
			fileWriter = csv.writer(f, delimiter=',')
			fileWriter.writerow(header)
			for row in sortedlist:
				fileWriter.writerow(row)

if args.list:
	print_table(file)
if args.dir:
	files = get_files()
	for f in files:
		print(f)
if args.search:
	search_csv()
if args.write:
	write_sorted(file)