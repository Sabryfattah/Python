"""
This script find a filename matching a pattern.
The default directory is e:\confidential, so you can search that directory by:
1. find [pattern]

You can search any other directory for a matching filename.
2. find [pattern] -d [Directory] 
***IN THIS ORDER :: Pattern -d directoryname***

The files matching the pattern are displayed in numbered list.
Select a number to run the file by its associated executable.
e.g. txt, pdf, docx, jpg, ..etc.
"""
#======================================================
import os
import re
from sys import argv
from os.path import basename
import argparse
#=====================================================
#argparse function
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description = __doc__,
usage = "\n1. find [pattern] #(for default 'e:\confidential' directory)\n2. find [pattern] -d [directory] #(for any other directory)")
parser.add_argument("-d",  "--dir", default='e:\\confidential\\', help="folder to search in")
parser.add_argument("pat",  help="Pattern to search for")
args = parser.parse_args()
#=======================================================
def get_file_dirs(src):
	"""get file list from source directory and add to list FILES"""
	tree = os.walk(src)
	DIRS = []
	FILES = []
	for d in tree:
		DIRS.append(d[0])
		for f in d[2]:
			FILES.append(d[0]+"\\"+f)
	return FILES

def find_matches(src,pat):
	"""match the pattern to names of files in FILES and print a list """
	matches =  []
	files = get_file_dirs(src)
	reg = re.compile(".*"+pat+".*$", re.IGNORECASE)
	for line in files:
		matches += reg.findall(line)
	return matches
		
def list_matches(matches):
	fileList = []
	for index,i in enumerate(matches, 1):
		name = os.path.splitext(basename(i))[0]
		fileList.append(name)
		print((index, "==", name))
	return fileList

def select_file2open(matches):
		selected = eval(input("Select a file number to open: "))
		try:
			os.startfile(matches[int(selected)-1])
			print(("file ...[", matches[int(selected)-1],"]....opened"))
			print(("="*78))
		except:
			print("You must select a number")
			select_file2open(matches)
 
def usr_continue(src, pat):
	matches = find_matches(src,pat)
	while True:
		answer = eval(input("Would you like to select another file? (y/Y or n/N): "))
		if answer in ['n', 'N']:
			print('Goodbye')
			exit()
		else:
			select_file2open(matches)	



pat = args.pat
src = args.dir
matches = find_matches(src,pat)
if matches != []:
	matches = find_matches(src,pat)
	list_matches(matches)
	select_file2open(matches)
	usr_continue(src, pat)
else:
	print("can not find file in e:/confidential")
	exit