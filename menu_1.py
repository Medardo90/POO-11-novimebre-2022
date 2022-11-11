# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 09:39:21 2022

@author: lab
"""

import tkinter as tk
from tkinter.colorchooser import askcolor

def configColor():
    result = tk.colorchooser.askcolor(title = "tkinter color chooser")
    label.configure(fg= result[1])
    print(result[0])
    
root = tk.Tk()
root.geometry('200x150')
tk.Button(root,text= "choose color" ,command = configColor).pack(pady=20)
label=tk.Label(root,text = "color", fg ="black")

label.pack()
tk.mainloop()
