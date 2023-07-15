#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP

#imports necessary modules
import tkinter as tk
from tkinter import messagebox

#Create Class For Add Entry
class Add_Entries:
    #Creates constructor for Add Entry
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")

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

        self.test_label= tk.Label(self.root, text="What Locations Have you been to the last 14 days?:") 
        self.test_label.place(x=300, y=140)

        # Create an entry box for Search Bar to view available entries
        self.search_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.search_entry.place(x=300, y=160)

        # Create a listbox for results
        self.suggestions_box = tk.Listbox(self.root, width=50)
        self.suggestions_box.place(x=300, y=200)

        # Create a binding on the entry box
        self.search_entry.bind("<KeyRelease>", self.check)

        # Create a binding on the listbox onclick
        self.suggestions_box.bind("<<ListboxSelect>>", self.fillout)


        self.test_label= tk.Label(self.root, text="Add New Entry:") 
        self.test_label.place(x=650, y=140)       
        self.new_choice_entry = tk.Entry(self.root)
        self.new_choice_entry.place(x=650, y=180)

        # Create a button to add new choices
        self.new_choice_button = tk.Button(self.root, text="Add New Location", command=self.add_new_choice)
        self.new_choice_button.place(x=650, y=220)

        button = tk.Button(self.root, text="Submit", command=self.export_input)
        button.place(x=500, y=500)

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
            for item in self.generate_suggestions("Locations.txt"):
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
    def generate_suggestions(self, file_path):

        #Creates list for suggestions
        suggestions = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            suggestions = [line.strip() for line in lines]
        #returns value of suggestion list
        return suggestions
    
    def add_new_choice(self):
        new_choice = self.new_choice_entry.get()
        file_path = "Locations.txt"

        with open(file_path, 'a') as file:
            file.write(f"\n{new_choice}")

        messagebox.showinfo("New Location Added", "The location has been added successfully.")

    def export_input(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()


        content = f"Name: {name}\nAge: {age}\nGender: {gender}\nAddress: {address}\nContact Details: {contact}"

        file_path = r"C:\Users\Cate\Desktop\A.Y 2022-2023\Contact_Tracing_App\All_Entries"+ "\\" + name + ".txt"

        try:
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Export Successful", f"Content exported to {file_path}")
        except Exception as e:
            messagebox.showerror("Export Failed", str(e))