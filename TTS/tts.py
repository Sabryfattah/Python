"""	
Text to Speech APP using pyttsx3:
Speak out text given on commandline or from a file or clipboard
Change voice, rate and volume
needs installed : pyttsx3, pyperclip
A window will open with clipboard content, click on button to hear it read aloud.
"""

import pyttsx3
import argparse
import pyperclip
from  tkinter import *
from multiprocessing import Process


class Voice:

	def __init__(self, engine=None, voice=None, rate=None):
		self.engine = engine
		self.voice = voice
		self.rate = rate
		self.parser = argparse.ArgumentParser(description = __doc__,
		formatter_class=argparse.RawDescriptionHelpFormatter,
		usage = "tts [options]"	)
		self.parser.add_argument("text", nargs="?", action = "store", help="text to say.")
		self.parser.add_argument("-t", "--tex", action = "store_true", help="speak out text.")
		self.parser.add_argument("-f", "--file", action = "store_true", help="Read a file aloud")
		self.parser.add_argument("-c", "--clip", action = "store_true", help="Read clipboard content aloud")
		self.parser.add_argument("-g", "--gui", action = "store_true", help="read from clip in gui")
		self.parser.add_argument("-v", action = "store", choices=[0,1,2], default = 0, help="Voice to use 0=Brian 1= Amy ")
		self.parser.add_argument("-r", "--rate", type= int, action = "store",default= 165, help="rate of voice speed 100-200")
		self.args = self.parser.parse_args()
		
	def Create_Engine(self):
		self.engine = pyttsx3.init()
	
	def say(self, text):
		self.Create_Engine()
		self.set_voice(0)
		self.set_rate(160)
		self.set_volume(1.0)
		self.engine.say(text)
		self.engine.runAndWait()

	def Stop(self):
		self.engine.Endloop()

	def get_clip_text(self):
		txt = pyperclip.paste()
		return txt

	def get_file_text(self):
		filename = input("Enter File Name :   ")
		t = open(filename, 'r')
		txt = t.read()
		return txt
		
	def get_voices(self):
		self.Create_Engine()
		voices = self.engine.getProperty('voices')       #getting details of current voices
		return voices

	def set_voice(self, n):
		voices = self.get_voices()
		self.engine.setProperty('voice', voices[n].id)   #changing index, changes voices. 1 for female

	def get_rate(self):
		rate = self.engine.getProperty('rate')   # getting details of current speaking rate
		print (rate)                        #printing current voice rate

	def set_rate(self, rate):
		self.engine.setProperty('rate', rate)     # setting up new voice rate
		
	def set_volume(self, vol):
		self.engine.setProperty('volume',vol)    # setting up volume level  between 0 and 1

	def gui(self):
		def say():
			self.say(txt)
		def stop():
			self.Stop()
		root = Tk()
		root.geometry("530x550")
		root.title("TTS CLIP")
		txt = root.clipboard_get()
		text_field = Text(root, height= 600, width= 500, bg="white", fg="black", font=("tahoma bold", 16),wrap=WORD)
		text_field.insert('end', txt)
		text_field.place(x=10, y=10, width=500, height=500)
		S = Scrollbar(root)
		S.config(command=text_field.yview)
		S.place(x=510, y=10, width=20, height=500)
		text_field.config(yscrollcommand=S.set)
		button = Button(root, text= "say", font=("tahoma bold", 14), relief="raised", bg="yellow", width=50, height=5, command=say)
		button.place(x=10, y=520, width=90, height=25)
		button = Button(root, text= "Stop", font=("tahoma bold", 14), relief="raised", bg="yellow", width=50, height=5, command= stop)
		button.place(x=140, y=520, width=90, height=25)
		root.mainloop()

if __name__ == "__main__":
	v = Voice()
	"read text entered at commandline"
	if v.args.tex:
		v.say(v.args.text)
	"Read text at the clipboard"
	if v.args.clip:
		v.say(v.get_clip_text())
	"Read file content"
	if v.args.file:
		v.say(v.get_file_text())
	"Read clipboard from gui window"
	if v.args.gui:
		p = Process(target=v.gui())
		p.start()
		p.join()