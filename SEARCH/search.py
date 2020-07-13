"""
This script reads a file and split it to chunks either by line or paragraph.
User search the file for a pattern string in file lines.
The script returns the line or the whole paragraph containing the pattern.
The Pattern is case-insensitive.
The Pattern will be displayed in upper case between square brackets.
How to Use:
default is to display all lines containing the pattern.
To display paragraphs containing the pattern add -p at the end.
pattern can be a full word or part of a word or a sentence.
to search for a number of words enclose them in double quotes.
to avoid searching part pattern in the middle of a word use word boundary \b or space.
to search for words separated by number of sentences use .* between them.
Use regex patterns for searching.
"""
""" required modules """
import re
import textwrap
import argparse
import sys,os
import string
from os import walk
from os.path import join

""" Argparse """
class CLARGS():

	@classmethod
	def clarg(cls):
		parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description=__doc__,
		usage="scrap <-l or -p> [file] [pat]")
		parser.add_argument('pat', nargs='*', help='pattern to search ["quote" adjacent words]')
		parser.add_argument('-d', '--directory', default="c:/info/", help="search by line")
		parser.add_argument('-l', '--line', action="store_true", help="search by line")
		parser.add_argument('-s','--sentence', action="store_true", help='search by sentence')
		parser.add_argument('-p','--paragraph', action="store_true", help='search by paragraph')
		args = parser.parse_args()
		return args

""" Text wrap function to wrap lines longer than screen width """

w = textwrap.TextWrapper(
	width= 80, 
	break_long_words=False, 
	replace_whitespace= False,
	expand_tabs = False,
	drop_whitespace = False,
	initial_indent = "",
	fix_sentence_endings = False,
	break_on_hyphens = False,
	subsequent_indent = ""
	)


class Scrap():
	
	def __init__(self, LF, dir, pat):
		self.LF = LF
		self.pat = pat
		self.dir = dir

	def clear_screen(cls):
		""" Clear Screen  and run all functions in sequence """
		os.system("cls")
		
	def get_files(self, dir):
		""" Get all files in directory """
		files = [join(folder, f) for folder, dirs, files in walk(dir) for f in files]
		return files

	def split2Chunks(self, files, LF):
		""" loop through file list and split each into chunks by number of \\n"""
		lines = []
		for file in files:
			f = open(file).read()
			line = f.split("{}".format(LF*"\n"))
			lines.append(line)
		return lines

	def check_pat(self, pat, lines, LF):
		""" check pattern given in args to each chunk of file  """
		lst = []
		fl = []
		for line in lines:
			#if set(args.pat).issubset(set(line.lower().split(" "))):
			""" add found chunks to a list """
			for item in line:
				if re.search(item, line, re.IGNORECASE |re.MULTILINE):
					lst.append("-"*80 + "\n {}".format(line) + "\n" + "-"*80)
					""" also make a list of files where match is found """
				#fl.append(file)
		return lst

	def print_chunks(self, lst):
		""" print all found chunks and wrap text """
		for  item in lst:
			print(("\n".join(w.wrap("".join(item)))))

	def print_file_list(self, fl):
		""" make a list of all matching unique files """ 
		nl = list(set(fl))
		""" print a numbered list of matching files """
		for index,  line in enumerate(nl):
			print((index+1, "-", line))
		print(("="*80))
		
	def get_user_select(self):
		""" get user file selection """
		n = eval(input("Enter a number to open file or ENTER to exit:   "))
		print(("="*80))
		if n:
			""" open selected file by default editor """
			os.system(nl[int(n)-1])
			split_files(1)
		elif n == '': 
			exit
			

###############################################################
if __name__ == "__main__":
	args = CLARGS.clarg()
	dir = args.directory
	pat = args.pat
	LF = 1
	if args.paragraph:
		LF = 3
	elif args.sentence:
		LF = 2
	elif args.line:
		LF = 1
session = Scrap(LF, dir, pat)
files = session.get_files(session.dir)
lines = session.split2Chunks(files, LF)
lst = session.check_pat(pat, lines, LF)
#print(fl)
#lst, fl = session.check_pat(session.pat, lines, fls, session.LF)
