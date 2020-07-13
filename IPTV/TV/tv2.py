import tkinter as tk
from tkinter import *
import os,sys
############################## GET TITLES AND STATIONS FROM FILE #################
titles = []
stations = []
text = open("n1.txt", "r").read()
lines = text.split("\n")
for line in lines:
	if "EXTINF" in line:
		titles.append(line[11:])
	elif "http" in line:
		stations.append(line)
##################### PLAY VIDEO FUNCTION #####################################
def play_video(station):
		#os.system("c:/ffmpeg/bin/play -fs -exitonmousedown -nostats -loglevel 0 {}".format(station))
		os.system("c:/ffmpeg/bin/ffplay -fs  -vcodec  h264  -x  1920 -y  1080  -infbuf  -exitonmousedown -nostats -loglevel 0 {}".format(station))

############# BUILD FRAME FOR RADIOBUTTONS ####################################
root=tk.Tk()
root.geometry("1280x860")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
v = tk.StringVar()
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+E+S+W)
############# CREATE RADIOBUTTONS FUNCTION ###################################
def create(start,end,colnumber):
	for col_index in range(1):
		for row_index in range(start,end,1):
			tk.Radiobutton(frame,
													text = titles[row_index+col_index],
													padx = 1,
													pady=  1,
													width = 15,
													bg="aqua",
													relief = "raised",
													font =("Tahoma", 10, "bold"),
													justify= "left",
													anchor="w",
													indicatoron=0,
													variable = v,
													value=row_index+col_index,
													command= lambda : play_video(stations[int(v.get())]),
													).grid(row=row_index-start, column=col_index+colnumber, sticky="n,e,s",padx=1, pady=1)
##################### CREATE RADIO BUTTONS ########################################
#length of each column L
l = 20
#no. of items in whole list
n = len(titles) #90
#remaining items if n divided by length of column
r = n%l  #10
#how many columns without the remaining column
c = n//l #4
#get list of values between each range of four with max length without remaining
ns = list(range(0,n,l)) #0 to 80 ranges, ns[-1] = 80
#start loop to create columns
x = 0
for x in range(c): #3
	#create column with items from list starting with first then next range
	create(ns[x],ns[x+1],x) #0,20,0|20,40,1|40,60,2|60,80,4
#now create last column from last ns and size of titles at col r+1
create(n-r,n,c+1)
#print(l,n,r,c,ns)
################### MAIN LOOP ##########################################
root.mainloop()
