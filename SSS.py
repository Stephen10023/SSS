from tkinter import *
import os
import tkinter as tk
from tkinter import ttk

import ctypes, sys

#First, check if the program is an elevated admin. If not, envoke the User Account Control (UAC) to allow elevation, alongside rerunning the program.
#https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#TKinter GUI
#https://www.youtube.com/watch?v=ji8pTynQhEo&list=PLCC34OHNcOtrZTjsC5qtn_X9eRAmGmGOI&index=25
if is_admin():
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

    def EnableRules():
        os.system('netsh advfirewall firewall set rule name="Solo Session GTAV (Outbound)" new enable=yes')
        os.system('netsh advfirewall firewall set rule name="Solo Session GTAV (Inbound)" new enable=yes')

    def DisableRules():
        os.system('netsh advfirewall firewall set rule name="Solo Session GTAV (Outbound)" new enable=no')
        os.system('netsh advfirewall firewall set rule name="Solo Session GTAV (Inbound)" new enable=no')

    myButton = Button(root,text="Add Firewall Rule", command=AddRule)
    myButton.pack(fill=X,pady=8)

    myButton2 = Button(root, text="Enable Rule", bg="green", fg="white", command=EnableRules)
    myButton2.pack(fill=X, pady=8)

    myButton3 = Button(root, text="Disable Rule", bg="red", fg="white", command=DisableRules)
    myButton3.pack(fill=X, pady=8)

    root.mainloop()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)