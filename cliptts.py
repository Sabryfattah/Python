from Tkinter import Tk
import os
text = Tk().clipboard_get()
os.system('start /min C:/Say/SayDynamic.exe %r' % text)