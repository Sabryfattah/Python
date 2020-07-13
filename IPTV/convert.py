"""
Convert m3u file to engima2 service bouquet format"""
import os,sys
"user enter name of m3u file"
file = sys.argv[1]
"get file as lines"
lines = open(file+".txt", 'r', encoding="utf-8").readlines()
"declare desc as empty as it changes with each channel"
desc = ""
"open bouquet file and add service line and description line for each channel"
with open("userbouquet."+file+".tv", 'a', encoding="utf-8") as f:
	f.write("#NAME IPTV Streams\n")
	for index, line in enumerate(lines,1):
		if line.startswith("#EXTINF"):
			"get service description"
			desc= line.split(',')[-1]
		if line.startswith("http"):
			f.write("#SERVICE 4097:0:0:0:0:0:0:0:0:0:http%3a//"+line[7:].strip()+": "+desc)
			f.write("#DESCRIPTION  "+desc+"\n")