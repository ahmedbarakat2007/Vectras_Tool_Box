import tkinter as Tk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
import json
import requests
import webbrowser
import shutil
from urllib.request import urlretrieve
from PIL import ImageTk, Image
import urllib.request
import io
from io import BytesIO
from urllib.request import urlopen
from tkinter import *
import os


# create the root window
root = Tk()
root.geometry('920x566')
root.resizable(0,0)
root.title('Tools')
root.iconbitmap("Textures\icon.ico")
root.configure(background='#202125')

# create a list box
columns = ('item_name', 'item_size', 'item_data')

tree = ttk.Treeview(root, columns=columns, show='headings',height=27)

# define headings
tree.heading('item_name', text='App Name')
tree.heading('item_size', text='Size')
url = 'https://raw.githubusercontent.com/epicstudios856/Vectras-windows-emulator/main/store_list.json'
resp = requests.get(url)
data = json.loads(resp.text)

# generate sample data
contacts = []
for item in data:
    contacts.append((item["item_name"], item["item_size"], item["item_data"],item["item_filename"],item["item_link"],item["item_icon"]))

# add data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        values = item['values']
        name = values[0]
        size = values[1]
        dab = values[2]
        filename = values[3]
        link = values[4]
        icon = values[5]
        

    def download():  # Add m3 as a paramete
        def close_loading():
            if (m3.winfo_ismapped() == True):
                m3.destroy()

        def donothing():
            pass          

        m3 = tk.Tk()
        m3.geometry('250x100')
        m3.resizable(0,0)
        m3.iconbitmap("Textures\icon.ico")
        m3.protocol('WM_DELETE_WINDOW',donothing)
        m3.configure(bg="#202125")
        m3.title('DownLoading...')
        Label(m3,bg="#1f242b").pack()
        Label(m3, text='Downloading'+ name +'....',bg="#1f242b",fg='black', font='san-serif 14 bold').pack()
        msg1 = messagebox.askyesno('Info', 'Are You Sure You Want To Install ' + name)
        if msg1:
            if(os.path.isfile("c:/Installed/" + filename) == False):
                urlretrieve(link, filename)
                bb = os.path.isdir('c:/Installed')
                if ( bb == True):
                    shutil.move(filename, "c:/Installed")
                    
                    close_loading()
                    msg = showinfo("Info", name + " Is Installed")
                else:
                    path = os.path.join("C:/", "Installed")
                    os.mkdir(path) 
                    shutil.move(filename, "c:/Installed")
                    
                    close_loading()
                    msg = showinfo("Info", name + " Is Installed")

            else:
                close_loading()
                msg = showinfo("Info", name + " Is Already Installed")
        else:
            close_loading()
        m3.mainloop()  # Move this line here
        
        
        

    a7a = StringVar()
    six = StringVar()

    m3 = tk.Label(root, textvariable=a7a,bg="#202125", font='san-serif 16 bold', foreground="white")
    m3.place(x=680, y=150)

    m4 = tk.Label(root, textvariable=six,bg="#202125", font='san-serif 10 bold', foreground="white")
    m4.place(x=680, y=190)

# When you want to update the text
    a7a.set("Name : " + name + "                           ")
    six.set("Size : " + size + "                           ")
        
    m5 = tk.Button(root,text='Download', font='san-serif 12 bold', bg='#0160c9',fg="white",borderwidth="0", padx=2,command=download)
    m5.place(x=729,y=450)
        
        


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=5, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll= scrollbar.set)
scrollbar.grid(row=5, column=1, sticky='nsew')

root.mainloop()
