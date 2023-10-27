import tkinter as Tk
from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser
import time
from tkinter import messagebox
from tkinter.messagebox import showinfo
import os
import requests

def about():
    def github():
       webbrowser.open('https://vectras.netlify.app')
    m5 = Tk()
    m5.geometry("400x200")
    m5.configure(bg="#202125")
    m5.resizable(0, 0)
    m5.iconbitmap("Textures\icon.ico")
    m5.title("About")
    
    Label(m5, text = "",bg="#202125", foreground="white").pack()
    Label(m5, text="Victras Tool box", font='san-serif 14 bold' ,bg="#202125", foreground="white").pack()
    Label(m5, text="Version : 1.0.1", font='san-serif 10 bold' ,bg="#202125", foreground="white").pack()
    Label(m5, text="Made By Vectras Development Team", font='san-serif 10 bold' ,bg="#202125", foreground="white").pack()
    Label(m5, text = "",bg="#202125", foreground="white").pack()
    m3 = Button(m5, text='Victras Website', font='san-serif 16 bold', bg='#0160c9',fg="white",borderwidth="0", padx=2,command= github).pack()
def drivers():
    def close():
       italia.destroy()

    italia = Tk()
    italia.geometry("300x150")
    italia.configure(bg="#202125")
    italia.resizable(0, 0)
    italia.iconbitmap("Textures\icon.ico")
    italia.title("Loading Drivers")

    def bar(): 
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
        try:
            response = requests.get("https://raw.githubusercontent.com/epicstudios856/Vectras-windows-emulator/main/store_list.json", timeout=5)
            os.system('python tools.py')
            root.destroy()
        except requests.ConnectionError:
            msg = messagebox.showerror('ERROR', 'Connection not found!!')
        
    
    Label(italia, text = "",bg="#202125", foreground="white").pack()
    Label(italia, text="Loading Tools", font='san-serif 14 bold' ,bg="#202125", foreground="white").pack()
    Label(italia, text = "",bg="#202125", foreground="white").pack()
    progress = ttk.Progressbar(italia, orient = HORIZONTAL, length = 150, mode = 'determinate')
    progress.pack()
    Label(italia, text = "",bg="#202125", foreground="white").pack()
    m3 = Button(italia, text='Cancel', font='san-serif 8 bold', bg='#0160c9',fg="white",borderwidth="0", padx=2,command= close).pack()
    bar()
    
'''def apps():
    def close():
       cayman.destroy()

    cayman = Tk()
    cayman.geometry("300x150")
    cayman.configure(bg="#202125")
    cayman.resizable(0, 0)
    cayman.iconbitmap("Textures\icon.ico")
    cayman.title("Loading Drivers")

    def bar(): 
        cayman.configure(bg="#202125")
        progress['value'] = 20
        cayman.update_idletasks() 
        time.sleep(1) 
  
        progress['value'] = 40
        cayman.update_idletasks() 
        time.sleep(1) 
  
        progress['value'] = 50
        cayman.update_idletasks() 
        time.sleep(1) 
  
        progress['value'] = 60
        cayman.update_idletasks() 
        time.sleep(1) 
  
        progress['value'] = 80
        cayman.update_idletasks() 
        time.sleep(1) 
        progress['value'] = 100
        close()
        try:
            response = requests.get("https://www.google.com", timeout=5)
            os.system('python appsandgames.py')
            root.destroy()
        except requests.ConnectionError:
            msg = messagebox.showerror('ERROR', 'Connection not found!!')

    
    Label(cayman, text = "",bg="#202125", foreground="white").pack()
    Label(cayman, text="Loading Apps and Games", font='san-serif 14 bold' ,bg="#202125", foreground="white").pack()
    Label(cayman, text = "",bg="#202125", foreground="white").pack()
    progress = ttk.Progressbar(cayman, orient = HORIZONTAL, length = 150, mode = 'determinate')
    progress.pack()
    Label(cayman, text = "",bg="#202125", foreground="white").pack()
    m3 = Button(cayman, text='Cancel', font='san-serif 8 bold', bg='#0160c9',fg="white",borderwidth="0", padx=2,command= close).pack()
    bar()'''
    

root = Tk()

root.geometry('300x480')
root.title('Vectras ToolBox')
root.iconbitmap("Textures\icon.ico")
root.configure(background='#202125')

h=Label(root,text="",background='#202125').pack()
Label(root, text="Vectras Tool Box", font='san-serif 16 bold', foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
f8 = Button(root, text='Tools', font='san-serif 16 bold', background='#0160c9',foreground="white",borderwidth="0", padx=2,command=drivers).pack()
Label(root,text="", foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
#f8 = Button(root, text='Apps and Games', font='san-serif 16 bold',background='#0160c9',foreground="white",borderwidth="0", padx=2,command=apps).pack()
Label(root,text="", foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
Label(root,text="", foreground="white", background='#202125').pack()
f8 = Button(root, text='About', font='san-serif 16 bold', background='#0160c9',foreground="white",borderwidth="0", padx=2,command=about).pack()

root.mainloop()