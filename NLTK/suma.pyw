"""Summarize a file using nltk and Sumy modules and display output in a text field with ratio 1:5 length of original text"""
from tkinter import *
from tkinter import filedialog
import sys, os
import math
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import word_tokenize
from sumy.summarizers.kl import KLSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 

class Summarize:
	def __init__(self, parent=None, text=None, file=None):
		self.parent = parent
		self.file = r"C:\Users\sf300\OneDrive\Desktop\PY\WIN\OK\te.txt"

	def ParentFrame(self):
		self.parent = Tk()
		self.parent.geometry("1500x800")
		self.parent.title("TextEditor")
		self.form = Text(self.parent, height=30, width=70, wrap= 'word', bg = "black", fg = "white", font = ("Arial Bold",20))
		self.form.place(x=10, y=10, width=1200, height=600)
		"Add scrollbar to parent Window"
		S = Scrollbar(self.parent)
		S.config(command=self.form.yview)
		self.form.config(yscrollcommand=S.set)
		S.place(x=1250, y= 10 , width=20, height=650)
		menubar = Menu(self.parent, bg="lightgrey", fg="black")
		self.file_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
		self.file_menu.add_command(label="Open", command=self.sumarize_text, accelerator="Ctrl+O")
		menubar.add_cascade(label="File", menu=self.file_menu)
		self.parent.config(menu=menubar)
		
	def ratio(self, file):
		text = open(file, 'r').read()
		working_sentences = sent_tokenize(text)
		sentences_number = len(working_sentences)
		return sentences_number
		
	def summarize(self):
		n = self.ratio(self.file)/5
		self.parser = PlaintextParser.from_file(self.file, Tokenizer("english"))
		summarizer = KLSummarizer()
		summary = summarizer(self.parser.document, n) 
		return summary

	def sumarize_text(self):
		self.file = filedialog.askopenfilename()
		text = self.summarize()
		self.form.delete('1.0', "end-1c")
		for item in text:
			self.form.insert(END, str(item)+"\n\n")

	def main(self):
		self.ParentFrame()
		self.sumarize_text()
		self.parent.mainloop()
#######################################################
if __name__ == "__main__":
	Summarize().main()