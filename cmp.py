import argparse

parser = argparse.ArgumentParser(description = 
"""This script  calculates compound interest of amount invested 
for a number of years. User enter 
the Principal Amount, Number of years, Annual interest Rate as a float
(e.g. 0.05 is 5%)'
Times compounded each year, e.g. 1 Annually, 4 Quarterly, 12 monthly.
The result is printed to the screen""",
usage = "cmp  [p: amount] [t: years] [r: rate] [n: number of annual compound]"	)
parser.add_argument("p", help="Principal Amount invested")
parser.add_argument("t", help=" Number of years of investment")
parser.add_argument("r", help="Annual rate of interest")
parser.add_argument("n", help="Number of Times interest is compounded each year(1,2,4,12)")
args = parser.parse_args()

p = int(args.p)
r = float(args.r)
n = int(args.n)
t = int(args.t)

result = p * (1 + (r/n) )** (n*t)
print """Payment received after %d years 
for investment of %d pounds 
with interest rate of %.1f percent
interest paid %d times every year
is""" %(t,p,(r*100),n), "%.2f" % result