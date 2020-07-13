"""
IPTV PLAYLIST PLAYER
using a text file containing channels in m3u format. This script display channels as labels.
Click on a label to play channel, ESC to stop playing, back to channel list.
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
			usage="player [file]")
		self.parser.add_argument('file',nargs="?", action='store', help='m3u text file')
		self.args = self.parser.parse_args()
		self.file = self.args.file
		
	def read_file(self):
		text = open("{}.txt".format(self.file), "r", encoding="utf-8").read()
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
		os.system("c:/ffmpeg/bin/ffplay -fs -vcodec  h264  -infbuf  -exitonmousedown -nostats -loglevel 0 {}".format(url)) #
		#os.system("vlc dummy  --dash-buffersize=2147483647 --fullscreen  {}".format(url))

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
###############################################################
if __name__ == "__main__":
	p = Playit()
	#p.draw_list(
	p.read_file()
