import tkinter as tk
from tkinter import Label, ttk
from tkinter.messagebox import showinfo
import time
import os
import platform
import subprocess
from tkinter import *
from tkinter import messagebox

def close():
       italia.destroy()

italia = tk.Tk()
italia.geometry("300x150")
italia.configure(bg="#202125")
italia.resizable(0, 0)
italia.iconbitmap("Textures\icon.ico")
italia.title("Loading Drivers")

def bar():
    try:
        if '32bit' in platform.architecture():
            process = '%systemroot%\Sysnative\pnputil.exe -e'
        else:
            process = 'pnputil.exe -e'

        p = subprocess.Popen(process, shell=True,
        stdout=subprocess.PIPE, universal_newlines=True)
        italia.configure(bg="#202125")
        progress['value'] = 20
        italia.update_idletasks() 
        time.sleep(1) 
  
        progress['value'] = 40
        italia.update_idletasks() 
        time.sleep(1) 
  
        progress['value'] = 50
        italia.update_idletasks() 
        time.sleep(1) 
  
        progress['value'] = 60
        italia.update_idletasks() 
        time.sleep(1) 
  
        progress['value'] = 80
        italia.update_idletasks() 
        time.sleep(1) 
        progress['value'] = 100
        close()
    except:
        msg = messagebox.showerror('ERROR', 'Connection not found!!')
        close()
        
        
        
    
Label(italia, text = "",bg="#202125", foreground="white").pack()
Label(italia, text="Loading Drivers", font='san-serif 14 bold' ,bg="#202125", foreground="white").pack()
Label(italia, text = "",bg="#202125", foreground="white").pack()
progress = ttk.Progressbar(italia, orient = HORIZONTAL, length = 150, mode = 'determinate')
progress.pack()
Label(italia, text = "",bg="#202125", foreground="white").pack()
bar()