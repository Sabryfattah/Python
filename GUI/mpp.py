from tkinter import *
import tkinter.ttk as ttk
import threading
import os
import subprocess
##########################################################
class VIRAD:
	def __init__(self, title=None, var =None):
		self.title = title
		self.var = var

	def get_stations(self):
		stations = open("stations.csv", 'r').readlines()
		self.list_stations = {}
		for station in stations:
			stn = station.strip().split(",")
			self.list_stations[stn[0]] =stn[1]

	def win(self):
		self.root = Tk()
		self.root.geometry("950x300")
		self.root.title("Internet Radio")
		self.parent= Frame(self.root, width=300, height=900)
		listbox = Listbox(self.parent, width=35, bd=5, relief='sunken', font=('tahoma', 14))
		self.get_stations()
		for k, v in sorted(self.list_stations.items(), reverse=True):
			listbox.insert(0, k)
		self.vsb = ttk.Scrollbar(orient="vertical", command=listbox.yview)
		listbox.grid(column=0, row=0)
		self.vsb.grid(column=1, row=0, sticky='ns', in_=self.parent)
		listbox.configure(yscrollcommand=self.vsb.set)
		self.var = StringVar()
		label = Label(self.parent, bg="yellow", font="Tahoma, 14", wraplength= 500, bd=4, padx=2, width=50, height=10, textvariable= self.var)
		label.grid(column=2, row=0)
		listbox.bind("<<ListboxSelect>>", self.play)
		btn = Button(self.parent, text="stop", command= self._stop).grid(column=0, row=4)
		self.parent.grid(column=0, row=0)
		thread = threading.Thread(target=self.play, args=(listbox,))
		thread.daemon = 1
		thread.start()
		self.root.mainloop()


	def play(self, event):
		w = event.widget
		index = int(w.curselection()[0])
		stn = w.get(index)
		url = self.list_stations[stn]
		self.proc = subprocess.Popen(["c:/mplayer/mplayer.exe", "-slave",  "-idle", "-softvol", url], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		while True:
			output = self.proc.stdout.readline()
			if self.proc.poll() is not None:
				break
			if output:
				if output.decode(encoding="iso8859-2").startswith('ICY') : 
					self.title = output.decode(encoding="UTF-8")
					self.var.set(self.title[23:-4])
			self.root.update_idletasks()


	def _stop(self):
		self.proc.stdin.write("('stop'.encode())")

###########################################################
VIRAD().win()

