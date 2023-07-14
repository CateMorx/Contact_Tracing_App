#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP
#Create a Covid-19 Contact Tracing App with GUI

#imports necessary elements
import tkinter as tk

#Create Class GUI
class GUI:
    #create def for constructor
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Contact Tracing")
        # Create the buttons
        self.button1 = tk.Button(self.root, text="Add Entry", command= self.Add_Entry)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.root, text="Search Entry", command= self.Search_Entry)
        self.button2.pack(pady=10)

        self.root.geometry("600x400")

    #creates main def to execute code
    def main(self):
        self.root.mainloop()

    #create def for Add Entry
    def Add_Entry(self):
    # Clear the current GUI
        for widget in self.root.winfo_children():
            widget.destroy()

    #Create def for Search Entry
    def Search_Entry(self):
    # Clear the current GUI
        for widget in self.root.winfo_children():
            widget.destroy()

    #Executes code within main
if __name__ == '__main__':
    window = GUI()
    window.main()