import argparse
import os
from . import find
from . import indexing
#==========================================================
path = os.path.dirname(__file__)+"\\data\\"
parser = argparse.ArgumentParser(
formatter_class=argparse.RawDescriptionHelpFormatter,
description="""This script searches for a file in a directory and open it.
find: searches for files matching a pattern and list them. 
The selected file is opened by default executable.
index: compiles or updates an index file for the directory contents . 
""", usage="""=====Secondary Positional Arguments ========
f find [pattern] [index file]
f index [folder]""")
subparsers = parser.add_subparsers()
find_parser = subparsers.add_parser("find", help="This sub-command lists all directory contents")
find_parser.add_argument('pat', action='store', help='Pattern to search for')
find_parser.add_argument('idx', action='store', help='index file to search')
index_parser = subparsers.add_parser("index", help="create an index file from directory listing")
index_parser.add_argument('dir', action='store', help='Directory to index')
#==========================================================
args = parser.parse_args()
d =  vars(args)
print(d)
if 'pat' in d:
	find.find(d['pat'],path+d['idx']+".txt")
elif 'dir' in d:
	indexing.index(d['dir'])