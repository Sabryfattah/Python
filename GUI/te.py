"""open text file and display it in a window with scrollbar"""
from tkinter import *
from tkinter import filedialog
import sys

class TextEditor:
	def __init__(self, parent=None, text=None, file=None):
		self.parent = parent
		self.file = "te.txt"
		self.text = text
	
	def ParentFrame(self):
		self.parent = Tk()
		self.parent.geometry("1500x800")
		self.parent.title("TextEditor")
		
	def textFrame(self):
		self.form = Text(self.parent, height=40, width=100, wrap= 'word', bg = "black", fg = "white", font = ("Arial Bold",20))
		self.form.place(x=10, y=10, width=1480, height=780)
		self.form.insert(END, self.text)
		self.scrollbar(self.form)
		
	def scrollbar(self, widget):
		"Add scrollbar to parent Window"
		S = Scrollbar(self.parent)
		S.config(command=widget.yview)
		widget.config(yscrollcommand=S.set)
		S.place(x=1470, y= 10 , width=20, height=780)
		
	def get_text(self):
		self.text = open(self.file, 'r').read()

	def file_open(self, event=None):
		self.form.delete('1.0', "end-1c")
		self.file = filedialog.askopenfilename()
		self.get_text()
		self.form.insert(END, self.text)
		
	def file_save(self):
		pass

	def menuBar(self):
		menubar = Menu(self.parent, bg="lightgrey", fg="black")
		self.file_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
		self.file_menu.add_command(label="Open", command=self.file_open, accelerator="Ctrl+O")
		self.file_menu.add_command(label="Save", command=self.file_save, accelerator="Ctrl+S")
		menubar.add_cascade(label="File", menu=self.file_menu)
		self.parent.config(menu=menubar)

	def main(self):
		self.ParentFrame()
		self.get_text()
		self.textFrame()
		self.menuBar()
		self.parent.mainloop()
#============================================================
if __name__ == "__main__":
	TextEditor().main()
