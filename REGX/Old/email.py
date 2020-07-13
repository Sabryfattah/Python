""" Extract Data from unstructured text file  """
import sys, re
from rx import *
#================================================
class EXREG():
	def __init__(self, file=None, text = None):
			self.parser = argparse.ArgumentParser(
				formatter_class=argparse.RawDescriptionHelpFormatter,
				description = __doc__,
				usage="exreg <options>")
			#self.parser.add_argument('file',nargs="?", action='store', help='text file')
			#self.parser.add_argument('string', nargs="?", action= 'store', help='string to match')
			self.parser.add_argument('-d',"--dates", action='store_true', help='extract titles (capitalized ngrams)')
			self.parser.add_argument('-e',"--emails", action='store_true', help='extract sentences including key word')
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
			#self.path = "NLTK/data/"
			self.folder = 'Emails'
			self.path = '%s' % self.folder

	def get_result(self):
		files = RX().get_files(self.path)
		result = []
		for file in files:
			text = open(file, 'r', encoding='iso-8859-1').read()
			regx = re.compile(r'(\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b)', re.M|re.I)
			result = re.findall(regx,text)
		return result

	def result_clean(self):
		result = self.get_result()
		cleaned = []
		for e in result:
			if e != None:
				cleaned.append(e)
		clean_list = list(set(cleaned))
		sorted_list = sorted(clean_list)
		return sorted_list

	def write2file(self):
		doc = self.result_clean()
		# write to txt file in current directory
		filename = input("Filename to write result ? \n")
		with open(filename+'.txt', 'w') as f:
				f.write("\n".join(doc))
	def main(self):
		self.write2file()
######################################################
if __name__ == "__main__" :
	ex = EXREG()
	ex.main()