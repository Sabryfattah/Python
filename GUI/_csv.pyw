from tkinter import *
from tkinter import filedialog
from tkinter import ttk

class CSV_EDITOR:
	def __init__(self):
		self.root = Tk()
		self.root.geometry("1000x800")
		self.menuBar()
		self._build_tree()
		self._widgets()

	def menuBar(self):
		menubar = Menu(self.root, bg="lightgrey", fg="black")
		self.file_menu = Menu(menubar, tearoff=0, bg="lightgrey", fg="black")
		self.file_menu.add_command(label="Open", command=self.file_open, accelerator="Ctrl+O")
		menubar.add_cascade(label="File", menu=self.file_menu)
		self.root.config(menu=menubar)

	def file_open(self):
		self.file = filedialog.askopenfilename()
		self.lines = open(self.file, 'r').readlines()
		cols = self.lines[0].split(",")
		self.tree_columns = (cols)
		
	def _build_tree(self):
		self.file_open()
		self.tree = ttk.Treeview(self.root, columns=self.tree_columns, selectmode='extended', show="headings")
		self.vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.tree.grid(column=0, row=0, sticky='nsew', in_=self.root)
		self.vsb.grid(column=1, row=0, sticky='ns', in_=self.root)
		self.tree.bind("<<TreeviewSelect>>", self.get_selected)
		for col in self.tree_columns:
			self.tree.heading(col,anchor="w", text=col.title(),
				command=lambda _col=col: self.treeview_sort_column(self.tree, _col, True))
				#command=lambda c=col: sortby(self.tree, c, 0))
			self.tree.column(col,width=200,anchor="w",stretch="no")
		for line in self.lines[1:]:
			row = line.split(",")
			item = self.tree.insert("",'end',values=(row))
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("Vertical.TScrollbar", gripcount=20, background="LightBlue", darkcolor="DarkGreen", lightcolor="LightGreen", troughcolor="gray", bordercolor="blue", arrowcolor="white")
		self.tree.configure(yscrollcommand=self.vsb.set)

	def _widgets(self):
		"Build widgets for entry, add, delete and save to file in container"
		self.app = Frame(self.root, width=1000, height=200).grid(column=0, row=1, sticky="w")
		self.var = StringVar()
		entry = Entry(self.app, bg="yellow", textvariable = self.var, justify = "left") 
		entry.focus_force() 
		add_item = Button(self.app, bg="aqua", text="Add item",command=self.add_item)
		edit= Button(self.app, bg="aqua", text="Edit item",command=self.edit_item)
		save = Button(self.app, bg="aqua", text="Save to File",command=self.save)
		delrec = Button(self.app, bg="aqua", text="Delete Row",command=self.delete_record)
		select = Button(self.app, bg="aqua", text="Select Another",command=self.select_another)
		entry.grid(column=0, row=1, rowspan=1, padx=10, sticky='we', in_=self.app)
		add_item.grid(column=0, row=2, rowspan=1, sticky='we', in_=self.app)
		edit.grid(column=0, row=3, rowspan=1, sticky='we', in_=self.app)
		save.grid(column=0, row=4, rowspan=1, sticky='we', in_=self.app)
		delrec.grid(column=0, row=5, rowspan=1, sticky='we', in_=self.app)
		select.grid(column=0, row=6, rowspan=1, sticky='we', in_=self.app)
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_rowconfigure(0, weight=1)
			
	def get_selected(self,event):
		itemId = self.tree.focus()
		self.content = self.tree.item(itemId)["values"]
		self.content = [str(x).strip() for x in self.content]
		self.content = tuple(self.content)
		self.tree.clipboard_clear()
		self.tree.clipboard_append(self.content)
		
	def add_item(self):
		self.tree.insert("", "end", values=(self.var.get().split(",")))
		
	def edit_item(self):
		focused = self.tree.focus()
		self.tree.delete(focused)
		self.tree.insert("", str(focused[1:]), values=(self.var.get()))
		
	def save(self):
		table = self.getchildren()
		#open(self.file, 'w')
		with open("{}_2.csv".format(self.file[:-4]), "w") as f:
			f.write(",".join(self.tree_columns))
			for item in table:
				if [type(x) == int for x in item]:
					f.writelines(",".join(["{}".format(x) for x in item]))
					
	def select_another(self):
		self.tree.destroy()
		self._build_tree()
	
	def getchildren(self):
		table = []
		for child in self.tree.get_children():
			line = self.tree.item(child)["values"]
			table.append(line)
		return table

	def delete_record(self):
		selection=self.tree.selection()[0] 
		self.tree.delete(selection)
		
	def ttk_style(self):
		"style for ttk widgets"
		#style = ttk.Style()
		#style.theme_use("clam")
		#style.configure(".", rowheight=40, highlightthickness=3, bd=2, font=('Ariel', 16), fieldbackground="white", fieldforeground="aqua", background= "black", foreground="blue", height= 4, wodth=4, ipady=4, ipadx=4)
		#style.configure("Treeview.Cell", rowheight=40, background= "aqua", foreground="black")
		#style.configure("Treeview.Heading",  rowheight=40, font=('Helvetica', 18), background= "green", foreground='white') 
		#style.configure("Scrollbar", rowheight=40, lightcolor='yellow', gripcount= 10, darkcolor='black', width=40, activebackground='red')
		
	def treeview_sort_column(self, tv, col, reverse):
		"sort treeview by clicking on columns"
		l = [(tv.set(k, col), k) for k in tv.get_children('')]
		l.sort(reverse=reverse)
		# rearrange items in sorted positions
		for index, (val, k) in enumerate(l):
			tv.move(k, '', index)
		# reverse sort next time
		tv.heading(col, command=lambda _col=col: self.treeview_sort_column(tv, _col, not reverse))

#================================================================
cse = CSV_EDITOR()
cse.root.mainloop()