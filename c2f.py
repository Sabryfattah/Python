import argparse

parser = argparse.ArgumentParser(description = """
This script convert temperature from Celsius to Fahrenheit and vice versa.
e.g. c2f 100 f    #=> 38 Celsius.
e.g. c2f 38 c #=> 100 Fahrenheit""",
usage = "conv [degrees] [scale]"	)
parser.add_argument("degrees",  help="degrees of temperature to convert.")
parser.add_argument("scale",  help="type of temperature scale (f or c)")
args = parser.parse_args()

if args.scale == 'f':
	print  (float(args.degrees)- 32) * 0.555556, " Celsius" 
else:
	print (float(args.degrees) * 1.8) + 32, " Fahrenheit"