from tkinter import *
import tkinter.ttk as ttk


class Tree(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent=parent
		self.initialize_user_interface()
		
	def initialize_user_interface(self):
		self.parent.title("Accounts")
		self.parent.grid_rowconfigure(0, weight=1)
		self.parent.grid_columnconfigure(0, weight=1)
		self.parent.config(background="lavender")
		self.scrollbar = Scrollbar(self.parent, orient=VERTICAL)
		self.tree = ttk.Treeview(self.parent, columns=('No.', 'Acc. No.', 'Bank', 'type', 'Holder', 'Balance'))
		self.scrollbar.config(command=self.tree.yview)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.populate()
		self.insertRows()
		self.treeview = self.tree
		self.TotalLabel()
		self.tree["show"] = "headings"
		style = ttk.Style()
		style.theme_use("clam")
		style.configure(".", font=('Helvetica', 14), background= "black", foreground="blue")
		style.configure("Treeview", background= "yellow", foreground="blue")
		style.configure("Treeview.Heading", font=('Helvetica', 14), background= "green", foreground='white') 
		self.tree.pack(side=TOP, expand=FALSE)
		
	def Getdata(self):
		lines = open('acc.csv').readlines()
		self.headers = lines[0]
		return lines


	def ScrollBar(self):
		self.scrollbar = Scrollbar(self.parent, orient=VERTICAL)
		self.scrollbar.config(command=self.tree.yview)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.tree["show"] = "headings"
		style = ttk.Style()
		style.theme_use("clam")
		style.configure(".", font=('Helvetica', 14), background= "black", foreground="blue")
		style.configure("Treeview", background= "yellow", foreground="blue")
		style.configure("Treeview.Heading", font=('Helvetica', 14), background= "green", foreground='white') 
		self.tree.pack(side=TOP, expand=FALSE)


	def populate(self):
		#Column width  and headings (Acc,Bank,Type,Holder,Balance)
		self.tree.column("0", width=200, minwidth=200, stretch=NO)
		self.tree.column("1", width=200, minwidth=200, stretch=YES)
		self.tree.column("2", width=200, minwidth=200, stretch=YES)
		self.tree.column("3", width=200, minwidth=200, stretch=YES)
		self.tree.column("4", width=200, minwidth=200, stretch=YES)
		self.tree.column("5", width=200, minwidth=200, stretch=YES)

		self.tree.heading("0", text="No.",anchor=W)
		self.tree.heading("1", text="ACC",anchor=W)
		self.tree.heading("2", text="BANK",anchor=W)
		self.tree.heading("3", text="TYPE",anchor=W)
		self.tree.heading("4",text="HOLDER",anchor=W)
		self.tree.heading("5",text="BALANCE",anchor=W)

# Configure tags
	def treeTags(self):
		self.tree.tag_configure('oddrow', background='orange')
		self.tree.tag_configure('evenrow', background='purple')
		self.tree.tag_configure("red_fg", foreground="red")
		self.tree.tag_configure("blue_fg", foreground="blue")


	def insertRows(self):
		# insert data in rows 
		lines = self.Getdata()
		self.i = 0
		for i,row in enumerate(lines[1:], 1):
			self.tree.insert("", END, i , values= (str(self.i),)+tuple(row.split(",")))
			# Increment counter for row numbering
			self.i = self.i + 1


	def sumtotal(self):
		total = []
		lines = self.Getdata()
		for line in lines[1:]:
			total.append(float(line.split(",")[-1]))
		return total


	def TotalLabel(self):
		label = ttk.Label(self.parent, background="yellow", font=('Helvetica bold', 15), text= "Total Balance :         {:>145}".format(sum(self.sumtotal())))
		label.pack(side=BOTTOM, anchor='se', fill=X)
#=====================INITIALIZATION==============================
if __name__ == '__main__':
		"create root frame"
		root= Tk()
		"use class to create parent frame in the root frame"
		d = Tree(root)
		root.mainloop()