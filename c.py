"""
Scientific Calculator
Enter equation in normal way to get result:
e.g.: pi * sin 90 - sqrt 81
Functions available: + (addition), -  (subtraction), * (multiplication)
/ (division), % (percentage), sine (sin(rad)), cosine (cos(rad)),
tangent (tan(rad)), sqrt(n) (square root), pi (3.141)
"""
import math
import re
import argparse
import sys



class Calc:
	def __init__(self):
		self.parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
			description=__doc__,
			usage="calc [string of equation]")
		self.parser.add_argument('string', nargs='+', help="string of equation")
		self.args=self.parser.parse_args()

	def calc(self, k):
		np = []
		for op in k:
			if op[0].isalpha():
				np.append("math.{}".format(op))
			else:
				np.append("{}".format(op))
		s = " ".join(np)
		s =  re.sub(r' (\d+)', r'(\1)', s)
		s =  re.sub(r'\^', r'**', s)
		print(s)
		k = eval(s)
		return k
#======================================================
if __name__ == "__main__":
	c = Calc()
	k = c.args.string
	print(c.calc(k))