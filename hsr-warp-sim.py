from tkinter import *
from tkinter import messagebox
import csv
from collections import defaultdict

# Create object 
root = Tk() 

# Adjust size 
root.geometry("500x500")

# Dropdown menu options
# Create a list of 5* limited character options
five_star_options = []
with open("hsr-limited-characters.csv", newline = "") as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		five_star_options.extend(row)
five_star_options.sort()

# Create a nested dictionary for the standard options
standard_options = defaultdict(lambda: defaultdict(list))
with open("hsr-standard-info.csv", newline = "") as csvfile:
	csvreader = csv.DictReader(csvfile)
	for row in csvreader:
		rarity = row["Rarity"]
		classification = row["Classification"]
		name = row["Name"]
		standard_options[rarity][classification].append(name)
standard_options = {rarity: dict(classification) for rarity, classification in standard_options.items()}

# Datatype of menu text 
five_star_selected = StringVar()
four_star_selected1 = StringVar()
four_star_selected2 = StringVar()
four_star_selected3 = StringVar()

# Initial menu text
# Have user select a 5* character and three rate-up 4* characters 
five_star_selected.set("Select a 5* Character")
four_star_selected1.set("Select a 4* Character") 
four_star_selected2.set("Select a 4* Character")
four_star_selected3.set("Select a 4* Character")

# Create dropdown menus
five_star_drop = OptionMenu(root, five_star_selected, *five_star_options) 
five_star_drop.pack()

four_star_drop1 = OptionMenu(root, four_star_selected1, *standard_options["4"]["Character"])
four_star_drop1.pack()

four_star_drop2 = OptionMenu(root, four_star_selected2, *standard_options["4"]["Character"])
four_star_drop2.pack()

four_star_drop3 = OptionMenu(root, four_star_selected3, *standard_options["4"]["Character"])
four_star_drop3.pack()

# Create a label that shows the banner the user created
def submit():
	if five_star_selected.get() == "Select a 5* Character":
		messagebox.showerror("Error!", "Please select a 5* character.")
	elif four_star_selected1.get() == "Select a 4* Character" or four_star_selected2.get() == "Select a 4* Character" or four_star_selected3.get() == "Select a 4* Character":
		messagebox.showerror("Error!", "Please select three 4* characters.")
	elif four_star_selected1.get() == four_star_selected2.get() or four_star_selected1.get() == four_star_selected3.get() or four_star_selected2.get() == four_star_selected3.get():
		messagebox.showerror("Error!", "The selected 4* characters cannot be the same.")
	else:
		label.config(text = f"YOUR BANNER:"
			   f"\n{five_star_selected.get()}"
			   f"\n{four_star_selected1.get()}"
			   f"\n{four_star_selected2.get()}"
			   f"\n{four_star_selected3.get()}")
		warp_button1 = Button(root, text = "WARP x1").pack()
		warp_button1 = Button(root, text = "WARP x10").pack()

# Create button, it will change label text 
start_button = Button(root, text = "START", command = submit).pack()

# Create Label 
label = Label(root, text = " ", anchor = "w", justify = "left")
label.pack()

# Execute tkinter 
root.mainloop()