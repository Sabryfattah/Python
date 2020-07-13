import re
from os import walk
import os
import pyPdf
from argparse import ArgumentParser
import textwrap
#=====================================================
parser = ArgumentParser(description='search pdf file for a string')
#parser.add_argument('dir', action='store', help='directory to search')
parser.add_argument('pat', action='store', help='pattern to search for')
args = parser.parse_args()
#=======================================================
FILES = []
DIRS = []
path = "c:\PDF"
#========================================================
def get_file_dirs(src):
	tree = os.walk(src)
	for d in tree:
		DIRS.append(d[0])
		for f in d[2]:
			 if f.endswith(".pdf"): 
				FILES.append(d[0]+"\\"+f)
	return FILES

def fnPDF_FindText(xFile, xString):
	# xfile : the PDF file in which to look
	# xString : the string to look for
	file_list = []
	PageFound = 1
	File_Found = ""
	m = ""
	pdfDoc = pyPdf.PdfFileReader(file(xFile, "rb"))
	for i in range(0, pdfDoc.getNumPages()):
		content = ""
		content += pdfDoc.getPage(i).extractText() + "\n"
		content1 = content.encode('ascii', 'ignore').lower()
		ResSearch = re.search(xString, content1, re.IGNORECASE)
		if ResSearch is not None:
			PageFound = i
			print(("="*78))
			text = ResSearch.group()
			text = re.sub("\.\s","\r\f", text )
			list = textwrap.wrap(text, width=78)
			for element in list:
				element = element.upper()
				print(element)
			print(("-"*78))
			selected = file_list.append(xFile)
			print(("Found in {}".format(xFile)))
			file_list.append(xFile)
			break
	return file_list
#===========================================================
if __name__ == "__main__":
	FILES = get_file_dirs(path)
	pat = args.pat 
	FL = []
	for f in FILES:
		rt  = fnPDF_FindText(f, pat)
		FL.append(rt)
	print(("="*78))
	print(("FOUND FILES".center(78)))
	print(("="*78))
	nnil = [x for x in FL if x != []]
	for index, f in  enumerate(nnil):
		print((index, " : ", f[0]))
	choice = ""
	while choice is not "q":
		try:
			choice = eval(input("Selected File No. to open or 'q' to quit : >> "))
			num = int(choice)
			os.startfile(nnil[num][0])
		except:
			print("Exiting .......")