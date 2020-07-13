"""
1- Draw Buttons of video streaming channels from m3u file
2- User click on Button to play video channel.
"""
#########################################
from tkinter import *
import os,sys
import argparse
#########################################
class Playit():

	def __init__(self):
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="player <options> [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='m3u text file')
		#self.parser.add_argument('-s',"--scrap", action='store_true', help='scrap links from a url')
		#self.parser.add_argument('-a',"--arab", action='store_true', help='extract arabfilms and drama from Alarab site')
		#self.parser.add_argument('-ss',"--sseq", action='store_true', help='scrap a sequence of numbered pages')
		#self.parser.add_argument('-u',"--utub", action='store_true', help='scrap youtube watch links')
		self.args = self.parser.parse_args()
		self.file = self.args.file
		
	def read_file(self):
		text = open("{}.txt".format(self.file), "r").read()
		return text
	
	def get_channels(self):
		titles = []
		urls = []
		text = self.read_file()
		lines = text.split("\n")
		for line in lines:
			if "EXTINF" in line:
				titles.append(line[11:])
			elif "http" in line:
				urls.append(line)
		return (titles,urls)
	
	def play_video(self,url):
		"Use ffmpeg or vlc as video player, customize"
		os.system("c:/ffmpeg/bin/ffplay -fs  -infbuf  -exitonmousedown -nostats -loglevel 0 {}".format(url))
		#os.system("vlc --fullscreen  {}".format(url))

	def draw_btn(self, frame, col,row,text, index):
		urls = self.get_channels()[1]
		v = StringVar()
		Radiobutton(frame,
			text = text,
			padx = 1,
			pady=  1,
			width = 14,
			bg="aqua",
			relief = "raised",
			font =("Tahoma", 10, "bold"),
			justify= "left",
			anchor="w",
			indicatoron=0,
			variable = v,
			value=index,
			command= lambda: self.play_video(urls[int(v.get())])).grid(row=row, column=col, sticky="n,e,s",padx=1, pady=1)

	def draw_list(self):
		"split list into number of sublists"
		"draw button for each sublist in sequence"
		root= Tk()
		root.geometry("1280x860")
		Grid.rowconfigure(root, 0, weight=1)
		Grid.columnconfigure(root, 0, weight=1)
		frame=Frame(root)
		frame.grid(row=0, column=0, sticky=N+E+S+W)
		data = self.get_channels()[0]
		n = 20 #number of rows
		chunks = [data[x:x+n] for x in range(0, len(data), n)]
		for i, chunk in enumerate(chunks):
			for index, value in enumerate(chunk):
				self.draw_btn(frame, i, index, chunk[index], data.index(chunk[index]))
		root.mainloop()
############################################################################
if __name__ == "__main__":
	p = Playit()
	p.draw_list()
