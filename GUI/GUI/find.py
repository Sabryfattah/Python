import os
import re
import tkinter as tk
from collections import defaultdict
import ntpath
##########################################################
class Find:
	def __init__(self, pat=None, dirc=None, var=None):
		self.pat = pat
		self.dirc = "F:/Pass"
		#self.dirc = "D:\Personal\Confidential"
		self.files = []
		self.var = var

	def gui(self):
		self.root = tk.Tk()
		self.root.title("Search for File and open it by default App")
		self.root.geometry('900x350')
		self.var = tk.StringVar()
		pat = self.var.get()
		self.label = tk.Label(self.root, text='Enter pattern to search', width= 40, font="tahoma, 18", relief='raised', bg= 'aqua')
		self.entry1 = tk.Entry(self.root, border=8, relief='sunken', bg= 'yellow', font="tahoma, 18", textvariable= self.var)
		def display():
			self.lb1.delete(0, tk.END)
			self.files = []
			pat = self.var.get()
			for root, _, files in os.walk(self.dirc):
				for file in files:
					if re.search('.*'+pat+'.*$', file, re.I):
						self.files.append(root+"/"+file)
			fill_listbox()
		def fill_listbox():
			for file in self.files:
				self.lb1.insert('end', ntpath.basename(file[:-4]))
		def run():
			sel = self.lb1.curselection()
			os.startfile(self.files[int(sel[0])])
		self.lb1 = tk.Listbox(self.root, width=70, height= 10, font='tahoma,20', selectmode="single", borderwidth=5, highlightthickness=5)
		self.button1 = tk.Button(self.root, text= "OK", border=5, relief="raised", font="tahoma, 12", command= display)
		self.button2 = tk.Button(self.root, text= "RUN", border=5, relief="raised", font="tahoma, 12", command= run)
		self.entry1.place(x=10, y=40)
		self.lb1.place(x=10, y=80)
		self.button1.place(x=285, y=44)
		self.button2.place(x=325, y=44)
		self.root.mainloop()
######################################################
if __name__ == '__main__':
	f = Find()
	f.gui()

