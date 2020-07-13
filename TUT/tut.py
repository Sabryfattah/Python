"""
gui : 
2 text : sections, one show code; the second show output
llistview of titles of subjects, click on row display code in text view, click on run button exec the code
and show output in output text field.
-----------------------------------------------------
entry field for pattern to search for in all files in a directory.
Entry for pattern--> get pattern
files -> text -> paras -> {title,subject}
label of subject <-- title
list view  : text area for code <-- subject from dict
listview  : text are for output  --> exec output
button to run code --> exec
----------------------------------------------------
search python tutorial text files in c:\\tut\\data for specific subject.
text files in directory contain blocks of text each separated by two linefeeds.
each block have a title and subject, titles separated from subjects by ==>
"""
import os
import string
import argparse
import glob
###############################################
class Pytut:
	def __init__(self, path=None):
		self.path = "C:\\Users\\User\\OneDrive\\PY\\python_documentation\\data\\"
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="Pytut [directory] [pattern]")
		self.parser.add_argument('pattern', nargs="+", action='store', help='Regex Pattern to search for')
		#self.parser.add_argument('-f', '--files', action='store_true', help='Get filenames in path')
		self.args = self.parser.parse_args()
		self.pat = self.args.pattern
		
	
	def get_files(self):
		files = glob.glob(self.path+'*.txt')
		return files
	
	def get_file_text(self, file):
		with open(file, 'r') as f:
			text = f.read()
		return text
	
	def get_blocks(self,text):
		blocks = text.split("\n\n\n")
		return blocks
		
	def make_dict(self):
		dict = {}
		files = self.get_files()
		try:
			for file in files:
				text = self.get_file_text(file)
				blocks = self.get_blocks(text)
				for block in blocks:
					key,value = block.split("==>")
					dict[key] = value
		except: print("error in file  ", file)
		
		return dict
		
	def get_matching_keys(self, pat):
		matching_keys = []
		for key in self.make_dict().keys():
			if set([x.lower() for x in pat]).issubset(set([k.lower() for k in key.split(' ')])):
				matching_keys.append(key)
		return matching_keys
		
	def list_matching_keys(self, pat):
		mks = self.get_matching_keys(pat)
		for i,key in enumerate(mks):
			print(i+1,"-",key)

	def select_key(self):
		selected = input("Select number : ")
		if selected : return int(selected)-1
		else : return 0

	def display_value(self, pat):
		matching_keys = self.get_matching_keys(pat)
		dict = self.make_dict()
		selected = self.select_key()
		print("="*80)
		try : 
			print(matching_keys[selected])
			print(dict[matching_keys[selected]])
			print("-"*80)
			exec(dict[matching_keys[selected]])
			print("="*80)
		except : print("Not found")

	def run(self):
		self.list_matching_keys(self.pat)
		self.display_value(self.pat)
		while input("Further Selection (y/n) :  ") == 'y' :
			self.display_value(self.pat)

###############################################
if __name__ == "__main__":
	p = Pytut()
	p.run()