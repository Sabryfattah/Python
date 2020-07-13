"""This script search a csv file for matching string or part of it 
and display result in formated output.

Headings are (URL,EMAIL,USERNAME,PASSWORD).
User enter the name of csv file without extension and search term.
Put all csv files in the data folder in current directory.
Remember to make all letters lowercase in csv file, 
and ensure that number of columns is only 4 or modify script 
if you use more columns."""
#=================================================================
import argparse
import sys
import csv
import opts
import os
#=================================================================
parser = argparse.ArgumentParser(description = __doc__, 
usage = "\nSearch CSV file for matching string\ntag [file] [search term]")
parser.add_argument("file",  help="filename to search without ext")
parser.add_argument("term",  help="pattern or term to search for")
args = parser.parse_args()

#===================================================
path = os.path.dirname(__file__)+"\\data\\"
term = opts.args.term.lower()
file= opts.args.file
#===================================================
csvfile = open(path+file+".csv", "r")
csvfile.seek 
reader = csv.reader(csvfile, dialect='excel', delimiter=",", quotechar="'")
#=======================================================
for line in reader:
	if any(term in col for col in line):
		print("------------------------------------------------------")
		print(("URL:          " + line[0]))
		print(("USERNAME:     " + line[2]))
		print(("EMAIL:        " + line[1]))
		print(("PASSWORD:     " + line[3]))
		print("------------------------------------------------------")
#=======================================================
csvfile.close()

