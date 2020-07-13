from .f import opts

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
#======================================================
import os
import re
from sys import argv
from os.path import basename
import argparse
#idx_file = "index.txt"
#=====================================================
#argparse function
def cl_args(self):
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description = __doc__,
	usage = "\n1. find [pattern] #(for default 'e:\confidential' directory)\n2. find [pattern] -d [directory] #(for any other directory)")
	parser.add_argument("-d",  "--dir", default='e:\\confidential\\', help="folder to search in")
	parser.add_argument("pat",  help="Pattern to search for")
	args = parser.parse_args()
	args = vars(args)
	return args
#=======================================================
def get_file_dirs():
	"get file list from source directory and add to list FILES"
	tree = os.walk(src)
	DIRS = []
	FILES = []
	for d in tree:
		DIRS.append(d[0])
		for f in d[2]:
			FILES.append(d[0]+"\\"+f)
	return FILES

def find_matches(src,pat):
	"match the pattern to names of files in FILES and print a list "
	matches =  []
	files = get_file_dirs()
	reg = re.compile(".*"+pat+".*$", re.IGNORECASE)
	for line in files:
		matches += reg.findall(line)
	return matches
		
def list_matches(matches):
	for i in matches:
		print((matches.index(i)+1, "==", basename(i)[:-4]))

def select_file2open(matches):
	while True:
		selected = eval(input("Select a file number to open: "))
		os.startfile(matches[int(selected)-1])
		print(("file ...["+ matches[int(selected)-1] +"]....opened"))
		print(("="*78))
		answer = eval(input("Would you like to select another file? (y/Y or n/N): "))
		if answer in ['n', 'N']:
			print('Goodbye')
			exit()
		if answer in ['y', 'Y']:
			select_file2open(matches)		


if __name__ == "__main__":
	pat = cl_args()['pat']
	src = cl_args()['dir']
	matches = find_matches(src,pat)
	list_matches(matches)
	select_file2open(matches)
	

#path = os.path.dirname(__file__)+"\\f\\data\\"
def find(pat,idx_file):
	textfile = open(path+idx_file, 'r')
	matches = []
	reg = re.compile(".*"+pat+".*$", re.IGNORECASE)
	for line in textfile:
		matches += reg.findall(line)
	textfile.close()
	for i in matches:
		print matches.index(i)+1, "==", basename(i)[:-4]		
	selected = input("Select a file number to open: ")
	os.startfile(matches[selected-1])
	print "file ...["+ matches[selected-1] +"]....opened"
	choice = raw_input("Would you like to go back? (y/Y or n/N): ")
	if choice not in ['n', 'N']:
		find(args.pat,idx_file)
	exit
#=======================================================
find(args.pat,idx_file)

"""
