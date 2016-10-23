import argparse

def hi():
	print "Hello"

def w():
	print "World"

parser = argparse.ArgumentParser() 
subparsers = parser.add_subparsers()
subparser_a = subparsers.add_parser('a')                                                                                                 
subparser_a.add_argument('--hh', default=hi(),  help='username') 
subparser_b = subparsers.add_parser('b')                                                                                                                       
subparser_b.add_argument('--w',  default= w(), help='debug flag')
args = subparser_a.parse_args('b')
#parser.set_defaults(func=hi)
