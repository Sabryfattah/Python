import csv
import tkinter as tk


root = tk.Tk()
root.title("Search for  Password")
root.geometry('900x350')
var = tk.StringVar()
def display_lists():
	pat = var.get()
	lb1.delete(0, tk.END)
	lb2.delete(0, tk.END)
	lb3.delete(0, tk.END)
	csvfile = open('pw.csv', newline='')
	reader = csv.DictReader(csvfile)
	for row in reader:
		if pat.lower() in row['Service'].lower(): 
			lb1.insert('end', row['Service'])
			lb2.insert('end',row['Username'])
			lb3.insert('end',row['Password'])

label = tk.Label(root, text='Enter service name to get login details', width= 40, font="tahoma, 18", relief='raised', bg= 'aqua')
entry1 = tk.Entry(root, border=8, relief='sunken', bg= 'yellow', font="tahoma, 18", textvariable=var)
lb1 = tk.Listbox(root, border= 5, width=300, font='tahoma,20')
lb2 = tk.Listbox(root, border= 5,  width=300, font='tahoma,20')
lb3 = tk.Listbox(root, border= 5,  width=300, font='tahoma,20')
button = tk.Button(root, text= "OK", border=5, relief="raised", font="tahoma, 12", command= display_lists)
label.place(x=10, y=10)
entry1.place(x=10, y=40)
lb1.place(x=10, y=80, bordermode='outside' )
lb2.place(x=300,y=80)
lb3.place(x=600,y=80)
button.place(x=285, y=44)
root.mainloop()