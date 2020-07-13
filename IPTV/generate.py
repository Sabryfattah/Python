"""Generate url list from a single url if it contains sequential numbers
Some iptv url links are only different in a sequential number.
You may be able to get all links on server if you list all link sequences 
and then check working channels using probe.py script"""
with open("urls.txt", 'a') as f:
	"specify url of working base link and range of numbers"
	for n in range(1,100):
		url = "https://www.filmon.com/vr-streams/{}.high/playlist.m3u8".format(n)
		f.write("#EXTINF:-1 , "+str(n)+"\n")
		f.write(url+"\n")