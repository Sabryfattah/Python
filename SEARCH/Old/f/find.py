import os
import re
from sys import argv
from os.path import basename
#=====================================================
path = os.path.dirname(__file__)+"\\data\\"
def find(pat,idx_file):
	textfile = open(idx_file, 'r')
	matches = []
	reg = re.compile(".*"+pat+".*$", re.IGNORECASE)
	for line in textfile:
		matches += reg.findall(line)
	textfile.close()
	for i in matches:
		print((matches.index(i)+1, "==", basename(i)[:-4]))		
	selected = eval(input("Select a file number to open: "))
	os.startfile(matches[selected-1])
	return find(pat,idx_file)
#=======================================================