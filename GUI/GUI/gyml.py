""" Search YAML file for a pattern and display list of matching keys.
select a key to display values.
Format:
Key 1 :
- value 1
- value 2
- value 3
Key2 : ...etc.
"""
import os
import re
import tkinter as tk
from tkinter import filedialog
from collections import defaultdict
import ntpath
import yaml
##########################################################
class GYML:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Search YAML File for a pattern in keys and display values")
		self.root.geometry('1400x550') 
		self.root.state('zoomed')
		#self.root.attributes('-zoomed', True)
		self.var = tk.StringVar()
		self.file = ""

	def get_doc(self):
		self.doc = {}
		self.file = filedialog.askopenfilename()
		self.title.configure(text= ntpath.basename(self.file[:-5]))
		with open('{}'.format(self.file), 'r', encoding='latin1') as f: #'iso-8859-1'
			self.doc = yaml.safe_load(f)

	def menubar(self):
		self.menubar = tk.Menu(self.root, bg="lightgrey", fg="black")
		self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
		self.file_menu.add_command(label="Open", command=self.get_doc, accelerator="Ctrl+O")
		self.menubar.add_cascade(label="File", menu=self.file_menu)
		self.root.config(menu=self.menubar)

	def widgets(self):
		self.label = tk.Label(self.root, text='Enter pattern to search', width= 40, font="tahoma, 18", relief='raised', bg= 'aqua')
		self.entry1 = tk.Entry(self.root, border=8, relief='sunken', bg= 'yellow', font="tahoma, 18", textvariable= self.var)
		self.title = tk.Label(self.root, text= self.file, width= 30, font="tahoma, 18", relief='raised', bg= 'yellow')
		self.lb1 = tk.Listbox(self.root, width=50, height= 28, font='tahoma,18', selectmode="single", borderwidth=5, highlightthickness=5)
		self.lb1.bind('<<ListboxSelect>>', self.run)
		self.textfield = tk.Text(self.root, wrap= 'word', width= 83, height=30, font='tahoma, 15', border=5, highlightthickness=5)
		self.button1 = tk.Button(self.root, text= "GO", border=5, relief="raised", font="tahoma, 12", command= self.display)
		#self.button2 = tk.Button(self.root, text= "SHOW", border=5, relief="raised", font="tahoma, 12", command= self.run)

	def display(self):
		self.lb1.delete(0, tk.END)
		pat = self.var.get()
		pat = pat.split(" ")
		self.keys = list(self.doc.keys())
		for key in self.keys:
			if re.search('.*'.join(pat), key, re.I):
			#if set(pat.split(" ")).issubset(set(key.split(" "))):
				self.lb1.insert('end', key)

	def run(self, event):
		w = event.widget
		index = int(w.curselection()[0])
		key = w.get(index)
		#content = self.doc[self.lb1.get(self.lb1.curselection())]
		self.textfield.delete(1.0,tk.END)
		for item in self.doc[key]:
			try:
				for k,v in item.items():
					self.textfield.insert(tk.END,"- "+str(k)+" : "+str(v)+"\n")
			except:
				self.textfield.insert(tk.END,"- "+item+"\n")
				
	def geometry(self):
		self.entry1.place(x=10, y=40)
		self.entry1.focus()
		self.label.place(x=10, y=10)
		self.title.place(x=580, y=10)
		self.lb1.place(x=10, y=80)
		self.button1.place(x=285, y=44)
		#self.button2.place(x=325, y=44)
		self.textfield.place(x=580, y=80)
	
	def main(self):
		self.menubar()
		self.widgets()
		self.geometry()
		self.root.mainloop()
#####################################################################
if __name__ == "__main__":
	g = GYML()
	g.main()