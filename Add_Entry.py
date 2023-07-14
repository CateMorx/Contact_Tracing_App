#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP

#imports necessary modules
import tkinter as tk

#Create Class For Add Entry
class Add_Entries:
    #Creates constructor for Add Entry
    def __init__(self, root):
        self.root = root
    #creates def for the GUI
    def GUI(self):
        self.title_label= tk.Label(self.root, text="Please Fill Out The Following Information: ", font=('Arial',16))
        self.title_label.pack()