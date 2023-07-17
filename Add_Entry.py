#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Final Project in OOP

#imports necessary modules
import tkinter as tk
from tkinter import messagebox
import datetime 

#Create Class For Add Entry
class Add_Entries:
    #Creates constructor for Add Entry
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")
        self.selected_items = []
        self.selected_items_2 = []
        self.selected_option= tk.IntVar()
        self.selected_gender= tk.IntVar()
        self.confirmed_cases = []

    #creates def for the GUI
    def GUI(self):
        #creates label for instruction
        self.title_label= tk.Label(self.root, text="Please Fill Out The Following Information: ", font=('Arial',16))
        self.title_label.place(x=300, y=50)

        #creates demographic label 
        self.demographic_label= tk.Label(self.root, text= "Basic Demographic")
        self.demographic_label.place(x=100, y=90)

        #creates label and entry box for Name
        self.name_label= tk.Label(self.root, text= "Full Name:")
        self.name_label.place(x=100, y=140)       
        self.name_entry=tk.Entry(self.root)
        self.name_entry.place(x=100, y=160)

        #creates label and entry box for Age
        self.age_label= tk.Label(self.root, text="Age:")
        self.age_label.place(x=100, y=220)
        self.age_entry=tk.Entry(self.root)
        self.age_entry.place(x=100, y=240)

        self.age_entry.bind("<KeyRelease>", self.validate_age_entry)

        #creates label and entry box for Gender
        self.gender_label= tk.Label(self.root, text="Gender:") 
        self.gender_label.place(x=100, y=300)

        #Adds multiple choice "Female"
        female_radio = tk.Radiobutton(self.root, text="Female", variable=self.selected_gender, value="1")
        female_radio.place(x=100, y=320)

        #Adds multiple choice "Male"
        male_radio = tk.Radiobutton(self.root, text="Male", variable=self.selected_gender, value="2")
        male_radio.place(x=100, y=340)

        #Adds multiple choice "Prefer Not To Say"
        prefer_not_radio = tk.Radiobutton(self.root, text="Prefer Not To Say", variable=self.selected_gender, value="3")
        prefer_not_radio.place(x=100, y=360)

        #creates label and entry box for Address
        self.address_label= tk.Label(self.root, text="Adress:") 
        self.address_label.place(x=100, y=420)
        self.address_entry=tk.Entry(self.root)
        self.address_entry.place(x=100, y=440)

        #creates label and entry box for Contact Details
        self.contact_label= tk.Label(self.root, text="Contact Details:") 
        self.contact_label.place(x=100, y=500)
        self.contact_entry=tk.Entry(self.root)
        self.contact_entry.place(x=100, y=520)

        #creates label for locations visited last 14 days
        self.test_label= tk.Label(self.root, text="What Locations Have you been to the last 14 days?:") 
        self.test_label.place(x=300, y=90)

        # Create an entry box for Search Bar to view available locations
        self.search_location = tk.Entry(self.root, font=("Helvetica", 16), fg="gray")
        self.search_location.place(x=300, y=110)

        #Adds temporary text within entry widget
        default_text = "Search For Locations"
        self.search_location.insert(0, default_text)
        self.search_location.bind("<FocusIn>", self.on_entry_click)
        self.search_location.bind("<FocusOut>", self.on_entry_leave)

        #creates result label 
        self.suggestions_box_1_results = tk.Label(self.root, text= "Results:")
        self.suggestions_box_1_results.place(x=300, y=140)

        # Create a listbox for results
        self.suggestions_box_1 = tk.Listbox(self.root, width=50, selectmode=tk.MULTIPLE)
        self.suggestions_box_1.place(x=300, y=160)

        #creates selected locations label 
        self.suggestions_box_2_results = tk.Label(self.root, text= "Selected Location:")
        self.suggestions_box_2_results.place(x=300, y=330)

        # Create a listbox for all selected locations
        self.suggestions_box_2 = tk.Listbox(self.root, width=50, selectmode=tk.MULTIPLE)
        self.suggestions_box_2.place(x=300, y=350)

        # Create a binding on the entry box
        self.search_location.bind("<KeyRelease>", self.check)

        # Create a binding on the listbox onclick
        self.suggestions_box_1.bind("<<ListboxSelect>>", self.transfer_items)
        self.suggestions_box_2.bind("<<ListboxSelect>>", self.transfer_items)

        # create label and entry to add new location
        self.test_label= tk.Label(self.root, text="Add New Location:") 
        self.test_label.place(x=650, y=90)       
        self.new_choice_entry = tk.Entry(self.root)
        self.new_choice_entry.place(x=650, y=110)

        # Create a button to add new choices
        self.new_choice_button = tk.Button(self.root, text="Add New Location", command=self.add_new_choice)
        self.new_choice_button.place(x=650, y=140)

        #Adds label for Covid-19 test result
        self.test_label= tk.Label(self.root, text="Have you been tested for the last 14 days?:") 
        self.test_label.place(x=650, y=220)

        #Adds multiple choice "Yes-Negative"
        yes_negative_radio = tk.Radiobutton(self.root, text="Yes-Negative", variable=self.selected_option, value="1")
        yes_negative_radio.place(x=650, y=240)

        #Adds multiple choice "Yes-Positive"
        yes_positive_radio = tk.Radiobutton(self.root, text="Yes-Positive", variable=self.selected_option, value="2")
        yes_positive_radio.place(x=650, y=260)

        #Adds multiple choice "No"
        no_radio = tk.Radiobutton(self.root, text="No", variable=self.selected_option, value="3")
        no_radio.place(x=650, y=280)

        #create submit button
        button = tk.Button(self.root, text="Submit", command=self.export_input)
        button.place(x=500, y=550)

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
                    if item not in self.suggestions_box_2.get(0, tk.END):
                        self.suggestions_box_1.insert(tk.END, item)

        # Re-select the previously selected items in the first listbox
        for index in selected_indices_1:
            self.suggestions_box_1.select_set(index)

        # Check if the search input is empty
        if not typed:
            return
        # Check if suggestions_box_1 is empty
        if self.suggestions_box_1.size() == 0:
            messagebox.showinfo("No Results", "No matching results found. Please Add A New Location")

    #creates def to transfer all selected item in suggestionbox1 to suggestionbox2
    def transfer_items(self, e):
        selected_indices_1 = self.suggestions_box_1.curselection()

        # Transfer selected items from the first listbox to the second listbox
        for index in selected_indices_1:
            item = self.suggestions_box_1.get(index)

            #Makes sure there is no duplicates within listbox 2
            if item not in self.suggestions_box_2.get(0, tk.END):
                self.selected_items_2=list(self.suggestions_box_2.get(0, tk.END))
                self.selected_items_2.append(item)
                self.suggestions_box_2.insert(tk.END, item)

        # Remove the selected item from Listbox 2 when clicked
        selected_indices_2 = self.suggestions_box_2.curselection()
        for index in selected_indices_2:
            item = self.suggestions_box_2.get(index)
            # Show a confirmation popup asking if the user wants to remove the location
            answer = messagebox.askyesno("Remove Location", f"Are you sure you want to remove {item}?")
            if answer:
                self.suggestions_box_2.delete(index)


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
        # Retrieves input from new_choice_entry
        new_choice = self.new_choice_entry.get()

        # Check if the input contains a comma
        if "," in new_choice:
            messagebox.showerror("Invalid Input", "Commas are not allowed in the location name.")
            return

        # Indicates the file where the new item will be stored
        file_path = "Locations.txt"

        # Opens file and appends new_choice into the file
        with open(file_path, 'a') as file:
            file.write(f"\n{new_choice}")

        # Shows a messagebox to confirm that the new input is successful
        messagebox.showinfo("New Location Added", "The location has been added successfully.")


    def on_entry_click(self,event):
        if self.search_location.get() == "Search For Locations":
            self.search_location.delete(0, tk.END)
            self.search_location.configure(foreground="black")

    def on_entry_leave(self,event):
        if self.search_location.get() == "":
            self.search_location.insert(0, "Search For Locations")
            self.search_location.configure(foreground="gray")

    def validate_age_entry(self, event):
        age = self.age_entry.get()

        if age:
            try:
                int(age)
            except ValueError:
                messagebox.showerror("Invalid Input", "Age must be an Integer")
                self.age_entry.delete(0, tk.END)
        else:
            return

    #Exports all user input within add entry into a text file
    def export_input(self):

        #Retrieves user input for age
        name = self.name_entry.get()

        #Retrieves user input for age
        get_age = self.age_entry.get()

        # Validate age input
        try:
            get_age =int(get_age)
            if get_age <= 0 or get_age >= 100:
                raise ValueError
            else:
                age=get_age
        except ValueError:
            messagebox.showerror("Invalid Age", "Please enter a valid age (1-99).")
            return

        #Retrieves user input for gender
        gender_selected= self.selected_gender.get()
        if gender_selected == 1:
            gender= "Female"
        elif gender_selected == 2:
            gender= "Male"
        elif gender_selected == 3:
            gender= "Prefer Not To Say"

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
            self.add_to_confirmed_cases(name, location)
        elif selected_option == 3:
            test_result= "Not Tested"

        # Check if any of the required fields are empty
        if not name or not age or not gender_selected or not address or not contact or not selected_option or not location:
            messagebox.showerror("Missing Information", "Please fill out all the required fields.")
            return
        
        # Create a timestamp with the current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #creates the content to be displayed within the text file
        content = f"Timestamp: {timestamp} \nName: {name}\nAge: {age}\nGender: {gender}\nAddress: {address}\nContact Details: {contact} \nTested for Covid-19 the last 14 days: {test_result} \nLocations Visited Last 14 Days: {location}"

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

        self.submit_entry()

        self.log_entry_submission(name)

    def submit_entry(self):
        confirm_contact = messagebox.askyesno("Contact Tracing", "Do you want to know your possible contacts with confirmed cases?")
        if confirm_contact:
            self.show_possible_contacts()

    def show_possible_contacts(self):
        # Get the locations visited by the user in the last 14 days
        visited_locations = self.suggestions_box_2.get(0, tk.END)

        # Load the data from the "Confirmed cases" text file
        confirmed_cases_file = "Confirmed cases.txt"
        confirmed_cases = []
        with open(confirmed_cases_file, 'r') as file:
            confirmed_cases = file.read().splitlines()

        # Initialize a dictionary to store word counts
        word_counts = {location: 0 for location in visited_locations}

        # Get the current timestamp
        current_time = datetime.datetime.now()

        # Count the occurrences of each location in the confirmed cases
        for case in confirmed_cases:
            name, locations, timestamp_str = case.split("\t")
            locations = locations.split(", ")
            timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            # Calculate the difference between the current timestamp and the entry's timestamp
            time_difference = current_time - timestamp

            # Skip counting the case if the entry is older than 14 days
            if time_difference.days > 14:
                continue

            # If the user responded with "Yes-Positive," skip counting their case
            if name == self.name_entry.get() and self.selected_option.get() == 2:
                continue

            for location in locations:
                if location in word_counts:
                    word_counts[location] += 1

        # Create a new window to display the results
        contacts_window = tk.Toplevel(self.root)
        contacts_window.title("Possible Contacts with Confirmed Cases in the Last 14 Days")
        contacts_window.geometry("400x300")

        # Display the number of confirmed cases for each visited location
        for location in visited_locations:
            num_cases = word_counts[location]
            label_text = f"Location: {location}\nNumber of Confirmed Cases: {num_cases}"
            location_label = tk.Label(contacts_window, text=label_text)
            location_label.pack()

    def add_to_confirmed_cases(self, name, location):
        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Add the user's name, locations, and timestamp to the confirmed cases list
        self.confirmed_cases.append((name, location, timestamp))
        # Save the confirmed cases to the "Confirmed cases" text file
        confirmed_cases_file = "Confirmed cases.txt"
        with open(confirmed_cases_file, "a") as file:
            file.write(f"{name}\t{location}\t{timestamp}\n")
        
    def log_entry_submission(self, name):
        # Create a timestamp with the current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create the log entry content
        log_entry = f"Timestamp: {timestamp} Name: {name}"

        # Append the log entry to the "Log_Book.txt" file
        log_file_path = "Log_Book.txt"
        try:
            # First, read the existing content of the log file (if any)
            existing_content = ""
            try:
                with open(log_file_path, "r") as log_file:
                    existing_content = log_file.read()
            except FileNotFoundError:
                # If the file doesn't exist, it's fine; we'll create it later
                pass

            # Now, write the log entry with the numbering order
            with open(log_file_path, "w") as log_file:
                # Count the number of entries in the log file to generate the numbering order
                num_entries = existing_content.count("Entry #") + 1
                log_file.write(existing_content + f"Entry #{num_entries}: {log_entry}\n")

        except Exception as e:
            # Print the exception details to the console for debugging
            print("Logging Failed:", e)
            # Show an error messagebox if logging failed
            messagebox.showerror("Logging Failed", str(e))