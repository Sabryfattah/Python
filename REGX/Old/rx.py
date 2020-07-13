"""
Extract Data from unstructured text using Regex:
=========================================
compile a regex pattern for type of data needed.
use regex on text
"""
#=====================================================
import re, os
import argparse
#=====================================================
class RX():
	def __init__(self, file=None, text = None):
			#self.path = "NLTK/data/"
			self.parser = argparse.ArgumentParser(
				formatter_class=argparse.RawDescriptionHelpFormatter,
				description = __doc__,
				usage="rx <options> [string]")
			#self.parser.add_argument('file',nargs="?", action='store', help='text file')
			self.parser.add_argument('string', nargs="?", action= 'store', help='string to match')
			#self.parser.add_argument('-t',"--term", action='store_true', help='extract titles (capitalized ngrams)')
			#self.parser.add_argument('-e',"--extract", action='store_true', help='extract sentences including key word')
			#self.parser.add_argument('-n',"--normalize", action='store_true', help='normalize text: lowercase, stopwords, stem,lemma,tokenize')
			#self.parser.add_argument('-wf',"--wfreq", action='store_true', help='word frequencies of top 20')
			#self.parser.add_argument('-i',"--inf", action='store_true', help='information and stats about text')
			#self.parser.add_argument('-c',"--colls", action='store_true', help='collocations : five best bigrams')
			#self.parser.add_argument('-tg',"--tags", action='store_true', help='get all words tagged in a list')
			#self.parser.add_argument('-d',"--data", action='store_true', help='get structured important data by Regex')
			#self.parser.add_argument('-s',"--sent", action='store_true', help='Sentiment analysis')
			#self.parser.add_argument('-r',"--repeat", action='store_true', help='get repetitions')
			#self.parser.add_argument('-ne',"--nent", action='store_true', help='get named Entities')
			#self.parser.add_argument('-nr',"--nrel", action='store_true', help='relationship between named Entities')
			#self.parser.add_argument('-sm',"--summarize", action='store_true', help='summarize text')
			#self.parser.add_argument('-gg',"--gtag", action='store_true', help='get list of tagged words by given tag')
			#self.parser.add_argument('-sr',"--srows", action='store_true', help='select specific rows')
			#self.parser.add_argument('-st',"--stats", action='store_true', help='do stats on column')
			#self.parser.add_argument('-g',"--groupby", action='store_true', help='group by column values')
			#self.parser.add_argument('-m',"--modify", action='store_true', help='modify a column by applying a function to it')
			#self.parser.add_argument('-p',"--plot", action='store_true', help='plot a pie')
			#self.parser.add_argument('-q',"--sql", action='store_true', help='read sql database table')
			#self.parser.add_argument('-r',"--csv", action='store_true', help='read csv file')
			#self.parser.add_argument('-u',"--update", action='store_true', help='update field')
			#self.parser.add_argument('-v',"--view", action='store_true', help='adjust view by columns and rows')
			self.args = self.parser.parse_args()
			#self.file = self.args.file
			#self.max = self.args.max

	def get_files(self, path):
		"Get list of files from folder recursively"
		FILES = []
		for (roots, dirs, files) in os.walk(path):
			for file in files:
				FILES.append(roots+"\\"+file)
		return FILES


	def get_emails(self, text):
		r = re.findall(r'((\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b))',text,re.M|re.I)
		emails = "\n".join([e[0] for e in set(r)])
		return emails

	def get_dates(self):
		r = re.findall(r'((^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$))',text,re.M|re.I)
		print("\n".join([e[0] for e in r]))


	def words_in_line(self):
		r = re.findall(r'((^(?=.*?\b%s\b).*?\b%s\b.*))' % ('subject', 'locum'),text,re.M|re.I)
		for n in range(len(r)):
			print(str(n)+": "+r[n-1][0])

	def first_name(self):
		r = re.findall(r'From:\s(\w+.\w+)@',text,re.M|re.I)
		for n in range(len(r)):
			print(str(n)+": "+r[n-1])

	def dates(self):
		r = re.findall(r'((.*\d{2}[.-/ ]((\d{2})|...)[.-/ ]20\d{2}))', text,re.M|re.I)
		s = re.findall(r'((re: .*))', text,re.M|re.I)
		t = re.findall(r'(((?(From: )Date.*|To:.*)))', text,re.M|re.I)
		for n in range(len(r)):
			print(str(n)+": \n"+t[n-1][0])
			#print(str(n)+": \n"+t[n-1][0]+" : \n"+s[n-1][0]+" : \n"+r[n-1][0])
	

	
	def search(self, text):
		string = self.args.string
		r = re.compile("("+string+".*(\n.*){3})", re.M|re.I)
		for m in re.finditer(r, text):
			print("="*80)
			print(file)
			print("-"*80)
			print(m.group(0))
######################################################
if __name__ == "__main__" :
	r = RX()
	print("\n".join(os.listdir('D:\INFO\\')))
	folder = input('folder? : ')
	path = r'%s\\' % folder
	files = r.get_files(path)
	for file in files:
		t = open(file, 'r', encoding='iso-8859-1').read()
		r.search(t)