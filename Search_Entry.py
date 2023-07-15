#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP

#imports necessary modules
import tkinter as tk
from tkinter import messagebox
import os

#Create Class For Add Entry
class Search_Entries:
    #Creates constructor for Search Entry
    def __init__(self, root):
        self.root = root

    #creates def for the GUI
    def GUI(self):

        # Create an entry box for Search Bar to view available entries
        self.search_entry = tk.Entry(self.root, font=("Helvetica", 20), fg="gray")
        self.search_entry.pack(pady=40)

        #Adds temporary text within entry widget
        default_text = "Search For Entries"
        self.search_entry.insert(0, default_text)
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_entry_leave)


        self.result_label= tk.Label(self.root, text="Results: ")
        self.result_label.pack()

        # Create a listbox for results
        self.suggestions_box = tk.Listbox(self.root, width=50)
        self.suggestions_box.pack()

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
            data = self.generate_suggestions(r"C:\Users\Cate\Desktop\A.Y 2022-2023\Contact_Tracing_App\All_Entries")
        else:
            #filters suggestion based on the user input in search bar, retrieves data from generate_suggestion method with given folder path
            data = []
            for item in self.generate_suggestions(r"C:\Users\Cate\Desktop\A.Y 2022-2023\Contact_Tracing_App\All_Entries"):
                if typed.lower() in item.lower():
                    data.append(item)

        # Update the listbox with filtered suggestion
        self.update(data)

        # Check if the search input is empty
        if not typed:
            return
            # Check if suggestions_box_1 is empty
        if self.suggestions_box.size() == 0:
            messagebox.showinfo("No Results", "No matching results found.")

    #Creates autofill based on selected item in listbox, also calls method for display file content
    def fillout(self, e):
        # Delete whatever is in the entry box
        self.search_entry.delete(0, tk.END)

        # Add clicked list item to entry box
        self.search_entry.insert(0,  self.suggestions_box.get(tk.ANCHOR))

        # intialize folder path
        folder_path = r"C:\Users\Cate\Desktop\A.Y 2022-2023\Contact_Tracing_App\All_Entries"
        # Reads and display the contents of the selected file
        file_path = os.path.join(folder_path, self.suggestions_box.get(tk.ANCHOR))
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_content = file.read()
                self.display_file_content(file_content)


    # Update the listbox with filtered suggestion
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
    
    #Displays file content of selected entry
    def display_file_content(self, content):
        # Create a new window
        window = tk.Toplevel(self.root)

        # Create a text widget
        text_widget = tk.Text(window, height=10, width=50)
        text_widget.pack(pady=10)

        # Insert the file content into the text widget
        text_widget.insert(tk.END, content)

    def on_entry_click(self,event):
        if self.search_entry.get() == "Search For Entries":
            self.search_entry.delete(0, tk.END)
            self.search_entry.configure(foreground="black")

    def on_entry_leave(self,event):
        if self.search_entry.get() == "":
            self.search_entry.insert(0, "Search For Entries")
            self.search_entry.configure(foreground="gray")