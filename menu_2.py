# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 10:05:06 2022

@author: lab
"""

from tkinter import *
root =Tk()
root.title("menu options")

menubar = menu(root)

file= Menu(menubar, tearoff = 0 )
menubar.add_cascade(label="File", menu =file)
file.add_command(label= "new file", command = None)
file.add_command(label= "open....", command = None)
file.add_command(label= "save", command = None)
file.add_separador()
file.add_command(label= "exit", command = root.destroy)

edit = Menu(menubar, tearoff = 0 )
menubar.add_cascade(label="edit", menu = edit)
edit.add_command(label= "open....", command = None)
edit.add_command(label= "open....", command = None)
edit.add_command(label= "open....", command = None)