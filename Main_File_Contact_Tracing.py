#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP
#Create a Covid-19 Contact Tracing App with GUI

#imports necessary elements
import tkinter as tk
from Search_Entry import Search_Entries
from Add_Entry import Add_Entries

#Create Class GUI
class GUI:
    #create def for constructor
    def __init__(self):
        # creates an instance of the Tk class
        self.root = tk.Tk()

        #Title of Window
        self.root.title("Contact Tracing")

        # Create the button for Add Entry
        self.add_entry_button = tk.Button(self.root, text="Add Entry", command= self.Add_Entry)
        self.add_entry_button.pack(pady=10)

        # Create the button for Search Entry
        self.search_entry_button = tk.Button(self.root, text="Search Entry", command= self.Search_Entry)
        self.search_entry_button.pack(pady=10)

        #Customizes window size
        self.root.geometry("600x400")

    #creates main def to execute program
    def main(self):
        self.root.mainloop()

    #create def for Add Entry
    def Add_Entry(self):
    # Clear the current GUI
        for widget in self.root.winfo_children():
            widget.destroy()

        #Button to go back to starting page
        self.go_back = tk.Button(self.root, text="Return", command= self.go_back_option)
        self.go_back.pack()

        add_entry = Add_Entries(self.root)
        add_entry.GUI()

    #Create def for Search Entry
    def Search_Entry(self):
    # Clear the current GUI
        for widget in self.root.winfo_children():
            widget.destroy()

        #Button to go back to starting page
        self.go_back = tk.Button(self.root, text="Return", command= self.go_back_option)
        self.go_back.pack()

        search_entry = Search_Entries(self.root)
        search_entry.GUI()

    #Create def to allow users to go back to Starting page
    def go_back_option(self):
        # Clears the current GUI
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the button for Add Entry
        self.add_entry_button = tk.Button(self.root, text="Add Entry", command= self.Add_Entry)
        self.add_entry_button.pack()

         # Create the button for Search Entry
        self.search_entry_button= tk.Button(self.root, text="Search Entry", command= self.Search_Entry)
        self.search_entry_button.pack()

#Executes code within main
if __name__ == '__main__':
    window = GUI()
    window.main()