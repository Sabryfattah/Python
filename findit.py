import os
import re
import sys
from os.path import basename
import argparse
#=====================================================
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, 
description=("""This script searches the 'D/Documents' directory 
for files matching a given pattern. 
All files are text files with extension 'txt'.
Once the pattern is found a list of matching files is displayed.
User select a number from the list, this opens the file in notepad.
Filenames are indexed in the file index.txt in the current directory.
To update or change this index file use the indexing.py script"""),
usage = '''find <pattern>
	e.g. find ebay''')
parser.add_argument('pat', help='pattern to search for')
args = parser.parse_args()
pat = args.pat

def findit():
	textfile = open("index.txt", 'r')
	matches = []
	reg = re.compile(".*"+pat+".*$", re.IGNORECASE)
	for line in textfile:
		matches += reg.findall(line)
	textfile.close()
	for i in matches:
		print matches.index(i)+1, "==", basename(i)[:-4]		
	selected = input("Select a file number to open: ")
	os.startfile(matches[selected-1])