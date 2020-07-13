#===============================================
import yaml
import sys, re
#===============================================
path = "DATA/"
filename = "t"
file = path+filename+".yaml"
#==============================================
def read_y():
	with open('{}'.format(file), 'r') as f:
		doc = yaml.safe_load(f)
	return doc
#=======================================================
print(read_y())