"""
1- check a list of m3u8 links if they are active.
2- Save only active urls to OK file.
3- ffprobe app in ffmpeg open each link and return data frame rate.
4- Links which are not working will be skipped.
5- Only working links will be saved to the OK file.
6- Script may stop at link which does not return a response: 
	press CTRL_C to exit
	then remove all links upto this invalid url in m3u file. 
7- The original file should contain #EXTM3U at the first line.
"""
####################################################
import os, sys
import time
import re
import argparse
###################################################
class ProbeUrl():

	def __init__(self):
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="probe [infile] [outfile]")
		self.parser.add_argument('infile',nargs="?", action='store', help='m3u text file')
		self.parser.add_argument('outfile',nargs="?", action='store', help='m3u text file')
		self.args = self.parser.parse_args()
		self.infile = self.args.infile
		self.outfile = self.args.outfile

	def get_sections(self):
		"Divide text to sections of title and url"
		sections = open("{}.txt".format(self.infile), 'r', encoding="iso-8859-1").read().split("#")
		return sections

	def split_sections(self):
		"split each section and "
		"add first part to title and second to station lists"
		sections = self.get_sections()
		titles = []
		stations = []
		for s in sections:
			lines = s.split("\n")
			for line in lines:
				if "EXTINF" in line:
					titles.append(line)
				elif "http" in line:
					stations.append(line)
		return (titles,stations)

	def probe(self):
		"probe each station and if response is OK "
		"write title and station to file"
		(titles, stations) = self.split_sections()
		for index, s in enumerate(stations):
			out = os.system("c:/ffmpeg/bin/ffprobe -v error {}".format(s))
			if out == 0 : 
				print(titles[index])
				f = open("{}.txt".format(self.outfile), 'a', encoding="iso-8859-1")
				f.write(titles[index])
				f.write("\n")
				f.write(s)
				f.write("\n")
######################################################
if __name__ == "__main__":
	p = ProbeUrl()
	p.probe()