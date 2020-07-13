import tkinter as tk
from tkinter import *
import os,sys
titles = []
stations = []
text = open("c:/py/tv/ar3.txt", "r").read()
lines = text.split("\n")
for line in lines:
	if "EXTINF" in line:
		titles.append(line[11:])
	elif "http" in line:
		stations.append(line)

def play_video(station):
		os.system("vlc dummy  --dash-buffersize=2147483647 --fullscreen  {}".format(station))

root=tk.Tk()
root.geometry("1280x860")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
v = tk.StringVar()
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

for col_index in range(1):
	for row_index in range(0,20,1):
		tk.Radiobutton(frame,
										text = titles[row_index+col_index],
										padx = 20,
										width = 10,
										bg="aqua",
										relief = "raised",
										font =("Helvetica", 12, "bold"),
										justify = "left",
										indicatoron=0,
										variable = v,
										value=row_index+col_index,
										command= lambda : play_video(stations[int(v.get())]),
										).grid(row=row_index, column=col_index, sticky="N,S,E,W")
for col_index in range(1):
	for row_index in range(20,40,1):
		tk.Radiobutton(frame,
										text = titles[row_index+col_index],
										padx = 20,
										width = 10,
										bg="aqua",
										relief = "raised",
										font =("Helvetica", 12, "bold"),
										justify = "left",
										indicatoron=0,
										variable = v,
										value=row_index+col_index,
										command= lambda : play_video(stations[int(v.get())]),
										).grid(row=row_index-20, column=col_index+1, sticky="N,S,E,W")
for col_index in range(1):
	for row_index in range(40,60,1):
		tk.Radiobutton(frame,
										text = titles[row_index+col_index],
										padx = 20,
										width = 18,
										bg="aqua",
										relief = "raised",
										font =("Helvetica", 12, "bold"),
										justify = "left",
										indicatoron=0,
										variable = v,
										value=row_index+col_index,
										command= lambda : play_video(stations[int(v.get())]),
										).grid(row=row_index-40, column=col_index+2, sticky="N,S,E,W")
for col_index in range(1):
	for row_index in range(60,80,1):
		tk.Radiobutton(frame,
										text = titles[row_index+col_index],
										padx = 20,
										width = 10,
										bg="aqua",
										relief = "raised",
										font =("Helvetica", 12, "bold"),
										justify = "left",
										indicatoron=0,
										variable = v,
										value=row_index+col_index,
										command= lambda : play_video(stations[int(v.get())]),
										).grid(row=row_index-60, column=col_index+3, sticky="N,S,E,W")
for col_index in range(1):
	for row_index in range(80,100,1):
		tk.Radiobutton(frame,
										text = titles[row_index+col_index],
										padx = 20,
										width = 10,
										bg="aqua",
										relief = "raised",
										font =("Helvetica", 12, "bold"),
										justify = "left",
										indicatoron=0,
										variable = v,
										value=row_index+col_index,
										command= lambda : play_video(stations[int(v.get())]),
										).grid(row=row_index-80, column=col_index+4, sticky="W")
for col_index in range(1):
	for row_index in range(100,120,1):
		tk.Radiobutton(frame,
										text = titles[row_index+col_index],
										padx = 20,
										width = 10,
										bg="aqua",
										relief = "raised",
										font =("Helvetica", 12, "bold"),
										justify = "left",
										indicatoron=0,
										variable = v,
										value=row_index+col_index,
										command= lambda : play_video(stations[int(v.get())]),
										).grid(row=row_index-100, column=col_index+5, sticky="N,S,E,W")
for col_index in range(1):
	for row_index in range(120,140,1):
		tk.Radiobutton(frame,
										text = titles[row_index+col_index],
										padx = 20,
										width = 10,
										bg="aqua",
										relief = "raised",
										font =("Helvetica", 12, "bold"),
										justify = "left",
										indicatoron=0,
										variable = v,
										value=row_index+col_index,
										command= lambda : play_video(stations[int(v.get())]),
										).grid(row=row_index-120, column=col_index+6, sticky="N,S,E,W")
root.mainloop()

