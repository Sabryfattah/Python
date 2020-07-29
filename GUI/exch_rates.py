import requests
import tkinter as tk
# Where USD is the base currency you want to use
url = 'https://api.exchangerate-api.com/v4/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
eg = data['rates']['EGP']
uk = data['rates']['GBP']
root = tk.Tk()
root.title("Exchange Rates")
root.geometry("780x160")
lbl = tk.Label(root, text= "Exchange Rates for Dollar and British Pounds in Egyptian Pounds", width= 59, bg="yellow", border=5, relief="raised", font=("tahoma, 16"))
labl2 = tk.Label(root, text= "Egyptian Pounds per Dollar", width=35, bg="aqua", border=5, relief="raised", font=("tahoma, 16"))
labl3 = tk.Label(root, text= "British Pounds per Dollar", width=35, bg="aqua", border=5, relief="raised", font=("tahoma, 16"))
labl4 = tk.Label(root, text= "Egyptian Pounds per Pound Sterling", width=35, bg="aqua", border=5, relief="raised", font=("tahoma, 16"))
labl5 = tk.Label(root, text= eg, bg="pink",width=25, border=5, relief="raised", font=("tahoma, 16"))
labl6 = tk.Label(root, text= uk, bg="pink", width= 25, border=5, relief="raised", font=("tahoma, 16"))
labl7 = tk.Label(root, text= 1/uk*eg, bg="pink", width=25, border=5, relief="raised", font=("tahoma, 16"))
print("Dollar = {} Egyptian pounds and {} Sterling Pounds ".format(eg,uk))
print("Sterling = {} Egyptian Pounds".format((1/uk)*eg))
lbl.place(x=0, y=0)
labl2.place(x=0, y = 30)
labl3.place(x=0, y = 60)
labl4.place(x=0, y = 90)
labl5.place(x=400, y = 30)
labl6.place(x=400, y = 60)
labl7.place(x=400, y = 90)
root.mainloop()