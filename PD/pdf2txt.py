"""Convert PDF File to Text File"""
import pandas as pd
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
#####################################################
def convert_pdf_to_txt(path_to_file):
	rsrcmgr = PDFResourceManager()
	retstr = io.StringIO()
	codec = 'iso-8859-1'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
	fp = open(path_to_file, 'rb')
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	password = ""
	maxpages = 0
	caching = True
	pagenos=set()

	for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
		interpreter.process_page(page)
	text = retstr.getvalue()
	fp.close()
	device.close()
	retstr.close()
	return text
	
text = convert_pdf_to_txt("pd/test.pdf")
print(text)
