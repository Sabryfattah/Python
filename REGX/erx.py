""" 
Extract Data from unstructured text file :
==================================
Review text and compile a regex pattern.
Enter regex pattern as argument between one or two (())
e.g. ((\bhttp://\w+[.]\w+[.]\w+[.]\w+))
Check result before printing to file
 """
 ###################################################
import argparse
#================================================
class EXREG():
	def __init__(self, folder=None, path=None):
		self.path = r'\data\'
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="exreg <options>")
		self.parser.add_argument('pattern', nargs="?", action= 'store', help='string to match')
		self.parser.add_argument('-ds',"--dates", action='store_true', help='extract titles (capitalized ngrams)')
		self.parser.add_argument('-em',"--emails", action='store_true', help='extract sentences including key word')
		self.parser.add_argument('-sd',"--sender", action='store_true', help='extract sentences including key word')
		self.parser.add_argument('-u',"--user", action='store_true', help='extract data by user entered regex pattern')
		self.parser.add_argument('-x',"--texe", action='store_true', help='extract text from exe file')
		self.args = self.parser.parse_args()

	def get_files(self, path):
		"Get list of files from folder recursively"
		FILES = []
		for (roots, dirs, files) in os.walk(path):
			for file in files:
				FILES.append(roots+"\\"+file)
		return FILES

	def get_result(self, regx):
		files = self.get_files(self.path)
		#txtfiles = [e for e in filter(lambda x: x[-4:] == '.htm', files)]
		result = []
		for file in files:
			text = open(file, 'r', encoding='iso-8859-1').read()
			r = re.findall(regx,text)
			if r != None:
				result.append(r)
		return result

	def result_clean(self, regx):
		result = self.get_result(regx)
		cleaned = []
		for e in result:
			if e:
				for m in e:
					cleaned.append(m)
		clean_list = list(set(cleaned))
		sorted_list = sorted(clean_list)
		return sorted_list

	def write2file(self, regx):
		doc = self.result_clean(regx)
		resp = input("Write to a text file? (y/n)\n>")
		text = "\n".join([re.sub(r'<.*.>', '', e[0]) for e in doc])
		print(text)
		if resp == 'y':
			filename = input("Filename to write result ? \n")
			with open('Extracts/'+filename+'.txt', 'w', encoding='iso-8859-1') as f:
					f.write("Pattern : {}".format(regx)+"\n")
					f.write(text)
		else:
			exit
			

	def extract_yaml(self, regx):
		folder = 'E://'
		file = input("file name ?  >\n")
		text = open(folder+file+'.txt', 'r', encoding='iso-8859-1').read()
		r = re.findall(regx, str(text))
		text = "\n".join([re.sub(r'<.*.>|with|of|within|mixed|on|and|miles|will|be|served', '', e[0]) for e in set(r)])
		print(text)
		return text
			
			
######################################################
if __name__ == "__main__" :
	email_regx = re.compile(r'(\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b)', re.M|re.I)
	dates_regx = re.compile(r'(\d{2}[.-/ ]((\d{2})|...)[.-/ ]20\d{2})', re.M|re.I)
	sender_regx = re.compile(r'(\b(From:|To:)\s\w+\s\w+\s)',re.M|re.I)
	yml_regex = re.compile(r'(\b([A-Z]\w+\s){2,3})',re.M|re.I)
	ex = EXREG()
	if ex.args.emails : ex.write2file(email_regx)
	if ex.args.dates : ex.write2file(dates_regx)
	if ex.args.sender : ex.write2file(sender_regx)
	if ex.args.user : 
		pat = re.compile(r"{}".format(ex.args.pattern), re.M|re.I)
		print(pat)
		ex.write2file(pat)
	if ex.args.texe : 
		text = ex.extract_yaml(yml_regex)
		filename = input("Filename to write result ? \n")
		with open(filename+'.txt', 'w', encoding='iso-8859-1') as f:
				f.write(text)