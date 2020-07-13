"""
Purpose : display python documentation for a keyword or function in a module.
dc -b ==> get a list of builtins  functions
dc -s ==> get a list of standard libraries modules
dc -m ==> get a list of all modules 
dc <keyword or module_name>.< module.method>
dc (keyword) shows all functions and objects. Select one for details : e.g. dc string.upper
"""
import argparse
import os,re
import subprocess
"import module stdlib_list to access standard library"
from stdlib_list import stdlib_list
####################################################
class Documentation:
	def __init__(self):
		"Argparse module"
		self.parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description=__doc__,
		usage = "dc <keyword>|<module_name>.<module.method> " )
		self.parser.add_argument("word", nargs="?", action= "store", help="Keyword ")
		self.parser.add_argument("-b", "--builtin", action= "store_true", help="builtins methods")
		self.parser.add_argument("-s", "--stdlib", action= "store_true", help="standard libraries")
		self.parser.add_argument("-m", "--modules", action= "store_true", help="all modules")
		self.parser.add_argument("-w", "--write", action= "store_true", help="write keyword documentation to a file")
		self.args = self.parser.parse_args()
		self.doc = []
	
	def builtins(self):
		"list builtins functions"
		blt = subprocess.check_output("python -c help(__builtins__)", shell=True)
		doc = blt.decode().split("\n")
		#sourcefile = open("builtins.txt", 'a')
		for line in doc:
			if "|" not in line and "class" not in line:
				print(line)
	
	def stdlib(self):
		"list all modules in standard libraries"
		libraries = stdlib_list("3.5")
		#sourceFile = open("stdlib.txt", 'w')
		print("\n".join(libraries))
		return libraries
	
	def docit(self):
		"display documentations for a keyword"
		output = subprocess.check_output("python -m pydoc {}".format(self.args.word), shell=True)
		doc = output.decode(encoding='UTF-8',errors='ignore').split("\r\n")
		for x in doc : print(x)
		for line in  doc[1:]:
			if line != "" and not "_" in line:
				line = re.sub("-|\|", "", line)
				if re.search(" ", line) : print(line)
				self.doc.append(line)
		
	def write_doc(self):
		"write documentation to a file"
		with open(self.args.word+".txt", 'w') as f:
			self.docit()
			for line in self.doc: f.write(line+"\n")
	
	def modules(self):
		"list all installed modules"
		mods = subprocess.check_output("python -c help('modules')", shell=True)
		doc = mods.decode().split("\r\n\r\n")
		for line in doc:
			print(line)
			open("Modules.txt", 'a').write(line)
###################################################
if __name__ == "__main__":
	d = Documentation()
	if d.args.stdlib:
		d.stdlib()
	elif d.args.builtin:
		d.builtins()
	elif d.args.modules:
		d.modules()
	elif d.args.write:
		d.write_doc()
	else: d.docit()