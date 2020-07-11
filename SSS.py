from tkinter import *
import os
import tkinter as tk
from tkinter import ttk

#https://www.youtube.com/watch?v=ji8pTynQhEo&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=25
#TKinter GUI
root = Tk()
root.title('Solo Session Stager (SSS)')
root.geometry("400x600")

'''
myLabel = Label(root, text = "Test Module")
myLabel.pack()

myTextbox = Entry(root, width = 30)
myTextbox.pack()
'''

def AddRule():
    win = tk.Toplevel()
    win.wm_title("Warning")
    win.geometry("400x200")

    l = tk.Label(win, text="Input")
    #l.grid(row=0, column=0)
    l.pack()
    b = ttk.Button(win, text="Yes", command=win.destroy)
    #b.grid(row=1, column=0)
    b.pack()


myButton = Button(root,text="Add Firewall Rule",command=AddRule)
myButton.pack()

root.mainloop()