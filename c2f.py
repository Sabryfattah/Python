"""convert temperature from Celsius to Fahrenheit and vice versa."""
import argparse
#--------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description =__doc__,
usage = "c2f <scale> [degree]")
parser.add_argument("degree", action="store", help="temperature degree")
parser.add_argument("-f", "--fahrenheit", action="store_true", help="fahenheit")
parser.add_argument("-c", "--celsius", action= "store_true",  help="celsius")
args = parser.parse_args()
#---------------------------------------------------------------------------------------
if __name__ == "__main__":
	if args.fahrenheit : print(round(float(args.degree) - 32 * 0.55, 2), " Celsius")
	if args.celsius : print(float(args.degree) * 1.8 + 32, " Fahrenheit")
