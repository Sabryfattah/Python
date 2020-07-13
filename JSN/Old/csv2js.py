import csv
import json
import argparse
##############################################
class JSYM():
	def __init__(self, file=None):
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="JSYM <options> [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='csv file')
		self.parser.add_argument('-j2c',"--js2csv", action='store_true', help='read csv file')
		self.parser.add_argument('-c2j',"--csv2js", action='store_true', help='update csv')
		self.parser.add_argument('-y2j',"--ym2js", action='store_true', help='Replace value in whole table')
		self.args = self.parser.parse_args()
		self.file = self.args.file

	def csv2js(self, file):
		csvfile = open(self.file+'.csv', 'r')
		jsonfile = open(self.file+'.json', 'w')
		fieldnames = ('Site', 'Email', 'User', 'Password')
		reader = csv.DictReader(csvfile, fieldnames)
		for row in reader:
			json.dump(row, jsonfile)
			jsonfile.write('\n')

	def yaml2jason(self, file):
		with open(self.file+".yaml", 'r') as yaml_in, open(self.file+".json", "w") as json_out:
			yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
			json.dump(yaml_object, json_out)

########################################################
if __name__ == "__main__" :
	j = JSYM()
	if j.args.csv2js : j.csv2js(file)
	if j.args.ym2js : j.yaml2jason(file)