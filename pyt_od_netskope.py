/* **********************************************************************
 * Copyright 2012 VMware, Inc.  All rights reserved. VMware Confidential
 * **********************************************************************/



#!/usr/bin/python

import tkinter
from tkinter.messagebox import *

window1 = tkinter.Tk()
window1.geometry("1220x950")
window1.resizable(False,False)
window1.title("Test App")
window1.iconbitmap("/Users/shashis/Downloads/Vargas21-Aquave-Metal-Photos.ico")

def win_close():
	window1.destroy()

def win_reset():
	entry1.delete(0,tkinter.END)
	entry2.delete(0,tkinter.END
)
def check_auth():
	if entry1.get() == 'john' and entry2.get() == 'abc':
		print ("Login Successful")
		showinfo(title="Info", message="Login Successful")
	else:
		print("Login Failed")
		showerror(title="Error", message="Login Failed: retry")

label1=tkinter.Label(window1,text="User").grid(row=0,column=0)
label1=tkinter.Label(window1,text="Pwd").grid(row=1,column=0)


entry1=tkinter.Entry(window1,width=10)
entry1.grid(row=0,column=1)
entry2=tkinter.Entry(window1,width=10,show='*')
entry2.grid(row=1,column=1)

button1=tkinter.Button(window1,text="Login",command=check_auth).grid(row=2,column=0)
button2=tkinter.Button(window1,text="Reset",command=win_reset).grid(row=2,column=1)
button3=tkinter.Button(window1,text="Close",command=win_close).grid(row=2,column=2)



window1.mainloop()

