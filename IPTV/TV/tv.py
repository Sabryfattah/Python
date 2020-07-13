import tkinter as tk
import os,sys

class TV:
	def __init__(self):
		titles = []
		stations = []
	
	def get_channes(self):
		text = open("c:/py/{}.txt".format(file), "r").read()
		lines = text.split("\n")
		for line in lines:
			if "EXTINF" in line:
				titles.append(line[11:])
			elif "http" in line:
				stations.append(line)
	def Gui(self):
		stations = [ "http://192.226.228.32:8080/hls/catv/index.m3u8","http://mbnhls-lh.akamaihd.net/i/MBN_1@118619/master.m3u8"]
		titles = ["Canadian TV","ALHURRA" ]
		root=tk.Tk()
		v = tk.StringVar()
		#v.set(1)
		tk.Label(root,
					text = "Select a Channel",
					justify = tk.LEFT).pack() 
		for val, title in enumerate(titles):
			tk.Radiobutton(root,
										text = title,
										padx = 20,
										width = 50,
										bg="aqua",
										relief = 'raised',
										font =("Helvetica bold", 36),
										justify = 'left',
										indicatoron=0,
										variable = v,
										value=val,
										command= lambda : self.play_video(stations[int(v.get())]),
										).pack()
										
		quit = tk.Button(root, text="QUIT", fg="red", command=root.destroy)
		quit.pack(side="bottom")
		root.mainloop()
	def play_video(self, station):
		os.system("c:/ffmpeg/bin/ffplay -fs -exitonmousedown -nostats -loglevel 0 {}".format(station))
#=========================================================
if __name__ == "__main__":
	tv = TV()
	tv.Gui()



