"""
search documents for a specific piece of information.
opens files in src (default='d:/inf') and searches them.
Each file is divided into sections by three linefeeds, 
with heading at first line separated by repeated '-'.
script searches for a regex pattern in heading and then list all matching headings. 
Under select one or more matching item to open and display relevant documentation.
Usage : pydc <pattern> <folder[optional]>
pattern is a number of words separated by spaces.
The order of such words should be the same as their order in matching headings.
To search for words in any order use option (-f) [for free]

"""

import re
import os,sys
import argparse
from os.path import isfile #, join
#======================================================
src = "d:/info"
#======================================================
parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description = __doc__,
	usage = " [pattern of multiple words in ' ' separated by spaces] <options>")
parser.add_argument("dir", nargs = '?', default='d:/info', help="folder to search (optional, default= 'c:\\py\\docum\\docs')")
parser.add_argument("pat", nargs="*", help="Pattern to search for")
args = parser.parse_args()
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
#===================================================
pattern = args.pat[0:]
dir = args.dir
#========================================================
" get a list of files in source folder "
def get_files(src):
	files = []
	root = []
	for root, dirs, files in os.walk(src):
		for file in files:
				files.append(file)
				root.append(root)
	return files,root
#=========================================================
""" split each file into chunks by \n\n\n """
def chunker(src):
	menu = []
	subject = []
	src_files = get_files(src)
	for file in src_files:
		with open("{}/{}".format(src,file), 'r') as f:
			text = f.read()
		"""split text by paragraph """
		chunk_list = text.split("\n\n\n\n")
		""" add paragraphs into list chunks """
		for para in chunk_list:
			" divide each chunk into two parts : menu and subject "
			parts = para.split("\n")
			a = re.search(".*".join(pattern), parts[0], re.I)
			b = set(pattern).issubset(set(list(parts[0].split(" "))))
			if b: 
				menu.append(parts[0])
				subject.append(parts[1:])
	return [menu, subject]

def display_list():
	menu = chunker(src)[0]
	subject = chunker(src)[1]
	for index, item in enumerate(menu, 1):
		print((index, " : ", item))
	while 1:
		selection =eval(input("Select a number from list : "))
		print(("="*78))
		print((menu[int(selection)-1]))
		print(("\n".join(subject[int(selection)-1])))
		print(("-"*78))
		answer = eval(input("Do you want to select another item : ['y' or 'n]"))
		if answer == 'n': break; exit

if __name__ == "__main__":
	#main()
	display_list()