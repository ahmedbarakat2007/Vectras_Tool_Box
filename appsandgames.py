import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.geometry('400x580')
root.resizable(0,0)
root.title('Apps and Games')
root.iconbitmap("Textures\icon.ico")
root.configure(background='#202125')

tk.Label(root,text="",background='#202125').pack()
tk.Label(root, text="Apps and Games", font='san-serif 16 bold', foreground="white", background='#202125').pack()
tk.Label(root,text="", foreground="white", background='#202125').pack()


# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')

var = tk.Variable(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED
)

listbox.pack(expand=True, fill=tk.BOTH)


def items_selected(event):
    # get all selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()
