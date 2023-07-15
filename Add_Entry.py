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
        self.selected_items = []
        self.selected_items_2 = []
        self.selected_option= tk.IntVar()

    #creates def for the GUI
    def GUI(self):
        #creates label for instruction
        self.title_label= tk.Label(self.root, text="Please Fill Out The Following Information: ", font=('Arial',16))
        self.title_label.place(x=200, y=90)

        #creates demographic label 
        self.demographic_label= tk.Label(self.root, text= "Basic Demographic")
        self.demographic_label.place(x=100, y=140)

        #creates label and entry box for Name
        self.name_label= tk.Label(self.root, text= "Name:")
        self.name_label.place(x=100, y=180)       
        self.name_entry=tk.Entry(self.root)
        self.name_entry.place(x=100, y=200)

        #creates label and entry box for Age
        self.age_label= tk.Label(self.root, text="Age:")
        self.age_label.place(x=100, y=260)
        self.age_entry=tk.Entry(self.root)
        self.age_entry.place(x=100, y=280)

        #creates label and entry box for Gender
        self.gender_label= tk.Label(self.root, text="Gender:") 
        self.gender_label.place(x=100, y=320)
        self.gender_entry=tk.Entry(self.root)
        self.gender_entry.place(x=100, y=340)

        #creates label and entry box for Address
        self.address_label= tk.Label(self.root, text="Adress:") 
        self.address_label.place(x=100, y=380)
        self.address_entry=tk.Entry(self.root)
        self.address_entry.place(x=100, y=400)

        #creates label and entry box for Contact Details
        self.contact_label= tk.Label(self.root, text="Contact Details:") 
        self.contact_label.place(x=100, y=440)
        self.contact_entry=tk.Entry(self.root)
        self.contact_entry.place(x=100, y=460)

        #creates label for locations visited last 14 days
        self.test_label= tk.Label(self.root, text="What Locations Have you been to the last 14 days?:") 
        self.test_label.place(x=300, y=140)

        # Create an entry box for Search Bar to view available locations
        self.search_location = tk.Entry(self.root, font=("Helvetica", 16), fg="gray")
        self.search_location.place(x=300, y=160)

        #Adds temporary text within entry widget
        default_text = "Search For Locations"
        self.search_location.insert(0, default_text)
        self.search_location.bind("<FocusIn>", self.on_entry_click)
        self.search_location.bind("<FocusOut>", self.on_entry_leave)

        # Create a listbox for results
        self.suggestions_box_1 = tk.Listbox(self.root, width=50, selectmode=tk.MULTIPLE)
        self.suggestions_box_1.place(x=300, y=200)

        # Create a listbox for all selected locations
        self.suggestions_box_2 = tk.Listbox(self.root, width=50, selectmode=tk.MULTIPLE)
        self.suggestions_box_2.place(x=300, y=300)

        # Create a binding on the entry box
        self.search_location.bind("<KeyRelease>", self.check)

        # Create a binding on the listbox onclick
        self.suggestions_box_1.bind("<<ListboxSelect>>", self.transfer_items)

        # create label and entry to add new location
        self.test_label= tk.Label(self.root, text="Add New Location:") 
        self.test_label.place(x=650, y=140)       
        self.new_choice_entry = tk.Entry(self.root)
        self.new_choice_entry.place(x=650, y=180)

        # Create a button to add new choices
        self.new_choice_button = tk.Button(self.root, text="Add New Location", command=self.add_new_choice)
        self.new_choice_button.place(x=650, y=220)

        #Adds label for Covid-19 test result
        self.test_label= tk.Label(self.root, text="Have you been tested for the last 14 days?:") 
        self.test_label.place(x=650, y=260)

        #Adds multiple choice "Yes-Negative"
        yes_negative_radio = tk.Radiobutton(self.root, text="Yes-Negative", variable=self.selected_option, value="1")
        yes_negative_radio.place(x=650, y=280)

        #Adds multiple choice "Yes-Positive"
        yes_positive_radio = tk.Radiobutton(self.root, text="Yes-Positive", variable=self.selected_option, value="2")
        yes_positive_radio.place(x=650, y=300)

        #Adds multiple choice "No"
        no_radio = tk.Radiobutton(self.root, text="No", variable=self.selected_option, value="3")
        no_radio.place(x=650, y=320)

        #create submit button
        button = tk.Button(self.root, text="Submit", command=self.export_input)
        button.place(x=500, y=500)

    #Creates filter based on user input in search Bar
    def check(self, e):
        typed = self.search_location.get().lower()

        # Get the selected items from the first listbox
        selected_indices_1 = self.suggestions_box_1.curselection()

        #Clears previous items in listbox
        self.suggestions_box_1.delete(0, tk.END)

        #Filters results in the firstlistbox depending on input in search bar
        if typed:
            for item in self.generate_suggestions("Locations.txt"):
                if typed in item.lower():
                    #Makes sure that there are no duplicates between listbox 1 and 2
                    if item not in self.selected_items_2:
                        self.suggestions_box_1.insert(tk.END, item)

        # Re-select the previously selected items in the first listbox
        for index in selected_indices_1:
            self.suggestions_box_1.select_set(index)

    #creates def to transfer all selected item in suggestionbox1 to suggestionbox2
    def transfer_items(self, e):
        selected_indices_1 = self.suggestions_box_1.curselection()

        # Transfer selected items from the first listbox to the second listbox
        for index in selected_indices_1:
            item = self.suggestions_box_1.get(index)

            #Makes sure there is no duplicates within listbox 2
            if item not in self.selected_items_2:
                self.selected_items_2.append(item)
                self.suggestions_box_2.insert(tk.END, item)


    #creates method for generating suggestion for the results
    def generate_suggestions(self, file_path):

        #Creates list for suggestions
        suggestions = []

        #reads alll item in the text file and stores each line as an individual item in suggestions list
        with open(file_path, 'r') as file:
            lines = file.readlines()
            suggestions = [line.strip() for line in lines]
        #returns value of suggestion list
        return suggestions
    
    #Allows user to add a new location
    def add_new_choice(self):
        #Retrieves input from new_choice_entry
        new_choice = self.new_choice_entry.get()

        #Indicates the file where the new item will be stored
        file_path = "Locations.txt"

        #opens file and appends new_choice into the file
        with open(file_path, 'a') as file:
            file.write(f"\n{new_choice}")

        #shows messagebox to cofirm that the new input is succesful
        messagebox.showinfo("New Location Added", "The location has been added successfully.")


    def on_entry_click(self,event):
        if self.search_location.get() == "Search For Entries":
            self.search_location.delete(0, tk.END)
            self.search_location.configure(foreground="black")

    def on_entry_leave(self,event):
        if self.search_location.get() == "":
            self.search_location.insert(0, "Search For Entries")
            self.search_location.configure(foreground="gray")


    #Exports all user input within add entry into a text file
    def export_input(self):
        #Retrieves user input for age
        name = self.name_entry.get()

        #Retrieves user input for age
        age = self.age_entry.get()

        #Retrieves user input for gender
        gender = self.gender_entry.get()

        #Retrieves user input for address
        address = self.address_entry.get()

        #Retrieves user input for contact details
        contact = self.contact_entry.get()

        # Retrieve all items in suggestions_box_2
        self.selected_items = self.suggestions_box_2.get(0, tk.END) 

        location= ', '.join(self.selected_items)

        #Retrieves user selected option for Covid-19 Test Results
        selected_option = self.selected_option.get()
        if selected_option == 1:
            test_result= "Yes-Negative"
        elif selected_option == 2:
            test_result= "Yes-Positive"
        elif selected_option == 3:
            test_result= "Not Tested"

        #creates the content to be displayed within the text file
        content = f"Name: {name}\nAge: {age}\nGender: {gender}\nAddress: {address}\nContact Details: {contact} \nTested for Covid-19 the last 14 days: {test_result} \nLocations Visited Last 14 Days: {location}"

        #indicates file path and sets the text file name as the name input
        file_path = r"C:\Users\Cate\Desktop\A.Y 2022-2023\Contact_Tracing_App\All_Entries"+ "\\" + name + ".txt"

        #exports the file along with the content
        try:
            with open(file_path, 'w') as file:
                file.write(content)

            #shows messagebox if succesful export    
            messagebox.showinfo("Export Successful", f"Content exported to {file_path}")

        #shows messageox if export failed
        except Exception as e:
            messagebox.showerror("Export Failed", str(e))