#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP

#imports necessary modules
import tkinter as tk

#Create Class For Add Entry
class Add_Entries:
    #Creates constructor for Add Entry
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")

    #creates def for the GUI
    def GUI(self):
        self.title_label= tk.Label(self.root, text="Please Fill Out The Following Information: ", font=('Arial',16))
        self.title_label.place(x=200, y=90)

        self.demographic_label= tk.Label(self.root, text= "Basic Demographic")
        self.demographic_label.place(x=100, y=140)

        self.name_label= tk.Label(self.root, text= "Name:")
        self.name_label.place(x=100, y=180)       
        self.name_entry=tk.Entry(self.root)
        self.name_entry.place(x=100, y=200)

        self.age_label= tk.Label(self.root, text="Age:")
        self.age_label.place(x=100, y=260)
        self.age_entry=tk.Entry(self.root)
        self.age_entry.place(x=100, y=280)

        self.gender_label= tk.Label(self.root, text="Gender:") 
        self.gender_label.place(x=100, y=320)
        self.gender_entry=tk.Entry(self.root)
        self.gender_entry.place(x=100, y=340)

        self.address_label= tk.Label(self.root, text="Adress:") 
        self.address_label.place(x=100, y=380)
        self.address_entry=tk.Entry(self.root)
        self.address_entry.place(x=100, y=400)

        self.contact_label= tk.Label(self.root, text="Contact Details:") 
        self.contact_label.place(x=100, y=440)
        self.contact_entry=tk.Entry(self.root)
        self.contact_entry.place(x=100, y=460)