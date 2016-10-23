"""
#parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, 
description=("""This script searches the 'E:/confidential' directory 
#for files matching a given pattern. 
#All files are text files with extension 'txt'.
#Once the pattern is found a list of matching files is displayed.
#User select a number from the list, this opens the file in notepad."""),
usage = '''find <pattern>
	e.g. find ebay''')
parser.add_argument('pat', help='pattern to search for')
subparsers = parser.add_subparsers(dest="subparser_name")
index_parser = subparsers.add_parser('index', help= 'indexing of filenames')
index_parser.add_argument('-f', '--folder', help= 'folder to index into file')
args = parser.parse_args()

"""