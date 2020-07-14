import os
from PIL import Image
from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
import vlc


class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.configure(background="#100E13")
		self.title("Simple Internet Radio Player")
		self.geometry("500x300+300+300")
		self.i = 0
		self.create_name_list()
		self.label_text = StringVar()  
		self.label_text.set(self.names[self.i]) 
		label = Label(self, textvariable=self.label_text, borderwidth=0, relief=SOLID, pady = 5, padx=10, foreground="#71D8F7", background="#18191E", width=32, height=2, font=("Arial",20), anchor="nw")
		label.pack(pady=15, padx=10)
		self.imgnext = ImageTk.PhotoImage(file="nextbutton.png")
		self.imgprev = ImageTk.PhotoImage(file="prevbutton.png")
		nextButton = Button(self, image=self.imgnext, width=145, height=145, borderwidth=0, highlightbackground="#100E13")
		nextButton.bind("<Button-1>",self.next_ch)
		nextButton.pack(side=RIGHT, padx=15, pady=10)
		prevButton = Button(self, image=self.imgprev, width=145, height=145, borderwidth=0, highlightbackground="#100E13")   
		prevButton.bind("<Button-1>",self.prev_ch)
		prevButton.pack(side=LEFT, padx=15, pady=10)
		self.protocol("WM_DELETE_WINDOW", self.on_exit)
		print(self.radio[self.names[self.i]])       # Test
		self.play(self.radio[self.names[self.i]])   # First playback at program startup
	## End of _init_

	# Creations of list with web radio names and addresses
	def create_name_list(self):
			self.i=0
			self.radio = {}
			# Let's open text file with web radio list
			radiolist = "radiolist.txt"
			# Let' s read text file line by line
			lines = open(radiolist, "r").readlines()
			for line in lines:
				line_ok = line.strip()
				splittedrecord = line_ok.split(",")
				self.radio[splittedrecord[0]] = splittedrecord[1]
			self.names = [] 
			for name in self.radio.keys(): # enumerate return tuple 
				self.names.append(name)      
				
	# Handler for player's buttons
	def next_ch(self, event):
		self.i += 1
		if self.i == len(self.names):
			self.i = 0
		self.label_text.set(self.names[self.i])
		self.player.stop()
		self.play(self.radio[self.names[self.i]])
	def prev_ch(self, event):
		self.i -= 1
		if self.i < 0:
			self.i = len(self.names)-1
		self.label_text.set(self.names[self.i]) 
		self.player.stop()
		self.play(self.radio[self.names[self.i]])

	# Playback the selectded radio
	def play(self,url):
		self.player = vlc.MediaPlayer(url, "-I")
		self.player.play()
	# When you click to exit, this function is called 
	def on_exit(self):
		self.destroy()
#=============================================================
if __name__ == '__main__':
	App().mainloop()



