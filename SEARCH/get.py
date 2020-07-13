import argparse
import re
import os, sys
"""
search documents for a specific piece of information.
opens files in src (default='d:/inf') and searches them.
Each file is divided into sections by three linefeeds, with heading at first line separated by repeated '-'.
script searches for a regex pattern in heading and then list all matching headings. 
Under select one or more matching item to open and display relevant documentation.
Usage : pydc <pattern> <folder[optional]>
pattern is a number of words separated by spaces.
The order of such words should be the same as their order in matching headings.
To search for words in any order use option (-f) [for free]

"""


#======================================================
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description = __doc__,
usage = " [pattern of multiple words in ' ' separated by spaces] <options>")
parser.add_argument("pat", nargs="*", help="Pattern to search for")
parser.add_argument("dir", nargs = '?', default='d:/info', help="folder to search (optional, default= 'd:/info')")
args = parser.parse_args()
pattern = args.pat
dir = args.dir

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
#========================================================

#========================================================
" get a list of files in source folder "

def get_files(src):
	list = []
	for root, dirs, files in os.walk(src):
		for file in files:
			list.append(root+"\\"+file)
	return list
	
#=========================================================
'split each file into chunks by \n\n\n '

def chunker(src):
	menu = []
	subject = []
	src_files = get_files(src)
	for file in src_files:
		with open(file, 'r') as f:
			text = f.read()
		"split text by paragraph "
		chunk_list = text.split("\n\n\n\n")
		" add paragraphs into list chunks "
		for para in chunk_list:
			" divide each chunk into two parts : menu and subject "
			parts = para.split("\n")
			a = re.search(".*".join(pattern), parts[0], re.I)
			b = set(pattern).issubset(set(list(parts[0].split(" "))))
			if a or b: 
				menu.append(parts[0])
				subject.append(parts[1:])
	return [menu, subject]
#=========================================================
def display_list(src):
	menu = chunker(src)[0]
	subject = chunker(src)[1]
	for index, item in enumerate(menu, 1):
		if re.search(".*".join(pattern), item, re.I):
			print((index, " : ", item))
	try:
		while 1:
			selection = eval(input("Select a number from list : "))
			print(("="*78))
			print((menu[int(selection)-1]))
			print(("="*78))
			print(("\n".join(subject[int(selection)-1])))
			print(("="*78))
			answer = eval(input("Do you want to select another item : ['y' or 'n]"))
			if answer == 'n': 
				break; exit
	except:
		print("You must select a number\n")
#=========================================================
	
display_list("d:/info")
