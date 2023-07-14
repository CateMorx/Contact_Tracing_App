#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP

#imports necessary modules
import tkinter as tk

#Create Class For Add Entry
class Search_Entries:
    #Creates constructor for Search Entry
    def __init__(self, root):
        self.root = root
    #creates def for the GUI
    def GUI(self):
        # Create an entry box for Search Bar
        self.search_entry = tk.Entry(self.root, font=("Helvetica", 20))
        self.search_entry.pack()

        # Create a listbox for results
        self.suggestions_box = tk.Listbox(self.root, width=50)
        self.suggestions_box.pack(pady=40)