""" find records in DataFrame 
by pattern or substring in a given column """
from pd import *
import pandas as pd
import os
#############################################################
class Find_df():
	def __init__(self, path=None, file=None):
		self.path = "data/"
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="fnd <options> [file]")
		self.parser.add_argument('file', action='store', help='csv file')
		self.parser.add_argument('-f',"--findpat", action='store_true', help='pattern to search for')
		self.args = self.parser.parse_args()
		self.file = self.args.file

	def print_table(self,df):
		print(tabulate(df, headers='keys', tablefmt='psql', showindex=True, numalign="left"))
		total = df.sum(numeric_only=True)
		print(total)
		return total

	def find_pat(self):
		pd.set_option('display.max_colwidth', 500)
		pd.set_option('display.expand_frame_repr', False)
		pd.set_option('display.max_columns', 500)
		df = pd.read_csv(self.path + self.file + ".csv", encoding='iso-8859-1')
		colnames = df.columns.values
		col = input("Select Column :..>>\n{}\n".format(colnames))
		pat = input("Enter Pattern :..>>\n")
		result = df[df[col].str.contains(r'{}'.format(pat), case = False)]
		self.print_table(result)
###############################################################
if __name__ == "__main__" :
	p = Find_df()
	if p.args.findpat: p.find_pat()