"""This script uses tkinter to build a GUI with entry field to search for a pattern in second column from two columns csv file. 
Thus a dictionary can be searched by description column rather than Name column."""

import csv
import tkinter as tk


root = tk.Tk()
root.title("Search for script")
root.geometry('900x350')
var = tk.StringVar()
def display_lists():
	pat = var.get()
	lb1.delete(0, tk.END)
	lb2.delete(0, tk.END)
	csvfile = open('all.csv', newline='')
	reader = csv.DictReader(csvfile)
	for row in reader:
		if pat in row['DESC']: 
			lb1.insert('end', row['NAME'])
			lb2.insert('end',row['DESC'])

label = tk.Label(root, text='Enter pattern to search', width= 40, font="tahoma, 18", relief='raised', bg= 'aqua')
entry1 = tk.Entry(root, border=8, relief='sunken', bg= 'yellow', font="tahoma, 18", textvariable=var)
lb1 = tk.Listbox(root, width=70, font='tahoma,20')
lb2 = tk.Listbox(root, width=70, font='tahoma,20')
button = tk.Button(root, text= "OK", border=5, relief="raised", font="tahoma, 12", command= display_lists)
label.place(x=10, y=10)
entry1.place(x=10, y=40)
lb1.place(x=10, y=80)
lb2.place(x=80,y=80)
button.place(x=285, y=44)
root.mainloop()
