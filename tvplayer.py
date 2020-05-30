"""
TV PLAYER
displays TV playlist as buttons in tkinter gui which can be played by clicking on channel name.
needs ffmpeg with ffplay.exe or vlc players installed.
Playlist is a textfile in playlist format , save below example to a text file:
"""
file = """
#EXTM3U
#EXTINF:-1 CATV1
http://192.226.228.32:8080/hls/catv/index.m3u8
#EXTINF:-1 ALHURRA
http://mbnhls-lh.akamaihd.net/i/MBN_1@118619/master.m3u8
#EXTINF:-1 BBC Arabic
http://bbcwshdlive01-lh.akamaihd.net/i/atv_1@61433/master.m3u8
#EXTINF:-1 CGTN
http://live.cgtn.com/1000a/prog_index.m3u8
#EXTINF:-1 DW
http://dwstream2-lh.akamaihd.net/i/dwstream2_live@124400/master.m3u8
#EXTINF:-1 NRT ARABIC
http://prxy-wza-02.iptv-playoutcenter.de/nrtarabic/nrtarabic.stream_1/playlist.m3u8
#EXTINF:-1 RT ARABIC
http://secure-streams.akamaized.net/rt-arab/index1600.m3u8
#EXTINF:-1 RT ARABIC
http://secure-streams.akamaized.net/rt-arab/index.m3u8
#EXTINF:-1 TRT ARABIC
http://trtcanlitv-lh.akamaihd.net/i/TRTARAPCA_1@181945/master.m3u8
#EXTINF:-1 ALMANAR
http://live.mediaforall.net:1935/liveorigin/livestream_480p/playlist.m3u8
#EXTINF:-1 ALMAYDEN
http://lmd.cdn.octivid.com/lmd/smil:switch.smil/chunklist_b850000_t64NTc2cA==.m3u8?v=1599780920
#EXTINF:-1 ARABICA
https://svs.itworkscdn.net/arabicatvlive/arabicatv/playlist.m3u8
#EXTINF:-1 LBC
http://selevision9891-i.akamaihd.net/hls/live/219336/98919/1.m3u8
#EXTINF:-1 SAMA TV
http://sama-tv.net:1935/live/samatv/playlist.m3u8
#EXTINF:-1 taghier
http://stream1.joinvisions.net:1935/taglive/taghier/media_b340674_w2040724908.m3u8
#EXTINF:-1 JORDAN AMEN
http://185.27.116.54:1935/live/amn/chunklist_w1521888123.m3u8
#EXTINF:-1 Alghadeer
http://149.255.37.212:1935/live/alghadeer/chunklist_w1787991045.m3u8
#EXTINF:-1 alrashid
http://streamer11.elementssys.com:8080/alrashid/alrashid_850kbps/index.m3u8
#EXTINF:-1 SHARQIA NEWS
http://ns8.indexforce.com:1935/home/mystream/playlist.m3u8
#EXTINF:-1 Alsharqiyalive
http://ns8.indexforce.com:1935/alsharqiyalive/mystream/playlist.m3u8
#EXTINF:-1 MASDAR_TV
http://streamer12.elementssys.com:8080/SAUDI-Channels/MASDAR_TV/index.m3u8
"""

from tkinter import *
import os,sys
############################## GET TITLES AND STATIONS FROM FILE #################
"open playlist file and get title of channel and url of stations "
titles = []
stations = []
#file = sys.argv[1]
#text = open("playlist.txt", "r").read()
text = file
lines = text.split("\n")
for line in lines:
	if "EXTINF" in line:
		titles.append(line[11:])
	elif "http" in line:
		stations.append(line)
#==========================================================
"draw the gui window"
root= Tk()
root.geometry("1280x860")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
v = StringVar()
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+E+S+W)
#========================================================
##################### PLAY VIDEO FUNCTION #### -vf setdar=16:9 ##################
def play_video(station):
	os.system("c:/ffmpeg/bin/ffplay -fs  -vcodec  h264  -infbuf  -exitonmousedown -nostats -loglevel 0 {}".format(station))
	#os.system("vlc dummy  --dash-buffersize=2147483647 --fullscreen  {}".format(station))
#############################################################################
"draw buttons in the window with names of channels and play channel by clicking"
def btn(col,row,text, index):
	Radiobutton(frame,
														text = text,
														padx = 1,
														pady=  1,
														width = 25,
														bg="aqua",
														relief = "raised",
														font =("Tahoma", 10, "bold"),
														justify= "left",
														anchor="w",
														indicatoron=0,
														variable = v,
														value=index,
														command= lambda: play_video(stations[int(v.get())])).grid(row=row, column=col, sticky="n,e,s",padx=1, pady=1)
#================================================
"""split list into number of sublists then bton each sublist in sequence """
data = titles
n = 20 #number of rows
chunks = [data[x:x+n] for x in range(0, len(data), n)]
for i, chunk in enumerate(chunks):
	for index, value in enumerate(chunk):
		btn(i, index, chunk[index], data.index(chunk[index]))
############################################################################
"run gui"
root.mainloop()

