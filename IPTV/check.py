"""
Check IPTV link if it is working and add it to a m3u playlist file.
1- read link file as text file.
2- if line starts with #EXTINF: save to [titles]
3- if line starts with http save to [urls]
4- for each url in urls, play station and watch:
5- ask user if he wants to save it
6- if answer is yes , write station and title[num] to file
7- if not continue
"""
#########################################
from tkinter import *
import os,sys
import argparse
#########################################

class Checkurl():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description = __doc__,
        usage="check [file]")
        self.parser.add_argument('file',nargs="?", action='store', help='m3u text file')
        self.args = self.parser.parse_args()
        self.file = self.args.file
        self.titles = []
        self.urls = []
        
    def readm3u(self):
        "Open text file containing links and separate them to titles and urls"
        text = open(self.file+".txt", 'r', encoding="utf-8").read()
        for line in text.split("\n"):
            if line.startswith("#EXTINF"):
                self.titles.append(line)
            if line.startswith("http"):
                self.urls.append(line)
                
    def write(self, title, url):
       "add title and url to m3u file"
        with open(self.file+".m3u", 'a') as f:
            f.write(title+url+"\n")
     
    def play_channels(self):
        "play channel url and select urls to add to file"
        self.readm3u()
        for index, url in enumerate(self.urls):
            print(self.titles[index])
            print(url)
            os.system("c:/ffmpeg/bin/ffplay -fs -loglevel 0 {}".format(url))
            #os.system("vlc --fullscreen {}".format(url))
            title = input("Title to use ?...e.g. EXTINF:- 1, ? >  ")
            resp = input("Save Channel ? y/n : ")
            if resp == "y":
                self.write("#EXTINF:- 1, {} \n".format(title), url)
            else : continue
#================================================================
if __name__ == "__main__":
    p = Checkurl()
    p.play_channels()