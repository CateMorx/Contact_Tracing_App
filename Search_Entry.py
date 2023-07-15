#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP

#imports necessary modules
import tkinter as tk
import os

#Create Class For Add Entry
class Search_Entries:
    #Creates constructor for Search Entry
    def __init__(self, root):
        self.root = root

    #creates def for the GUI
    def GUI(self):
        # Create an entry box for Search Bar to view available entries
        self.search_entry = tk.Entry(self.root, font=("Helvetica", 20))
        self.search_entry.pack()

        # Create a listbox for results
        self.suggestions_box = tk.Listbox(self.root, width=50)
        self.suggestions_box.pack(pady=40)

        # Create a binding on the entry box
        self.search_entry.bind("<KeyRelease>", self.check)

        # Create a binding on the listbox onclick
        self.suggestions_box.bind("<<ListboxSelect>>", self.fillout)

    #Creates filter based on user input in search Bar
    def check(self, e):
        # Retrieve what was typed
        typed = self.search_entry.get()

        #If there is ' ' input in search entry, calls generate_suggestion method with given folder path
        if typed == '':
            data = self.generate_suggestions("Locations.txt")
        else:
            #filters suggestion based on the user input in search bar, retrieves data from generate_suggestion method with given folder path
            data = []
            for item in self.generate_suggestions(r"C:\Users\Cate\Desktop\A.Y 2022-2023\Contact_Tracing_App\All_Entries"):
                if typed.lower() in item.lower():
                    data.append(item)

        # Update the listbox with selected items
        self.update(data)


    def fillout(self, e):
        # Delete whatever is in the entry box
        self.search_entry.delete(0, tk.END)

        # Add clicked list item to entry box
        self.search_entry.insert(0,  self.suggestions_box.get(tk.ANCHOR))


    def update(self, data):
        # Clear the listbox
        self.suggestions_box.delete(0, tk.END)

        # Add items to listbox
        for item in data:
            self.suggestions_box.insert(tk.END, item)


    #creates method for generating suggestion for the results
    def generate_suggestions(self, folder_path):

        #Creates list for suggestions
        suggestions = []

        #Returns list of all files within the given folder "All_Entries"
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            #If item is a file, appends to suggestions list
            if os.path.isfile(item_path):
                suggestions.append(item)

        #returns value of suggestion list
        return suggestions