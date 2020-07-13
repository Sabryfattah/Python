import tkinter as tk
import os,sys
titles = []
stations = []
file = sys.argv[1]
text = open("c:/py/{}.txt".format(file), "r").read()
lines = text.split("\n")
for line in lines:
	if "EXTINF" in line:
		titles.append(line[11:])
	elif "http" in line:
		stations.append(line)

#stations = [ "http://192.226.228.32:8080/hls/catv/index.m3u8","http://mbnhls-lh.akamaihd.net/i/MBN_1@118619/master.m3u8"]
#titles = ["Canadian TV","ALHURRA" ]
def play_video(station):
		os.system("c:/ffmpeg/bin/play -fs -exitonmousedown -nostats -loglevel 0 {}".format(station))

root=tk.Tk()
v = tk.StringVar()
#v.set(1)
def go(title):
	print(title)

tk.Label(root,
				text = "Select a Channel",
				justify = tk.LEFT).pack()
for val, title in enumerate(titles):
	tk.Radiobutton(root,
								text = title,
								padx = 20,
								bg="aqua",
								indicatoron=0,
								variable = v,
								value=val,
								command= lambda : play_video(stations[int(v.get())]),
								).pack()
								


#quit = Button(frame, text="QUIT", fg="red", command=root.destroy)
#quit.pack(side="bottom")
root.mainloop()

