from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os


class CSVV:
	def __init__(self):
		self.root = Tk()
		self.root.geometry("1500x800")

	def menuBar(self):
		menubar = Menu(self.root, bg="lightgrey", fg="black")
		self.file_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
		self.file_menu.add_command(label="Open", command=self.file_open, accelerator="Ctrl+O")
		menubar.add_cascade(label="File", menu=self.file_menu)
		self.root.config(menu=menubar)

	def del_tree(self):
		self.tree.destroy()
		self.main()
	
	def file_open(self):
		self.file = filedialog.askopenfilename()
		try:
			self.lines = open(self.file, 'r').readlines()
			cols = self.lines[0].split(",")
			self.tree_columns = (cols)
		except: messagebox.showinfo("No File", "No Such file or directory")
		self.root.title(self.file)
	
	def _build_tree(self):
		self.file_open()
		self.tree = ttk.Treeview(self.root, columns=self.tree_columns, selectmode='extended', show="headings")
		self.vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.tree.grid(column=0, row=0, sticky='nsew', in_=self.root)
		self.vsb.grid(column=1, row=0, sticky='ns', in_=self.root)
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("Vertical.TScrollbar", gripcount=20, background="LightBlue", darkcolor="DarkGreen", lightcolor="LightGreen", troughcolor="gray", bordercolor="blue", arrowcolor="white")
		style.configure(".", rowheight=40, highlightthickness=3, bd=2, font=('Ariel', 16), fieldbackground="white", fieldforeground="aqua", background= "LightGreen", foreground="blue", height= 4, width=4, ipady=4, ipadx=4)
		style.configure("Treeview.Heading", font=('Helvetica', 16)) 
		self.tree.configure(yscrollcommand=self.vsb.set)
		self.tree.tag_configure('gray', background='#cccccc')
		self.tree.tag_configure('yellow', background='#cf0000')
		for col in self.tree_columns:
			self.tree.heading(col,anchor="w", text=col.title(),
				command=lambda _col=col: self.treeview_sort_column(self.tree, _col, True))
				#command=lambda c=col: sortby(self.tree, c, 0))
			self.tree.column(col,width=200,anchor="w",stretch="no")
		for i, line in enumerate(self.lines[1:], 1):
			row = line.split(",")
			if i % 2 == 0:
				item = self.tree.insert("",'end',values=(row), tag =("grey"))
			else:
				item = self.tree.insert("",'end',values=(row), tag =('yellow', ))


	def _widgets(self):
		"Build widgets in container"
		self.app = Frame(self.root, width=1000, height=200).grid(column=0, row=1, sticky="w")
		self.button = Button(self.app, bg="aqua", text="New File",command=self.del_tree)
		self.button.grid(column=0, row=3, rowspan=1, sticky='we', in_=self.app)
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_rowconfigure(0, weight=1)
	
	def main(self):
		self.menuBar()
		self._build_tree()
		self._widgets()
		self.root.mainloop()
#================================================================
cv = CSVV()
cv.main()
