""" Extract email senders from a folder recursively """
import sys, re
sys.path.insert(0, 'c:/py/jsn/')
from rx import *
#================================================
#get all emails in files in emails folder in d:\info directory
#folder, path, list, outfile name
folder = 'Emails'
path = '\%s' % folder
# get names of all files
files = RX().get_files(path)
dates = []
# extract emails
for file in files:
	text = open(file, 'r', encoding='iso-8859-1').read()
	result = re.findall(r'(\d{2}[.-/ ]((\d{2})|...)[.-/ ]20\d{2})', text,re.M|re.I)
	#remove empty results
	for e in result:
		if e[0] != None:
			dates.append(e[0])
# remove duplicates
return_list = list(set(dates))
#sort alphabetically
sorted_list = sorted(return_list, key=lambda x : x[-1:])
# write to emails.txt file in current directory
with open('dates.txt', 'w', encoding='utf-8') as f:
		f.write("\n".join(sorted_list))