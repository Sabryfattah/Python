""" 
1- create a data file with names of scripts and their use, each on a separate line separated by ;
(List all scripts in c:\py folder and what each script actually does.)
2- read the file into var and then split each line into 2 parts
3- print the two parts formated
"""
src = "./data/all.csv"
#assign filename to var src

#build a function list_files with arg src
def list_files(src):
	#assign sorted lines read from src filename to var list
	list= sorted(open(src, 'r').readlines())
	#iterate line by line over list of file lines
	for line in list:
		#assign each split line by ; to a list named script, stripping all whitespaces
		script = line.strip().split(";")
		#print each part of script formatted at 7 and 10 characters from left
		print(("{:<7} => {:<10}".format(script[0],script[1])))

#call function list_files with arg src
list_files(src)

"""
1- assign to variable
2- build a function with arguments
3- read file into string variable
4- read file lines into a list
5- strip whitespaces from lines in a file
6- split a string into list
7- format printed string
8- call a function
9- sort lines read from a file
"""